# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.5.3 Head-of-Line Blocking Test
#
# Step			:	Test Step 1: According to Figure 7, randomly select 4 switch ports to connect with the tester, assign as port A, port B, port C, and port D;
#                   Test Step 2: Both the tester and switch disable flow control, port 1 sends 100% traffic to port 2, port 3 sends 50% traffic to port 2, port 3 sends 50% traffic to port 4;
#                    1) Create untagged traffic on port connected to switch access vlan 100,
#                    2) Port connected to switch trunk vlan 100,200
#                    3) Create vlan 200, vlan4094 traffic on port connected to switch trunk vlan 200,4094
#                    4) Port connected to switch access vlan 4094
#                   Test Step 3: Record whether there is packet loss on port D.
#
# Criteria    	:   Expected Result 1: Record whether there is packet loss on port D.
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

    port1, port2, port3, port4 = ports
    edit_port_load_profile(Ports=port1, TransmitMode='TIME', Rate=100, Seconds=30)

    smac_address_list = ['00:00:00:13:40:21', '00:00:00:13:40:22', '00:00:00:13:40:23', '00:00:00:13:40:24']
    dmac_address_list = ['00:00:01:13:40:20', '00:00:01:13:40:21', '00:00:01:13:40:22', '00:00:01:13:40:23']
    # 端口1创建绑定1-》2 绑定流量
    # 数据流 1：untag 的 tcp 报文
    stream = add_stream(Ports=port1, Names=f'{port1.Name}_100%')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan', 'ipv4', 'tcp'])
    edit_header_vlan(Stream=stream, ID=100)
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[0], DestMacAdd=dmac_address_list[0])

    # 端口3创建创建绑定3-》2 绑定流量
    edit_port_load_profile(Ports=port3, LoadProfileType='STREAM_BASE',TransmitMode='TIME', Seconds=30)
    #edit_port_load_profile(Ports=port3, Seconds=30)
    # 数据流 1：vlan 200 的 tcp 报文
    stream = add_stream(Ports=port3, Names=f'{port3.Name}_vlan200_50%')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan','ipv4', 'tcp'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[1], DestMacAdd=dmac_address_list[1])
    edit_header_vlan(Stream=stream, ID=200)
    edit_stream_load_profile(Streams=stream,Rate= 50)
    # 数据流 2：vlan 4094 的 tcp 报文；
    stream = add_stream(Ports=port3, Names=f'{port3.Name}_vlan4094_50%')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan','ipv4', 'tcp'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[2], DestMacAdd=dmac_address_list[2])
    edit_header_vlan(Stream=stream, ID=4094)
    edit_stream_load_profile(Streams=stream, Rate=50)
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

        # 检查统计结果
        # 获取端口流量结果
        stream1=get_streams(Ports=port1)
        Result = get_streamblock_statistic(Stream=stream1, StaItems=['TxStreamFrames', 'RxStreamFrames'])
        TxStreamFrames = Result['TxStreamFrames']
        StreamBlockID = Result['StreamBlockID']
        if TxStreamFrames == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is equal to 0',
                step=3, result=False)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is not equal to 0',
                step=3, result=True)
        stream_object = get_streams(Ports=port3)
        for stream in stream_object:
            Result = get_streamblock_statistic(Stream=stream, StaItems=['TxStreamFrames', 'RxStreamFrames'])
            TxStreamFrames = Result['TxStreamFrames']
            StreamBlockID = Result['StreamBlockID']
            if TxStreamFrames == 0:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is equal to 0',
                    step=3, result=False)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'{StreamBlockID} TxStreamFrames({TxStreamFrames}) is not equal to 0',
                    step=3, result=True)

        stream = stream_object[1]
        result = get_streamblock_statistic(Stream=stream,
                                           StaItems=['TxStreamFrames', 'RxStreamFrames', 'TxTotalBytes',
                                                     'RxTotalBytes'])
        RxStreamFrames = Result['RxStreamFrames']
        StreamBlockID = Result['StreamBlockID']
        if RxStreamFrames != TxStreamFrames:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is not equal to TxStreamFrames({TxStreamFrames}),端口D丢包',
                step=4, result=False)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{StreamBlockID} RxStreamFrames({RxStreamFrames}) is equal to TxStreamFrames({TxStreamFrames}),端口D未丢包',
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
