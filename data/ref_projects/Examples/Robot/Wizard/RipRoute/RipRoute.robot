*** Settings ***
Documentation     Rip Route Wizard
Resource          ../../Common.robot

*** Test Cases ***
rip_route_wizard
    [Documentation]    测试目的 : 检查Rip Route向导配置生成正常
    ...
    ...    测试步骤1: 创建2个离线端口Port_1、Port_2;
    ...
    ...    测试步骤2: 创建Rip会话;
    ...
    ...    测试步骤3: 创建Rip Route向导;
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
    # 创建Rip会话
    ${rip_1}    create_rip    Port=${port_1}
    ${rip_2}    create_rip    Port=${port_2}    Version=RIPNG
    select_interface    Session=${rip_1}    Interface=${interface_1}
    select_interface    Session=${rip_2}    Interface=${interface_2}
    ${rip}    Create List    ${rip_1}    ${rip_2}
    # 创建Rip Route向导
    ${wizard}    create_rip_route_wizard    Sessions=${rip}
    # 配置ipv4 route
    config_rip_route_wizard_ipv4    Wizards=${wizard}    Ipv4RoutesPrefixLenType=LINEAR    Ipv4RoutesPrefixLenStart=8    Ipv4RoutesPrefixLenEnd=24
    # 配置ipv6 route
    config_rip_route_wizard_ipv6    Wizards=${wizard}    Ipv6StartRoutesPrefix=2022::    Ipv6EndRoutesPrefix=2033::
    # 生成Rip Route向导配置
    expand_rip_route_wizard     Wizards=${wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
