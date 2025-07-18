# =================================================================================
# Objective   	:   测试目的 : 检查802.3ah协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建802.3ah协议;
#                   测试步骤3: 启动协议，查看协议统计;
#
# Criteria    	:   预期结果1: 步骤6中所有流量收发包相等;
#
# Created by   	:  	Tester-003
#
# Bugs   	    :  	None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/9', '//10.0.11.191/1/10'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
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

    edit_interface_stack(Interfaces=interfaces_1)
    edit_interface_stack(Interfaces=interfaces_2)

    edit_interface(Interface=interfaces_1, Layer='IPv4Layer', Address='1.1.1.1', Gateway='1.1.1.2')
    edit_interface(Interface=interfaces_2, Layer='IPv4Layer', Address='1.1.1.2', Gateway='1.1.1.1')

    # 创建802.3ah协议会话

    session_1 = create_dot3ah(Port=Port_UP)
    session_2 = create_dot3ah(Port=Port_Down)

    select_interface(Session=session_1, Interface=interfaces_1)
    select_interface(Session=session_2, Interface=interfaces_2)


    # 订阅统计

    subscribe_result(Types=['Dot3ahErrorEventStats', 'Dot3ahSessionStatistic'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待802.3ah协议会话达到COMPLETED状态

    wait_dot3ah_state(Sessions=[session_1, session_2], State='COMPLETED')

    time.sleep(5)

    # 获取802.3ah会话1统计
    import pandas
    result = get_dot3ah_error_event_stats()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_dot3ah_error_event_stats(Session=session_1)
    print(result)
    result = get_dot3ah_error_event_stats(Session=session_2)
    print(result)

    result = get_dot3ah_session_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_dot3ah_session_statistic(Session=session_1)
    print(result)
    result = get_dot3ah_session_statistic(Session=session_2)
    print(result)

    stop_protocol()


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
