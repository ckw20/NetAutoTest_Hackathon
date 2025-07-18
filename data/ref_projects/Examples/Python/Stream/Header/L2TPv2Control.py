# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1创建一条流量StreamTemplate_1;
#                   测试步骤3: 修改流量StreamTemplate_1的L2TPv2 Control头部内容;
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
    stream = add_stream(Ports=Port_UP, FrameLengthType='AUTO')

    # 修改流量报文头部
    create_stream_header(Stream=stream, HeaderTypes=['EthernetII', 'IPv4', 'UDP', 'l2tpv2Control'])

    # 修改l2tpv2 control头部
    edit_header_l2tpv2_control(Stream=stream, Level=0,
                               Type=1,
                               Reserved1=11,
                               Ns=5,
                               Nr=6,
                               )

    # 修改l2tpv2 control头部，添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=0,
                                      Types='generalTLV',
                                      AttributeValue='11',
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=1,
                                      Types='messageType',
                                      MessageType=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=2,
                                      Types='resultCode',
                                      ErrorCode=1,
                                      ErrorMessage='01',
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=3,
                                      Types='protocolVersion',
                                      Ver=1,
                                      Rev=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=4,
                                      Types='framingCapabilities',
                                      Abit=1,
                                      Sbit=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=5,
                                      Types='bearerCapabilities',
                                      Abit=1,
                                      Dbit=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=6,
                                      Types='tieBreaker',
                                      TieBreakerValue='0000000000000001',
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=7,
                                      Types='firmwareRevision',
                                      FirmwareRevision=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=8,
                                      Types='assignedTunnelId',
                                      TunnelId=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=9,
                                      Types='receiveWindowSize',
                                      WindowSize=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=10,
                                      Types='assignedSessionId',
                                      SessionId=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=11,
                                      Types='response',
                                      ResponseValue='00000000000000000000000000000001',
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=12,
                                      Types='callSerialNumber',
                                      CallSerialNumber=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=13,
                                      Types='minimumBps',
                                      MinimumBps=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=14,
                                      Types='maximumBps',
                                      MaximumBps=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=15,
                                      Types='bearerType',
                                      Abit=1,
                                      Dbit=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=16,
                                      Types='framingType',
                                      Abit=1,
                                      Sbit=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=17,
                                      Types='txConnectSpeed',
                                      Bps=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=18,
                                      Types='rxConnectSpeed',
                                      HighBPS=1,
                                      LowBPS=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=19,
                                      Types='physicalChannelId',
                                      PhysicalChannelId=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=20,
                                      Types='proxyAuthenType',
                                      AuthenType=1,
                                      )

    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option(Stream=stream, Level=0,
                                      Index=21,
                                      Types='proxyAuthenId',
                                      AuthenId=1,
                                      )

    # 配置过滤抓包
    pdu_pattern = create_capture_pdu_pattern(Port=Port_Down,
                                             HeaderTypes=['EthernetII', 'IPv4', 'UDP', 'l2tpv2Control'],
                                             FieldName='l2tpv2Control_1.ns',
                                             Value=5,
                                             MaxValue=5,
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