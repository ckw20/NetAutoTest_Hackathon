# =================================================================================
# Objective   	:   测试目的 : 检查IEEE802.1As协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建Ieee802.1As协议，并且绑定接口;
#                   测试步骤3: 订阅Ieee802.1As相关统计;
#                   测试步骤4: 启动会话，等待一段时间;
#                   测试步骤5: 查看统计信息;
#
# Criteria    	:   预期结果1: 步骤5中所有统计结果均有数据;
#
# Created by   	:  	Tester-001
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
    interfaces_1 = create_interface(Port=Port_UP, Layers='ipv4')
    interfaces_2 = create_interface(Port=Port_Down, Layers='ipv4')

    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='192.168.1.2',
                   Gateway='192.168.1.3')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='192.168.1.3',
                   Gateway='192.168.1.2')

    # 创建IEEE802.1As协议会话
    session_1 = create_ieee8021as(Port=Port_UP)
    session_2 = create_ieee8021as(Port=Port_Down)

    # IEEE802.1As协议会话与接口绑定
    select_interface(Session=session_1, Interface=interfaces_1)
    select_interface(Session=session_2, Interface=interfaces_2)

    # 订阅统计
    subscribe_result(
        Types=['Ieee8021asClockStatistic', 'Ieee8021asClockSyncStatistic', 'Ieee8021asMessageRateStatistic',
               'Ieee8021asParentClockInfoStatistic', 'Ieee8021asStateSummaryStatistic',
               'Ieee8021asTimePropertiesStatistic'])

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议
    start_protocol()

    # 等待IEEE802.1As协议会话达到RUNNING状态
    time.sleep(3)
    wait_ieee8021as_state(Sessions=[session_1, session_2])
    wait_ieee8021as_clock_state(Sessions=[session_1, session_2])

    time.sleep(10)

    import pandas

    result = get_ieee8021as_clock_statistic()
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    result = get_ieee8021as_clock_sync_statistic()
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    result = get_ieee8021as_message_rate_statistic()
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    result = get_ieee8021as_parent_clock_info_statistic()
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    result = get_ieee8021as_state_summary_statistic()
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    result = get_ieee8021as_time_properties_statistic()
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    stop_protocol()
    time.sleep(3)

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
