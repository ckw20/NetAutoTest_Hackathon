# =================================================================================
# Objective   	:   测试目的 : 使用智能脚本创建bgp协议并通告路由
#
# Step			:	测试步骤1: 创建2个离线端口Port_1、Port_2;
#                   测试步骤2: 创建bgp会话及路由;
#                   测试步骤3: 启动协议通告路由;
#                   测试步骤4: 检查统计;
#
# Criteria    	:   预期结果1: 步骤4 获取通告路由数量;
#
# Created by   	:  	Tester-002
#
# Bugs   	    :  	# None
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
    Port_1, Port_2 = reserve_port(Locations=locations[:2])

    # 创建接口
    interfaces_1 = create_interface(Port=Port_1, Layers='ipv4')
    interfaces_2 = create_interface(Port=Port_2, Layers='ipv4')

    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='192.168.1.2',
                   Gateway='192.168.1.3')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='192.168.1.3',
                   Gateway='192.168.1.2')

    # 创建BGP协议会话
    session_1 = create_bgp(Port=Port_1)
    session_2 = create_bgp(Port=Port_2)

    edit_bgp(Session=session_1, AsNumber=100, DutAsNumber=200)
    edit_bgp(Session=session_2, AsNumber=200, DutAsNumber=100)

    # BGP协议会话与接口绑定
    select_interface(Session=session_1, Interface=interfaces_1)
    select_interface(Session=session_2, Interface=interfaces_2)

    # BGP协议会话1创建ipv4 route pool
    ipv4_route_1 = create_bgp_ipv4_route_pool(Session=session_1, FirstRoute='100.0.0.1')
    ipv4_route_2 = create_bgp_ipv4_route_pool(Session=session_2, FirstRoute='200.0.0.1')

    # 订阅统计
    subscribe_result(Types=['BgpSessionBlockStatistic'])

    # 使用智能脚本启动协议
    ggroup = smart_scripter_global_group()
    group = smart_scripter_command(ggroup, 'GroupCommand', 'start')
#    start = smart_scripter_command(group, 'StartProtocolCommand', ProtocolList=[session_1.handle, session_2.handle])
    bgp = get_object_attrs([session_1, session_2])
    start = smart_scripter_command(group, 'StartProtocolCommand', ProtocolList=bgp)
    run_benchmark()
    #StartSmartScripterCommand().execute()
    wait_bgp_state(Sessions=[session_1, session_2])
    # 获取统计
    result = get_bgp_session_block_statistic(Session=session_1)
    print(result)
    result = get_bgp_session_block_statistic(Session=session_2)
    print(result)

    # 使用智能脚本停止协议
    group = smart_scripter_command(ggroup, 'GroupCommand', 'stop')
    stop = smart_scripter_command(group, 'StopProtocolCommand', ProtocolList=[session_1.handle, session_2.handle])
    run_benchmark()
    #StartSmartScripterCommand().execute()
    wait_bgp_state(Sessions=[session_1, session_2], State=['NOT_START'])

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
