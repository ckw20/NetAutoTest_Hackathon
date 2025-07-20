# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.5.8 Network Storm Suppression: Should support broadcast storm suppression, multicast storm suppression, and unknown unicast storm suppression functions. By default, broadcast storm suppression is enabled.
#
# Step			:	Test Step 1: Connect the traffic generator to the switch, as shown in Figure 4;
#                   Test Step 2: Set the test frame length to 64, port load to full load, and test duration to 30s;
#                   Test Step 3: Enable broadcast storm suppression, multicast storm suppression, and unknown unicast storm suppression functions on the switch;
#                   Test Step 4: Set the suppression value to 1M+ granularity;
#                   Test Step 5: Port 1 sends 3 streams to port 2, namely Stream1 (broadcast frame), Stream2 (broadcast frame), Stream3 (IPv4 frame); port 2 sends 2 streams to port 1, namely Stream1 (multicast frame), Stream2 (unknown unicast frame);
#                   Test Step 6: Record the frame loss rate of different streams and determine whether the network storm suppression function is set successfully;
#                   Test Step 7: Calculate the deviation ratio of network storm suppression according to the frame loss rate.
#
# Criteria    	:   Expected Result 1: Should support broadcast storm suppression, multicast storm suppression, and unknown unicast storm suppression functions, and broadcast storm suppression is enabled by default;
#                   Expected Result 2: The actual suppression value of the network storm should not exceed 110% of the set suppression value.
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

    port1, port2 = ports
    edit_port_load_profile(Ports=ports, TransmitMode='TIME', Rate=100, Seconds=30)
    smac_address_list = ['00:00:00:13:40:21', '00:00:00:13:40:22', '00:00:00:13:40:23', '00:00:00:13:40:24']
    dmac_address_list = ['ff:ff:ff:ff:ff:ff', '01:00:00:13:40:22', '00:00:01:13:40:22', '01:00:5E:00:01:01']
    # 端口1创建流量
    # 数据流 1：Stream1(广播帧)
    stream = add_stream(Ports=port1, Names=f'Stream1(广播帧)')
    edit_stream(Stream=stream, FixedLength=64)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[0], DestMacAdd=dmac_address_list[0])
    # 数据流 2：Stream2(广播帧)；
    stream = add_stream(Ports=port1, Names=f'Stream2(广播帧)')
    edit_stream(Stream=stream, FixedLength=64)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[1], DestMacAdd=dmac_address_list[0])
    # 数据流 3：Stream3(IPv4帧)；
    stream = add_stream(Ports=port1, Names=f'IPv4帧')
    edit_stream(Stream=stream, FixedLength=64)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[2], DestMacAdd=dmac_address_list[2])

    # 端口2创建流量
    # 数据流 1：Stream1（组播帧)
    stream = add_stream(Ports=port2, Names=f'Stream2（组播帧)')
    edit_stream(Stream=stream, FixedLength=64)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[1], DestMacAdd=dmac_address_list[3])
    # 数据流 2：Stream2（未知单播帧)
    stream = add_stream(Ports=port2, Names=f'Stream3（未知单播帧)')
    edit_stream(Stream=stream, FixedLength=64)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[3], DestMacAdd=dmac_address_list[2])

    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试

        # 端口1测试
        # 启动流量测试
        start_stream(Type='port', Objects=port1)
        time.sleep(5)
        wait_stream_state()
        time.sleep(3)
        streams_obj = get_streams(port1)
        for stream in streams_obj:
            # 获取流量统计结果
            Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                        'RxStreamFrames', 'RxLossStreamFrames',
                                                                        'RealtimeLossRate'])
            StreamBlockID = Result['StreamBlockID']
            if Result['RealtimeLossRate'] > 99:
                    CustomData.verdict, CustomData.errInfo = printf(
                        message=f'{StreamBlockID}网络风暴抑制成功', step=5, result=True)
            else:
                if 'IPv4' in StreamBlockID:
                    if Result['TxStreamFrames'] == Result['RxStreamFrames']:
                        CustomData.verdict, CustomData.errInfo = printf(
                            message=f'{StreamBlockID}转发成功', step=5, result=True)
                    else:
                        CustomData.verdict, CustomData.errInfo = printf(
                            message=f'{StreamBlockID}转发失败或者风暴抑制失败', step=5, result=False)

        clear_result()
        # 端口2测试
        start_stream(Type='port', Objects=port2)
        time.sleep(5)
        wait_stream_state()
        time.sleep(3)
        streams_obj = get_streams(port2)
        for stream in streams_obj:
            # 获取流量统计结果
            Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                        'RxStreamFrames', 'RxLossStreamFrames',
                                                                        'RealtimeLossRate'])
            StreamBlockID = Result['StreamBlockID']
            if Result['RealtimeLossRate'] > 99:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID}网络风暴抑制成功', step=5, result=True)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID}网络风暴抑制失败', step=5, result=False)
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
