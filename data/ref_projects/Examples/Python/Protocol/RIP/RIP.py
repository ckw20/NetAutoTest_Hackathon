# =================================================================================
# Objective   	:   测试目的 : 检查RIP协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 创建RIP协议及组播组;
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

    # 创建RIP协议会话

    session_1 = create_rip(Port=Port_UP)

    session_2 = create_rip(Port=Port_Down)

    # RIP协议会话与接口绑定

    select_interface(Session=session_1, Interface=interfaces_1)

    select_interface(Session=session_2, Interface=interfaces_2)

    # RIP协议会话1创建IPv4 Route

    ipv4_route_1 = create_rip_ipv4_route(Session=session_1)

    # RIP协议会话2创建IPv4 Route

    ipv4_route_2 = create_rip_ipv4_route(Session=session_2)

    # 获取RIP协议绑定流端点对象

    point_1 = get_rip_router_from_route(Route=ipv4_route_1)

    point_2 = get_rip_router_from_route(Route=ipv4_route_2)

    # 创建RIP绑定流

    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 订阅统计

    subscribe_result(Types=['RipSessionBlockStats', 'RipSessionStats', 'StreamBlockStats'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待RIP协议会话达到Full状态

    wait_rip_state(Sessions=[session_1, session_2])

    advertise_rip(Sessions=[session_1, session_2])

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    withdraw_rip(Sessions=[session_1, session_2])

    time.sleep(5)

    stop_protocol()

    time.sleep(3)

    import pandas
    result = get_rip_session_block_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    # 获取RIP会话1统计

    result = get_rip_session_block_statistic(Session=session_1)
    print(result)
    TxAdvertised = result['TxAdvertised']
    RxAdvertised = result['RxAdvertised']
    print('TxAdvertised:', TxAdvertised)
    print('RxAdvertised:', RxAdvertised)
    TxWithdrawn = result['TxWithdrawn']
    RxWithdrawn = result['RxWithdrawn']
    print('TxWithdrawn:', TxWithdrawn)
    print('RxWithdrawn:', RxWithdrawn)

    # 获取RIP会话2统计

    result = get_rip_session_block_statistic(Session=session_2)
    print(result)
    TxAdvertised = result['TxAdvertised']
    RxAdvertised = result['RxAdvertised']
    print('TxAdvertised:', TxAdvertised)
    print('RxAdvertised:', RxAdvertised)
    TxWithdrawn = result['TxWithdrawn']
    RxWithdrawn = result['RxWithdrawn']
    print('TxWithdrawn:', TxWithdrawn)
    print('RxWithdrawn:', RxWithdrawn)

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
