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

locations = ['//10.0.11.191/1/7', '//10.0.11.191/1/8'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:
    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    Port_UP, Port_Down = reserve_port(Locations=locations)
    interface_1 = create_interface(Port=Port_UP, Layers='ipv4')
    edit_interface(Interface=interface_1, Layer='IPv4Layer', Address='20.0.0.1', Gateway='20.0.0.2')
    interface_2 = create_interface(Port=Port_Down, Layers='ipv4')
    edit_interface(Interface=interface_2, Layer='IPv4Layer', Address='20.0.0.2', Gateway='20.0.0.1')
    ipv4_ping(Interface=interface_1, IpAddr='20.0.0.2', PacketCount=5)

    # 保存配置文件s
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
