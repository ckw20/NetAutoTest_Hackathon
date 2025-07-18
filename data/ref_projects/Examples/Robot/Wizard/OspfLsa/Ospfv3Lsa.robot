*** Settings ***
Force Tags        Ospfv3 Lsa
Resource          ../../Common.robot

*** Test Cases ***
ospfv3_lsa_wizard
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口
    ${Ports}    reserve_port    Locations=${Locations}    Debug=True
    ${port_1}    ${port_2}    Set Variable    ${Ports}
    # 创建接口
    ${interface_1}    create_interface    Port=${port_1}    Layers=ipv6
    ${interface_2}    create_interface    Port=${port_2}    Layers=ipv6
    edit_interface    Interface=${interface_1}    Layer=IPv6Layer    Address=2001::1    Gateway=2001::2
    edit_interface    Interface=${interface_2}    Layer=IPv6Layer    Address=2001::2    Gateway=2001::1
    # 创建Ospfv3会话
    ${ospf_1}    create_ospfv3    Port=${port_1}
    ${ospf_2}    create_ospfv3    Port=${port_2}
    select_interface    Session=${ospf_1}    Interface=${interface_1}
    select_interface    Session=${ospf_2}    Interface=${interface_2}
    ${ospf}    Set Variable    ${ospf_1}    ${ospf_2}
    # 创建ospfv3 lsa向导
    ${wizard}    create_ospfv3_lsa_wizard    Sessions=${ospf}
    # 配置ospfv3拓扑
    config_ospfv3_lsa_wizard_ospfv3_topo    Wizards=${wizard}    Type=GRID    RowCount=10    ColumnCount=20
    # 配置ospfv3
    config_ospfv3_lsa_wizard_ospfv3    Wizards=${wizard}    AreaType=STUB
    # 配置ospfv3 Intra Area Route
    config_ospfv3_lsa_wizard_ospfv3_intra_area_route     Wizards=${wizard}    IntraAreaEmulated=ALL    IntraAreaSimulated=NONE
    # 配置ospfv3 Inter Area Route
    config_ospfv3_lsa_wizard_ospfv3_inter_area_route    Wizards=${wizard}    InterAreaRoutesCount=10
    # 配置ospfv3 external route
    config_ospfv3_lsa_wizard_ospfv3_external_route     Wizards=${wizard}    ExternalOverride=True
    # 生成Ospfv3 Lsa向导配置
    expand_ospfv3_lsa_wizard    Wizards=${wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
