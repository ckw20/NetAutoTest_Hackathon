# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.5.1 Virtual LAN (VLAN) Function
#
# Step			:	Test Step 1: Test with frame length of 128 bytes, test duration is 30;
#                   Test Step 2: Randomly select 3 ports to connect with the tester, test configuration as shown in Figure 6;
#                   Test Step 3: Construct 7 data streams on tester port 3;
#                   Test Step 4: Set all switch ports as untagged, port A as VLAN100, port B as VLAN4094, port C as TRUNK port and VLAN1, others as default;
#                   Test Step 5: Tester port 3 sends 10% load of data to port 1 and port 2 respectively;
#                   Test Step 6: Record the frame loss rate of different data streams, and determine whether VLAN division is successful;
#                   Test Step 7: Construct above 7 data streams on tester port 1 and port 2;
#                   Test Step 8: Port 1 and port 2 send 10% load of data to port 3 respectively;
#                   Test Step 9: Record the frame loss rate of different data streams, and determine whether VLAN TRUNK is successful.
#
# Criteria    	:   Expected Result 1: Data streams sent from tester to switch, if VLAN IDs are different, switch discards the data stream (not forwarded at ingress) or forwards to corresponding VLAN port (forwarded at ingress); if same, forwards to the same VLAN port. Broadcast storms are limited within VLAN.
#
# Created by   	:  	Tester-001
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

    edit_port_load_profile(Ports=ports, TransmitMode='TIME', Rate=10, Seconds=30)

    # 端口1创建流量
    mac_address_list = ['00:02:00:00:00:01', '00:02:00:00:00:02', '00:02:00:00:00:03']
    vlan_id_list = [100, 4094, 1]

    # interfaces_1 = create_interface(Port=ports[0], Layers=['eth', 'vlan'])
    # interfaces_2 = create_interface(Port=ports[1], Layers=['eth', 'vlan'])
    # interfaces_3 = create_interface(Port=ports[2], Layers=['eth', 'vlan'])
    # edit_interface(Interface=interfaces_1,
    #                Layer='EthIILayer',
    #                Address=mac_address_list[0])
    # edit_interface(Interface=interfaces_2,
    #                Layer='EthIILayer',
    #                Address=mac_address_list[1])
    # edit_interface(Interface=interfaces_3,
    #                Layer='EthIILayer',
    #                Address=mac_address_list[2])
    # edit_interface(Interface=interfaces_1,
    #                Layer='VLANLayer',
    #                VlanId=vlan_id_list[0])
    # edit_interface(Interface=interfaces_2,
    #                Layer='VLANLayer',
    #                VlanId=vlan_id_list[1])
    # edit_interface(Interface=interfaces_3,
    #                Layer='VLANLayer',
    #                VlanId=vlan_id_list[2])

    streams = {}
    # 端口创建7条流量
    number = -1
    for port in ports:
        number += 1
        test_mac_address = mac_address_list.copy()
        source_mac = test_mac_address.pop(number)
        # 数据流 1：无 VID 标识 IPv4 报文
        stream = add_stream(Ports=port, Names=f'{port.Name}_VID_NO')
        edit_stream(Stream=stream, FixedLength=128)
        create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
        params = edit_header_ethernet(Stream=stream, SourceMacAdd=source_mac, DestMacAdd=mac_address_list[1])
        edit_modifier(Stream=stream, Attribute=params['DestMacAdd'], Type='List', List=test_mac_address,
                      StreamType='InterModifier')
        streams.update({stream[0].Name: stream})

        # 数据流 2：VID 为 100 的 IPv4 报文；
        stream = add_stream(Ports=port, Names=f'{port.Name}_VID_100')
        edit_stream(Stream=stream, FixedLength=128)
        create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan', 'ipv4'])
        params = edit_header_ethernet(Stream=stream, SourceMacAdd=source_mac, DestMacAdd=mac_address_list[1])
        edit_modifier(Stream=stream, Attribute=params['DestMacAdd'], Type='List', List=test_mac_address,
                      StreamType='InterModifier')
        edit_header_vlan(Stream=stream, ID=vlan_id_list[0])
        streams.update({stream[0].Name: stream})

        # 数据流 3：VID 为 4094 的 IPv4 报文；
        stream = add_stream(Ports=port, Names=f'{port.Name}_VID_4094')
        edit_stream(Stream=stream, FixedLength=128)
        create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan', 'ipv4'])
        params = edit_header_ethernet(Stream=stream, SourceMacAdd=source_mac, DestMacAdd=mac_address_list[1])
        edit_modifier(Stream=stream, Attribute=params['DestMacAdd'], Type='List', List=test_mac_address,
                      StreamType='InterModifier')
        edit_header_vlan(Stream=stream, ID=vlan_id_list[1])
        streams.update({stream[0].Name: stream})

        # 数据流 4：无 VID 标识的组播报文；
        stream = add_stream(Ports=port, Names=f'{port.Name}_VID_NO_Multicast ')
        edit_stream(Stream=stream, FixedLength=128)
        create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
        params = edit_header_ethernet(Stream=stream, SourceMacAdd=source_mac, DestMacAdd=mac_address_list[1])

        edit_modifier(Stream=stream, Attribute=params['DestMacAdd'], Type='List', List=test_mac_address,
                      StreamType='InterModifier')
        edit_header_ipv4(Stream=stream, Destination='225.0.0.1')
        streams.update({stream[0].Name: stream})
        # 数据流 5：VID 为 100 的组播报文；
        stream = add_stream(Ports=port, Names=f'{port.Name}_VID_100_Multicast ')
        edit_stream(Stream=stream, FixedLength=128)
        create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan', 'ipv4'])
        params = edit_header_ethernet(Stream=stream, SourceMacAdd=source_mac, DestMacAdd=mac_address_list[1])
        edit_modifier(Stream=stream, Attribute=params['DestMacAdd'], Type='List', List=test_mac_address,
                      StreamType='InterModifier')
        edit_header_vlan(Stream=stream, ID=vlan_id_list[0])
        edit_header_ipv4(Stream=stream, Destination='225.0.0.1')
        streams.update({stream[0].Name: stream})

        # 数据流 6：VID 为 4094 的组播报文；
        stream = add_stream(Ports=port, Names=f'{port.Name}_VID_4094_Multicast ')
        edit_stream(Stream=stream, FixedLength=128)
        create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan', 'ipv4'])
        params = edit_header_ethernet(Stream=stream, SourceMacAdd=source_mac, DestMacAdd=mac_address_list[1])
        edit_modifier(Stream=stream, Attribute=params['DestMacAdd'], Type='List', List=test_mac_address,
                      StreamType='InterModifier')
        edit_header_vlan(Stream=stream, ID=vlan_id_list[1])
        edit_header_ipv4(Stream=stream, Destination='225.0.0.1')
        streams.update({stream[0].Name: stream})

        # 数据流 7：广播报文，无 VID 标识；
        stream_port1_VID_100 = add_stream(Ports=port, Names=f'{port.Name}_VID_NO_Broadcast')
        edit_stream(Stream=stream_port1_VID_100, FixedLength=128)
        create_stream_header(Stream=stream_port1_VID_100, HeaderTypes=['ethernetii', 'ipv4'])
        params = edit_header_ethernet(Stream=stream_port1_VID_100, SourceMacAdd=source_mac,
                                      DestMacAdd='ff:ff:ff:ff:ff:ff')
        streams.update({stream[0].Name: stream})

    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试
        # 步骤5：端口3发流量测试
        printf(message='step5：port3 start stream')
        start_stream(Type='port', Objects=ports[2])
        time.sleep(5)
        wait_stream_state()

        # 检查统计结果，1,2口没有收到报文
        printf(message='step6：get port3 stream statistic')
        # 获取端口3下所有流量统计结果
        streams_obj = get_streams(ports[2])
        for stream in streams_obj:
            Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                        'RxStreamFrames', 'TxTotalBytes',
                                                                        'RxTotalBytes'])
            # 判断流量是否发出
            TxStreamFrames = Result['TxStreamFrames']
            RxStreamFrames = Result['RxStreamFrames']
            StreamBlockID = Result['StreamBlockID']
            RxPortID = Result['RxPortID']
            if TxStreamFrames == 0:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is equal to 0', step=6, result=False)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is not equal to 0', step=6, result=True)

            if 'VID_NO' in StreamBlockID:
                if RxStreamFrames == 0:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to 0', step=6, result=True)
                else:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to 0', step=6,
                        result=False)
            if 'VID_100' in StreamBlockID:
                if RxStreamFrames == TxStreamFrames and RxPortID == 'Port_1':
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames}),RxPortID is ({RxPortID})',
                        step=6, result=True)
                else:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})) or RxPortID is not({RxPortID})',
                        step=6,
                        result=False)
            if 'VID_4094' in StreamBlockID:
                if RxStreamFrames == TxStreamFrames and RxPortID == 'Port_2':
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames}),RxPortID is ({RxPortID})',
                        step=6, result=True)
                else:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})) or RxPortID is not({RxPortID})',
                        step=6,
                        result=False)
        clear_result()
        # 步骤8：端口1，2发流量测试
        printf(message='step8：port1,port2 start stream')
        start_stream(Type='port', Objects=ports[:2])
        time.sleep(5)
        wait_stream_state()

        # 检查统计结果，3口收到报文
        # 获取端口流量结果
        # 获取端口1,2下所有流量统计结果
        streams_obj = get_streams(ports[:2])
        for stream in streams_obj:
            Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                        'RxStreamFrames', 'TxTotalBytes',
                                                                        'RxTotalBytes'])
            # 判断流量是否发出
            TxStreamFrames = Result['TxStreamFrames']
            RxStreamFrames = Result['RxStreamFrames']
            StreamBlockID = Result['StreamBlockID']
            RxPortID = Result['RxPortID']
            if TxStreamFrames == 0:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is equal to 0', step=9, result=False)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is not equal to 0', step=9, result=True)

            if 'VID_NO' in StreamBlockID:
                if RxStreamFrames == TxStreamFrames:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames}))',
                        step=9, result=True)
                else:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})',
                        step=9, result=False)
            if 'Port_1_VID_100' in StreamBlockID:
                if RxStreamFrames == TxStreamFrames and RxPortID == 'Port_3':
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames}),RxPortID is ({RxPortID})',
                        step=9, result=True)
                else:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})) or RxPortID is not({RxPortID})',
                        step=9,
                        result=False)
            if 'Port_2_4094' in StreamBlockID:
                if RxStreamFrames == TxStreamFrames and RxPortID == 'Port_2':
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames}),RxPortID is ({RxPortID})',
                        step=9, result=True)
                else:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames})) or RxPortID is not({RxPortID})',
                        step=9,
                        result=False)
            else:
                if RxStreamFrames == 0:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to 0,RxPortID is ({RxPortID})',
                        step=9, result=True)
                else:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to 0',
                        step=9, result=True)

        # 释放端口资源
        release_port(locations)
        printf(message='Test completed')

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
