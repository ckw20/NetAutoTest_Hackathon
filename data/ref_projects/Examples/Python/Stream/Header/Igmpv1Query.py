# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发IGMPv1_Query报文统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 修改流量StreamTemplate_1的IGMPv1_Query头部内容;;
#                   测试步骤3: 配置过滤抓包;
#                   测试步骤4: 订阅StreamBlockStats统计;;
#                   测试步骤5: 设置端口发送模式为突发包;
#                   测试步骤6: 发送所有流量，等待一段时间;
#                   测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;;
#
# Criteria    	:   预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
#
# Created by   	:  	Tester-004
#
# Bugs   	    :  	None
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
    Ports = reserve_port(Locations=locations)
    # 创建流量
    stream = add_stream(Ports=Ports[0], FixedLength=256)
    # 修改流量报文头部
    HeaderTypes = ['EthernetII', 'IPv4', 'IGMPv1Query']
    create_stream_header(Stream=stream, HeaderTypes=HeaderTypes)
    # 修改igmpv3 report头部
    header = edit_header_igmpv1_query(Stream=stream, Level=0, Type=99, Unused=255, Checksum='ffff',
                             GroupAddress='10.1.1.1')
    edit_modifier(Stream=stream, Level=0, HeaderType='IGMPv1Query', Attribute=header['GroupAddress'],
                  Type='Increment', Count=10)

    # 配置过滤抓包
    pdu_pattern_1 = create_capture_pdu_pattern(Port=Ports[1], HeaderTypes=HeaderTypes,
                                               FieldName='igmpv1Query_1.type',
                                               Value='99', MaxValue='99')
    pdu_pattern_2 = create_capture_pdu_pattern(Port=Ports[1], HeaderTypes=HeaderTypes,
                                               FieldName='igmpv1Query_1.unused',
                                               Value='255',
                                               MaxValue='255')
    edit_capture_filter(Port=Ports[1], Expression=f'{pdu_pattern_1} && {pdu_pattern_2}')
    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['StreamBlockStats'])
    # 设置端口发送模式为突发包
    edit_port_load_profile(Ports=Ports[0], TransmitMode='BURST', BurstCount='100')
    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')
    # 启动抓包，发送流量
    start_capture()
    start_stream()
    time.sleep(10)
    stop_stream()
    stop_capture()
    time.sleep(3)
    # 下载捕获到的报文
    packages_path = download_packages(Port=Ports[1], FileDir=f'{dirname}/pcap', FileName=filename, MaxCount=100)
    print(f'packages_path: {packages_path}')
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    result = get_streamblock_statistic(Stream=stream)
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    print('TxStreamFrames: {}'.format(TxStreamFrames))
    print('RxStreamFrames: {}'.format(RxStreamFrames))
    assert TxStreamFrames == RxStreamFrames
    # 释放端口资源
    result = release_port(Locations=locations)
except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
