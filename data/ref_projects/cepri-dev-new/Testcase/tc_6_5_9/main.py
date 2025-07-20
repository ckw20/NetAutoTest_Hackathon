# =================================================================================
# Objective   	:   Test Objective : 6.5.9 Spanning Tree Protocol
#
# Step			:	Test Step 1: Connect 4 switches as shown in Figure 9, all uplink ports use 100M optical ports;
#                   Test Step 2: The whole network runs the standard spanning tree protocol, configure the spanning tree parameters of each device;
#                   Test Step 3: Observe whether the device can prune the ring according to the configured parameters and complete the spanning tree;
#                   Test Step 4: Block the current spanning tree link of the device, observe whether the device can automatically complete network convergence and reconstruction;
#                   Test Step 5: Enable RSTP function on all switches;
#                   Test Step 6: Connect the switches as shown in Figure 9;
#                   Test Step 7: Use SmartBits to load 95Mbps data stream between any two switches;
#                   Test Step 8: Unplug any link in the ring network, check whether the network can recover normally
#
# Criteria    	:   Expected Result 1:
#
# Created by   	:  	Tester-006
#
# Bugs   	    :  	None
# =================================================================================

from CustomLibrary.common import cfg, testbed, setup, teardown, printf, temp_dir, get_locations, CustomData, edit_port_params
from NtoLibrary.common import NTO
from TesterLibrary.base import *


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
    ports = reserve_port(Locations=locations, Force=testbed['tester']['force']['default'], Debug=testbed['tester']['debug']['default'], WaitForStatusUp=False)
    port_up, port_down = ports
    if testbed['nto']['enable']['default']:
        nto = NTO(host=testbed['nto']['ip'], port=testbed['nto']['port']['default'], username=testbed['nto']['username']['default'], password=testbed['nto']['password']['default'], content_type='multipart/form-data')
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
    port1, port2 = ports
    edit_port_load_profile(Ports=ports,
                           LoadProfileType='PORT_BASE',
                           Unit='FRAME_PER_SEC',
                           TransmitMode="CONTINUOUS",
                           Rate=95,)

    smac_address_list = ['00:00:00:13:40:21']
    dmac_address_list = ['00:00:01:13:40:20']

    stream1 = add_stream(Ports=port1, Names=f'stream1')
    edit_stream(Stream=stream1, FixedLength=64)
    create_stream_header(Stream=stream1, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ethernet(Stream=stream1, SourceMacAdd=smac_address_list[0], DestMacAdd=dmac_address_list[0])

    # 订阅统计视图
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['name'])))
    printf(message='Save case to xcfg')


    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试

        # 端口1测试
        # 启动二层学习
        start_l2_learning()
        time.sleep(5)
        # 启动流量测试
        start_stream(Type='stream', Objects=stream1)
        #拔插链路
        time.sleep(30)

        # 查看收敛时间
        Result = get_streamblock_statistic(Stream=stream1, StaItems=['TxStreamFrames', 'RxStreamFrames'])
        TxStreamFrames = Result['TxStreamFrames']
        RxStreamFrames = Result['RxStreamFrames']
        Result = get_streamblock_statistic(Stream=stream1, StaItems=['TxStreamFrames', 'RxStreamFrames'])
        TxStreamFrames = Result['TxStreamFrames']
        RxFCSErr = Result['RxFCSErr']
        if TxStreamFrames == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'stream1 TxStreamFrames({TxStreamFrames}) is equal to 0',
                step=3, result=False)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'stream1 TxStreamFrames({TxStreamFrames}) is not equal to 0',
                step=3, result=True)

        if RxStreamFrames != TxStreamFrames:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})',
                step=4, result=False)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames})',
                step=4, result=True)

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
