# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.5.4 Port Mirroring: Support single-port mirroring and multi-port mirroring. The mirrored port should ensure the system-required forwarding rate without data loss.
#
# Step			:	Test Step 1: Test frame length is 64 bytes, test duration is not less than 30s;
#                   Test Step 2: Test configuration as shown in Figure 7, set port 4 of the switch as the mirror port, and ports 1 and 3 as mirrored ports, mirroring mode is both input and output;
#                   Test Step 3: Port 1 sends data bidirectionally to port 2, and port 2 and port 3 send data bidirectionally, with load rates of 25% respectively;
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

    smac_address_list = ['00:00:00:13:40:21', '00:00:00:13:40:22', '00:00:00:13:40:23', '00:00:00:13:40:24']
    dmac_address_list = ['00:00:01:13:40:20', '00:00:01:13:40:21', '00:00:01:13:40:22', '00:00:01:13:40:23']
    # 端口1创建绑定1-》2 流量
    # 数据流 1：untag 的 tcp 报文
    stream = add_stream(Ports=port1, Names=f'{port1.Name}_25%')
    edit_port_load_profile(Ports=port1, TransmitMode='TIME', Rate=25, Seconds=30)
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4', 'tcp'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[0], DestMacAdd=dmac_address_list[0])

    # 端口3创建创建绑定3-》2 流量
    edit_port_load_profile(Ports=port2, LoadProfileType='STREAM_BASE',TransmitMode='TIME', Seconds=30)
    # 数据流 1：vlan 200 的 tcp 报文
    stream = add_stream(Ports=port2, Names=f'{port2.Name}_vlan200_25%')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan','ipv4', 'tcp'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[1], DestMacAdd=dmac_address_list[1])
    edit_header_vlan(Stream=stream, ID=200)
    edit_stream_load_profile(Streams=stream,Rate= 25)
    # 数据流 2：vlan 4094 的 tcp 报文；
    stream = add_stream(Ports=port2, Names=f'{port2.Name}_vlan100_25%')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'vlan','ipv4', 'tcp'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[2], DestMacAdd=dmac_address_list[2])
    edit_header_vlan(Stream=stream, ID=100)
    edit_stream_load_profile(Streams=stream, Rate= 25)

    # 端口3创建绑定1-》2 绑定流量
    edit_port_load_profile(Ports=port3, TransmitMode='TIME', Rate=25, Seconds=30)
    # 数据流 1：untag 的 tcp 报文
    stream = add_stream(Ports=port3, Names=f'{port3.Name}_25%')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4', 'tcp'])
    edit_header_ethernet(Stream=stream, SourceMacAdd=smac_address_list[0], DestMacAdd=dmac_address_list[0])

    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['PortStats'])

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
        #清空统计计数
        clear_result()
        # 启动流量测试
        start_stream()
        time.sleep(5)
        wait_stream_state()
        time.sleep(3)
        # 检查统计结果
        # 获取端口流量结果
        result = get_port_statistic(StaItems=['TxStreamFrames', 'RxSignatureStreamFrames'])
        Port1_Result = get_port_statistic(Port=port1, StaItems=['TxStreamFrames', 'RxSignatureStreamFrames'])
        Port3_Result = get_port_statistic(Port=port3, StaItems=['TxStreamFrames', 'RxSignatureStreamFrames'])
        Port4_Result = get_port_statistic(Port=port4, StaItems=['TxStreamFrames', 'RxSignatureStreamFrames'])
        MirrotFrames = Port1_Result['TxStreamFrames']+Port1_Result['RxSignatureStreamFrames']+Port3_Result['TxStreamFrames']+Port3_Result['RxSignatureStreamFrames']
        RX_Result=Port4_Result['RxSignatureStreamFrames']
        if MirrotFrames == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{port1.Name} TxStreamFrames is equal to 0',
                step=3, result=False)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{port1.Name} TxStreamFrames is not equal to 0',
                step=3, result=True)

        if  MirrotFrames == RX_Result:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{port4.Name} RxStreamFrames({RX_Result}) is equal to TxStreamFrames({MirrotFrames})',
                step=4, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'{port4.Name} RxStreamFrames({RX_Result}) is not equal to TxStreamFrames({MirrotFrames})',
                step=4, result=False)
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
