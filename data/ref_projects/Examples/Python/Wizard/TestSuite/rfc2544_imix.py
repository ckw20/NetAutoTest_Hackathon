# =================================================================================
# Objective   	:   测试目的 : 检查BLDP VPLS向导配置生成正常
#
# Step			:	测试步骤1: 创建8个离线端口Port_1、Port_2;
#                   测试步骤2: 创建LDP VPLS向导;
#                   测试步骤3: 配置客户端侧端口和提供商侧端口;
#                   测试步骤4: 配置提供商侧路由器;
#                   测试步骤5: 配置VPLS;
#                   测试步骤6: 配置Host;
#                   测试步骤7: 配置流量;
#                   测试步骤8: 生成LDP VPLS向导配置;
#
# Criteria    	:   预期结果1: 步骤8 LDP VPLS向导配置生成无异常;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :  	# None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/13', '//10.0.11.191/1/14'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''

try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    port_up, port_down = reserve_port(Locations=locations, Debug=True)

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

    # 获取仪表已有imix模板
    imix_template = [get_imix_from_name(Name='Default'), get_imix_from_name(Name='4-Point'),
                     get_imix_from_name(Name='IPSEC'), get_imix_from_name(Name='TCPv4')]

    # 创建新imix模板
    imix = create_imix(Name='Imix_01')
    add_imix_distribution_frame(IMix=imix, Type='random', Min=64, Max=128, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=128, Max=256, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=256, Max=512, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=512, Max=1024, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=1024, Max=1280, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=1280, Max=1518, Weight=10)
    imix_template.append(imix)

    imix = create_imix(Name='Imix_02')
    add_imix_distribution_frame(IMix=imix, Type='random', Min=64, Max=128, Weight=5)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=128, Max=256, Weight=5)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=256, Max=512, Weight=5)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=512, Max=1024, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=1024, Max=1280, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=1280, Max=1518, Weight=10)
    imix_template.append(imix)

    imix = create_imix(Name='Imix_03')
    add_imix_distribution_frame(IMix=imix, Type='random', Min=64, Max=128, Weight=20)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=128, Max=256, Weight=20)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=256, Max=512, Weight=20)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=512, Max=1024, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=1024, Max=1280, Weight=10)
    add_imix_distribution_frame(IMix=imix, Type='random', Min=1280, Max=1518, Weight=10)
    imix_template.append(imix)

    # 创建RFC2544 Throughput测试套件
    wizard, Config = create_benchmark(Type='rfc2544', Items=['throughput'])
    relate_benchmark_ports(Config=wizard, Ports=[port_up, port_down])
    benchmark_stream_use_exist(Config=wizard, Streams=streams)
    edit_benchmark_learning(Configs=Config, Frequency='once', EnableArp=False)
    edit_benchmark_duration(Config=Config, Count=1)
    edit_benchmark_frame(Config=Config, Type='imix', ImixTemplates=imix_template)
    edit_benchmark_search(Config=Config, Init=100, Lower=100, Upper=100)
    expand_benchmark(Config=wizard)
    imix = create_imix(Name='CTRI_IMIX424')
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
