# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1创建一条流量StreamTemplate_1;
#                   测试步骤3: 修改流量StreamTemplate_1的DHCPv4 Client头部内容;
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
    create_stream_header(Stream=stream, HeaderTypes=['EthernetII', 'IPv4', 'UDP', 'dhcpv4Client'])

    # 修改dhcpv4 client头部
    header = edit_header_dhcpv4_client(Stream=stream, Level=0,
                                       MessageType=1,
                                       HardwareType=1,
                                       Hops=1,
                                       Bootpflags='0001',
                                       )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header['MessageType'],
                  Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=0,
                                              Types='serverId',
                                              ReqAddr='1.1.1.1',
                                              )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['ReqAddr'],
                  Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=1,
                                              Types='message',
                                              Value='01',
                                              )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Value'],
                  Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=2,
                                              Types='leaseTime',
                                              LeaseTime=1,
                                              )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['LeaseTime'],
                  Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=3,
                                              Types='endOfOptions',
                                              Type='01',
                                              )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Type'],
                  Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=4,
                                              Types='messageSize',
                                              Value='01',
                                              )
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Value'],
                  Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=5,
                                              Types='clientIdHW',
                                              IdType='01',
                                              ClientHWA='00:00:00:00:00:01',
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['ClientHWA'],
    #               Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=6,
                                              Types='clientIdNoneHW',
                                              IdType='01',
                                              Value='01',
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Value'],
    #               Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=7,
                                              Types='hostName',
                                              Value='01',
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Value'],
    #               Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=8,
                                              Types='paramReqList',
                                              Value='01',
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Value'],
    #               Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=9,
                                              Types='reqAddr',
                                              ReqAddr='1.1.1.1',
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['ReqAddr'],
    #               Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=10,
                                              Types='optionOverload',
                                              Overload=1,
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Overload'],
    #               Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=11,
                                              Types='customOption',
                                              Overload='01',
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Overload'],
    #               Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=12,
                                              Types='generalTLV',
                                              Value='01',
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Value'],
    #               Type='Increment', Count=10)

    # 修改dhcpv4 client头部，添加一个Option头部
    header_option = edit_header_dhcpv4_option(Stream=stream, Level=0,
                                              Index=13,
                                              Types='messageType',
                                              Code=4,
                                              )
    # 设置跳变
    # edit_modifier(Stream=stream, Level=0, HeaderType='dhcpv4Client', Attribute=header_option['Code'],
    #               Type='Increment', Count=10)

    # 配置过滤抓包
    pdu_pattern = create_capture_pdu_pattern(Port=Port_Down,
                                             HeaderTypes=['EthernetII', 'IPv4', 'UDP', 'dhcpv4Client'],
                                             FieldName='dhcpv4Client_1.hops',
                                             Value=1,
                                             MaxValue=1,
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
