# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1创建一条流量StreamTemplate_1;
#                   测试步骤3: 修改流量StreamTemplate_1的Imix模板;
#                   测试步骤4: 订阅StreamBlockStats统计;
#                   测试步骤5: 发送所有流量，等待一段时间;
#                   测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
#
# Criteria    	:   预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :  	CSR-10199
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

    # 创建流量
    stream = add_stream(Ports=Port_UP)

    # 修改流量报文头部
    imix = create_imix(Name='Imix_01')
    add_imix_distribution_frame(IMix=imix, Type='random', Min=78, Max=178, Weight=50)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=206, Max=306, Weight=50)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=462, Max=562, Weight=50)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=974, Max=1074, Weight=50)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=1230, Max=1330, Weight=50)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=1468, Max=1568, Weight=50)
    bind_stream_imix(Stream=stream, IMix=imix)

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
