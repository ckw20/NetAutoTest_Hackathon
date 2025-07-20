# =================================================================================
# Objective   	:   Test Objective : 6.7.8 Internet Group Management Protocol (IGMP)
#
# Step			:	Test Step 1: Build the test environment according to Figure 10;
#                   Test Step 2: tester port1 address is 192.168.1.100/24, port2 address is 192.168.2.100/24;
#                   Test Step 3: DUT port1 address is 192.168.1.1/24, port2 address is 192.168.2.1/24;
#                   Test Step 4: Configure IGMPv2 multicast query on DUT;
#                   Test Step 5: tester sends IGMPv2 report packets with destination address 225.1.1.1, TTL=1, group address 225.1.1.1, period 1s, to port1;
#                   Test Step 6: Stop sending IGMPv2 report packets from step 5, observe the change of switch multicast group membership;
#                   Test Step 7: tester sends IGMPv2 report packets with destination address 225.1.1.1, TTL=1, group address 225.1.1.1, period 1s, to port1, then immediately sends IGMPv2 leave packets with destination address 224.0.0.2, TTL=1, group address 225.1.1.1, to port1; observe the change of switch multicast group membership;
#                   Test Step 8: Stop sending packets from step 7;
#                   Test Step 9: Check DUT configuration to see if IGMPv1, IGMPv2, IGMPv3 are supported.
#
# Criteria    	:   Expected Result 1:
#
# Created by   	:  	Tester-006
#
# Bugs   	    :  	None
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

    # 创建IGMP协议会话
    igmp = create_igmp(Port=port_up, Version='IGMPV2')
    edit_igmp(Session=igmp, InitialJoin=True)

    # IGMP协议会话与接口绑定
    select_interface(Session=igmp, Interface=interfaces_up)

    # 创建组播组
    multicast_group = create_multicast_group(Start='225.1.1.1')

    # IGMP协议会话创建组成员关系
    memberships = create_memberships(Session=igmp, DeviceGroupMapping='ROUNDROBIN')

    # IGMP协议会话组成员关系与组播组绑定
    binding_multicast_group(Session=igmp, Memberships=memberships, MulticastGroup=multicast_group)

    # 创建IGMP Querier协议会话

    igmp_querier = create_igmp_querier(Port=port_down, Version='IGMPV2')

    edit_igmp_querier(Session=igmp_querier, RobustnessVariable=3)

    # IGMP Querier协议会话与接口绑定

    select_interface(Session=igmp_querier, Interface=interfaces_down)

    # 创建IGMP绑定流

    # point = get_layer_from_interfaces(Interfaces=interfaces_down)
    #
    # streams1 = add_stream(Type='binding', SrcPoints=point, DstPoints=multicast_group, Bidirection=False)
    # streams1 = add_stream(Type='binding', SrcPoints=point, DstPoints='224.0.0', Bidirection=False)


    # edit_port_load_profile(Ports=ports,
    #                        LoadProfileType='PORT_BASE',
    #                        Rate=100,
    #                        Unit='FRAME_PER_SEC',
    #                        TransmitMode="STEP",
    #                        Frames=20)


    #创建IGMPv2报文
    # stream1 = add_stream(Ports=port_up, Names=f'igmpv2_report')
    # edit_stream(Stream=stream1, FixedLength=128)
    # create_stream_header(Stream=stream1, HeaderTypes=['ethernetii', 'ipv4','igmpv2'])
    # edit_header_ipv4(Stream=stream1, Source='192.168.1.100', Destination= '225.1.1.1', TTl=1)
    #
    # stream2 = add_stream(Ports=port_up, Names=f'igmpv2_query')
    # edit_stream(Stream=stream2, FixedLength=128)
    # create_stream_header(Stream=stream2, HeaderTypes=['ethernetii', 'ipv4','igmpv2query'])
    # edit_header_ipv4(Stream=stream2, Source='192.168.1.100', Destination= '224.0.0.2', TTl=1)

    # 订阅统计
    subscribe_result(Types=['StreamBlockStats', 'IgmpHostResults', 'IgmpPortAggregatedResults', 'IgmpQuerierResults'])
    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')


    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 启动协议
        start_protocol()

        # 等待IGMP协议会话稳定状态
        wait_igmp_state(Sessions=[igmp])

        # 查询igmp group
        cmd_cfg = '_'.join('DeviceA_Step4'.split('_')[1:])
        for _ in range(3):
            flag = device['DeviceA'].execute(row=cmd_cfg)
            if flag:
                break
        #停止协议
        stop_protocol()

        # 查询igmp group
        cmd_cfg = '_'.join('DeviceA_Step4'.split('_')[1:])
        for _ in range(3):
            flag = device['DeviceA'].execute(row=cmd_cfg)
            if flag:
                break

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
