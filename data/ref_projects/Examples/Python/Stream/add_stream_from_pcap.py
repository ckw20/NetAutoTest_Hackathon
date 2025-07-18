# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流StreamBlockStats统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1, Port_2分别创建两条流量StreamTemplate_1、2、3、4;
#                   测试步骤3: 订阅StreamBlockStats统计;
#                   测试步骤4: 发送所有流量，查看StreamBlockStats统计信息，等待一段时间;
#                   测试步骤5: 停止所有流量，查看StreamBlockStats统计信息;
#
# Criteria    	:   预期结果1: 步骤4,5中StreamBlockStats统计信息获取正确;
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
    Port_UP, Port_Down = reserve_port(Locations=locations, Force=True)

    # 创建流量
    stream = add_stream(Ports=Port_UP)

    # 设置端口发送模式为突发包
    BurstCount = 3
    edit_port_load_profile(Ports=Port_UP, TransmitMode='BURST', BurstCount=BurstCount)

    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['StreamBlockStats'])

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动抓包
    start_capture()
    # 发送流量
    start_stream()
    # 发送流获取统计建议等待10sec获取到稳定统计数据
    time.sleep(10)

    stop_stream()
    # 停止抓包
    stop_capture()
    # 停流获取统计必须等待3sec才能获取到稳定统计数据
    time.sleep(3)

    result = get_streamblock_statistic()
    print(result)

    # 下载报文
    result = download_packages(Port=Port_Down, FileDir=f'{dirname}/xcfg', FileName=f'{filename}.pcap')

    # 导入PCAP流量
    stream_pcap = add_stream(Ports=Port_Down, Type='pcap', FilePath=result)

    # 修改EthernetII头部
    attribute_dict = edit_header_ethernet(Stream=stream_pcap[0], Level=0, DestMacAdd='00:00:00:00:00:01',
                                          SourceMacAdd='00:00:00:00:00:02')
    print(attribute_dict)

    # EthernetII头部目的Mac地址字段添加跳变
    edit_modifier(Stream=stream_pcap[0], Level=0, HeaderType='ethernetii', Attribute=attribute_dict['DestMacAdd'],
                  Type='Increment',
                  Count=10, Step=2)

    # 保存配置文件
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 发送流量
    start_stream()
    # 发送流获取统计建议等待10sec获取到稳定统计数据
    time.sleep(10)

    stop_stream()
    # 停流获取统计必须等待3sec才能获取到稳定统计数据
    time.sleep(3)

    result = get_streamblock_statistic()
    # 使用tabulate库表格化输出DataFrame二维数据
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')
    # 将DataFrame数据转成list[dict]形式
    data = result.to_dict('records')
    print(data)





except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
