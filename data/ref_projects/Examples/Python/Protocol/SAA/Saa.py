# =================================================================================
# Objective   	:   测试目的 : 检查Saa协议绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建Saa协议;
#                   测试步骤3: 启动协议，查看协议统计;
#
# Criteria    	:   预期结果1: 步骤3中统计获取正确;
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

    interfaces_1 = create_interface(Port=Port_UP, Layers='eth', Tops='ipv6')
    interfaces_2 = create_interface(Port=Port_Down, Layers='eth', Tops='ipv6')
    edit_interface(Interface=interfaces_1, Layer='IPv6Layer', Address='2022::2', Gateway='2022::3')
    edit_interface(Interface=interfaces_2, Layer='IPv6Layer', Address='2022::3', Gateway='2022::2')

    # 创建协议会话

    session_1 = create_saa(Port=Port_UP)
    session_2 = create_saa(Port=Port_Down)

    select_interface(Session=session_1, Interface=interfaces_1)
    select_interface(Session=session_2, Interface=interfaces_2)

    # 订阅统计

    subscribe_result(Types=['SaaPortStatistics', 'SaaSessionBlockStatistics', 'SaaSessionStatistics'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待协议会话达到状态

    wait_saa_state(Sessions=[session_1, session_2], State='IDLE')

    time.sleep(1)

    # 获取统计
    import pandas
    result = get_saa_port_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'
    result = get_saa_port_statistic(Port=Port_UP)
    print(result)
    result = get_saa_port_statistic(Port=Port_Down)
    print(result)

    result = get_saa_session_block_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'
    result = get_saa_session_block_statistic(Session=session_1)
    print(result)
    result = get_saa_session_block_statistic(Session=session_2)
    print(result)

    result = get_saa_session_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'
    result = get_saa_session_statistic(Session=session_1, SessionId=1)
    print(result)
    result = get_saa_session_statistic(Session=session_2, SessionId=1)
    print(result)

    stop_protocol()


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
