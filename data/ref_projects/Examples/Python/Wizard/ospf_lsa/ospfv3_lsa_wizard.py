# =================================================================================
# Objective   	:   测试目的 : 检查Ospfv3 Lsa向导配置生成正常
#
# Step			:	测试步骤1: 创建2个离线端口Port_1、Port_2;
#                   测试步骤2: 创建Ospfv3会话;
#                   测试步骤3: 创建Ospfv3 Lsa向导;
#                   测试步骤4: 生成向导配置;
#
# Criteria    	:   预期结果1: 步骤4 Ospfv3 Lsa向导配置生成无异常;
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
    interfaces_1 = create_interface(Port=Port_1, Layers='ipv6')
    interfaces_2 = create_interface(Port=Port_2, Layers='ipv6')
    edit_interface(Interface=interfaces_1,
                   Layer='IPv6Layer',
                   Address='2001::1',
                   Gateway='2001::2')
    edit_interface(Interface=interfaces_1,
                   Layer='IPv6Layer',
                   Address='2001::2',
                   Gateway='2001::1')

    # 创建Ospfv3会话
    ospf_1 = create_ospfv3(Port=Port_1)
    ospf_2 = create_ospfv3(Port=Port_2)

    select_interface(Session=ospf_1, Interface=interfaces_1)
    select_interface(Session=ospf_2, Interface=interfaces_2)

    # 创建Ospfv3 lsa向导
    wizard = create_ospfv3_lsa_wizard(Sessions=[ospf_1, ospf_2])

    # 配置Ospfv3拓扑
    config_ospfv3_lsa_wizard_ospfv3_topo(Wizards=wizard, Type='GRID',
                                         RowCount=10,
                                         ColumnCount=20)

    # 配置Ospfv3
    config_ospfv3_lsa_wizard_ospfv3(Wizards=wizard,
                                    AreaType='STUB')

    # 配置Ospfv3 intra area route
    config_ospfv3_lsa_wizard_ospfv3_intra_area_route(Wizards=wizard,
                                                     IntraAreaEmulated='ALL',
                                                     IntraAreaSimulated='NONE'
                                                     )

    # 配置Ospfv3 inter area route
    config_ospfv3_lsa_wizard_ospfv3_inter_area_route(Wizards=wizard,
                                                     InterAreaRoutesCount=10)

    # 配置Ospfv3 external network
    config_ospfv3_lsa_wizard_ospfv3_external_route(Wizards=wizard,
                                                   ExternalDistributionType='CUSTOM',
                                                   ExternalCustomPrefixLength=[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0,
                                                                               10, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 10, 0.0, 0.0, 0.0,
                                                                               10, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               10,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                               ])

    # 生成Ospfv3 Lsa向导配置
    expand_ospfv3_lsa_wizard(Wizards=wizard)

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
