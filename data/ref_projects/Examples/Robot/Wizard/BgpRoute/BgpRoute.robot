*** Settings ***
Documentation     BGP Route Wizard
Suite Setup
Suite Teardown
Resource          ../../Common.robot

*** Test Cases ***
bgp_route_wizard
    [Documentation]    测试目的 : 检查Bgp Route向导配置生成正常
    ...
    ...    测试步骤1: 创建2个离线端口Port_1、Port_2;
    ...
    ...    测试步骤2: 创建Bgp会话;
    ...
    ...    测试步骤3: 创建Bgp Route向导;
    ...
    ...    测试步骤4: 生成向导配置;
    [Tags]    Tester-002
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口
    ${Ports}    reserve_port    Locations=${Locations}    Debug=True
    ${port_1}    ${port_2}    Set Variable    ${Ports}
    # 创建接口
    ${layers}    Create List    ipv4    ipv6
    ${interface_1}    create_interface    Port=${port_1}    Layers=eth    Tops=${layers}
    ${interface_2}    create_interface    Port=${port_2}    Layers=eth    Tops=${layers}
    edit_interface    Interface=${interface_1}    Layer=IPv4Layer    Address=192.168.1.2    Gateway=192.168.1.3
    edit_interface    Interface=${interface_2}    Layer=IPv4Layer    Address=192.168.1.3    Gateway=192.168.1.2
    edit_interface    Interface=${interface_1}    Layer=IPv6Layer    Address=2001::1    Gateway=2001::2
    edit_interface    Interface=${interface_2}    Layer=IPv6Layer    Address=2001::2    Gateway=2001::1
    # 创建BGP会话
    ${bgp_1}    create_bgp    Port=${port_1}
    ${bgp_2}    create_bgp    Port=${port_2}
    select_interface    Session=${bgp_1}    Interface=${interface_1}
    select_interface    Session=${bgp_2}    Interface=${interface_2}
    ${bgps}    Set Variable    ${bgp_1}    ${bgp_2}
    # 创建BGP Route向导
    ${wizard}    create_bgp_route_wizard    Sessions=${bgps}    BgpRouteType=IPV4_IPV6    EnableLinkState=True
    # 配置ipv4 route
    config_bgp_route_wizard_ipv4    Wizards=${wizard}    TotalIpv4RouteCount=2
    # 配置ipv6 route
    config_bgp_route_wizard_ipv6    Wizards=${wizard}    TotalIpv6RouteCount=10
    # 配置IGP拓扑
    config_bgp_route_wizard_igp_topo    Wizards=${wizard}    ProtocolType=ISIS_IPV4
    # 配置IGP
    config_bgp_route_wizard_igp    Wizards=${wizard}    EnableTeOptions=True
    config_bgp_route_wizard_igp_te_option    Wizards=${wizard}    EnableUnreserved=True
    # 生成BGP Route向导配置
    expand_bgp_route_wizard    Wizards=${wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg

*** Keywords ***
