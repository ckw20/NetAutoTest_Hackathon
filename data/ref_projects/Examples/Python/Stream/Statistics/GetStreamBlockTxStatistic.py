# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发流StreamBlockTxStats统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1, Port_2分别创建两条流量StreamTemplate_1、2、3、4;
#                   测试步骤3: 订阅StreamBlockTxStats统计;
#                   测试步骤4: 发送所有流量，查看StreamBlockTxStats统计信息，等待一段时间;
#                   测试步骤5: 停止所有流量，查看StreamBlockTxStats统计信息;
#
# Criteria    	:   预期结果1: 步骤4,5中StreamBlockTxStats统计信息获取正确;
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

    # 创建流量
    streams = add_stream(Ports=[Port_UP, Port_UP, Port_Down, Port_Down])

    # 订阅StreamBlockTxStats统计视图
    subscribe_result(Types=['StreamBlockTxStats'])

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 发送流量
    start_stream()
    # 发送流获取统计建议等待10sec获取到稳定统计数据
    time.sleep(10)

    # NOTE: 统计获取数据返回基本原则，当获取到单行数据时返回dict类型数据，
    # 当获取到多行数据时返回Pandas的DataFrame数据，Pandas详细请参考: https://www.pypandas.cn/
    # 统计获取方式1 -- 获取StreamBlockTxStats所有统计结果:
    # get_streamblock_tx_statistic不传参数，返回值为DataFrame数据
    result = get_streamblock_tx_statistic()
    # 使用tabulate库表格化输出DataFrame二维数据
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')
    # 将DataFrame数据转成list[dict]形式
    data = result.to_dict('records')
    print(data)

    # 根据DataFrame数据筛选出StreamTemplate_1的TxFrameRate和RxStreamFrames
    df = result[(result['StreamBlockID'] == streams[0].Name)][['TxFrameRate', 'TxBitRate']]
    data = df.to_dict('records')[0]
    # 判断StreamTemplate_1收发包速率不为0
    if data['TxFrameRate'] == 0 or data['TxBitRate'] == 0:
        verdict = 'fail'
        errInfo += f'{streams[0].Name} TxFrameRate or TxBitRate is equal to 0\n'

    stop_stream()
    # 停流获取统计必须等待3sec才能获取到稳定统计数据
    time.sleep(3)

    # 统计获取方式2 -- 获取指定一条流量的统计:
    # get_streamblock_tx_statistic传Stream参数,实参只有一个元素，返回值为字典
    result = get_streamblock_tx_statistic(Stream=streams[-1])
    print(result)

    # 统计获取方式3 -- 获取指定一条流量和端口的统计:
    # get_streamblock_tx_statistic传Stream和Port参数,实参只有一个元素，返回值为字典
    result = get_streamblock_tx_statistic(Stream=streams[-1], Port=Port_Down)
    print(result)

    # 统计获取方式4 -- 获取指定一条流量的统计,并且StaItems参数指定统计项目:
    # get_streamblock_tx_statistic传Stream参数,实参只有一个元素，StaItems参数传入获取的统计项目列表，返回值为字典
    result = get_streamblock_tx_statistic(Stream=streams[:1], StaItems=['TxStreamFrames', 'TxTotalBytes', 'TxByteRate', 'TxBitRate'])
    print(result)

    # 统计获取方式5 -- 获取指定多条流量的统计:
    # get_streamblock_tx_statistic传Stream参数,实参是一个多个元素的列表，返回值为DataFrame数据
    result = get_streamblock_tx_statistic(Stream=streams[:2])
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    # 统计获取方式6 -- 获取指定多条流量的统计,并且StaItems参数指定统计项目:
    # get_streamblock_tx_statistic传Stream参数,实参是一个多个元素的列表，StaItems参数传入获取的统计项目列表， 返回值为DataFrame数据
    result = get_streamblock_tx_statistic(Stream=streams[:3], StaItems=['TxStreamFrames', 'TxTotalBytes', 'TxByteRate', 'TxBitRate'])
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')

    # 统计获取方式7 -- 获取指定所有流量的统计,并且StaItems参数指定统计项目:
    # get_streamblock_tx_statistic不传Stream参数，StaItems参数传入获取的统计项目列表， 返回值为DataFrame数据
    result = get_streamblock_tx_statistic(StaItems=['TxStreamFrames', 'TxTotalBytes', 'TxByteRate', 'TxBitRate'])
    print('\n' + tabulate(result, headers='keys', tablefmt='psql') + '\n')


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
