# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1创建一条流量StreamTemplate_1;
#                   测试步骤3: 修改流量StreamTemplate_1内容;
#                   测试步骤4: 订阅StreamBlockStats统计;
#                   测试步骤5: 发送所有流量，等待一段时间;
#                   测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
#
# Criteria    	:   预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
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
    Port_UP, Port_Down = reserve_port(Locations=locations, Force=True)

    # NOTE: add_stream函数返回值是list
    # 创建流量
    stream = add_stream(Ports=Port_UP)

    # 修改流量报文头部
    create_stream_header(Stream=stream, HeaderTypes=['EthernetII', 'IPv4'])

    # 修改流量报文内容

    # 修改ethernet头部
    edit_header_ethernet(Stream=stream, SourceMacAdd='00:01:01:a0:00:01')
    # 修改ipv4头部， Option添加EndOfOption和RouterAlert
    edit_header_ipv4(Stream=stream, Destination='10.10.0.1', HeaderOption=['EndOfOption', 'RouterAlert'])
    # 修改ipv4头部中RouterAlert的参数
    edit_header_ipv4_option(Stream=stream, Index=1, Option=['RouterAlert'], routerAlertValue=1)
    # 流量报文IPv4头部源IP地址添加Modifier跳变
    edit_modifier(Stream=stream, Level=1, Attribute='source',
                  Start='192.168.1.1',
                  Type='Increment',
                  Count=5,
                  Step=1,
                  StreamType='InterModifier',
                  )

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 订阅StreamBlockStats统计视图
    subscribe_types = [
        'PortStats',
        'PortAvgLatencyStats',
        'StreamStats',
        'StreamTxStats',
        'StreamRxStats',
        'StreamBlockStats',
        'StreamBlockTxStats',
        'StreamBlockRxStats',
    ]
    subscribe_result(Types=subscribe_types)

    # 发送流量
    start_stream()
    time.sleep(10)

    # NOTE: 统计获取数据返回基本原则，当获取到单行数据时返回dict类型数据，
    # NOTE: 当获取到多行数据时返回Pandas的DataFrame数据，Pandas详细请参考: https://www.pypandas.cn/
    # 获取流量PortStats返回DataFrame数据
    result = get_port_statistic(StaItems=['TxFrameRate', 'RxFrameRate'])
    print('端口PortStats统计数据:\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    # 停止流量
    stop_stream()
    time.sleep(3)

    # 获取流量StreamBlockStats返回Dict数据
    result = get_streamblock_statistic(Stream=stream, StaItems=['TxStreamFrames', 'RxStreamFrames'])
    print(f'StreamBlockStats流量{stream[0].Name}统计数据:\n{result}')
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']

    # 判断流量收发包是否相等
    if TxStreamFrames != RxStreamFrames:
        verdict = 'fail'
        errInfo += f'Test fail: {stream[0].Name} TxStreamFrames({TxStreamFrames}) is not equal to RxStreamFrames({RxStreamFrames})\n'
    else:
        print(f'Test pass: {stream[0].Name} TxStreamFrames({TxStreamFrames}) is equal to RxStreamFrames({RxStreamFrames})\n')

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
