# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1创建一条流量StreamTemplate_1;
#                   测试步骤3: 修改流量StreamTemplate_1的isis头部内容;
#                   测试步骤4: 订阅StreamBlockStats统计;
#                   测试步骤5: 发送所有流量，等待一段时间;
#                   测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
#
# Criteria    	:   预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
#
# Created by   	:  	Tester-002
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
    Port_UP, Port_Down = reserve_port(Locations=locations)

    # 创建流量
    stream = add_stream(Ports=Port_UP)

    # 修改流量报文头部
    create_stream_header(Stream=stream, HeaderTypes=['EthernetII', 'p2phelloheader'])

    header = edit_header_isis_p2p_hello(Stream=stream,
                                        PDUType=10,
                                        IsIsTlv=['AreaAddress', 'Padding', 'AuthentionInfo', 'ProtocolSupport',
                                                 'IpInterfaceAddress', 'P2pAdjacencyState', 'RestartSignal',
                                                 'Ipv6InterfaceAddress'])
    edit_modifier(Stream=stream, Level=0, HeaderType='p2phelloheader', Attribute=header['PDUType'],
                  Type='Increment', Count=10)

    edit_header_isis_tlv_header(Stream=stream, Option='AreaAddress', AreaAddressEntries=1)
    edit_header_isis_area_address_entry(Stream=stream, TlvIndex=0, EntryIndex=1, AreaAddress='ff')

    edit_header_isis_tlv_header(Stream=stream, Option='Padding', Index=1, TlvLength=10)

    edit_header_isis_tlv_header(Stream=stream, Option='AuthentionInfo', Index=2, AuthenticationLength=20)

    edit_header_isis_tlv_header(Stream=stream, Option='ProtocolSupport', Index=3, NlPIDEntriesField=2)
    edit_header_isis_nlpid_entry(Stream=stream, TlvIndex=3, NlpidIndex=0, TlvLength=30)

    edit_header_isis_tlv_header(Stream=stream, Option='p2pAdjacencyState', Index=5,
                                **{'adjacencyStateInitializing.extendLocalCircuitId':'10203040'})

    # 配置过滤抓包
    # pdu_pattern = create_capture_pdu_pattern(Port=Port_Down,
    #                                          HeaderTypes=['EthernetII', 'l1csnpheader'],
    #                                          FieldName='IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime',
    #                                          Value=10,
    #                                          MaxValue=10,
    #                                          )
    # edit_capture_filter(Port=Port_Down, Expression=pdu_pattern)

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
