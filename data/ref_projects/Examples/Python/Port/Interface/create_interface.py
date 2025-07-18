# =================================================================================
# Objective   	:   测试目的 : 检查仪表创建接口正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建各种类型接口;
#
# Criteria    	:   预期结果1: 步骤2中所有接口创建成功;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :  	None
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
    Port_UP, Port_Down = reserve_port(Locations=locations, Debug=True)

    # 创建接口
    # ------------------------------------------------------------------------------
    # 链路层: eth,  网络层: None
    interface = create_interface(Port=Port_UP, Layers='eth')
    # 等价写法, 先使用create_interface创建接口，再使用edit_interface_stack修改接口结构
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers='eth')

    # 链路层: eth,  网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers='eth', Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers='eth', Tops='ipv4')

    # 链路层: eth,  网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers='eth', Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers='eth', Tops='ipv6')

    # 链路层: eth,  网络层: ipv4, ipv6
    interface = create_interface(Port=Port_UP, Layers='eth', Tops=['ipv4', 'ipv6'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers='eth', Tops=['ipv4', 'ipv6'])

    # -------------------------------------单层vlan-----------------------------------------
    # 链路层: eth, vlan  网络层: None
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan'])

    # 链路层: eth, vlan  网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan'], Tops='ipv4')

    # 链路层: eth, vlan  网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan'], Tops='ipv6')

    # 链路层: eth, vlan  网络层: ipv4, ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan'], Tops=['ipv4', 'ipv6'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan'], Tops=['ipv4', 'ipv6'])

    # -------------------------------------双层vlan-----------------------------------------
    # 链路层: eth, vlan, vlan  网络层: None
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'vlan'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'vlan'])

    # 链路层: eth, vlan, vlan  网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'vlan'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'vlan'], Tops='ipv4')

    # 链路层: eth, vlan, vlan  网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'vlan'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'vlan'], Tops='ipv6')

    # 链路层: eth, vlan, vlan  网络层: ipv4, ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'vlan'], Tops=['ipv4', 'ipv6'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'vlan'], Tops=['ipv4', 'ipv6'])

    # -------------------------------------pppoe-----------------------------------------
    # 链路层: eth, pppoe  网络层: None
    interface = create_interface(Port=Port_UP, Layers=['eth', 'pppoe'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'pppoe'])

    # 链路层: eth, pppoe  网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'pppoe'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'pppoe'], Tops='ipv4')

    # 链路层: eth, pppoe  网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'pppoe'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'pppoe'], Tops='ipv6')

    # 链路层: eth, pppoe  网络层: ipv4, ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'pppoe'], Tops=['ipv4', 'ipv6'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'pppoe'], Tops=['ipv4', 'ipv6'])

    # 链路层: eth, vlan, pppoe  网络层: ipv4, ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'pppoe'], Tops=['ipv4', 'ipv6'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'pppoe'], Tops=['ipv4', 'ipv6'])

    # 链路层: eth, vlan, vlan, pppoe  网络层: ipv4, ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'vlan', 'pppoe'], Tops=['ipv4', 'ipv6'])
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'vlan', 'pppoe'], Tops=['ipv4', 'ipv6'])

    # -------------------------------------l2tp-----------------------------------------
    # 链路层: eth, l2tp 网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'l2tp'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'l2tp'], Tops='ipv4')
    # 链路层: eth, l2tp 网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'l2tp'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'l2tp'], Tops='ipv6')

    # 链路层: eth, l2tp, ipv4 网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'l2tp', 'ipv4'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'l2tp', 'ipv4'], Tops='ipv4')
    # 链路层: eth, l2tp, ipv4 网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'l2tp', 'ipv4'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'l2tp', 'ipv4'], Tops='ipv6')

    # 链路层: eth, l2tp, ipv6 网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'l2tp', 'ipv6'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'l2tp', 'ipv6'], Tops='ipv4')
    # 链路层: eth, l2tp, ipv4 网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'l2tp', 'ipv6'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'l2tp', 'ipv6'], Tops='ipv6')

    # 链路层: eth, l2tp, ipv4/ipv6 网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv4')
    # 链路层: eth, l2tp, ipv4/ipv6 网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv6')

    # 链路层: eth, vlan, l2tp, ipv4/ipv6 网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv4')
    # 链路层: eth, vlan, l2tp, ipv4/ipv6 网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv6')

    # 链路层: eth, vlan, vlan, l2tp, ipv4/ipv6 网络层: ipv4
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'vlan', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv4')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'vlan', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv4')
    # 链路层: eth, vlan, vlan, l2tp, ipv4/ipv6 网络层: ipv6
    interface = create_interface(Port=Port_UP, Layers=['eth', 'vlan', 'vlan', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv6')
    # 等价写法
    interface = create_interface(Port=Port_Down)
    edit_interface_stack(Interfaces=interface, Layers=['eth', 'vlan', 'vlan', 'l2tp', 'ipv4', 'ipv6'], Tops='ipv6')

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
