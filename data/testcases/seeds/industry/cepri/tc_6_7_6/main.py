# =================================================================================
# Objective   	:   测试目的 :  开放式最短路径优先路由协议（OSPF)
#
# Step			:	测试步骤1: ：1.按图10搭建测试环境；
#                   测试步骤2:  tester port1 IP地址为192.168.1.100/24，port2为192.168.2.100/24；
#                   测试步骤3:  DUT port1 IP地址为192.168.1.1/24，port2为 192.168.2.1/24；
#                   测试步骤4: 在DUT上配置OSPFv2路由协议；
#                   测试步骤5: 测试仪tester使用port1、port2建立OSPF路由器，在port1插入一些LSA，并使port1和DUT的port1达到FULL状态，port2和DUT的port2达到FULL状态，观察port2是否能得到port1的LSA。
#
# Criteria    	:   预期结果1: ospf建立成功，可以收到lsa
#
# Created by   	:  	Tester-006
#
# Bugs   	    :  	None
# =================================================================================


# "comments": {
#     "test_environment": "建议使用专业测试仪如Ixia或Spirent进行测试",
#     "variations": "可考虑测试不同LSA类型(Type 1-5)的传播情况",
#     "extended_tests": "后续可增加OSPF收敛时间、路由计算正确性等性能测试"
# }

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

    #创建ospf协议
    session_1 = create_ospf(Port=port_up, Priority=1)
    session_2 = create_ospf(Port=port_down, Priority=2)

    # OSPFv2协议会话与接口绑定
    select_interface(Session=session_1, Interface=interfaces_up)
    select_interface(Session=session_2, Interface=interfaces_down)

    # OSPFv2协议会话1创建Summary Lsa
    summary_lsa = create_ospf_summary_lsa(Session=session_1)

    # OSPFv2协议会话2创建External Lsa
    external_lsa = create_ospf_external_lsa(Session=session_2)

    # 获取OSPFv2协议绑定流端点对象
    point_1 = get_ospf_router_from_lsa(Lsa=summary_lsa)
    point_2 = get_ospf_router_from_lsa(Lsa=external_lsa)

    # 创建OSPFv2绑定流
    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 订阅统计

    subscribe_result(Types=['Ospfv2SessionResultPropertySet', 'StreamBlockStats'])
    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')


    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 启动协议
        start_protocol()
        # 等待OSPFv2协议会话达到Full状态
        wait_ospf_adjacency_state(Sessions=[session_1, session_2])
        advertise_ospf_lsa(Lsa=[summary_lsa, external_lsa])
        time.sleep(5)

        # 发送流量
        start_stream()
        time.sleep(10)
        stop_stream()
        withdraw_ospf_lsa(Lsa=[summary_lsa, external_lsa])
        time.sleep(5)
        stop_protocol()
        time.sleep(3)

        # 获取OSPFv2会话1统计
        import pandas
        result = get_ospf_statistic()
        print(result)
        if not isinstance(result, pandas.DataFrame):
            verdict = 'fail'

        result = get_ospf_statistic(Session=session_1)
        print(result)
        TxSummaryLsa = result['TxSummaryLsa']
        RxAsExternalLsa = result['RxAsExternalLsa']
        print('TxSummaryLsa: {}'.format(TxSummaryLsa))
        print('RxAsExternalLsa: {}'.format(RxAsExternalLsa))

        # 获取OSPFv2会话2统计
        result = get_ospf_statistic(Session=session_2)
        print(result)
        RxSummaryLsa = result['RxSummaryLsa']
        TxAsExternalLsa = result['TxAsExternalLsa']
        print('RxSummaryLsa: {}'.format(RxSummaryLsa))
        print('TxAsExternalLsa: {}'.format(TxAsExternalLsa))

        # 获取流量1统计
        result = get_streamblock_statistic(Stream=streams[0])
        print(result)
        TxStreamFrames = result['TxStreamFrames']
        RxStreamFrames = result['RxStreamFrames']
        print('TxStreamFrames: {}'.format(TxStreamFrames))
        print('RxStreamFrames: {}'.format(RxStreamFrames))

        if TxStreamFrames != RxStreamFrames:
            verdict = 'fail'
            errInfo += '{} TxStreamFrames({}) is not equal to RxStreamFrames({})\n'.format(streams[0].Name,TxStreamFrames,RxStreamFrames)

        # 获取流量2统计

        result = get_streamblock_statistic(Stream=streams[1])
        print(result)
        TxStreamFrames = result['TxStreamFrames']
        RxStreamFrames = result['RxStreamFrames']
        print('TxStreamFrames: {}'.format(TxStreamFrames))
        print('RxStreamFrames: {}'.format(RxStreamFrames))

        if TxStreamFrames != RxStreamFrames:
            verdict = 'fail'
            errInfo += '{} TxStreamFrames({}) is not equal to RxStreamFrames({})\n'.format(streams[1].Name,TxStreamFrames,RxStreamFrames)
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
