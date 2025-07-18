# =================================================================================
# Objective   	:   测试目的 : 局域网交换机设备背靠背测试
#
# Step			:	测试步骤1: 创建端口，并预约端口
#                   测试步骤2: 创建TSN Qcr向导;
#                   测试步骤3: 配置Qcr stream;
#                   测试步骤4: 配置Stream identification function;
#                   测试步骤5: 生成向导配置;
#
# Criteria    	:   预期结果1: 步骤5 向导配置生成成功;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :  	# None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/5', '//10.0.11.191/1/6'] if len(sys.argv) < 2 else sys.argv[1].split(
    ' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''

try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    port_1, port_2 = reserve_port(Locations=locations, Force=True)

    # =============== *选择测试项* ===============
    wizard = create_tsn_wizard(Type='qcr')

    # =============== *创建Qcr stream* ===============
    qcr_stream_config = create_tsn_qcr_stream(wizard, TalkerPort=port_1, ListenerPortList=port_2, Priority=3)

    # =============== *配置Stream identification function* ===============
    config_tsn_qcr_stream_identification_function(qcr_stream_config, StreamIdentificationFunction='IP_OCTUPLE_STREAM',
                                                  SourceMacAddress='00:01:02:03:00:02',
                                                  DestinationMacAddress='00:02:02:03:00:02', VlanId=100)

    # =============== *生成向导配置* ===============
    expand_tsn_wizard(Wizard=wizard)

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
