# =================================================================================
# Objective   	:   测试目的 : 检查LDP VPLS向导配置生成正常
#
# Step			:	测试步骤1: 创建8个离线端口Port_1、Port_2;
#                   测试步骤2: 创建LDP VPLS向导;
#                   测试步骤3: 配置客户端侧端口和提供商侧端口;
#                   测试步骤4: 配置提供商侧路由器;
#                   测试步骤5: 配置VPLS;
#                   测试步骤6: 配置Host;
#                   测试步骤7: 配置流量;
#                   测试步骤8: 生成LDP VPLS向导配置;
#
# Criteria    	:   预期结果1: 步骤8 LDP VPLS向导配置生成无异常;
#
# Created by   	:  	Tester-001
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

    # 创建LDP VPLS向导

    wizard = create_mpls_wizard(Type='ldp_vpls')

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

    # 配置VPLS

    edit_mpls_vpls_basic_parameters(Wizard=wizard,
                                    NumberOfVpls=1000,
                                    Mtu=9000,
                                    GroupId=0,
                                    EnableOverrideEncapsulation=True,
                                    Encapsulation='EthernetVlan')

    edit_mpls_fec128(Wizard=wizard, StartVcId=1, StepVcId=1)

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

    # 生成LDP VPLS向导配置

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
