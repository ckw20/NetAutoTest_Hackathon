# =================================================================================
# Objective   	:   测试目的 : 检查twamp统计获取正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建client / server;
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
    interfaces_1 = create_interface(Port=Port_UP)
    interfaces_2 = create_interface(Port=Port_Down)
    edit_interface(Interface=interfaces_1, Layer='IPv4Layer', Address='1.1.1.1', Gateway='1.1.1.2')
    edit_interface(Interface=interfaces_2, Layer='IPv4Layer', Address='1.1.1.2', Gateway='1.1.1.1')

    # 创建协议会话

    client = create_twamp(Port=Port_UP,
                          ActiveClient=True,
                          PeerIpv4Address='1.1.1.2')
    server = create_twamp(Port=Port_Down,
                          ActiveServer=True)

    select_interface(Session=client, Interface=interfaces_1)
    select_interface(Session=server, Interface=interfaces_2)

    # 创建test session
    session_1 = edit_twamp_test_session(Twamps=client)
    session_2 = edit_twamp_test_session(Twamps=client)

    # 订阅统计

    subscribe_result(Types=['TwampClientStats', 'TwampServerStats'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    twamp_start(Sessions=[client, server])
    wait_twamp_state(Sessions=client)
    wait_twamp_state(Sessions=server, State='STARTED')
    time.sleep(2)

    # 获取统计
    result = get_twamp_client_statistic(Sessions=client)
    print(result)

    result = get_twamp_server_statistic(Sessions=server)
    print(result)

    twamp_stop(Sessions=[client, server])


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
