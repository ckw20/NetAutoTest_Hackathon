# =================================================================================
# Objective   	:   测试目的 : 检查Isis Lsp向导配置生成正常
#
# Step			:	测试步骤1: 创建2个离线端口Port_1、Port_2;
#                   测试步骤2: 创建Isis会话;
#                   测试步骤3: 创建Isis Lsp向导;
#                   测试步骤4: 生成向导配置;
#
# Criteria    	:   预期结果1: 步骤4 Isis Lsp向导配置生成无异常;
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
    Port_1, Port_2 = reserve_port(Locations=locations[:2], Debug=True)

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

    # 创建Isis会话
    Isis_1 = create_isis(Port=Port_1, IpVersion='IPV4IPV6')
    Isis_2 = create_isis(Port=Port_2, IpVersion='IPV4IPV6')

    select_interface(Session=Isis_1, Interface=interfaces_1)
    select_interface(Session=Isis_2, Interface=interfaces_2)

    # 创建Isis Lsp向导
    wizard = create_isis_lsp_wizard(Sessions=[Isis_1, Isis_2])

    # 配置组网拓扑
    config_isis_lsp_wizard_network_topo(Wizards=wizard, Type='GRID',
                                        GridNumberOfRows=10,
                                        GridNumberOfColumns=20)

    # 配置isis
    config_isis_lsp_wizard_isis(Wizards=wizard,
                                EnableTrafficEngine=True,
                                EnableSegmentRouting=True,
                                EnableSegmentRoutingIPv6=True,
                                EnableFlexAlgo=True)
    te = config_isis_lsp_wizard_isis_te(Wizards=wizard,
                                        EnableTeGroup=True,
                                        TeGroup=10)
    sr = config_isis_lsp_wizard_isis_sr(Wizards=wizard,
                                        ValueType='BIT32')
    srv6 = config_isis_lsp_wizard_isis_srv6(Wizards=wizard,
                                            MtId=10)
    flex_algo = config_isis_lsp_wizard_isis_flex_algo(Wizards=wizard,
                                                      FlexAlgo=255)

    # 配置ipv4 internal route
    config_isis_lsp_wizard_ipv4_internal_route(Wizards=wizard,
                                               Ipv4InternalRoutesPrefixLenType='CUSTOM',
                                               Ipv4InternalRoutesPrefixLenCustom=
                                               [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                0.0, 0.0, 0.0, 0.0, 0.0, 10, 0.0, 0.0, 0.0, 30, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                0.0, 0.0, 50]
                                                )

    # 配置ipv4 external route
    config_isis_lsp_wizard_ipv4_external_route(Wizards=wizard,
                                               Ipv4ExternalRoutesPrefixLenType='LINEAR',
                                               Ipv4ExternalRoutesPrefixLenStart=10,
                                               Ipv4ExternalRoutesPrefixLenEnd=20)

    # 配置ipv6 internal route
    config_isis_lsp_wizard_ipv6_internal_route(Wizards=wizard,
                                               Ipv6InternalWideMetric=20)

    # 配置ipv6 external route
    config_isis_lsp_wizard_ipv6_external_route(Wizards=wizard,
                                               Ipv6ExternalAdvEmulatedRouters=True
                                               )

    # 生成Isis Lsp向导配置
    expand_isis_lsp_wizard(Wizards=wizard)

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
