# =================================================================================
# Objective   	:   测试目的 : 局域网交换机设备背靠背测试
#
# Step			:	测试步骤1: 创建端口，并预约端口
#                   测试步骤2: 创建TSN Avb向导,选择端口;
#                   测试步骤3: 配置Qav;
#                   测试步骤4: 配置gPTP;
#                   测试步骤5: 配置Non-AVB stream;
#                   测试步骤6: 生成向导配置;
#
# Criteria    	:   预期结果1: 步骤6 向导配置生成成功;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :  	# None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/5', '//10.0.11.191/1/6', '//10.0.11.191/1/7'] if len(sys.argv) < 2 else sys.argv[1].split(
    ' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''

try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    port_1, port_2, port_3 = reserve_port(Locations=locations, Force=True)

    # =============== *选择测试项* ===============
    wizard = create_tsn_wizard(Type='avb', TalkerPort=port_1, ListenerPort=port_2, NonAvbPort=port_3, IsAppended=False)

    # =============== *配置Qav* ===============
    config_tsn_avb_qav(wizard, FrameSize=120, SrClassVid=10, EnableClassA=True, ClassABwRsvPct=50,
                       ClassAStreamNum=2, ClassAStreamsBwRsvPct=[25, 25], EnableClassB=True, ClassBBwRsvPct=25,
                       ClassBStreamNum=1, ClassBStreamsBwRsvPct=[25])

    # =============== *配置gPTP* ===============
    config_tsn_avb_gptp(wizard, Priority1=100, Priority2=101, ClockAccuracy=EnumClockAccuracy.CLOCK_ACCURACY_22,
                        LogAnnounceInterval=1, LogSyncInterval=1, AnnounceReceiptTimeout=4, PropogationDelay=1000)

    # =============== *配置Non-AVB stream* ===============
    config_tsn_avb_non_stream(wizard, NonAvbFrameSize=150, LoadRate=10, StreamNumber=1)

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
