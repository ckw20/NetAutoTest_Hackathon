# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.5.6 IGMP-Snooping Multicast: Layer 2 Switch Should Support IGMP-Snooping Multicast Function
#
# Step			:	Test Step 1: Connect the traffic generator and the switch as shown in Figure 4, switch ports are untagged ports within the same VLAN;
#                   Test Step 2: Port 1 sends a multicast stream to port 2;
#                   Test Step 3: Disable IGMP Snooping function on the tested switch, observe the receiving status of the stream on port 2;
#                   Test Step 4: Enable IGMP Snooping function on the tested switch, observe the receiving status of the stream on port 2;
#                   Test Step 5: Port 2 joins the multicast group using IGMPv2, observe the receiving status of the stream on port 2;
#                   Test Step 6: Port 2 sends a leave group request, observe the receiving status of the stream on port 2.
#
# Criteria    	:   Expected Result 1: Step 2) When IGMP Snooping is disabled on the tested switch, all ports should be able to receive the multicast stream;
#                   Expected Result 2: Step 3) When IGMP Snooping is enabled on the tested switch, non-multicast client ports should not receive the multicast stream;
#                   Expected Result 3: Step 4) After port 2 sends a join group request, it should be able to receive the multicast stream;
#                   Expected Result 4: Step 5) After port 2 sends a leave group request, it should not receive the multicast stream.
#
# Created by   	:  	Tester-008
#
# Tags   	    :  	function
# =================================================================================
import time
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

    port_1, port_2 = ports
    # 创建接口
    interface_1 = create_interface(Port=port_1,Layers=['eth', 'ipv4'])
    interface_2 = create_interface(Port=port_2,Layers=['eth', 'ipv4'])

    # 创建IGMP协议会话
    igmp = create_igmp(Port=port_2, Version='IGMPV2')

    # IGMP协议会话与接口绑定
    select_interface(Session=igmp, Interface=interface_2)

    # 创建全局组播组
    multicast_group = create_multicast_group(Start='225.0.1.2',Count=1)

    # 创建组播协议和组播组绑定关系对象
    memberships = create_memberships(Session=igmp)

    # IGMP协议会话组成员关系与组播组绑定
    binding_multicast_group(Session=igmp, Memberships=memberships, MulticastGroup=multicast_group)

    # 创建IGMP绑定流
    src_point = get_layer_from_interfaces(Interfaces=interface_1)

    stream = add_stream(Type='binding', SrcPoints=src_point, DstPoints=multicast_group, Bidirection=False)

    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试

        # 清空统计计数
        clear_result()
        # 启动流量测试
        start_stream()
        time.sleep(10)
        stop_stream()
        time.sleep(5)
        # 获取流量统计结果
        Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'RxLossStreamFrames',
                                                                    'RealtimeLossRate'])
        if  Result['RxStreamFrames'] > 0  and Result['RxLossStreamFrames'] == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'在被测交换机上禁用IGMP Snooping 功能时，所有端口应均可接收到组播流量', step=5, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'在被测交换机上禁用IGMP Snooping 功能时，没有所有端口都接收到组播流量', step=5, result=False)

        # 被测设备使能igmp snooping
        cmd_cfg = '_'.join('DeviceA_Step3'.split('_')[1:])
        for _ in range(3):
            flag = device['DeviceA'].execute(row=cmd_cfg)
            if flag:
                break
        # 清空统计计数
        clear_result()
        # 启动协议
        start_protocol()

        # 等待IGMP协议会话稳定状态
        wait_igmp_state(Sessions=[igmp])
        # 启动流量测试
        start_stream()
        time.sleep(10)
        stop_stream()
        time.sleep(5)
        printf(message='step3：端口1向端口2发送1个组的组播流量, 在被测交换机上启用IGMP Snooping 功能')
        Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'TxTotalBytes',
                                                                    'RxTotalBytes'])
        if  Result['TxStreamFrames'] == Result['RxStreamFrames']:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'在被测交换机上启用IGMP Snooping 功能时，非组播客户端端不能接收组播流量', step=5, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'在被测交换机上启用IGMP Snooping 功能时，非组播客户端端不能接收组播流量', step=5, result=False)

        igmp_send_report(Sessions=igmp)
        time.sleep(3)
        # 清空统计计数
        clear_result()
        # 启动流量测试
        start_stream()
        time.sleep(10)
        stop_stream()
        time.sleep(5)
        Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                      'RxStreamFrames', 'TxTotalBytes',
                                                                      'RxTotalBytes'])
        if Result['TxStreamFrames'] == Result['RxStreamFrames']:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'端口2 发送组加入请求后，可接收组播流量', step=5, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'端口2 发送组加入请求后，可接收组播流量', step=5, result=False)

        igmp_send_leave(Sessions=igmp)
        # 清空统计计数
        clear_result()
        # 启动流量测试
        start_stream()
        time.sleep(10)
        stop_stream()
        time.sleep(5)
        Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'TxTotalBytes',
                                                                    'RxTotalBytes'])
        if Result['TxStreamFrames'] != Result['RxStreamFrames'] and Result['RxStreamFrames'] == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'端口2 发送离开组请求后，不能接收组播流量', step=5, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'端口2 发送离开组请求后，不能接收组播流量', step=5, result=False)
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
