# =================================================================================
# Objective   	:   测试目的 : 检查Rip Route向导配置生成正常
#
# Step			:	测试步骤1: 创建2个离线端口Port_1、Port_2;
#                   测试步骤2: 创建Rip会话;
#                   测试步骤3: 创建Rip Route向导;
#                   测试步骤4: 生成向导配置;
#
# Criteria    	:   预期结果1: 步骤4 Rip Route向导配置生成无异常;
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

    # 创建Rip会话
    rip_1 = create_rip(Port=Port_1)
    rip_2 = create_rip(Port=Port_2, Version='RIPNG')

    select_interface(Session=rip_1, Interface=interfaces_1)
    select_interface(Session=rip_2, Interface=interfaces_2)

    # 创建Rip Route向导
    wizard = create_rip_route_wizard(Sessions=[rip_1, rip_2])

    # 配置ipv4 route
    config_rip_route_wizard_ipv4(Wizards=wizard,
                                 Ipv4RoutesPrefixLenType='LINEAR',
                                 Ipv4RoutesPrefixLenStart=8,
                                 Ipv4RoutesPrefixLenEnd=24)

    # 配置ipv6 route
    config_rip_route_wizard_ipv6(Wizards=wizard,
                                 Ipv6StartRoutesPrefix='2022::',
                                 Ipv6EndRoutesPrefix='2033::')

    # 生成Rip Route向导配置
    expand_rip_route_wizard(Wizards=wizard)

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
