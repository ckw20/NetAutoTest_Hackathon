*** Settings ***
Resource          ../Common.robot
*** Test Cases ***
groupcommand
    [Documentation]    测试目的 : 使用智能脚本创建bgp协议并通告路由
    ...
    ...    测试步骤1: 创建2个离线端口Port_1、Port_2;
    ...
    ...    测试步骤2: 创建bgp会话及路由;
    ...
    ...    测试步骤3: 启动协议通告路由;
    ...
    ...    测试步骤4: 检查统计;
    ...
    ...    预期结果1: 步骤4 获取通告路由数量;
    [Tags]    Tester-002
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv4
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv4
    edit_interface    Interface=${Interface_1}    Layer=IPv4Layer    Address=192.168.1.3
    edit_interface    Interface=${Interface_2}    Layer=IPv4Layer    Address=192.168.1.2
    # 创建BGP协议会话
    ${Session_1}    create_bgp    Port=${Ports[0]}
    ${Session_2}    create_bgp    Port=${Ports[1]}
    ${Sessions}    Create List    ${Session_1}    ${Session_2}
    edit_bgp    Session=${Session_1}    AsNumber=100    DutAsNumber=200
    edit_bgp    Session=${Session_2}    AsNumber=200    DutAsNumber=100
    # BGP协议会话与接口绑定
    select_interface    Session=${Session_1}    Interface=${Interface_1}
    select_interface    Session=${Session_2}    Interface=${Interface_2}
    # BGP协议会话创建route pool
    ${RoutePool_1}    create_bgp_ipv4_route_pool    Session=${Session_1}    RouteCount=10
    ${RoutePool_2}    create_bgp_ipv4_route_pool    Session=${Session_2}    RouteCount=10
    # 订阅StreamBlockStats、BgpSessionStatistic、BgpSessionBlockStatistic统计视图
    ${SubscribeTypes}    Create List    BgpSessionBlockStatistic
    subscribe_result    Types=${SubscribeTypes}
    # 使用智能脚本启动协议
    ${ggroup}    smart_scripter_global_group
    ${group}    smart_scripter_command    ${ggroup}    GroupCommand    start
    ${handles}    get_object_attrs    ${Sessions}
    ${start}    smart_scripter_command    ${group}    StartProtocolCommand    ProtocolList=${handles}
    run_benchmark
    wait_bgp_state    Sessions=${Session_1}
    wait_bgp_state    Sessions=${Session_2}
    ${Result}    get_bgp_session_block_statistic    Session=${Session_1}
    Log    ${Result}
    &{Result}    get_bgp_session_block_statistic    Session=${Session_2}
    Log    ${Result}
    # 使用智能脚本停止协议
    ${group}    smart_scripter_command    ${ggroup}    GroupCommand    stop
    ${stop}    smart_scripter_command    ${group}    StopProtocolCommand    ProtocolList=${handles}
    run_benchmark
    wait_bgp_state    Sessions=${Session_1}    State=NOT_START
    wait_bgp_state    Sessions=${Session_2}    State=NOT_START
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg

