# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.6.2 Routing Table Capacity
#
# Step			:	Test Step 1: Build the test environment according to the topology diagram;
#                   Test Step 2: Tester port1 IP address is 192.168.1.100/24, port2 is 192.168.2.100/24;
#                   Test Step 3: DUT port1 IP address is 192.168.1.1/24, port2 IP address is 192.168.2.1/24;
#                   Test Step 4: Configure DUT and tester in the same Area, DUT interfaces 1 and 2 establish OSPF adjacency with tester respectively;
#                   Test Step 5: Tester interfaces port1 and port2 respectively send Type LSA to DUT interfaces port1 and port2, with a total number equal to the specified value of the DUT routing table capacity.
#
# Criteria    	:   Expected Result 1: View and record the OSPF-generated routing table statistics information of the DUT.
#
# Created by   	:  	Tester-001
#
# Tags   	    :  	performance
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

    # 创建OSPFv2协议会话
    session_1 = create_ospf(Port=port_up, Priority=cfg['arg']['ospf']['default']['priority_session_up']['default'], AreaId=cfg['arg']['ospf']['default']['area_id']['default'])
    session_2 = create_ospf(Port=port_down, Priority=cfg['arg']['ospf']['default']['priority_session_down']['default'], AreaId=cfg['arg']['ospf']['default']['area_id']['default'])

    # OSPFv2协议会话与接口绑定
    select_interface(Session=session_1, Interface=interfaces_up)
    select_interface(Session=session_2, Interface=interfaces_down)

    route_count = int(cfg['arg']['ospf']['default']['advertise_count']['default'] / 2)
    # OSPFv2协议会话创建External Lsa
    external_lsa_1 = create_ospf_external_lsa(Session=session_1, RouteCount=route_count)
    external_lsa_2 = create_ospf_external_lsa(Session=session_2, RouteCount=route_count)

    # 获取OSPFv2协议绑定流端点对象
    point_1 = get_ospf_router_from_lsa(Lsa=external_lsa_1)
    point_2 = get_ospf_router_from_lsa(Lsa=external_lsa_2)

    # 创建OSPFv2绑定流
    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 负载模式：Base On Port, （端口负载：, 负载单位：PERCENT 传输模式：Time
    edit_port_load_profile(Ports=[port_up, port_down],
                           LoadProfileType='PORT_BASE',
                           Unit='PERCENT',
                           TransmitMode="TIME",
                           Rate=cfg['arg']['load_profile']['default']['rate']['default'],
                           Seconds=cfg['arg']['load_profile']['default']['rate']['default'])

    # 订阅统计
    subscribe_result(Types=['PortStats', 'StreamBlockStats', 'Ospfv2SessionResultPropertySet', 'StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        # 启动协议
        printf(message='Test start')
        start_protocol()
        time.sleep(3)
        # 等待OSPFv2协议会话达到Full状态
        wait_ospf_adjacency_state(Sessions=[session_1, session_2])
        result = get_ospf_statistic()
        # 使用tabulate库表格化输出DataFrame二维数据
        print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n', flush=True)
        advertise_ospf_lsa(Lsa=[external_lsa_1, external_lsa_2])
        time.sleep(cfg['arg']['ospf']['default']['advertise_wait']['default'])
        result = get_ospf_statistic()
        # 使用tabulate库表格化输出DataFrame二维数据
        print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n', flush=True)

        # 发送流量
        printf(message='Stream test start')
        start_stream()
        time.sleep(3)
        df = get_streamblock_statistic()
        wait_stream_state(State='RUNNING')
        time.sleep(3)
        result = get_streamblock_statistic()
        # 使用 concat 拼接 DataFrame
        df = pd.concat([df, result])
        # 重置索引
        df = df.reset_index(drop=True)
        printf(message='Test completed')
        print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n', flush=True)
        data.write_report(df)
        printf(message='Test data save successfully')

        stop_protocol()
        time.sleep(3)
        result = get_ospf_statistic()
        # 使用tabulate库表格化输出DataFrame二维数据
        print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n', flush=True)

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
