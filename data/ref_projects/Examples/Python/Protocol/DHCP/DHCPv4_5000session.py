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
# Created by   	:  	Tester-004
#
# Bugs   	    :  	None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/3', '//10.0.11.191/1/4'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:
    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口

    Ports = reserve_port(Locations=locations, Force=True)

    # 创建接口

    interfaces_1 = create_interface(Port=Ports[0], Layers=['ipv4'])
    edit_interface(Interface=interfaces_1, Count=5000)
    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='12.12.12.2',
                   PrefixLength=19,
                   Gateway='12.12.12.1')
    interfaces_2 = create_interface(Port=Ports[1], Layers=['ipv4'])
    # 保证MAC地址不冲突
    edit_interface(Interface=interfaces_2,
                   Layer='EthIILayer',
                   Address='12:12:12:12:12:12')
    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='12.12.12.1',
                   PrefixLength=19,
                   Gateway='12.12.12.2')

    # 创建DHCPv4协议会话
    client = create_dhcp_client(Port=Ports[0])
    server = create_dhcp_server(Port=Ports[1])
    # DHCPv4协议会话与接口绑定
    select_interface(Session=client, Interface=interfaces_1)
    select_interface(Session=server, Interface=interfaces_2)
    # 获取DHCP Server地址池
    configDict = get_configs(Configs='Dhcpv4AddressPool')
    dhcpv4AddressPool = list(configDict.values())[0]
    edit_configs(Configs=dhcpv4AddressPool, PoolAddressStart='12.12.12.2', PrefixLength=19, PoolAddressCount=5100)
    # 获取接口绑定流端点对象
    point_1 = get_layer_from_interfaces(Interfaces=interfaces_1)
    point_2 = get_layer_from_interfaces(Interfaces=interfaces_2)
    # 创建DHCPV4绑定流
    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)
    # 订阅统计
    subscribe_result(Types=['StreamBlockStats', 'Dhcpv4ServerStats', 'Dhcpv4ClientBlockStats',
                            'Dhcpv4PortStats'])

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
    time.sleep(3)
    # 获取DHCP端口统计
    result = get_dhcp_port_statistic(Port=Ports[0])
    CurrentBound = result['CurrentBound']
    TotalBound = result['TotalBound']
    assert CurrentBound == TotalBound == 5000
    # 获取DHCP客户端统计
    result = get_dhcp_client_block_statistic(Session=client)
    CurrentBound = result['CurrentBound']
    TotalBound = result['TotalBound']
    assert CurrentBound == TotalBound == 5000
    # 获取DHCP服务器统计
    result = get_dhcp_server_statistic(Session=server)
    CurrentBound = result['CurrentBound']
    TotalBound = result['TotalBound']
    assert CurrentBound == TotalBound == 5000
    # 获取流量1统计
    result = get_streamblock_statistic(Stream=streams[0])
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    assert TxStreamFrames == RxStreamFrames
    # 获取流量2统计
    result = get_streamblock_statistic(Stream=streams[1])
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    assert TxStreamFrames == RxStreamFrames
except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
