# =================================================================================
# Objective   	:   测试目的 : 检查DHCPv4协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建DHCPv4协议，并且创建路由;
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
                   Address='2.1.1.2',
                   Gateway='2.1.1.1')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='2.1.2.2',
                   Gateway='2.1.1.1')

    # 创建DHCPv4协议会话

    client = create_dhcp_client(Port=Port_UP)

    server = create_dhcp_server(Port=Port_Down)

    # DHCPv4协议会话与接口绑定

    select_interface(Session=client, Interface=interfaces_1)

    select_interface(Session=server, Interface=interfaces_2)

    # 获取DHCP Server地址池
    configDict = get_configs(Configs='Dhcpv4AddressPool')
    dhcpv4AddressPool = list(configDict.values())[0]
    edit_configs(Configs=dhcpv4AddressPool, PoolAddressStart='2.1.2.3')

    # 获取接口绑定流端点对象

    point_1 = get_layer_from_interfaces(Interfaces=interfaces_1)

    point_2 = get_layer_from_interfaces(Interfaces=interfaces_2)

    # 创建OSPFv2绑定流

    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 订阅统计

    subscribe_result(Types=['StreamBlockStats', 'Dhcpv4ServerStats', 'Dhcpv4ClientBlockStats', 'Dhcpv4ClientStats',
                            'Dhcpv4PortStats', 'Dhcpv4LeaseStats', ])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待DHCP协议协议会话状态正确

    wait_dhcp_client_state(Sessions=client)
    wait_dhcp_server_state(Sessions=server)

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    # 获取DHCP端口统计
    import pandas
    result = get_dhcp_port_statistic()
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'
    result = get_dhcp_port_statistic(Port=Port_UP)
    print(result)
    result = get_dhcp_port_statistic(Port=Port_Down)
    print(result)

    # 获取DHCP客户端统计
    result = get_dhcp_client_statistic()
    print(result)
    result = get_dhcp_client_statistic(Session=client)
    print(result)

    result = get_dhcp_client_block_statistic(Session=client)
    print(result)

    # 获取DHCP服务器统计
    result = get_dhcp_server_statistic()
    print(result)
    result = get_dhcp_server_statistic(Session=server)
    print(result)

    result = get_dhcp_server_lease_statistic(Session=server, ClientId='00:00:02:01:01:02')
    print(result)

    # 获取流量1统计

    result = get_streamblock_statistic(Stream=streams[0])
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    print('TxStreamFrames: {}'.format(TxStreamFrames))
    print('RxStreamFrames: {}'.format(RxStreamFrames))

    if TxStreamFrames != RxStreamFrames:
        verdict = 'fail'
        errInfo += '{} TxStreamFrames({}) is not equal to RxStreamFrames({})\n'.format(streams[0].Name, TxStreamFrames,
                                                                                       RxStreamFrames)

    # 获取流量2统计

    result = get_streamblock_statistic(Stream=streams[1])
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    print('TxStreamFrames: {}'.format(TxStreamFrames))
    print('RxStreamFrames: {}'.format(RxStreamFrames))

    if TxStreamFrames != RxStreamFrames:
        verdict = 'fail'
        errInfo += '{} TxStreamFrames({}) is not equal to RxStreamFrames({})\n'.format(streams[1].Name, TxStreamFrames,
                                                                                       RxStreamFrames)

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
