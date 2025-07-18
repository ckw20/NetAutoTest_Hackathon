# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发ipv6报文统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 修改流量StreamTemplate_1的ipv6头部内容;;
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
    Ports = reserve_port(Locations=locations)
    # 创建流量
    stream = add_stream(Ports=Ports[0], FixedLength=256)
    # 修改流量报文头部
    HeaderTypes = ['EthernetII', 'IPv6', 'ipv6fragmentheader']
    create_stream_header(Stream=stream, HeaderTypes=HeaderTypes)
    # 修改ipv6头部
    attribute_dict = edit_header_ipv6(Stream=stream, Level=0, HopLimit=20,
                                      Source='2022::2', Destination='2020::2', Gateway='2022::1')
    # ipv6头部HopLimit字段添加Increment跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='IPv6', Attribute=attribute_dict['HopLimit'],
                  Type='Increment', Count=10, Step=2)
    # ipv6头部Source字段添加List跳变
#    edit_modifier(Stream=stream, Level=0, HeaderType='IPv6', Attribute=attribute_dict['Source'],
#                  Type='List', List=['2022::2', '2022::5', '2022::3'])
    # ipv6头部Destination的Length字段添加List跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='IPv6', Attribute=attribute_dict['Destination'],
                  Type='Random', Range='2020::10')
    # ipv6 fragment
    attr = edit_header_ipv6_fragment(Stream=stream, NextHeader=10)
    edit_modifier(Stream=stream, Level=0, HeaderType='ipv6fragmentheader', Attribute=attr['NextHeader'],
                  Type='Increment', Count=10, Step=2)

    # 配置过滤抓包
    # 使用Level和Attribute参数添加pdu_pattern
    # pdu_pattern_1 = create_capture_pdu_pattern(Port=Ports[1], HeaderTypes=HeaderTypes,
    #                                            Level=1,
    #                                            Attribute=attribute_dict['HopLimit'],
    #                                            Value=20, MaxValue=22)
    # pdu_pattern_2 = create_capture_pdu_pattern(Port=Ports[1], HeaderTypes=HeaderTypes,
    #                                            Level=1,
    #                                            Attribute=attribute_dict['Source'],
    #                                            Value='2022::2', MaxValue='2022::2')
    # 使用FieldName参数添加pdu_pattern
    # pdu_pattern_3 = create_capture_pdu_pattern(Port=Ports[1], HeaderTypes=HeaderTypes,
    #                                            FieldName='ipv6_1.destination',
    #                                            Value='2020::2', MaxValue='2020::2')
    # edit_capture_filter(Port=Ports[1], Expression=f'{pdu_pattern_1} && {pdu_pattern_2} && {pdu_pattern_3}')
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
