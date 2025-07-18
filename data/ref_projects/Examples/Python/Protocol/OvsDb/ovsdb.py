# =================================================================================
# Objective   	:   测试目的 : 检查ovsdb统计获取正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 创建ovsdb;
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
    edit_interface(Interface=interfaces_1, Layer='IPv4Layer', Address='1.1.1.2', Gateway='1.1.1.3')
    edit_interface(Interface=interfaces_2, Layer='IPv4Layer', Address='1.1.1.3', Gateway='1.1.1.2')

    # 创建协议会话

    ovsdb = create_ovsdb(Port=Port_UP)
    select_interface(Session=ovsdb, Interface=interfaces_1)


    # 订阅统计

    subscribe_result(Types=['OvsdbResults'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()
    wait_ovsdb_state(Sessions=ovsdb)
    time.sleep(2)

    # 获取统计
    result = get_ovsdb_statistic(Sessions=ovsdb)
    print(result)

    stop_protocol()


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
