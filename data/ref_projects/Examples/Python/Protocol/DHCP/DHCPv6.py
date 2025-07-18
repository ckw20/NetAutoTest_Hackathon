# =================================================================================
# Objective   	:   测试目的 : 检查DHCPv6协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建DHCPv6协议;
#                   测试步骤3: 创建绑定流量;
#                   测试步骤4: 订阅StreamBlockStats统计;
#                   测试步骤5: 发送所有流量，等待一段时间;
#                   测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
#
# Criteria    	:   预期结果1: 步骤6中所有流量收发包相等;
#
# Created by   	:  	Tester-002
#
# Bugs   	    :  	None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/5', '//10.0.11.191/1/6'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
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
                   Address='2011::2',
                   Gateway='2011::1')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv6Layer',
                   Address='2011::1',
                   Gateway='2011::2')

    # 创建DHCPv6协议会话

    client = create_dhcpv6_client(Port=Port_UP, Name='Client')

    server = create_dhcpv6_server(Port=Port_Down, Name='Server')

    # DHCPv6协议会话与接口绑定

    select_interface(Session=client, Interface=interfaces_1)

    select_interface(Session=server, Interface=interfaces_2)

    # 获取DHCP Server地址池
    pool = create_dhcpv6_server_address_pool(Sessions=server, StartAddress='2011::2')

    # 获取接口绑定流端点对象
    point_1 = get_layer_from_interfaces(Interfaces=interfaces_1, Layer='ipv6')

    point_2 = get_layer_from_interfaces(Interfaces=interfaces_2, Layer='ipv6')

    # 创建DHCP绑定流

    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 订阅统计

    subscribe_result(Types=['StreamBlockStats', 'Dhcpv6PortStatistics', 'Dhcpv6ClientBlockStatistics',
                            'Dhcpv6ServerStatistics', 'Dhcpv6LeaseStatistics'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待DHCP协议协议会话状态正确

    wait_dhcpv6_client_state(Sessions=client)
    wait_dhcpv6_server_state(Sessions=server)

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    # 获取DHCP端口统计
    import pandas
    result = get_dhcpv6_port_statistic()
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_dhcpv6_port_statistic(Port=Port_UP)
    print(result)
    result = get_dhcpv6_port_statistic(Port=Port_Down)
    print(result)

    # 获取DHCP客户端统计
    result = get_dhcpv6_client_block_statistic()
    print(result)
    result = get_dhcpv6_client_block_statistic(Session=client)
    print(result)

    # 获取DHCP服务器统计
    result = get_dhcpv6_server_statistic()
    print(result)
    result = get_dhcpv6_server_statistic(Session=server)
    print(result)

    result = get_dhcpv6_server_lease_statistic()
    print(result)
    result = get_dhcpv6_server_lease_statistic(Session=server, Pool=pool)
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
