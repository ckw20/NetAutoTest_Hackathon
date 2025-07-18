# =================================================================================
# Objective   	:   测试目的 : 检查BGP VPLS向导配置生成正常
#
# Step			:	测试步骤1: 创建8个离线端口Port_1、Port_2;
#                   测试步骤2: 创建BGP VPLS向导;
#                   测试步骤3: 配置客户端侧端口和提供商侧端口;
#                   测试步骤4: 配置提供商侧路由器;
#                   测试步骤5: 配置VPLS;
#                   测试步骤6: 配置Host;
#                   测试步骤7: 配置流量;
#                   测试步骤8: 生成BGP VPLS向导配置;
#
# Criteria    	:   预期结果1: 步骤8 BGP VPLS向导配置生成无异常;
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

# locations_1 = ['//10.0.11.191/1/13', '//10.0.11.191/1/14', '//10.0.11.191/1/15', '//10.0.11.191/1/16']
# locations_2 = ['//10.0.11.191/1/3', '//10.0.11.191/1/4', '//10.0.11.191/1/5', '//10.0.11.191/1/6']

locations_1 = locations[0]
locations_2 = locations[1]

try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口

    Port_customer = reserve_port(Locations=[locations_1], Debug=True)
    Port_provider = reserve_port(Locations=[locations_2], Debug=True)

    # 创建BGP VPLS向导

    wizard = create_mpls_wizard(Type='bgp_vpls', enable_vpls_scalability=True)

    # 配置客户端侧端口和提供商侧端口
    for port in Port_customer:
        edit_mpls_customer_port(Wizard=wizard, Port=port, EnableSubInterface=True, SubInterfaceCount=250,
                                VlanId=1000)
    for port in Port_provider:
        edit_mpls_provider_port(Wizard=wizard, Port=port, DutIpv4Address='50.1.1.1', Ipv4PrefixLength=24)

    # 配置提供商侧路由器

    edit_mpls_provider_router_basic_parameters(Wizard=wizard,
                                               DutRouterId='1.1.1.1',
                                               DutAsNumber=100,
                                               IgpProtocol='ISIS',
                                               MplsProtocol='LDP',
                                               EnablePRouter=False,
                                               PeRouterIdStart='2.1.1.1',
                                               PeRouterIdStep='0.0.0.1')
    edit_mpls_provider_router_isis(Wizard=wizard,
                                   UseSrcMacAsSystemId=False,
                                   SystemId='22:11:11:11:11:11',
                                   SystemIdStep='00:00:00:00:00:02',
                                   Level='L1L2',
                                   NetworkType='P2P',
                                   RouterPriority=10,
                                   MetricMode='WIDE',
                                   AuthenticationMode='SIMPLE',
                                   Password='passwd',
                                   AreaId=20,
                                   EnableGracefulRestart=True,
                                   MultiTopologyId='IPV4',
                                   EnableBfd=True,
                                   HelloPadding=False,
                                   Algorithm=30,
                                   SidLabelBase=40,
                                   SidLabelRange=50,
                                   NodeSidIndex=60,
                                   NodeSidIdnexStep=2)

    edit_mpls_provider_router_ldp(Wizard=wizard,
                                  HelloType='TARGETED',
                                  TransportAddressTlvMode='ROUTER_ID',
                                  LabelAdvertisementMode='DOD',
                                  EgressLabelMode='IMPLICIT',
                                  MinLabel=20,
                                  AuthenticationMode='MD5',
                                  Password='test')
    # 配置VPLS

    edit_bgp_vpls(Wizard=wizard,
                  NumberOfVplss=10,
                  RdAssignment='Manual',
                  RouteTargetStart='2:0',
                  RouteTargetStep='3:0',
                  Mtu=1518,
                  VplsAssignment='Sequential',
                  CustomerRdStart='4:0',
                  CustomerVeIdStart=20,
                  CustomerStepPerVplsEnabled=True,
                  CustomerRdStepPerVpls='5:0',
                  CustomerStepPerCeEnabled=True,
                  CustomerRdStepPerCe='6:0',
                  CustomerVeIdStepPerCe=30,
                  CustomerOverlapEnabled=True,
                  ProviderDistributionSelector='PEsPerVPLS',
                  ProviderDistributionSelectorCount=40,
                  ProviderMeshed=False,
                  ProviderRdStart='7:0',
                  ProviderVeIdStart=50,
                  ProviderStepPerVplsEnabled=True,
                  ProviderRdStepPerVpls='8:0',
                  ProviderStepPerCeEnabled=True,
                  ProviderRdStepPerCe='9:0',
                  ProviderVeIdStepPerCe=60,
                  ProviderOverlapEnabled=True)

    # 配置Host

    edit_mpls_host(Wizard=wizard,
                   HostAssignmentVpls='HostsOrMacsPerVpls',
                   HostsPerVpls=32,
                   CustomerHostPercent=50,
                   ProviderHostPercent=50)

    # 配置流量

    edit_traffic_parameters(Wizard=wizard,
                            TrafficFlow='CustomerProviderBoth',
                            StreamBlockGrouping='Aggregate',
                            TrafficLoadPercentProvider=10)

    # 生成BGP VPLS向导配置

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
