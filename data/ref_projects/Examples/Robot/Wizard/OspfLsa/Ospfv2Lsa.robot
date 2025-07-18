*** Settings ***
Documentation     Ospfv2 Lsa Wizard
Force Tags        Ospfv2 Lsa
Resource          ../../Common.robot

*** Test Cases ***
ospfv2_lsa_wizard
    [Documentation]    测试目的 : 检查Ospfv2 Lsa向导配置生成正常
    ...
    ...    测试步骤1: 创建2个离线端口Port_1、Port_2;
    ...
    ...    测试步骤2: 创建Ospfv2会话;
    ...
    ...    测试步骤3: 创建Ospfv2 Lsa向导;
    ...
    ...    测试步骤4: 生成向导配置;
    [Tags]    Tester-002
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口
    ${Ports}    reserve_port    Locations=${Locations}    Debug=True
    ${port_1}    ${port_2}    Set Variable    ${Ports}
    # 创建接口
    ${interface_1}    create_interface    Port=${port_1}    Layers=ipv4
    ${interface_2}    create_interface    Port=${port_2}    Layers=ipv4
    edit_interface    Interface=${interface_1}    Layer=IPv4Layer    Address=192.168.1.2    Gateway=192.168.1.3
    edit_interface    Interface=${interface_2}    Layer=IPv4Layer    Address=192.168.1.3    Gateway=192.168.1.2
    # 创建Ospfv2会话
    ${ospf_1}    create_ospf    Port=${port_1}
    ${ospf_2}    create_ospf    Port=${port_2}
    select_interface    Session=${ospf_1}    Interface=${interface_1}
    select_interface    Session=${ospf_2}    Interface=${interface_2}
    ${ospf}    Set Variable    ${ospf_1}    ${ospf_2}
    # 创建ospfv2 lsa向导
    ${wizard}    create_ospfv2_lsa_wizard    Sessions=${ospf}
    # 配置ospfv2拓扑
    config_ospfv2_lsa_wizard_ospfv2_topo    Wizards=${wizard}    Type=GRID    RowCount=10    ColumnCount=20
    # 配置ospfv2
    config_ospfv2_lsa_wizard_ospfv2    Wizards=${wizard}    EnableTeOption=True    EnableSegmentRouting=True
    config_ospfv2_lsa_wizard_ospfv2_te_option    Wizards=${wizard}    EnableGroup=True    Group=10
    config_ospfv2_lsa_wizard_ospfv2_sr    Wizards=${wizard}    SidLabelType=BIT32
    # 配置ospfv2 stub network
    config_ospfv2_lsa_wizard_ospfv2_stub_network    Wizards=${wizard}    StubStartingIpPrefix=1.1.1.1    StubEndingIpPrefix=2.2.2.2    StubOverride=True
    # 配置ospfv2 summary network
    config_ospfv2_lsa_wizard_ospfv2_summary_route    Wizards=${wizard}    SummaryEmulated=NONE    SummarySimulated=ALL
    # 配置ospfv2 external network
    config_ospfv2_lsa_wizard_ospfv2_external_route    Wizards=${wizard}    ExternalPrimaryMetric=20
    # 生成Ospfv2 Lsa向导配置
    expand_ospfv2_lsa_wizard    Wizards=${wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