controlcommand
    [Documentation]    测试目的 : 使用智能脚本控制命令while if elseif else break
    ...
    ...    测试步骤1: 创建端口;
    ...
    ...    测试步骤2: 创建bgp会话及路由;
    ...
    ...    测试步骤3: 启动协议发送流量;
    ...
    ...    测试步骤4: 检查统计;
    ...
    ...    预期结果1: 步骤4 判断端口发送报文数量;
    [Tags]    Tester-002
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv4
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv4
    ${Interface_3}    create_interface    Port=${Ports[2]}    Layers=IPv4
    edit_interface    Interface=${Interface_1}    Layer=IPv4Layer    Address=192.168.1.2
    edit_interface    Interface=${Interface_2}    Layer=IPv4Layer    Address=192.168.1.3
    edit_interface    Interface=${Interface_3}    Layer=IPv4Layer    Address=192.168.1.4
    # 创建BGP协议会话
    ${Session_1}    create_bgp    Port=${Ports[0]}
    ${Session_2}    create_bgp    Port=${Ports[1]}
    ${Session_3}    create_bgp    Port=${Ports[2]}
    ${Sessions}    Create List    ${Session_1}    ${Session_2}    ${Session_3}
    edit_bgp    Session=${Session_1}    AsNumber=100    DutAsNumber=200
    edit_bgp    Session=${Session_2}    AsNumber=200    DutAsNumber=100
    # BGP协议会话与接口绑定
    select_interface    Session=${Session_1}    Interface=${Interface_1}
    select_interface    Session=${Session_2}    Interface=${Interface_2}
    select_interface    Session=${Session_3}    Interface=${Interface_3}
    # BGP协议会话创建route pool
    ${RoutePool_1}    create_bgp_ipv4_route_pool    Session=${Session_1}    RouteCount=10
    ${RoutePool_2}    create_bgp_ipv4_route_pool    Session=${Session_2}    RouteCount=10
    ${RoutePool_3}    create_bgp_ipv4_route_pool    Session=${Session_3}    RouteCount=10
    # 创建raw stream
    ${stream_1}    add_stream    Ports=${Ports[0]}
    ${stream_2}    add_stream    Ports=${Ports[1]}
    ${stream_3}    add_stream    Ports=${Ports[2]}
    # 订阅StreamBlockStats、BgpSessionStatistic、BgpSessionBlockStatistic统计视图
    ${SubscribeTypes}    Create List    PortStats
    subscribe_result    Types=${SubscribeTypes}
    # 使用智能脚本的while if elseif else break命令
    ${ggroup}    smart_scripter_global_group
    ${whilecommand}    smart_scripter_command    ParentGroup=${ggroup}    Command=WhileCommand
    ${bgphandles}    get_object_attrs    ${Sessions}
    ${whilecontrol}    smart_scripter_control_condition    ControlCommand=${whilecommand}    ControlConditionName=StartProtocolCommand    ConditionResult=PASS    ProtocolList=${bgphandles}
    ${ifcommand}    smart_scripter_command    ParentGroup=${whilecommand}    Command=IfCommand
    ${stream_handle_1}    get_object_attrs    ${stream_1}
    ${startstreamcommand_1}    smart_scripter_command    ParentGroup=${ifcommand}    Command=StartStreamCommand    StreamList=${stream_handle_1}
    ${bgp_route_1}    get_object_attrs    ${RoutePool_1}
    ${ifcontrol}    smart_scripter_control_condition    ControlCommand=${ifcommand}    ControlConditionName=AdvertiseBgpRouteBlockCommand    ConditionResult=PASS    BgpRouteBlockHandles=${bgp_route_1}
    ${breakcommand}    smart_scripter_command    ParentGroup=${ifcommand}    Command=BreakCommand
    ${elseifcommand}    smart_scripter_command    ParentGroup=${whilecommand}    Command=ElseIfCommand
    ${stream_handle_2}    get_object_attrs    ${stream_2}
    ${startstreamcommand_2}    smart_scripter_command    ParentGroup=${elseifcommand}    Command=StartStreamCommand    StreamList=${stream_handle_2}
    ${bgp_route_2}    get_object_attrs    ${RoutePool_2}
    ${elseifcontrol}    smart_scripter_control_condition    ControlCommand=${elseifcommand}    ControlConditionName=AdvertiseBgpRouteBlockCommand    ConditionResult=PASS    BgpRouteBlockHandles=${bgp_route_2}
    ${elsecommand}    smart_scripter_command    ParentGroup=${whilecommand}    Command=ElseCommand
    ${stream_handle_3}    get_object_attrs    ${stream_3}
    ${startstreamcommand_3}    smart_scripter_command    ParentGroup=${elsecommand}    Command=StartStreamCommand    StreamList=${stream_handle_3}
    # 启动智能脚本
    run_benchmark
    # 获取统计
    Sleep    5
    ${result}    get_port_statistic
    Log    ${result}
    ${TxStreamFrames}    Get From Dictionary    ${result}    key=TxStreamFrames
    Should Be True    ${TxStreamFrames[0]} > 0
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
