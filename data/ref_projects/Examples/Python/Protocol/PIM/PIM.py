# =================================================================================
# Objective   	:   测试目的 : 检查PIM协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 创建PIM协议及组播组;
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

    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='1.1.1.1',
                   Gateway='1.1.1.2')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='1.1.1.2',
                   Gateway='1.1.1.1')

    # 创建pim协议会话

    pim_1 = create_pim(Port=Port_UP)

    pim_2 = create_pim(Port=Port_Down)

    pim_group_1 = create_pim_group(Session=pim_1, GroupAddr='225.0.0.1')

    pim_group_2 = create_pim_group(Session=pim_2, GroupAddr='225.0.0.2')


    # DHCPv6协议会话与接口绑定

    select_interface(Session=pim_1, Interface=interfaces_1)

    select_interface(Session=pim_2, Interface=interfaces_2)

    # 创建组播组

    multicast_group_1 = create_multicast_group(Start='225.0.0.1')

    multicast_group_2 = create_multicast_group(Start='225.0.0.2')

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 创建DHCP绑定流

    point_1 = get_layer_from_interfaces(Interfaces=interfaces_1)

    point_2 = get_layer_from_interfaces(Interfaces=interfaces_2)

    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=multicast_group_1)

    stream = add_stream(Type='binding', SrcPoints=point_2, DstPoints=multicast_group_2)
    streams.extend(stream)
    # 订阅统计

    subscribe_result(Types=['StreamBlockStats', 'PimSessionStats', 'PimGroupStats'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待DHCP协议协议会话状态正确

    wait_pim_state(Sessions=[pim_1, pim_2])

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    # 获取PIM会话统计
    import pandas
    result = get_pim_session_stats()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_pim_session_stats(Session=pim_1)
    print(result)

    result = get_pim_session_stats(Session=pim_2)
    print(result)

    # 获取PIM Group统计
    result = get_pim_group_stats()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_pim_group_stats(Session=pim_1, Group=pim_group_1)
    print(result)

    result = get_pim_group_stats(Session=pim_2, Group=pim_group_2)
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
