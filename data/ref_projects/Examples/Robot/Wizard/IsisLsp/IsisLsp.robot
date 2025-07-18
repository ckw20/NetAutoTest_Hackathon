*** Settings ***
Resource          ../../Common.robot

*** Test Cases ***
isis_lsp
    [Documentation]    测试目的 : 检查Isis Lsp向导配置生成正常
    ...
    ...    测试步骤1: 创建2个离线端口Port_1、Port_2;
    ...
    ...    测试步骤2: 创建Isis会话;
    ...
    ...    测试步骤3: 创建Isis Lsp向导;
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
    # 创建Isis会话
    ${isis_1}    create_isis    Port=${port_1}    IpVersion=IPV4IPV6
    ${isis_2}    create_isis    Port=${port_2}    IpVersion=IPV4IPV6
    select_interface    Session=${isis_1}    Interface=${interface_1}
    select_interface    Session=${isis_2}    Interface=${interface_2}
    ${isis}    Create List    ${isis_1}    ${isis_2}
    # 创建Isis Lsp向导
    ${wizard}    create_isis_lsp_wizard    Sessions=${isis}
    # 配置组网拓扑
    config_isis_lsp_wizard_network_topo    Wizards=${wizard}    Type=GRID    GridNumberOfRows=10    GridNumberOfColumns=20
    # 配置isis
    config_isis_lsp_wizard_isis    Wizards=${wizard}    EnableTrafficEngine=True    EnableSegmentRouting=True    EnableSegmentRoutingIPv6=True    EnableFlexAlgo=True
    config_isis_lsp_wizard_isis_te    Wizards=${wizard}    EnableTeGroup=True    TeGroup=10
    config_isis_lsp_wizard_isis_sr    Wizards=${wizard}    ValueType=BIT32
    config_isis_lsp_wizard_isis_srv6    Wizards=${wizard}    MtId=10
    config_isis_lsp_wizard_isis_flex_algo    Wizards=${wizard}    FlexAlgo=255
    # 配置ipv4 internal route
    config_isis_lsp_wizard_ipv4_internal_route    Wizards=${wizard}    Ipv4InternalAdvEmulatedRouters=True
    # 配置ipv4 external route
    config_isis_lsp_wizard_ipv4_external_route    Wizards=${wizard}    Ipv4ExternalRoutesOverride=True
    # 配置ipv6 internal route
    config_isis_lsp_wizard_ipv6_internal_route    Wizards=${wizard}    Ipv6InternalWideMetric=20
    # 配置ipv6 external route
    config_isis_lsp_wizard_ipv6_external_route    Wizards=${wizard}    Ipv6ExternalRoutesPrefixLenType=LINEAR
    # 生成Isis Lsp向导配置
    expand_isis_lsp_wizard    Wizards=${wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
