# =================================================================================
# Objective   	:   测试目的 : 检查MPLS IP VPN向导配置生成正常
#
# Step			:	测试步骤1: 创建2个离线端口Port_1、Port_2;
#                   测试步骤2: 创建MPLS IP VPN向导;
#                   测试步骤3: 配置客户端侧端口和提供商侧端口;
#                   测试步骤4: 配置提供商侧路由器;
#                   测试步骤5: 配置VPN;
#                   测试步骤6: 配置VPN路由;
#                   测试步骤7: 配置VPN流量;
#                   测试步骤8: 配置LSP Ping;
#                   测试步骤9: 生成向导配置;
#
# Criteria    	:   预期结果1: 步骤9 MPLS IP VPN向导配置生成无异常;
#
# Created by   	:  	Tester-002
#
# Bugs   	    :  	# None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/15', '//10.0.11.191/1/16'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''

try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口

    Port_customer = reserve_port(Locations=[locations[0]], Force=True)
    Port_provider = reserve_port(Locations=[locations[1]], Force=True)

    # 创建MPLS IP VPN向导

    wizard = create_mpls_wizard(Type='mpls_ip_vpn')

    # 配置客户端侧端口和提供商侧端口
    edit_mpls_customer_port(Wizard=wizard, Port=Port_customer[0],
                            EnableSubInterface=True, SubInterfaceCount=250,
                            DutIpv4Address='1.1.1.1', VlanId=1000)
    edit_mpls_provider_port(Wizard=wizard, Port=Port_provider[0],
                            DutIpv4Address='50.1.1.1', Ipv4PrefixLength=24)

    # 配置提供商侧路由器

    edit_mpls_provider_router_basic_parameters(Wizard=wizard,
                                               DutRouterId='2.2.2.2',
                                               DutAsNumber=100,
                                               IgpProtocol='ISIS',
                                               MplsProtocol='LDP',
                                               EnablePRouter=True,
                                               PRoutersPerInterface=10,
                                               TopologyType='Grid',
                                               PRouterStartIp='3.3.3.3',
                                               PRouterIdStart='4.4.4.4',
                                               PeRoutersPerInterface=20,
                                               PeRouterIdStart='5.5.5.5',
                                               EnableRouteReflectors=True)
    edit_mpls_provider_router_isis(Wizard=wizard,
                                   UseSrcMacAsSystemId=False,
                                   SystemId='22:22:22:22:22:22',
                                   Level='L1L2',
                                   NetworkType='P2P',
                                   RouterPriority=10,
                                   MetricMode='WIDE',
                                   AuthenticationMode='SIMPLE',
                                   Password='test',
                                   AreaId=20,
                                   EnableGracefulRestart=True,
                                   MultiTopologyId='IPV4',
                                   EnableBfd=True,
                                   )
    edit_mpls_provider_router_ldp(Wizard=wizard,
                                  HelloType='DIRECT_TARGETED',
                                  TransportAddressTlvMode='ROUTER_ID',
                                  LabelAdvertisementMode='DOD',
                                  EgressLabelMode='IMPLICIT',
                                  MinLabel=20,
                                  AuthenticationMode='MD5',
                                  Password='test')
    # edit_mpls_provider_route_reflector(Wizard=wizard,
    #                                    RouteReflectorSource='DutAsRouteReflector',
    #                                    RrsPerPortOrSubInterface=1,
    #                                    RrsPerPe=1,
    #                                    RrRouterIdStart='1.1.1.1',
    #                                    ClusterIdStart='2.2.2.2')
    edit_mpls_provider_route_reflector(Wizard=wizard,
                                       RrRouterIds=['1.1.1.1','2.2.2.2'])

    # 配置VPN

    edit_mpls_vpn_parameters(Wizard=wizard,
                             NumberOfVpns=10,
                             RdAssignment='Manual',
                             RouteTargetStart='2:0')

    edit_mpls_vpn_customer_parameters(Wizard=wizard,
                                      VpnAssignment='Sequential',
                                      CeProtocol='Mixed',
                                      CeProAssignment='BGP=20%,RIP=40%,OSPF=30%,IS-IS=5%,Static=5%',
                                      CustomerRdStart='3:0',
                                      CustomerRdStepPerVpn='4:0',
                                      CustomerRdStepPerCeEnabled=True,
                                      CustomerRdStepPerCe='5:0')
    edit_mpls_vpn_as_number(Wizard=wizard,
                            CustomerCeAsNumberStart=10,
                            CustomerCeAsNumberStepPerVpn=20,
                            CustomerCeAsNumberStepPerCeEnabled=True,
                            CustomerCeAsNumberStepPerCe=30)

    edit_mpls_vpn_provider_parameters(Wizard=wizard,
                                      ProviderDisSel='PEsPerVPN',
                                      ProviderMeshed=True,
                                      ProviderRdStart='6:0',
                                      ProviderRdStepPerVpn='7:0',
                                      ProviderRdStepPerCeEnabled=True,
                                      ProviderRdStepPerCe='8:0')
    edit_mpls_vpn_as_number(Wizard=wizard,
                            ProviderAppendCeAsToPath=True,
                            ProviderCeAsNumberStart=10,
                            ProviderCeAsNumberStepPerVpnEnabled=True,
                            ProviderCeAsNumberStepPerVpn=20,
                            ProviderCeAsNumberStepPerCeEnabled=True,
                            ProviderCeAsNumberStepPerCe=30)

    # 配置VPN路由

    edit_mpls_vpn_ipv4_route_customer_parameters(Wizard=wizard,
                                                 CustomerStartRoute='1.1.1.1',
                                                 CustomerRouteStep='0.1.0.0',
                                                 CustomerPrefixLength=16,
                                                 CustomerRoutesPerCe=10,
                                                 CustomerOverlapRoutes=True,
                                                 CustomerRouteType='External')
    edit_mpls_vpn_ipv4_route_provider_parameters(Wizard=wizard,
                                                 ProviderStartRoute='2.2.2.2',
                                                 ProviderRouteStep='0.1.0.0',
                                                 ProviderPrefixLength=16,
                                                 ProviderRoutesPerCe=20,
                                                 ProviderOverlapRoutes=True,
                                                 ProviderLabelType='LabelPerRoute',
                                                 ProviderStartLabel=30)

    # 配置流量

    edit_traffic_parameters(Wizard=wizard,
                            TrafficFlow='CustomerProviderBoth',
                            StreamBlockGrouping='Aggregate',
                            UseSingleStreamNumber=True,
                            TrafficLoadPercentProvider=10,
                            TrafficLoadPercentCustomer=20)

    # 配置Lsp Ping

    edit_lsp_ping(Wizard=wizard,
                  EnableLspPing=True,
                  DestinationIpv4Address='1.1.1.1',
                  PingInterval=10,
                  PingTimeout=20,
                  TimeToLive=30,
                  LspExpValue=7,
                  ValidateFecStack=True,
                  PadMode='RequestPeerToDropPadTlv',
                  PadData=[1,2,3])

    # 生成MPLS IP VPN向导配置

    expand_mpls_wizard(Wizard=wizard)

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
