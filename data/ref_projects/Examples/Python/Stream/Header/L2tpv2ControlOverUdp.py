# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发L2TPv2 Control Over UDP报文统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 修改流量StreamTemplate_1的L2TPv2 Control Over UDP头部内容;;
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

locations = ['//10.0.11.191/1/3', '//10.0.11.191/1/4'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
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
    HeaderTypes = ['EthernetII', 'IPv4', 'UDP', 'l2tpv2Control']
    create_stream_header(Stream=stream, HeaderTypes=HeaderTypes)
    # 修改l2tpv2Control头部
    header = edit_header_l2tpv2_control(Stream=stream, Level=0, Reserved1=11, Ns=5, Nr=6)
    # 设置跳变
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header['Nr'],
                  Type='Increment', Count=10)
    # 修改l2tp control option
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=0, Types='GeneralTLV', AttributeValue='11')
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['AttributeValue'],
                  Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=1, Types='MessageType', MessageType='1')
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['MessageType'],
                  Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=2, Types='ResultCode', ErrorCode='1', ErrorMessage='01')
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['ErrorCode'],
                  Type='Increment', Count=10)
    edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['ErrorMessage'],
                  Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=3, Types='ProtocolVersion', Ver='1', Rev='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['Ver'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=4, Types='FramingCapabilities', Abit='1', Sbit='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['Abit'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=5, Types='BearerCapabilities', Abit='1', Dbit='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['Dbit'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=6, Types='TieBreaker', TieBreakerValue='0000000000000001')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['TieBreakerValue'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=7, Types='FirmwareRevision', FirmwareRevision='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['FirmwareRevision'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=8, Types='AssignedTunnelId', TunnelId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['TunnelId'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=9, Types='ReceiveWindowSize', WindowSize='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['WindowSize'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=10, Types='AssignedSessionId', SessionId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['SessionId'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=11, Types='Response', ResponseValue='00000000000000000000000000000001')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['ResponseValue'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=12, Types='CallSerialNumber', CallSerialNumber='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['CallSerialNumber'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=13, Types='MinimumBps', MinimumBps='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['MinimumBps'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=14, Types='MaximumBps', MaximumBps='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['MaximumBps'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=15, Types='BearerType', Abit='1', Dbit='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['Dbit'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=16, Types='FramingType', Abit='1', Sbit='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['Sbit'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=17, Types='TxConnectSpeed', Bps='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['Bps'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=18, Types='RxConnectSpeed', HighBPS='1', LowBPS='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['HighBPS'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=19, Types='PhysicalChannelId', PhysicalChannelId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['PhysicalChannelId'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=20, Types='ProxyAuthenType', AuthenType='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['AuthenType'],
    #               Type='Increment', Count=10)
    header_option = edit_header_l2tpv2_control_option(Stream=stream, Level=0, Index=21, Types='ProxyAuthenId', AuthenId='1')
    # edit_modifier(Stream=stream, Level=0, HeaderType='l2tpv2Control', Attribute=header_option['AuthenId'],
    #               Type='Increment', Count=10)

    # 配置过滤抓包
    pdu_pattern_1 = create_capture_pdu_pattern(Port=Ports[1], HeaderTypes=HeaderTypes,
                                               FieldName='l2tpv2Control_1.ns',
                                               Value='5', MaxValue='5')
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
    result = get_streamblock_statistic(Stream=stream[0])
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
