# =================================================================================
# Objective   	:   测试目的 : 检查L2TP协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建L2TP协议，并且创建路由;
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

    interfaces_1 = create_interface(Port=Port_UP)
    interfaces_2 = create_interface(Port=Port_Down)
    
    edit_interface_stack(Interfaces=interfaces_1, Layers=['eth', 'l2tp', 'ipv4'], Tops='ipv4')
    edit_interface_stack(Interfaces=interfaces_2, Layers=['eth', 'l2tp', 'ipv4'], Tops='ipv4')
    
    edit_interface(Interface=interfaces_1, Layer='IPv4Layer', Level=0, Address='1.1.1.1', Gateway='1.1.1.2')
    edit_interface(Interface=interfaces_2, Layer='IPv4Layer', Level=0, Address='1.1.1.2', Gateway='1.1.1.1')


    # 创建L2TP协议会话

    l2tp_1 = create_l2tp(Port=Port_UP)
    l2tp_2 = create_l2tp(Port=Port_Down, EmulationMode='LNS')

    select_interface(Session=l2tp_1, Interface=interfaces_1)
    select_interface(Session=l2tp_2, Interface=interfaces_2)

    pppoe_1 = create_pppoe(Port=Port_UP, EmulationMode='CLIENT')
    pppoe_2 = create_pppoe(Port=Port_Down, EmulationMode='SERVER')
    pppoe_1.EmulationMode = 'PPPOL2TP'
    pppoe_2.EmulationMode = 'PPPOL2TP'
    select_interface(Session=pppoe_1, Interface=interfaces_1)
    select_interface(Session=pppoe_2, Interface=interfaces_2)


    # 获取接口绑定流端点对象

    point_1 = get_layer_from_interfaces(Interfaces=interfaces_1)

    point_2 = get_layer_from_interfaces(Interfaces=interfaces_2)

    # 创建接口绑定流

    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 订阅统计

    subscribe_result(Types=['L2tpPortStatistic', 'L2tpBlockStatistic', 'L2tpSessionStatistic', 'L2tpTunnelStatistic', 'PppoeClientStatistic', 'StreamBlockStats'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待PPPoE协议会话达到CONNECTED状态

    wait_l2tp_state(Sessions=[l2tp_1, l2tp_2])

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    # 获取L2TP会话1统计
    import pandas
    result = get_l2tp_port_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_l2tp_port_statistic(Port=Port_UP)
    print(result)
    result = get_l2tp_port_statistic(Port=Port_Down)
    print(result)

    result = get_l2tp_session_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_l2tp_session_statistic(Session=l2tp_1, NodeIndexInBlock=1)
    print(result)
    result = get_l2tp_session_statistic(Session=l2tp_2, NodeIndexInBlock=1)
    print(result)

    result = get_l2tp_block_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_l2tp_block_statistic(Session=l2tp_1)
    print(result)
    result = get_l2tp_block_statistic(Session=l2tp_2)
    print(result)

    result = get_l2tp_tunnel_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_l2tp_tunnel_statistic(Session=l2tp_1, NodeIndexInBlock=1)
    print(result)
    result = get_l2tp_tunnel_statistic(Session=l2tp_2, NodeIndexInBlock=1)
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
