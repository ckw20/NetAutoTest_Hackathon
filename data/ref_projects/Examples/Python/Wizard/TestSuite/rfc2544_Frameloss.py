# =================================================================================
# Objective   	:   测试目的 : 局域网交换机设备丢包率测试
#
# Step			:	测试步骤1: 创建端口，并预约端口
#                   测试步骤2: 创建RFC2544向导, 选择丢包率测试;
#                   测试步骤3: 选择端口;
#                   测试步骤4: 配置端点;
#                   测试步骤5: 配置流;
#                   测试步骤6: 配置测试选项;
#                   测试步骤7: 地址缓存容量参数设置;
#                   测试步骤8: 生成智能脚本;
#                   测试步骤8: 执行智能脚本测试;
#
# Criteria    	:   预期结果1: 步骤9 正确测出设备地址缓存容量;
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
    port_up, port_down = reserve_port(Locations=locations, Force=True)

    # =============== *选择测试项* ===============
    wizard, Config = create_benchmark(Type='RFC2544', Items=['frameloss'])

    # =============== *选择端口* ===============
    relate_benchmark_ports(Config=wizard, Ports=[port_up, port_down])

    # =============== *配置端点* ===============
    interfaces_1 = create_interface(Port=port_up, Layers=['eth', 'ipv4'])
    interfaces_2 = create_interface(Port=port_down, Layers=['eth', 'ipv4'])

    # =============== *配置流* ===============
    point_1 = get_layer_from_interfaces(Interfaces=interfaces_1, Layer='ipv4')
    point_2 = get_layer_from_interfaces(Interfaces=interfaces_2, Layer='ipv4')
    streams = create_benchmark_streams(Config=wizard, Items=Config, Type='ipv4', SrcPoints=point_1, DstPoints=point_2,
                                       Bidirectional=False)

    # =============== *配置rfc2544* ===============
    edit_benchmark_learning(Configs=Config, Frequency='once', EnableArp=False)
    edit_benchmark_latency(Configs=Config, Type='FILO', DelayBefore=1, DelayAfter=2)
    edit_benchmark_transport_layer(Configs=Config, HeaderType='tcp')
    edit_benchmark_path(Configs=Config, Path='D:/test')

    # =============== *配置丢包率* ===============
    # 试验次数
    edit_benchmark_duration(Config=Config, Trial=1)
    # 帧长设置
    edit_benchmark_frame(Config=Config, Type='custom', Custom=[128])
    # 负载
    edit_benchmark_traffic_load_loop(Config=Config, LoadMode='step', LoadStart=10, LoadEnd=20, LoadStep=10)
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name(Config=Config, EnableCustomResult=True, ResultFileName='frameloss',
                                    AddTimeStamp=True)

    # =============== *生成智能脚本* ===============
    expand_benchmark(Config=wizard)

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # =============== *执行智能脚本测试* ===============
    db = run_benchmark(Mode=0, Timer=1200, Analyzer=True)
    result = get_benchmark_result(DB=db, Type='RFC2544')
    tmp = format_benchmark_result(Result=result)
    print(tmp)

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
