# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1创建一条流量StreamTemplate_1;
#                   测试步骤3: 修改流量StreamTemplate_1的Hdlc头部内容;
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
    create_stream_header(Stream=stream, HeaderTypes=['chdlc', 'ipv4'])

    # 修改Hdlc头部
    attr = edit_header_hdlc(Stream=stream, Level=0,
                            Address='FF')
    edit_modifier(Stream=stream, Attribute=attr['Address'],
                  Type='Increment', Count=10, HeaderType='chdlc')

    # 订阅统计
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])

    # 设置端口发送模式为突发包
    BurstCount = 100
    edit_port_load_profile(Ports=Port_UP, TransmitMode='BURST', BurstCount=BurstCount)

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 发送流量
    start_stream()

    # 等待流量停止
    wait_stream_state()

    # 流量停止后，必须等待大于等于3sec才能正确获得统计结果
    time.sleep(3)

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

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
