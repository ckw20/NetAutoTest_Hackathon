# =================================================================================
# Objective   	:   Test Objective : 6.7.4 Static Routing
#
# Step			:	Test Step 1: Build the test environment according to the figure
#                   Test Step 2: tester port1 IP address is 192.168.1.100/24, port2 is 192.168.2.100/24
#                   Test Step 3: DUT1 port1 IP address is 192.168.1.1/24, port2 is 1.1.1.1/24;
#                   Test Step 4: DUT2 port2 IP address is 192.168.2.1/24, port1 is 1.1.1.2/24;
#                   Test Step 5: Configure static routes between tester port1 and port2 on DUT1 and DUT2;
#                   Test Step 6: tester uses port1 and port2 to send bidirectional data streams, check connectivity
#
# Criteria    	:   Expected Result 1: The client can receive the correct address configuration
#
# Created by   	:  	Tester-006
#
# Bugs   	    :  	None
# =================================================================================
import time

from CustomLibrary.common import cfg, testbed, setup, teardown, printf, temp_dir, get_locations, CustomData, edit_port_params
from NtoLibrary.common import NTO
from TesterLibrary.base import *
import pandas


dirname, filename = os.path.split(os.path.abspath(__file__))
data = CustomData()
# 测试前下发配罿
device = setup(cfg, testbed)

verdict = 'pass'
errInfo = ''

try:
    # 初始化仪表
    printf(message='Initialize tester')
    if testbed['tester']['rtsm']['ip']:
        init_tester(Rtsm=testbed['tester']['rtsm']['ip'])
    else:
        init_tester()

    locations = get_locations(cfg['port'])
    # 创建端口，并预约端口
    ports = reserve_port(Locations=locations, Force=testbed['tester']['force']['default'],
                         Debug=testbed['tester']['debug']['default'],
                         WaitForStatusUp=testbed['tester']['wait_for_status_up']['default'])
    port_up, port_down = ports
    if testbed['nto']['enable']['default']:
        nto = NTO(host=testbed['nto']['ip'], port=testbed['nto']['port']['default'],
                  username=testbed['nto']['username']['default'], password=testbed['nto']['password']['default'],
                  content_type='multipart/form-data')
        nto.actions_import(os.path.join(dirname, 'topu.ata'))
    if not testbed['tester']['debug']['default']:
        for k, v in testbed['tester'].items():
            edit_port_kwargs = {}
            if k in edit_port_params:
                edit_port_kwargs.update({k: v['default']})
        if edit_port_kwargs:
            edit_port(Ports=ports, **edit_port_kwargs)
            time.sleep(10)
        if  testbed['tester']['wait_for_status_up']['default']:
            wait_port_state(ports)

    # 创建接口
    interfaces_up = create_interface(Port=port_up, Layers=['ipv4'])
    interfaces_down = create_interface(Port=port_down, Layers=['ipv4'])
    edit_interface(Interface=interfaces_up,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['mac_up_address']['default'])

    edit_interface(Interface=interfaces_down,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['mac_down_address']['default'])

    edit_interface(Interface=interfaces_up,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_up_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    edit_interface(Interface=interfaces_down,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_down_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_down_gateway']['default'])

    edit_port_load_profile(Ports=ports, TransmitMode='TIME', Rate=100, Seconds=30)
    sip_address_list = ['192.168.1.100','192.168.2.100']
    dip_address_list = ['192.168.3.1']

    # step5：tester port1 向 192.168.3.1 发送 ip 包，观察是否能收到正确的响应（网络不可达，类型为3，编码为0）；
    stream = add_stream(Ports=port_up, Names=f'stream1_2')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ipv4(Stream=stream, Source=sip_address_list[0], Destination=dip_address_list[0])

    stream = add_stream(Ports=port_down, Names=f'stream2_1')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ipv4(Stream=stream, Source=sip_address_list[1], Destination=dip_address_list[0])

    # 订阅统计视图
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['name'])))
    printf(message='Save case to xcfg')


    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试
        # 启动流量测试
        start_stream(Type='port', Objects=ports)
        time.sleep(5)
        wait_stream_state()

        # 获取端口流量结果
        Result = get_streamblock_statistic(Stream=stream, StaItems=['TxStreamFrames', 'RxStreamFrames'])
        TxStreamFrames = Result['TxStreamFrames']
        if TxStreamFrames == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{port_up.Name} TxStreamFrames({TxStreamFrames}) is equal to 0',
                step=3, result=False)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{port_up.Name} TxStreamFrames({TxStreamFrames}) is not equal to 0',
                step=3, result=True)

        result = get_streamblock_statistic(Stream=stream,
                                           StaItems=['TxStreamFrames', 'RxStreamFrames', 'TxTotalBytes',
                                                     'RxTotalBytes'])
        RxStreamFrames = Result['RxStreamFrames']
        if RxStreamFrames == TxStreamFrames:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'stream is avaliable',
                step=6, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'stream is not avaliable',
                step=6, result=False)
        clear_result()
        # 测试结束
        printf(message='Test completed')

        # 释放端口资源
        release_port(locations)

except Exception as e:
    CustomData.verdict = 'fail'
    CustomData.errInfo = repr(e)
finally:
    # 关闭仪表进程
    shutdown_tester()
    # 测试结束清除配置
    teardown(cfg, testbed)
    print(f'errInfo:\n{CustomData.errInfo}', flush=True)
    print(f'verdict:{CustomData.verdict}', flush=True)
