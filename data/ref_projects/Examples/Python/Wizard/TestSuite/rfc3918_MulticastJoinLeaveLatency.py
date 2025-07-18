# =================================================================================
# Objective   	:   测试目的 : 确定再DUT/SUT收到IGMP陈工加入离开组消息开始，DUT/SUT开始/停止转发多播帧需要的时间
#
# Step			:	测试步骤1: 创建端口，并预约端口
#                   测试步骤2: 创建RFC3918向导, 选择测试项加入离开组时延测试;
#                   测试步骤3: 选择端口;
#                   测试步骤4: 配置端点;
#                   测试步骤5: 配置流;
#                   测试步骤6: 配置组播参数;
#                   测试步骤7: 配置测试选项;
#                   测试步骤8: 配置加入离开组时延;
#                   测试步骤9: 生成智能脚本;
#
# Criteria    	:   预期结果1: 步骤9 正确生成加入离开组时延测试项;
#
# Created by   	:  	Tester-001
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
    wizard, Config = create_benchmark(Type='RFC3918', Items=['multicastJoinLeaveLatency'])

    # =============== *选择端口* ===============
    relate_benchmark_ports(Config=wizard, Ports=[port_up, port_down])

    # =============== *配置端点* ===============
    interfaces_1 = create_interface(Port=port_up, Layers=['ipv4'])
    interfaces_2 = create_interface(Port=port_down, Layers=['ipv4'])
    edit_interface(Interface=interfaces_1, Layer='IPv4Layer', Address='1.1.1.1', Gateway='1.1.1.2')
    edit_interface(Interface=interfaces_2, Layer='IPv4Layer', Address='1.1.1.2', Gateway='1.1.1.1')

    # =============== *配置流* ===============
    point_1 = get_layer_from_interfaces(Interfaces=interfaces_1, Layer='ipv4')
    point_2 = get_layer_from_interfaces(Interfaces=interfaces_2, Layer='ipv4')
    streams = create_benchmark_streams(Config=wizard, Items=Config, Type='ipv4', SrcPoints=point_1, DstPoints=point_2,
                                       Bidirectional=False, Mode='m2m')

    # =============== *配置组播参数* ===============
    # 组播客户端版本号、组播组地址和步长、组播加入/离开延迟、组播组分配模式
    edit_benchmark_multicast_base_parameters(Configs=Config, Version='igmpv2', Ipv4GroupAddressStart='225.0.0.1',
                                             Ipv4GroupAddressStep='0.1.0.0', Ipv4PrefixLength=32, GroupIncrement=1,
                                             JoinGroupDelay=15, LeaveGroupDelay=15, JoinLeaveSendRate=1000,
                                             GroupDistributeMode='even')
    # 传输层配置
    edit_benchmark_transport_layer(Configs=Config, HeaderType='udp', EnableRandomPort=True, SrcPortBase=7,
                                   SrcPortStep=1,
                                   SrcPortCount=0, DstPortBase=7, DstPortStep=1, DstPortCount=0)
    # 流配置
    edit_benchmark_multicast_stream_tos(Configs=Config, Tos=2, TTL=11, Priority=1)

    # =============== *配置测试选项* ===============
    # 地址学习
    edit_benchmark_learning(Configs=Config, Frequency='frame', EnableLearning=True, LearningRate=1000, LearningRepeat=5,
                            DelayBefore=2, EnableArp=True, ArpRate=1000, ArpRepeat=3)
    # 测试时长
    edit_benchmark_duration(Config=Config, Trial=1, Mode='burst', Count=1)
    # 帧长度设置
    edit_benchmark_frame(Config, Type='random', Min=128, Max=512, Start=128, End=256, Step=128)
    # 时延类型
    edit_benchmark_latency(Configs=Config, Type='FIFO')
    # 其他设置
    edit_benchmark_multicast_other(Configs=Config, StopTestWhenFailed=True, VerifyFreq='topo_changed', DurationMode='second',
                                   TimeDurationCount=2, TxFrameRate=1000)
    # 结果
    edit_benchmark_path(Configs=Config, Path='D:/test')
    edit_benchmark_latency(Configs=Config, DelayAfter=20)

    # =============== *配置加入离开组时延* ===============
    # 组播组
    edit_benchmark_multicast_group_count_loop(Config=Config, LoopMode='random', FixedGroup=10, MinGroup=10, MaxGroup=50,
                                              StartGroup=10, EndGroup=50, StepGroup=10, CustomGroup=(10, 20, 100))
    # 负载设置
    edit_benchmark_traffic_load_loop(Config=Config, LoadUnit='percent', LoadMode='random', LoadMin=10, LoadMax=50)
    # 延迟设置
    edit_benchmark_multicast_join_leave_delay(Config=Config, DelayBetweenJoinAndStartStream=20, DelayBetweenJoinAndLeave=15)
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name(Config=Config, EnableCustomResult=True, ResultFileName='Rfc3918MixedThroughput',
                                    AddTimeStamp=True)

    # =============== *生成智能脚本* ===============
    expand_benchmark(Config=wizard)

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # =============== *执行智能脚本测试* ===============
    db = run_benchmark(Mode=0, Timer=3600, Analyzer=True)
    result = get_benchmark_result(DB=db, Type='RFC3918', Item='multicastThroughput')
    tmp = format_benchmark_result(Result=result)
    print(tmp)


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
