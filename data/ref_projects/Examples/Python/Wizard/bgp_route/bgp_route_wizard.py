# =================================================================================
# Objective   	:   测试目的 : 检查Bgp Route向导配置生成正常
#
# Step			:	测试步骤1: 创建2个离线端口Port_1、Port_2;
#                   测试步骤2: 创建Bgp会话;
#                   测试步骤3: 创建Bgp Route向导;
#                   测试步骤4: 生成向导配置;
#
# Criteria    	:   预期结果1: 步骤4 Bgp Route向导配置生成无异常;
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

try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    Port_1 = Port(upper=get_sys_entry())
    Port_2 = Port(upper=get_sys_entry())

    # 创建接口
    interfaces_1 = create_interface(Port=Port_1, Layers='eth', Tops=['ipv4', 'ipv6'])
    interfaces_2 = create_interface(Port=Port_2, Layers='eth', Tops=['ipv4', 'ipv6'])
    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='192.168.1.2',
                   Gateway='192.168.1.3')
    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='192.168.1.3',
                   Gateway='192.168.1.2')
    edit_interface(Interface=interfaces_1,
                   Layer='IPv6Layer',
                   Address='2001::1',
                   Gateway='2001::2')
    edit_interface(Interface=interfaces_1,
                   Layer='IPv6Layer',
                   Address='2001::2',
                   Gateway='2001::1')

    # 创建BGP会话
    Bgp_1 = create_bgp(Port=Port_1)
    Bgp_2 = create_bgp(Port=Port_2)

    select_interface(Session=Bgp_1, Interface=interfaces_1)
    select_interface(Session=Bgp_2, Interface=interfaces_2)

    # 创建BGP Route向导
    wizard = create_bgp_route_wizard(Sessions=[Bgp_1, Bgp_2],
                                     BgpRouteType='IPV4_IPV6',
                                     EnableLinkState=True)

    # 配置ipv4 route
    config_bgp_route_wizard_ipv4(Wizards=wizard,
                                 TotalIpv4RouteCount=2,
                                 IPv4DistributionType='LINEAR',
                                 PrefixLength=16,
                                 EndPrefixLength=32)

    # 配置ipv6 route
    config_bgp_route_wizard_ipv6(Wizards=wizard,
                                 TotalIpv6RouteCount=10)

    # 配置IGP拓扑
    config_bgp_route_wizard_igp_topo(Wizards=wizard,
                                     ProtocolType='ISIS_IPV4')

    # 配置IGP
    config_bgp_route_wizard_igp(Wizards=wizard,
                                EnableTeOptions=True)
    config_bgp_route_wizard_igp_te_option(Wizards=wizard,
                                          EnableUnreserved=True)

    # 生成BGP Route向导配置
    expand_bgp_route_wizard(Wizards=wizard)

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
