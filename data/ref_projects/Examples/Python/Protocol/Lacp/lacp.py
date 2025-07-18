# =================================================================================
# Objective   	:   测试目的 : 检查lacp统计获取正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建lacp;
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

    # 创建协议会话

    lacp_1 = create_lacp(Ports=Port_UP)
    lacp_2 = create_lacp(Ports=Port_Down)

    # 订阅统计

    subscribe_result(Types=['LacpPortStats', 'LagPortStats'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_lacp_port(Ports=[Port_UP, Port_Down])
    time.sleep(5)

    # 获取统计
    result = get_lacp_port_statistic(Port=Port_UP)
    print(result)

    result = get_lag_port_statistic(Lacp=lacp_1)
    print(result)

    stop_lacp_port(Ports=[Port_UP, Port_Down])


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
