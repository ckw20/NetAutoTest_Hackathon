# =================================================================================
# Objective   	:   测试目的 : 确定局域网交换机设备的吞吐量
#
# Step			:	测试步骤1: 创建端口，并预约端口
#                   测试步骤2: 创建RFC2544向导, 选择测试项吞吐量;
#                   测试步骤3: 选择端口;
#                   测试步骤4: 配置端点;
#                   测试步骤5: 配置流;
#                   测试步骤6: 配置测试选项;
#                   测试步骤7: 吞吐量参数设置;
#                   测试步骤8: 生成智能脚本;
#                   测试步骤8: 执行智能脚本测试;
#
# Criteria    	:   预期结果1: 步骤9 正确测出设备吞吐量;
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

    # 创建接口
    interfaces_1 = create_interface(Port=port_up, Layers=['ipv4'])
    interfaces_2 = create_interface(Port=port_down, Layers=['ipv4'])
    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='192.168.1.2',
                   Gateway='192.168.1.3')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='192.168.1.3',
                   Gateway='192.168.1.2')

    # 创建绑定流
    point_1 = get_layer_from_interfaces(Interfaces=interfaces_1, Layer='ipv4')
    point_2 = get_layer_from_interfaces(Interfaces=interfaces_2, Layer='ipv4')
    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    wizard, Config = create_benchmark(Type='rfc2544', Items=['throughput'])
    relate_benchmark_ports(Config=wizard, Ports=[port_up, port_down])
    benchmark_stream_use_exist(Config=wizard, Streams=streams)
    edit_benchmark_learning(Configs=Config, Frequency='once', EnableArp=False)
    edit_benchmark_duration(Config=Config, Count=1)
    edit_benchmark_frame(Config=Config, Type='custom')
    edit_benchmark_search(Config=Config, Init=100, Lower=100, Upper=100)
    expand_benchmark(Config=wizard)

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
