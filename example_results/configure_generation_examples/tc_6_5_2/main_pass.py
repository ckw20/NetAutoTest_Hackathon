# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.5.2 Priority QoS
#
# Step			:	Test Step 1: According to Figure 6, randomly select three switch ports to connect with the tester, assign as port 1, port 2, and port 3, configure the switch as absolute priority, set switch port trunk mode to ensure VLAN1 is not stripped;
#                   Test Step 2: Ports 1 and 2 send data to port 3 simultaneously;
#                   Test Step 3: Construct two data streams with priorities 7 and 5 on port 1, and two data streams with priorities 3 and 1 on port 2, set VLAN1 priorities as 7 and 5, 3 and 1;
#                   Test Step 4: Test with frame length of 64 bytes, test duration 30s, port load set to 100%;
#                   Test Step 5: Record the frame loss rate of different data streams, and determine whether the priority is set successfully.
#
# Criteria    	:   Expected Result 1: The frame loss rate of different data streams is consistent with the priority setting.
#
# Created by   	:  	Tester-008
#
# Tags   	    :  	function
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
    if testbed['nto']['enable']['default']:
        nto = NTO(host=testbed['nto']['ip']['default'], port=testbed['nto']['port']['default'], username=testbed['nto']['username']['default'], password=testbed['nto']['password']['default'], content_type='multipart/form-data')
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


    edit_port_load_profile(Ports=ports, TransmitMode='TIME', Rate=100, Seconds=30)
    port1,port2,port3=ports
    smac_address_list = ['00:00:00:13:40:21', '00:00:00:13:40:22', '00:00:00:13:40:23', '00:00:00:13:40:24']
    dmac_address_list = ['00:00:01:13:40:20', '00:00:01:13:40:21', '00:00:01:13:40:22', '00:00:01:13:40:23']
    # 端口1创建流量
    # 数据流 1：qos优先级为 7 的 IPv4 报文
    stream = add_stream(Ports=port1, Names=f'{port1.Name}_Priority_7')
    edit_stream(Stream=stream, FixedLength=64, RxPorts=port3)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[0], DestMacAdd=dmac_address_list[0])
    edit_header_vlan(Stream=stream, Priority=7)
    # 数据流 2：qos优先级为 5 的标识 的 IPv4 报文；
    stream = add_stream(Ports=port1, Names=f'{port1.Name}_Priority_5')
    edit_stream(Stream=stream, FixedLength=64, RxPorts=port3)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[1], DestMacAdd=dmac_address_list[1])
    edit_header_vlan(Stream=stream, Priority=5)

    # 端口2创建流量
    # 数据流 1：qos优先级为 3 的 IPv4 报文
    stream = add_stream(Ports=port2, Names=f'{port2.Name}_Priority_3')
    edit_stream(Stream=stream, FixedLength=64, RxPorts=port3)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii','vlan', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[2], DestMacAdd=dmac_address_list[2])
    edit_header_vlan(Stream=stream, Priority=3)
    # 数据流 2：qos优先级为 1 的标识 的 IPv4 报文；
    stream = add_stream(Ports=port2, Names=f'{port2.Name}_Priority_1')
    edit_stream(Stream=stream, FixedLength=64, RxPorts=port3)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii','vlan', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[3], DestMacAdd=dmac_address_list[3])
    edit_header_vlan(Stream=stream, Priority=1)

    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试

        # 端口1测试
        # 启动二层学习
        start_l2_learning()
        time.sleep(5)
        # 启动流量测试
        start_stream(Type='port', Objects=ports)
        time.sleep(5)
        wait_stream_state()
        time.sleep(5)
        # 检查统计结果
        # 获取端口流量结果
        # 获取端口1,2下所有流量统计结果
        streams_obj = get_streams(ports[:2])
        for stream in streams_obj:
            Result = get_streamblock_statistic(Stream=stream, StaItems=['TxStreamFrames', 'RxStreamFrames', 'TxPortID'])
            TxStreamFrames = Result['TxStreamFrames']
            RxStreamFrames = Result['RxStreamFrames']
            TxPortID = Result['TxPortID']
            StreamBlockID = Result['StreamBlockID']
            if TxStreamFrames == 0:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is equal to 0',
                    step=5, result=False)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is not equal to 0',
                    step=5, result=True)
            if RxStreamFrames != TxStreamFrames:
                if TxPortID == port2.Name:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})',
                        step=5, result=True)
                else:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})',
                        step=5, result=False)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames})',
                    step=5, result=True)
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
