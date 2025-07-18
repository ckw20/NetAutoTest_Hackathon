# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发l2tpv3 control over ip报文统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 修改流量StreamTemplate_1的l2tpv3 control over ip头部内容;;
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
    stream = add_stream(Ports=Ports[0], FrameLengthType='AUTO')
    # 修改流量报文头部
    HeaderTypes = ['EthernetII', 'IPv4', 'l2tpv3ControlOverIp']
    create_stream_header(Stream=stream, HeaderTypes=HeaderTypes)
    # 修改l2tpv3 control over ip头部
    header = edit_header_l2tpv3_control_over_ip(Stream=stream, Level=0, SessionId='1', Type='1',
                                                UseLength='1', ExcludeSessionLength='1', SequenceNumberNs=1, SequenceNumberNr=2)
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header['ExcludeSessionLength'],
                  Type='Increment', Count=10)
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header['SequenceNumberNs'],
                  Type='Increment', Count=10)

    # 增加l2tpv3 control over ip选项并修改
    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=0, Types='generalTLV', AttributeValue='11')
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['AttributeValue'],
                  Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=1, Types='messageType', MessageType='1')
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['MessageType'],
                  Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=2, Types='resultCode', ErrorCode='1', ErrorMessage='01')
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['ErrorCode'],
                  Type='Increment', Count=10)
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['ErrorMessage'],
                  Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=3, Types='tieBreaker', TieBreakerValue='0000000000000001')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['TieBreakerValue'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=4, Types='receiveWindowSize', WindowSize='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['WindowSize'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=5, Types='callSerialNumber', CallSerialNumber='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['CallSerialNumber'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=6, Types='physicalChannelId', PhysicalChannelId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['PhysicalChannelId'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=7, Types='circuitError', AlignmentOverruns='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['AlignmentOverruns'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=8, Types='routeId', RouteId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['RouteId'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=9, Types='assignedConnection', ConnectionId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['ConnectionId'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=10, Types='localSessionId', SessionId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['SessionId'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=11, Types='remoteSessionId', SessionId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['SessionId'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=12, Types='assignedCookie', Cookie4Byte='00000001')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['Cookie4Byte'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=13, Types='pwType', PwType='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['PwType'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=14, Types='l2SpecificSub', L2SpecificSublayer='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['L2SpecificSublayer'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=15, Types='dataSequencing', DataSequencing='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['DataSequencing'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=16, Types='txConnectSpeed', SpeedBps='0000000000000001')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['SpeedBps'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=17, Types='rxConnectSpeed', SpeedBps='0000000000000001')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['SpeedBps'],
    #               Type='Increment', Count=10)

    header_option = edit_header_l2tpv3_control_option(Stream=stream, Level=0, Index=18, Types='circuitStatus', Nbit='1', Abit='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv3ControlOverIp', Attribute=header_option['Nbit'],
    #               Type='Increment', Count=10)

    # 配置过滤抓包
    pdu_pattern_1 = create_capture_pdu_pattern(Port=Ports[1], HeaderTypes=HeaderTypes,
                                               FieldName='l2tpv3ControlOverIp_1.type',
                                               Value='1', MaxValue='1')
    edit_capture_filter(Port=Ports[1], Expression=f'{pdu_pattern_1}')
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
