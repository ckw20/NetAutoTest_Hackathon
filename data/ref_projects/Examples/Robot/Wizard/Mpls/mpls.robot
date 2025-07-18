*** Settings ***
Documentation     MPLS Wizard
Suite Setup       SuiteSetup
Resource          ../../Common.robot
*** Test Cases ***
mpls_ip_vpn
    [Documentation]    测试目的 : 检查MPLS IP VPN向导配置生成正常
    [Tags]    Tester-002
    [Setup]    CaseSetup    type=mpls_ip_vpn
    # 配置提供商侧路由器
    edit_mpls_provider_router_basic_parameters    Wizard=${wizard}    EnableRouteReflectors=True
    ${address}    Create List    3.3.3.3    4.4.4.4
    edit_mpls_provider_route_reflector    Wizard=${wizard}    RrRouterIds=${address}
    # 配置VPN
    edit_mpls_vpn_parameters    Wizard=${wizard}    NumberOfVpns=10
    edit_mpls_vpn_customer_parameters    Wizard=${wizard}    VpnAssignment=Sequential
    edit_mpls_vpn_provider_parameters    Wizard=${wizard}    ProviderMeshed=True
    edit_mpls_vpn_as_number    Wizard=${wizard}    CustomerCeAsNumberStart=10    ProviderAppendCeAsToPath=True    ProviderCeAsNumberStart=20
    # 配置VPN路由
    edit_mpls_vpn_ipv4_route_customer_parameters    Wizard=${wizard}    CustomerStartRoute=1.1.2.1
    edit_mpls_vpn_ipv4_route_provider_parameters    Wizard=${wizard}    ProviderStartRoute=1.1.3.1
    # 配置VPN流量
    edit_traffic_parameters    Wizard=${wizard}    TrafficFlow=CustomerProviderBoth
    # 配置LSP Ping
    edit_lsp_ping    Wizard=${wizard}    EnableLspPing=True    DestinationIpv4Address=2.2.2.2
    [Teardown]    CaseTeardown

6pe_6vpe
    [Documentation]    测试目的 : 检查6PE/6VPE向导配置生成正常
    [Tags]    Tester-002
    [Setup]    CaseSetup    type=mpls_6vpe
    # 配置提供商侧路由器
    edit_mpls_provider_router_basic_parameters    Wizard=${wizard}    Enable6Vpe=True
    # 配置VPN
    edit_mpls_vpn_parameters    Wizard=${wizard}    NumberOfVpns=10
    edit_mpls_vpn_customer_parameters    Wizard=${wizard}    VpnAssignment=Sequential
    edit_mpls_vpn_provider_parameters    Wizard=${wizard}    ProviderMeshed=True
    edit_mpls_vpn_as_number    Wizard=${wizard}    CustomerCeAsNumberStart=10    ProviderAppendCeAsToPath=True    ProviderCeAsNumberStart=20
    # 配置VPN路由
    edit_mpls_vpn_ipv6_route_customer_parameters    Wizard=${wizard}    CustomerStartRoute=2022::2
    edit_mpls_vpn_ipv6_route_provider_parameters    Wizard=${wizard}    ProviderStartRoute=2033::3
    # 配置VPN流量
    edit_traffic_parameters    Wizard=${wizard}    TrafficFlow=CustomerProviderBoth
    [Teardown]    CaseTeardown

bgp_vpls
    [Documentation]    测试目的 : 检查BGP VPLS向导配置生成正常
    [Tags]    Tester-002
    [Setup]    Casesetup    type=bgp_vpls
    # 配置VPLS
    edit_bgp_vpls    Wizard=${wizard}    NumberOfVplss=10    CustomerOverlapEnabled=True    ProviderOverlapEnabled=True
    # 配置Host
    edit_mpls_host    Wizard=${wizard}    EnableHostVlan=True    VlanIdStart=10
    # 配置VPN流量
    edit_traffic_parameters    Wizard=${wizard}    TrafficFlow=CustomerProviderBoth
    [Teardown]    CaseTeardown

ldp_vpls
    [Documentation]    测试目的 : 检查LDP VPLS向导配置生成正常
    [Tags]    Tester-002
    [Setup]    Casesetup    type=ldp_vpls
    edit_mpls_vpls_basic_parameters    Wizard=${wizard}    NumberOfVpls=10    VplsAssignment=Sequential    FecType=FEC129
    edit_mpls_fec129    Wizard=${wizard}    Agi=30:1    Saii=3.3.3.3    Taii=4.4.4.4
    # 配置Host
    edit_mpls_host    Wizard=${wizard}    HostAssignmentVpls=HostsOrMacsPerVpls    HostsPerCustomerCe=10    HostsPerProviderCe=20
    # 配置VPN流量
    edit_traffic_parameters    Wizard=${wizard}    TrafficFlow=CustomerProviderBoth
    [Teardown]    CaseTeardown

pwe
    [Documentation]    测试目的 : 检查PWE向导配置生成正常
    [Tags]    Tester-002
    [Setup]    CaseSetup    type=pwe
    # 配置伪线
    edit_mpls_pwe_basic_parameters    Wizard=${wizard}    NumberOfPseudoWire=10    FecType=FEC128
    edit_mpls_fec128    Wizard=${wizard}    StartVcId=10
    # 配置Host
    edit_mpls_host    Wizard=${wizard}    HostAssignmentVpls=HostsOrMacsPerVpls    HostsPerCustomerCe=10    HostsPerProviderCe=20
    # 配置VPN流量
    edit_traffic_parameters    Wizard=${wizard}    TrafficFlow=CustomerProviderBoth
    # 配置LSP Ping
    edit_lsp_ping    Wizard=${wizard}    EnableLspPing=True    DestinationIpv4Address=2.2.2.2
    [Teardown]    CaseTeardown
*** Keywords ***
SuiteSetup
    [Documentation]    MPLS Wizard suite setup
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}    Force=True
    ${Provider}    ${Customer}    Set Variable    ${Ports}
    Set Suite Variable    ${Provider}
    Set Suite Variable    ${Customer}

CaseSetup
    [Arguments]    ${type}
    [Documentation]    MPLS wizard case setup
    # 创建向导对象
    ${wizard}    create_mpls_wizard    Type=${type}
    Set Suite Variable    ${wizard}
    # 选择端口
    edit_mpls_customer_port    Wizard=${wizard}    Port=${Customer}    DutIpv4Address=1.1.1.1    EnableSubInterface=True    SubInterfaceCount=10
    edit_mpls_provider_port    Wizard=${wizard}    Port=${Provider}    DutIpv4Address=2.2.2.2
    # 配置提供商侧路由器
    edit_mpls_provider_router_basic_parameters    Wizard=${wizard}    IgpProtocol=ISIS    MplsProtocol=LDP
    edit_mpls_provider_router_isis    Wizard=${wizard}    Level=L1L2
    edit_mpls_provider_router_ldp    Wizard=${wizard}    HelloType=DIRECT_TARGETED

CaseTeardown
    [Documentation]    MPLS Wizard case teardown
    # 生成向导配置
    expand_mpls_wizard    Wizard=${wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # Shutdown Tester
