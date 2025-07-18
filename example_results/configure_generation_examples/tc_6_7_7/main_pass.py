# =================================================================================
# Objective   	:   Test Objective : 6.7.7 Virtual Router Redundancy Protocol (VRRP)
#
# Step			:	Test Step 1: Build the test environment according to Figure 12
#                   Test Step 2: DUT1 and DUT4 are connected to the switch at Layer 2
#                   Test Step 3: DUT2 (master) and DUT3 (backup) form a dual-router redundancy, a heartbeat line can be added between the two;
#                   Test Step 4: tester port1 IP address is 192.168.1.100/24, port2 is 192.168.2.100/24
#                   Test Step 5: DUT2 port1 and DUT3 port1 act as the gateway for 192.168.1.0/24, virtual IP is 192.168.1.1/24;
#                   Test Step 6: DUT2 port2 and DUT3 port2 act as the gateway for 192.168.2.0/24, virtual IP is 192.168.2.1/24;
#                   Test Step 7: tester builds a stream from port1 to port2, frame length is 256 bytes, stream rate is 10000 frames/sec, gateway is set to the virtual IP of the VRRP group, check and record the data reception
#                   Test Step 8: Disconnect the connection between DUT1 and the VRRP master, check and record the VRRP status and data loss on DUT2 and DUT3, calculate VRRP convergence time based on the number of lost packets and sending rate; restore the switch link, check the VRRP status on DUT2 and DUT3, resend the data stream;
#                   Test Step 9: Repeat steps 7 and 8 twice.
# Criteria    	:   Expected Result 1:
#
# Created by   	:  	Tester-006
#
# Bugs   	    :  	None
# =================================================================================
import sys
import os

dirname, filename = os.path.split(os.path.abspath(__file__))
ntolibrary_path = os.path.join(dirname, os.path.pardir, os.path.pardir)

# 将库的路径添加到 sys.path
if ntolibrary_path not in sys.path:
    sys.path.append(ntolibrary_path)

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

    # tester 构建port1至port2 的流量，帧长设置为256bytes，流量设置为10000 帧/秒，10.1.1.111
    edit_port_load_profile(Ports=ports,
                           LoadProfileType='PORT_BASE',
                           Unit='FRAME_PER_SEC',
                           TransmitMode="CONTINUOUS",
                           Frames=10000)

    stream = add_stream(Ports=port_up, Names=f'stream1')
    edit_stream(Stream=stream, FixedLength=256)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ipv4(Stream=stream, Source=cfg['arg']['interface']['default']['ipv4_up_address'],
                     Destination=cfg['arg']['interface']['default']['ipv4_down_address'],Gateway ='10.1.1.111')

    # 订阅统计视图
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])
    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['name'])))
    printf(message='Save case to xcfg')


    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试
        # 启动流量测试
        for i in range(2):
            start_stream()
            time.sleep(5)
            wait_stream_state()
            stop_stream()
            Result = get_streamblock_statistic(Stream=stream, StaItems=['TxStreamFrames', 'RxStreamFrames'])
            TxStreamFrames = Result['TxStreamFrames']
            RxStreamFrames = Result['RxStreamFrames']
            if RxStreamFrames != TxStreamFrames or TxStreamFrames == 0:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})',
                    step=4, result=False)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames})',
                    step=4, result=True)

            clear_result()

            start_stream()
            # 断开交换机DUT1与VRRP主机的连接,，查看并记录DUT2、DUT3上VRRP的状态及数据的丢失情况，根据丢包数量和发包速率计算VRRP的收敛时间
            time.sleep(5)
            wait_stream_state()
            stop_stream()
            Result = get_streamblock_statistic(Stream=stream, StaItems=['TxStreamFrames', 'RxStreamFrames'])
            TxStreamFrames = Result['TxStreamFrames']
            RxStreamFrames = Result['RxStreamFrames']
            #VRRP的收敛时间
            Convergence_time = (TxStreamFrames - RxStreamFrames)/TxStreamFrames
            clear_result()
            #恢复交换机链路，查看DUT2、DUT3上VRRP的状态，重新发送数据流
            start_stream()
            time.sleep(5)
            wait_stream_state()
            stop_stream()
            Result = get_streamblock_statistic(Stream=stream, StaItems=['TxStreamFrames', 'RxStreamFrames'])
            TxStreamFrames = Result['TxStreamFrames']
            RxStreamFrames = Result['RxStreamFrames']
            if RxStreamFrames != TxStreamFrames or TxStreamFrames == 0:
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
