# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发ipv4报文统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 修改流量StreamTemplate_1的ipv4头部内容;;
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

locations = ['//10.0.11.191/1/13', '//10.0.11.191/1/14'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:
    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    port1, port2 = reserve_port(Locations=locations)
    # 创建流量
    stream = add_stream(Ports=port1, FixedLength=256)
    # 修改流量报文头部
    create_stream_header(Stream=stream, HeaderTypes=['EthernetII', 'IPv4'])
    # 修改ipv4头部
    HeaderOption = ['Security', 'RouterAlert']
    attribute_dict = edit_header_ipv4(Stream=stream, Level=0, TTL=200, Source='10.1.1.2', Destination='20.1.1.2',
                                      Flags=111, HeaderOption=HeaderOption)
    # ipv4头部Source字段添加Increment跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=attribute_dict['Source'],
                  Type='Increment', Count=10, Step=2)
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')
    # 修改ipv4头部，添加一个Security
    attribute_dict_security = edit_header_ipv4_option(Stream=stream, Index=0, Option='Security', Security=1)
    # ipv4头部Security的Security字段添加List跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=attribute_dict_security['Security'],
                  Type='List', List=[1, 11, 111])
    # ipv4头部RouterAlert的Length字段添加Random跳变
    attribute_dict_RouterAlert = edit_header_ipv4_option(Stream=stream, Index=1, Option='RouterAlert', Length=10)
    edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=attribute_dict_RouterAlert['Length'],
                  Type='Random', Range=15)
    # 修改ipv4头部，添加一个LooseSourceRoute节点
    attribute_dict_loose = edit_header_ipv4_option(Stream=stream, Index=2, Option='LooseSourceRoute',
                                                   AddressList=['1.1.1.1', '2.2.2.2'])
    # 修改其中一个地址的跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=attribute_dict_loose['AddressList: 2.2.2.2'],
                  Type='Increment', Count=10)
    # 修改ipv4头部，添加一个TimeStamp节点
    timestamp = edit_header_ipv4_option(Stream=stream, Index=3, Option='TimeStamp',
                                        TimeStampSet=['10203040', '50607080'])
    # 修改其中一个地址的跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=timestamp['TimeStampSet: 50607080'],
                  Type='Increment', Count=10)
    # 使用Level和Attribute参数添加pdu_pattern
    pdu_pattern_1 = create_capture_pdu_pattern(Port=port2, HeaderTypes=['EthernetII', 'IPv4'],
                                               Level=1,
                                               Attribute=attribute_dict_security['Security'],
                                               Value=1, MaxValue=1)
    # 使用FieldName参数添加pdu_pattern
    pdu_pattern_2 = create_capture_pdu_pattern(Port=port2, HeaderTypes=['EthernetII', 'IPv4'],
                                               FieldName='ipv4_1.ipv4HeaderOption.ipv4HeaderOptionList_1.optionRouterAlert.length',
                                               Value=10, MaxValue=10)

    edit_capture_filter(Port=port2, Expression=f'{pdu_pattern_1} && {pdu_pattern_2}')
    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['StreamBlockStats'])
    # 设置端口发送模式为突发包
    edit_port_load_profile(Ports=port1, TransmitMode='BURST', BurstCount=100)
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
    PackagesPath = download_packages(Port=port2, FileDir=f'{dirname}/pcap/', FileName=filename, MaxCount=100)
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    Result = get_streamblock_statistic(Stream=stream)
    TxStreamFrames = Result['TxStreamFrames']
    RxStreamFrames = Result['RxStreamFrames']
    assert TxStreamFrames == RxStreamFrames
    # 释放端口资源
    release_port(locations)


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
