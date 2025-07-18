# =================================================================================
# Objective   	:   测试目的 : 检查ISIS协议IPv4绑定流发送正常
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建ISIS协议，并且创建路由;
#                   测试步骤3: 创建绑定流量;
#                   测试步骤4: 订阅StreamBlockStats统计;
#                   测试步骤5: 发送所有流量，等待一段时间;
#                   测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
#
# Criteria    	:   预期结果1: 步骤6中所有流量收发包相等;
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

    Port_UP, Port_Down = reserve_port(Locations=locations)

    # 创建接口

    interfaces_1 = create_interface(Port=Port_UP, Layers='ipv4')

    interfaces_2 = create_interface(Port=Port_Down, Layers='ipv4')

    edit_interface(Interface=interfaces_1,
                          Layer='IPv4Layer',
                          Address='192.168.1.2',
                          Gateway='192.168.1.3')

    edit_interface(Interface=interfaces_2,
                          Layer='IPv4Layer',
                          Address='192.168.1.3',
                          Gateway='192.168.1.2')

    # 创建ISIS协议会话

    session_1 = create_isis(Port=Port_UP)
    session_2 = create_isis(Port=Port_Down)

    edit_isis(Session=session_1, Level='L1L2', MtParams=2, PerPduAuthentication=4)
    edit_isis(Session=session_2, Level='L1L2', MtParams=2, PerPduAuthentication=4)

    # 修改ISIS Mt参数

    edit_isis_mt_params(Session=session_1, Index=0, MtId='IPV4', MtFlags='NOSHOW')
    edit_isis_mt_params(Session=session_1, Index=1, MtId='IPV6', MtFlags=['ABIT', 'OBIT'])
    mt = get_isis_mt_params(Session=session_1, Index=0)
    print(mt)
    mt = get_isis_mt_params(Session=session_1, Index=1)
    print(mt)

    edit_isis_mt_params(Session=session_2, Index=0, MtId='IPV4', MtFlags='NOSHOW')
    edit_isis_mt_params(Session=session_2, Index=1, MtId='IPV6', MtFlags=['ABIT', 'OBIT'])
    mt = get_isis_mt_params(Session=session_2, Index=0)
    print(mt)
    mt = get_isis_mt_params(Session=session_2, Index=1)
    print(mt)

    # 修改ISIS PerPduAuthentication参数

    edit_isis_per_pdu(Session=session_1, Index=0, PdusType='L1_HELLO', AuthMethod='NONE')
    edit_isis_per_pdu(Session=session_1, Index=1, PdusType='L2_HELLO', AuthMethod='SIMPLE', Password='test')
    edit_isis_per_pdu(Session=session_1, Index=2, PdusType='L1_AREA_PDUS', AuthMethod='MD5', Password='test')
    edit_isis_per_pdu(Session=session_1, Index=3, PdusType='L2_DOMAIN_PDUS', AuthMethod='NONE')
    per_pdu = get_isis_per_pdu(Session=session_1, Index=0)
    print(per_pdu)
    per_pdu = get_isis_per_pdu(Session=session_1, Index=1)
    print(per_pdu)
    per_pdu = get_isis_per_pdu(Session=session_1, Index=2)
    print(per_pdu)
    per_pdu = get_isis_per_pdu(Session=session_1, Index=3)
    print(per_pdu)

    edit_isis_per_pdu(Session=session_2, Index=0, PdusType='L1_HELLO', AuthMethod='NONE')
    edit_isis_per_pdu(Session=session_2, Index=1, PdusType='L2_HELLO', AuthMethod='SIMPLE', Password='test')
    edit_isis_per_pdu(Session=session_2, Index=2, PdusType='L1_AREA_PDUS', AuthMethod='MD5', Password='test')
    edit_isis_per_pdu(Session=session_2, Index=3, PdusType='L2_DOMAIN_PDUS', AuthMethod='NONE')
    per_pdu = get_isis_per_pdu(Session=session_2, Index=0)
    print(per_pdu)
    per_pdu = get_isis_per_pdu(Session=session_2, Index=1)
    print(per_pdu)
    per_pdu = get_isis_per_pdu(Session=session_2, Index=2)
    print(per_pdu)
    per_pdu = get_isis_per_pdu(Session=session_2, Index=3)
    print(per_pdu)

    # ISIS协议会话与接口绑定

    select_interface(Session=session_1, Interface=interfaces_1)
    select_interface(Session=session_2, Interface=interfaces_2)

    # ISIS协议会话创建LSP

    ipv4_lsp_1 = create_isis_lsp(Session=session_1, Level='L1')
    ipv4_lsp_2 = create_isis_lsp(Session=session_2, Level='L1')

    # ISIS协议会话LSP创建IPv4 TLV

    ipv4_tlv_1 = create_isis_ipv4_tlv(Lsp=ipv4_lsp_1, RouteCount=10)
    ipv4_tlv_2 = create_isis_ipv4_tlv(Lsp=ipv4_lsp_2, RouteCount=10)

    # 获取ISIS协议绑定流端点对象

    point_1 = get_isis_router_from_tlv(Configs=ipv4_tlv_1)
    point_2 = get_isis_router_from_tlv(Configs=ipv4_tlv_2)

    # 创建ISIS绑定流

    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 订阅统计

    subscribe_result(Types=['IsisSessionStats', 'IsisTlvStats', 'StreamBlockStats'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待ISIS协议会话稳定状态

    wait_isis_state(Sessions=[session_1, session_2])

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    import pandas
    result = get_isis_session_stats()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_isis_tlv_stats()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    # 获取流量1统计

    result = get_streamblock_statistic(Stream=streams[0])
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    print('TxStreamFrames: {}'.format(TxStreamFrames))
    print('RxStreamFrames: {}'.format(RxStreamFrames))

    if TxStreamFrames != RxStreamFrames:
        verdict = 'fail'
        errInfo += '{} TxStreamFrames({}) is not equal to RxStreamFrames({})\n'.format(streams[0].Name, TxStreamFrames,
                                                                                       RxStreamFrames)

    # 获取流量2统计

    result = get_streamblock_statistic(Stream=streams[1])
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    print('TxStreamFrames: {}'.format(TxStreamFrames))
    print('RxStreamFrames: {}'.format(RxStreamFrames))

    if TxStreamFrames != RxStreamFrames:
        verdict = 'fail'
        errInfo += '{} TxStreamFrames({}) is not equal to RxStreamFrames({})\n'.format(streams[1].Name, TxStreamFrames,
                                                                                       RxStreamFrames)

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
