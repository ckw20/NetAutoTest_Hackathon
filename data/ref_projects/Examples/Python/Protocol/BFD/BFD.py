# =================================================================================
# Objective   	:   测试目的 : 检查BFD与ISIS协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建ISIS协议，并且创建路由;
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

locations = ['//10.0.11.191/1/3', '//10.0.11.191/1/4'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:
    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口

    Port_UP, Port_Down = reserve_port(Locations=locations)

    # 创建接口

    interfaces_1 = create_interface(Port=Port_UP)

    interfaces_2 = create_interface(Port=Port_Down)

    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='1.1.1.1',
                   Gateway='1.1.1.2')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='1.1.1.2',
                   Gateway='1.1.1.1')

    # 创建BFD协议会话

    bfd_1 = create_bfd(Port=Port_UP)
    bfd_2 = create_bfd(Port=Port_Down, RouterRole='PASSIVE')

    select_interface(Session=bfd_1, Interface=interfaces_1)
    select_interface(Session=bfd_2, Interface=interfaces_2)

    # 创建ISIS协议会话及Tlv
    isis_1 = create_isis(Port=Port_UP, EnableBFD=True)
    isis_2 = create_isis(Port=Port_Down, EnableBFD=True)

    select_interface(Session=isis_1, Interface=interfaces_1)
    select_interface(Session=isis_2, Interface=interfaces_2)

    ipv4_lsp_1 = create_isis_lsp(Session=isis_1, Level='L1')
    ipv4_lsp_2 = create_isis_lsp(Session=isis_2, Level='L1')

    ipv4_tlv_1 = create_isis_ipv4_tlv(Lsp=ipv4_lsp_1, RouteCount=10, StartIpv4Prefix='2.0.0.1')
    ipv4_tlv_2 = create_isis_ipv4_tlv(Lsp=ipv4_lsp_2, RouteCount=10, StartIpv4Prefix='3.0.0.1')


    # 获取接口绑定流端点对象
    point_1 = get_isis_router_from_tlv(Configs=ipv4_tlv_1)
    point_2 = get_isis_router_from_tlv(Configs=ipv4_tlv_2)


    # 创建数据流量

    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 订阅统计

    subscribe_result(Types=['StreamBlockStats', 'IsisBfdSessionResult'])


    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')


    # 启动协议

    start_protocol()

    # 等待ISIS协议协议会话状态正确

    wait_isis_state(Sessions=[isis_1, isis_2], State='UP')

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    # 获取BFD ISIS统计

    bfd_isis_ipv4_result_1 = get_bfd_isis_session_result(BfdSession=bfd_1, IsisSession=isis_1, SessionId=1)
    print(bfd_isis_ipv4_result_1)
    bfd_isis_ipv4_result_2 = get_bfd_isis_session_result(BfdSession=bfd_2, IsisSession=isis_2, SessionId=1)
    print(bfd_isis_ipv4_result_2)


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
