# =================================================================================
# Objective   	:   测试目的 : 使用智能脚本控制命令while if elseif else break
#
# Step			:	测试步骤1: 创建端口;
#                   测试步骤2: 创建bgp会话及路由;
#                   测试步骤3: 启动协议发送流量;
#                   测试步骤4: 检查统计;
#
# Criteria    	:   预期结果1: 步骤4 判断端口发送报文数量;
#
# Created by   	:  	Tester-002
#
# Bugs   	    :  	# None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.192/1/1', '//10.0.11.192/1/2', '//10.0.11.192/1/3'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'BigTao' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''

try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    port_1, port_2, port_3 = reserve_port(Locations=locations[:3])

    # 创建接口
    interfaces_1 = create_interface(Port=port_1, Layers='ipv4')
    interfaces_2 = create_interface(Port=port_2, Layers='ipv4')
    interfaces_3 = create_interface(Port=port_3, Layers='ipv4')

    # 创建BGP协议会话
    session_1 = create_bgp(Port=port_1)
    session_2 = create_bgp(Port=port_2)
    session_3 = create_bgp(Port=port_3)

    select_interface(Session=session_1, Interface=interfaces_1)
    select_interface(Session=session_2, Interface=interfaces_2)
    select_interface(Session=session_3, Interface=interfaces_3)

    # BGP协议会话1创建ipv4 route pool
    ipv4_route_1 = create_bgp_ipv4_route_pool(Session=session_1, FirstRoute='1.0.0.1')
    ipv4_route_2 = create_bgp_ipv4_route_pool(Session=session_2, FirstRoute='2.0.0.1')
    ipv4_route_3 = create_bgp_ipv4_route_pool(Session=session_3, FirstRoute='3.0.0.1')

    # 创建raw stream
    stream_1 = add_stream(Ports=port_1)
    stream_2 = add_stream(Ports=port_2)
    stream_3 = add_stream(Ports=port_3)

    # 订阅统计
    subscribe_result(Types=['PortStats'])

    # 使用智能脚本的while if elseif else break命令
    ggroup = smart_scripter_global_group()

    whilecommand = smart_scripter_command(ParentGroup=ggroup,
                                          Command='WhileCommand')
    bgp_handles = get_object_attrs([session_1, session_2, session_3])
    whilecontrol = smart_scripter_control_condition(ControlCommand=whilecommand,
                                                    ControlConditionName='StartProtocolCommand',
                                                    ConditionResult='PASS',
                                                    ProtocolList=bgp_handles)

    ifcommand = smart_scripter_command(ParentGroup=whilecommand,
                                       Command='IfCommand')
    stream_handle_1 = get_object_attrs(stream_1)
    startstreamcommand_1 = smart_scripter_command(ParentGroup=ifcommand,
                                                  Command='StartStreamCommand',
                                                  StreamList=stream_handle_1)

    bgp_route_1 = get_object_attrs(ipv4_route_1)
    ifcontrol = smart_scripter_control_condition(ControlCommand=ifcommand,
                                                 ControlConditionName='AdvertiseBgpRouteBlockCommand',
                                                 ConditionResult='PASS',
                                                 BgpRouteBlockHandles=bgp_route_1)
    breakcommand = smart_scripter_command(ParentGroup=ifcommand,
                                          Command='BreakCommand')

    elseifcommand = smart_scripter_command(ParentGroup=whilecommand,
                                           Command='ElseIfCommand')
    stream_handle_2 = get_object_attrs(stream_2)
    startstreamcommand_2 = smart_scripter_command(ParentGroup=elseifcommand,
                                                  Command='StartStreamCommand',
                                                  StreamList=stream_handle_2)
    bgp_route_2 = get_object_attrs(ipv4_route_2)
    elseifcontrol = smart_scripter_control_condition(ControlCommand=elseifcommand,
                                                     ControlConditionName='AdvertiseBgpRouteBlockCommand',
                                                     ConditionResult='PASS',
                                                     BgpRouteBlockHandles=bgp_route_2)

    elsecommand = smart_scripter_command(ParentGroup=whilecommand,
                                         Command='ElseCommand')
    stream_handle_3 = get_object_attrs(stream_3)
    startstreamcommand_3 = smart_scripter_command(ParentGroup=elsecommand,
                                                  Command='StartStreamCommand',
                                                  StreamList=stream_handle_3)

    run_benchmark()
    # 获取统计
    time.sleep(5)
    result = get_port_statistic()
    print(result)
    assert result['TxStreamFrames'][0] > 0
    stop_stream()
    clear_result()

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
