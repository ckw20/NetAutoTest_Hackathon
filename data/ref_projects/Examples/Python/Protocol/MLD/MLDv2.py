# =================================================================================
# Objective   	:   测试目的 : 检查MLD协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建MLD协议，并且创建路由;
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

    interfaces_1 = create_interface(Port=Port_UP, Layers=['ipv6'])

    interfaces_2 = create_interface(Port=Port_Down, Layers=['ipv6'])

    edit_interface(Interface=interfaces_1,
                   Layer='IPv6Layer',
                   Address='2000::3',
                   Gateway='2000::2')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv6Layer',
                   Address='2000::2',
                   Gateway='2000::3')

    # 创建MLD协议会话

    mld = create_mld(Port=Port_UP)

    edit_mld(Session=mld, Version='MLDV2')

    # MLD协议会话与接口绑定

    select_interface(Session=mld, Interface=interfaces_1)

    # MLD协议会话1创建Summary Lsa

    multicast_group = create_multicast_group(Start='ff1e::2', Version="IPv6")

    # MLD协议会话2创建External Lsa

    memberships = create_memberships(Session=mld,
                                     DeviceGroupMapping='ROUNDROBIN',
                                     UserDefinedSources=False)

    # 获取MLD协议绑定流端点对象

    binding_multicast_group(Session=mld, Memberships=memberships, MulticastGroup=multicast_group)

    select_source_interface(Session=mld, Memberships=memberships, Interface=interfaces_2)

    # 创建MLD Querier协议会话

    mld_querier = create_mld_querier(Port=Port_Down, Version='MLDV1')

    edit_mld_querier(Session=mld_querier, RobustnessVariable=3)

    # MLD Querier协议会话与接口绑定

    select_interface(Session=mld_querier, Interface=interfaces_2)

    # 创建MLD绑定流

    point = get_layer_from_interfaces(Interfaces=interfaces_2, Layer='ipv6')

    streams = add_stream(Type='binding', SrcPoints=point, DstPoints=multicast_group, Bidirection=False)

    # 订阅统计

    subscribe_result(Types=['StreamBlockStats', 'MldHostResults', 'MldPortAggregatedResults', 'MldQuerierResults'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待MLD协议会话稳定状态

    wait_mld_state(Sessions=[mld])
    wait_mld_querier_state(Sessions=[mld_querier])

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(60)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    # 获取MLD Host统计

    result = get_mld_host_statistic(Session=mld)
    print(result)

    # 获取MLD Port统计

    result = get_mld_port_statistic(Port=Port_UP)
    print(result)

    # 获取MLD Querier统计

    result = get_mld_querier_statistic(Session=mld_querier)
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
