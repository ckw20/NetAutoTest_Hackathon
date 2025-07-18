# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1创建一条流量StreamTemplate_1;
#                   测试步骤3: 修改流量StreamTemplate_1的DHCPv6 Client头部内容;
#                   测试步骤4: 订阅StreamBlockStats统计;
#                   测试步骤5: 发送所有流量，等待一段时间;
#                   测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
#
# Criteria    	:   预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
#
# Created by   	:  	Tester-003
#
# Bugs   	    :  	None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/7', '//10.0.11.191/1/8'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:
    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    Port_UP, Port_Down = reserve_port(Locations=locations)

    # 创建流量
    stream = add_stream(Ports=Port_UP, FixedLength=512)

    # 修改流量报文头部
    create_stream_header(Stream=stream, HeaderTypes=['EthernetII', 'IPv6', 'UDP', 'dhcpv6Client'])

    # 修改dhcpv6 client头部
    header = edit_header_dhcpv6_client(Stream=stream, Level=0,
                              MessageType=2,
                              TransId=2,
                              )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header['MessageType'],
                  Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=0,
                                     Types='clientIdOption',
                                     Duid='01',
                                     )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['Duid'],
                  Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=1,
                                     Types='serverIdOption',
                                     DuidType=2,
                                     HardwareType=2,
                                     LinkAddress='00:00:00:00:00:02',
                                     )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['LinkAddress'],
                  Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=2,
                                     Types='ianaOption',
                                     Iaid='00000003',
                                     T1=3,
                                     T2=3,
                                     IaOption=1
                                     )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['T1'],
                  Type='Increment', Count=10)
    ia_option = edit_header_dhcpv6_option_ia_address(Stream=stream, Index=2,
                                                Type=5, Length=5, Ipv6Address='2020::1',
                                                PreferredLifetime=1, ValidLifetime=1)
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=ia_option['Ipv6Address'],
                  Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=3,
                                     Types='requestOption',
                                     Value='04',
                                     )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['Value'],
                  Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=4,
                                     Types='elapsedTimeOption',
                                     ElapseTime=5,
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['ElapseTime'],
    #               Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=5,
                                     Types='serverUnicastOption',
                                     ServerAddress='2022::1',
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['ServerAddress'],
    #               Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=6,
                                     Types='statusCodeOption',
                                     StatusCode=7,
                                     StatusMsg='0000000007',
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['StatusMsg'],
    #               Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=7,
                                     Types='rapidCommitOption',
                                     Length=8,
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['Length'],
    #               Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=8,
                                     Types='interfaceIdOption',
                                     InterfaceId='0000000009',
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['InterfaceId'],
    #               Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=9,
                                     Types='reconfigureAcceptOption',
                                     Type=10,
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['Type'],
    #               Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=10,
                                     Types='iapdOption',
                                     Iaid='00000011',
                                     T1=11,
                                     T2=11,
                                     IaOption=1
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['Iaid'],
    #               Type='Increment', Count=10)
    ia_option = edit_header_dhcpv6_option_ia_prefix(Stream=stream, Index=10,
                                                            Type=5, Length=5, Ipv6Address='2020::1',
                                                            PreferredLifetime=1, ValidLifetime=1, PrefixLength=128)
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=ia_option['Ipv6Address'],
    #               Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=11,
                                     Types='customOption',
                                     Value='12',
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['Value'],
    #               Type='Increment', Count=10)

    # 修改dhcpv6 client头部，添加一个Option头部
    header_option = edit_header_dhcpv6_option(Stream=stream, Level=0,
                                     Index=12,
                                     Types='generalTLV',
                                     Value='13',
                                     )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv6Client', Attribute=header_option['Value'],
    #               Type='Increment', Count=10)

    # 配置过滤抓包
    pdu_pattern = create_capture_pdu_pattern(Port=Port_Down,
                                             HeaderTypes=['EthernetII', 'IPv6', 'UDP', 'dhcpv6Client'],
                                             FieldName='dhcpv6Client_1.messageType',
                                             Value=2,
                                             MaxValue=2,
                                             )
    edit_capture_filter(Port=Port_Down, Expression=pdu_pattern)

    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])

    # 设置端口发送模式为突发包
    BurstCount = 100
    edit_port_load_profile(Ports=Port_UP, TransmitMode='BURST', BurstCount=BurstCount)

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动抓包，发送流量
    start_capture()
    start_stream()

    # 等待流量停止
    wait_stream_state()
    stop_capture()

    # 流量停止后，必须等待大于等于3sec才能正确获得统计结果
    time.sleep(3)

    # 下载捕获到的报文
    pkt = download_packages(Port=Port_Down, FileDir=f'{dirname}/pcap/', FileName=filename, MaxCount=100)
    print(pkt)

    # 获取端口捕获报文信息
    capture_info = get_capture_info(Port=Port_Down)
    print(capture_info)
    if capture_info['CapturedPacketCount'] != capture_info['DownloadedPacketCount'] != BurstCount:
        verdict = 'fail'
        errInfo += f'Download packages is not equal to BurstCount({BurstCount})\n'

    # 获取流量StreamBlockStats
    result = get_streamblock_statistic(Stream=stream)
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    print('TxStreamFrames: {}'.format(TxStreamFrames))
    print('RxStreamFrames: {}'.format(RxStreamFrames))

    if TxStreamFrames != RxStreamFrames != BurstCount:
        verdict = 'fail'
        errInfo += f'{stream} TxStreamFrames({TxStreamFrames}) is not equal to RxStreamFrames({RxStreamFrames})\n'

    # 获取报文过滤统计结果
    StaItems = ['RxFilter0Count', 'RxFilter1Count', 'RxFilter2Count', 'RxFilter3Count', 'RxFilter4Count',
                'RxFilter5Count', 'RxFilter6Count', 'RxFilter7Count']
    result = get_port_statistic(Port=Port_Down, StaItems=StaItems)
    print(result)


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
