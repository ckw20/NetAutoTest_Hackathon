# =================================================================================
# Objective   	:   测试目的 : 检查VXLAN协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 创建VXLAN协议及组播组;
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

    interfaces_1 = create_interface(Port=Port_UP, Layers=['ipv4'])

    interfaces_2 = create_interface(Port=Port_Down, Layers=['ipv4'])

    interfaces_3 = create_interface(Port=Port_UP, Layers=['ipv4'])

    interfaces_4 = create_interface(Port=Port_Down, Layers=['ipv4'])

    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='1.1.1.1',
                   Gateway='1.1.1.2')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='1.1.1.2',
                   Gateway='1.1.1.1')

    edit_interface(Interface=interfaces_3,
                   Layer='IPv4Layer',
                   Address='2.2.2.1',
                   Gateway='2.2.2.2')

    edit_interface(Interface=interfaces_4,
                   Layer='IPv4Layer',
                   Address='2.2.2.2',
                   Gateway='2.2.2.1')
    # 创建VXLAN协议会话

    session_1 = create_vxlan(Port=Port_UP)

    session_2 = create_vxlan(Port=Port_Down)

    # VXLAN协议会话与接口绑定

    select_interface(Session=session_1, Interface=interfaces_1)

    select_interface(Session=session_2, Interface=interfaces_2)

    # 创建VXLAN Segment

    segment = create_vxlan_segment(StartVni=10)

    # 绑定VXLAN VM

    binding_vxlan_vm(Segments=segment, Interfaces=interfaces_3)

    binding_vxlan_vm(Segments=segment, Interfaces=interfaces_4)

    binding_vxlan_vtep(Vteps=session_1, Interfaces=interfaces_3)

    binding_vxlan_vtep(Vteps=session_2, Interfaces=interfaces_4)

    # 创建VXLAN绑定流

    point_1 = get_vxlan_vm_point(Vxlan=session_1)

    point_2 = get_vxlan_vm_point(Vxlan=session_2)

    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 订阅统计

    subscribe_result(Types=['VxlanBindingStats', 'StreamBlockStats'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待VXLAN协议会话达到STARTED状态

    wait_vxlan_state(Sessions=[session_1, session_2])

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    time.sleep(5)

    stop_protocol()

    time.sleep(3)

    import pandas
    result = get_vxlan_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    # 获取VXLAN会话1统计

    result = get_vxlan_statistic(Session=session_1)
    print(result)

    # 获取VXLAN会话2统计

    result = get_vxlan_statistic(Session=session_2)
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
