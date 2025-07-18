# =================================================================================
# Objective   	:   测试目的 : 检查IGMP协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建IGMP协议，并且创建路由;
#                   测试步骤3: 创建绑定流量;
#                   测试步骤4: 订阅StreamBlockStats统计;
#                   测试步骤5: 发送所有流量，等待一段时间;
#                   测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
#
# Criteria    	:   预期结果1: 步骤6中所有流量收发包相等;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :  	None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/15', '//10.0.11.191/1/16'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口

    Port_UP, Port_Down = reserve_port(Locations=locations)

    # 创建接口

    interfaces_1 = create_interface(Port=Port_UP, Layers=['ipv4'])

    interfaces_2 = create_interface(Port=Port_Down, Layers=['ipv4'])

    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='192.168.1.2',
                   Gateway='192.168.1.3')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='192.168.1.3',
                   Gateway='192.168.1.2')

    # 创建IGMP协议会话

    igmp = create_igmp(Port=Port_UP, Version='IGMPV1')

    edit_igmp(Session=igmp, InitialJoin=True)

    # IGMP协议会话与接口绑定

    select_interface(Session=igmp, Interface=interfaces_1)

    # 创建组播组

    multicast_group = create_multicast_group(Start='225.0.1.2')

    # IGMP协议会话创建组成员关系

    memberships = create_memberships(Session=igmp, DeviceGroupMapping='ROUNDROBIN')

    # IGMP协议会话组成员关系与组播组绑定

    binding_multicast_group(Session=igmp, Memberships=memberships, MulticastGroup=multicast_group)

    # 创建IGMP Querier协议会话

    igmp_querier = create_igmp_querier(Port=Port_Down, Version='IGMPV1')

    edit_igmp_querier(Session=igmp_querier, RobustnessVariable=3)

    # IGMP Querier协议会话与接口绑定

    select_interface(Session=igmp_querier, Interface=interfaces_2)

    # 创建IGMP绑定流

    point = get_layer_from_interfaces(Interfaces=interfaces_2)

    streams = add_stream(Type='binding', SrcPoints=point, DstPoints=multicast_group, Bidirection=False)

    # 订阅统计

    subscribe_result(Types=['StreamBlockStats', 'IgmpHostResults', 'IgmpPortAggregatedResults', 'IgmpQuerierResults'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待IGMP协议会话稳定状态

    wait_igmp_state(Sessions=[igmp])
    wait_igmp_querier_state(Sessions=[igmp_querier])

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(60)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    # 获取IGMP Host统计
    result = get_igmp_host_statistic()
    print(result)

    result = get_igmp_host_statistic(Session=igmp)
    print(result)

    # 获取IGMP Port统计
    result = get_igmp_port_statistic()
    print(result)

    result = get_igmp_port_statistic(Port=Port_UP)
    print(result)

    # 获取IGMP Querier统计
    result = get_igmp_querier_statistic()
    print(result)

    result = get_igmp_querier_statistic(Session=igmp_querier)
    print(result)

    # 获取流量统计

    result = get_streamblock_statistic(Stream=streams[0])
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    print('TxStreamFrames: {}'.format(TxStreamFrames))
    print('RxStreamFrames: {}'.format(RxStreamFrames))

    if TxStreamFrames != RxStreamFrames:
        verdict = 'fail'
        errInfo += f'{streams[0].Name} TxStreamFrames({TxStreamFrames}) is not equal to RxStreamFrames({RxStreamFrames})\n'

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
