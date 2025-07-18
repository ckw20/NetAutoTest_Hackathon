# =================================================================================
# Objective   	:   Test Objective : 6.7.1 IP Broadcast Function
#
# Step			:	Test Step 1: Build the test environment according to Figure 10;
#                   Test Step 2: tester port1 address is 192.168.1.100/24, port2 address is 192.168.2.100/24;
#                   Test Step 3: DUT port1 address is 192.168.1.1/24, port2 address is 192.168.2.1/24; both port1 and port2 enable direct broadcast support;
#                   Test Step 4: tester port1 sends data packets with destination address 255.255.255.255;
#                   Test Step 5: tester port1 sends data packets with destination address 192.168.2.255;
#                   Test Step 6: DUT port2 configures route 192.168.3.0;
#                   Test Step 7: tester port1 sends data packets with destination address 192.168.3.255;
#                   Test Step 8: Record whether tester port2 receives broadcast packets in steps 4, 5, and 7.
#
# Criteria    	:   Expected Result 1: 1. Limited broadcast cannot be forwarded. 2. Layer 3 switch must make the network prefix direct broadcast effective.
#
# Created by   	:  	Tester-006
#
# Bugs   	    :  	None
# =================================================================================
import time
import sys
import os

dirname, filename = os.path.split(os.path.abspath(__file__))
ntolibrary_path = os.path.join(dirname, os.path.pardir, os.path.pardir)

# 将库的路径添加到 sys.path
if ntolibrary_path not in sys.path:
    sys.path.append(ntolibrary_path)

from CustomLibrary.common import cfg, testbed, setup, teardown, printf, temp_dir, get_locations, CustomData, \
    edit_port_params
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
    ports = reserve_port(Locations=locations, Force=testbed['tester']['force']['default'],
                         Debug=testbed['tester']['debug']['default'], WaitForStatusUp=False)
    port_up, port_down = ports
    if testbed['nto']['enable']['default']:
        nto = NTO(host=testbed['nto']['ip']['default'], port=testbed['nto']['port']['default'],
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
        if testbed['tester']['wait_for_status_up']['default']:
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

    port1, port2 = ports
    edit_port_load_profile(Ports=ports,
                           LoadProfileType='PORT_BASE',
                           Unit='FRAME_PER_SEC',
                           TransmitMode="CONTINUOUS",
                           Rate=100)
    # edit_port_load_profile(Ports=ports,
    #                        LoadProfileType='PORT_BASE',
    #                        TransmitMode="CONTINUOUS",
    #                        Frames=100,
    #                        Unit='FRAME_PER_SEC')
    # edit_port_load_profile(Ports=ports, TransmitMode='TIME', Rate=10, Seconds=30)
    sip_address_list = ['192.168.1.100']
    dip_address_list = ['255.255.255.255', '192.168.2.255', '192.168.3.255']

    # 创建广播流量
    # edit_port_load_profile(Ports=port1,LoadProfileType='PORT_BASE',Rate=30,Unit='FRAME_PER_SEC',TransmitMode="STEP",Frames=20)
    # tester port1 发送目的地址为255.255.255.255的数据包
    stream = add_stream(Ports=port1, Names=f'step4')
    edit_stream(Stream=stream, FixedLength=64)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ipv4(Stream=stream, Source=sip_address_list[0], Destination=dip_address_list[0],
                     Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    # tester port1 发送目的地址为192.168
    # .2.255的数据包；
    stream = add_stream(Ports=port1, Names=f'step5')

    edit_stream(Stream=stream, FixedLength=64, )
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ipv4(Stream=stream, Source=sip_address_list[0], Destination=dip_address_list[1],
                     Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    # tester port1 发送目的地址为192.168.3.255的数据包；
    stream = add_stream(Ports=port1, Names=f'step7')
    edit_stream(Stream=stream, FixedLength=64)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ipv4(Stream=stream, Source=sip_address_list[0], Destination=dip_address_list[2],
                     Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    edit_port_load_profile(Ports=port1, LoadProfileType='STREAM_BASE', TransmitMode='TIME', Seconds=30)

    # 订阅统计视图
    subscribe_result(Types=['StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试

        # 端口1测试
        # 启动二层学习
        start_l3_learning()
        time.sleep(5)
        clear_result()
        # 启动流量测试
        streams = get_streams(Ports=port1)
        start_stream(Type='stream', Objects=streams[0])
        time.sleep(5)
        wait_stream_state()

        # 检查统计结果
        # 获取端口流量结果
        Result = get_streamblock_statistic(Stream=streams[0],
                                           StaItems=['StreamBlockID', 'TxStreamFrames', 'RxStreamFrames'])
        TxStreamFrames = Result['TxStreamFrames']
        RxStreamFrames = Result['RxStreamFrames']
        StreamBlockID = Result['StreamBlockID']
        if TxStreamFrames > 0 and RxStreamFrames == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID}, tester port2 未收到广播包',
                step=3, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID} , tester port2 收到广播包',
                step=3, result=False)

        start_l3_learning()
        time.sleep(5)
        clear_result()
        # 启动流量测试
        start_stream(Type='stream', Objects=streams[1])
        time.sleep(5)
        wait_stream_state()

        # 检查统计结果
        # 获取端口流量结果
        Result = get_streamblock_statistic(Stream=streams[1],
                                           StaItems=['StreamBlockID', 'TxStreamFrames', 'RxStreamFrames'])
        TxStreamFrames = Result['TxStreamFrames']
        RxStreamFrames = Result['RxStreamFrames']
        StreamBlockID = Result['StreamBlockID']
        if TxStreamFrames > 0 and RxStreamFrames > 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID}, tester port2 收到广播包',
                step=4, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID} , tester port2 未收到广播包',
                step=4, result=False)

        start_l3_learning()
        time.sleep(5)
        clear_result()
        # 启动流量测试
        start_stream(Type='stream', Objects=streams[2])
        time.sleep(5)
        wait_stream_state()
        time.sleep(3)
        # 检查统计结果
        # 获取端口流量结果
        Result = get_streamblock_statistic(Stream=streams[2],
                                           StaItems=['StreamBlockID', 'TxStreamFrames', 'RxStreamFrames'])
        TxStreamFrames = Result['TxStreamFrames']
        RxStreamFrames = Result['RxStreamFrames']
        StreamBlockID = Result['StreamBlockID']
        if TxStreamFrames > 0 and RxStreamFrames > 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID}, tester port2 收到广播包',
                step=5, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID} , tester port2 未收到广播包',
                step=5, result=False)

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
