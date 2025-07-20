# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.5.5 Multi-link Aggregation: No Data Loss During Link Aggregation
#
# Step			:	Test Step 1: Set up the test environment according to Figure 8;
#                   Test Step 2: Connect 2 ports of Switch 1 and 2 ports of Switch 2 correspondingly. Configure the 2 ports of Switch 1 as a static aggregation port, and the 2 ports of Switch 2 as a static aggregation port;
#                   Test Step 3: Tester ports 1 and 3 send data streams to ports 2 and 4 respectively, with a load rate of 100%;
#                   Test Step 4: Observe the receiving status of the streams on tester ports 2 and 4, there should be no packet loss;
#                   Test Step 5: Disconnect one link between Switch 1 and Switch 2, observe the receiving status of the streams, each should lose 50%;
#                   Test Step 6: Stop the data streams on ports 3 and 4, observe the receiving status of the streams on ports 1 and 2, there should be no packet loss.
#
# Criteria    	:   Expected Result 1: Record the number of frames received by port 4, and determine whether the mirroring function is set successfully.
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

    port1, port2, port3, port4 = ports
    smac_address_list = ['00:00:00:13:40:21', '00:00:00:13:40:22', '00:00:00:13:40:23', '00:00:00:13:40:24']
    dmac_address_list = ['00:00:01:13:40:20', '00:00:01:13:40:21', '00:00:01:13:40:22', '00:00:01:13:40:23']

    edit_port_load_profile(Ports=ports, TransmitMode='TIME', Rate=100, Seconds=30)
    # 端口1创建 流量
    # 数据流：untag 的 tcp 报文
    stream1 = add_stream(Ports=port1, Names=f'{port1.Name}_100%')
    edit_stream(Stream=stream1, FixedLength=128)
    create_stream_header(Stream=stream1, HeaderTypes=['ethernetii', 'ipv4', 'tcp'])
    edit_header_ethernet(Stream=stream1, SourceMacAdd=smac_address_list[0], DestMacAdd=dmac_address_list[0])
    # 端口3创建 流量
    # 数据流：untag 的 tcp 报文
    stream2 = add_stream(Ports=port3, Names=f'{port3.Name}_100%')
    edit_stream(Stream=stream2, FixedLength=128)
    create_stream_header(Stream=stream2, HeaderTypes=['ethernetii', 'ipv4', 'tcp'])
    edit_header_ethernet(Stream=stream2, SourceMacAdd=smac_address_list[1], DestMacAdd=dmac_address_list[1])
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
        # 清空统计计数
        clear_result()
        # 启动流量测试
        start_stream()
        time.sleep(5)
        wait_stream_state()
        time.sleep(3)
        # 检查统计结果
        # 获取流量结果
        # 检查统计结果，1,2口没有收到报文
        printf(message='step4：get  stream statistic')
        # 获取流量1统计结果
        Result1 = get_streamblock_statistic(Stream=stream1, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'TxTotalBytes',
                                                                    'RxTotalBytes'])
        Result2 = get_streamblock_statistic(Stream=stream2, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'TxTotalBytes',
                                                                    'RxTotalBytes'])
        if  Result1['TxStreamFrames']==Result1['RxStreamFrames'] and Result2['TxStreamFrames']==Result2['RxStreamFrames']:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'Stream RxStreamFrames is equal to TxStream1Frames', step=4, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'Stream RxStreamFrames is not equal to TxStream1Frames', step=4, result=False)
        # 断开交换机1 和2 之间的一条链路获取流量统计结果，各丢50%
        # 清空统计计数
        clear_result()
        # 启动流量测试
        start_stream()
        time.sleep(5)
        wait_stream_state()
        time.sleep(3)
        Result1 = get_streamblock_statistic(Stream=stream1, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'TxTotalBytes',
                                                                    'RxTotalBytes'])
        Result2 = get_streamblock_statistic(Stream=stream2, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'TxTotalBytes',
                                                                    'RxTotalBytes'])
        if  Result1['TxStreamFrames']==Result1['RxStreamFrames']*2 and Result2['TxStreamFrames']==Result2['RxStreamFrames']*2:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'Stream RxStreamFrames is equal to TxStream1Frames', step=4, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'Stream RxStreamFrames is not equal to TxStream1Frames', step=4, result=False)
        # 断开交换机1 和2 之间的一条链路获取流量统计结果，各丢50%
        # 清空统计计数
        clear_result()
        # 启动流量测试
        start_stream()
        time.sleep(10)
        # 停止3口流量
        stop_stream(Type='stream',Objects=stream2)
        wait_stream_state()
        time.sleep(3)
        Result1 = get_streamblock_statistic(Stream=stream1, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                      'RxStreamFrames', 'TxTotalBytes',
                                                                      'RxTotalBytes'])
        Result2 = get_streamblock_statistic(Stream=stream2, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                      'RxStreamFrames', 'TxTotalBytes',
                                                                      'RxTotalBytes'])
        if Result1['TxStreamFrames'] == Result1['RxStreamFrames']  and Result2['TxStreamFrames'] == Result2[
            'RxStreamFrames'] :
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'Stream RxStreamFrames is equal to TxStream1Frames', step=4, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'Stream RxStreamFrames is not equal to TxStream1Frames', step=4, result=False)
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
