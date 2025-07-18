# =================================================================================
# Objective   	:   测试目的 : 使用智能脚本控制命令loop
#
# Step			:	测试步骤1: 创建端口;
#                   测试步骤2: 创建流量;
#                   测试步骤3: 检查统计;
#
# Criteria    	:   预期结果1: 步骤3 判断端口发送报文数量;
#
# Created by   	:  	Tester-002
#
# Bugs   	    :  	# None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.192/1/1', '//10.0.11.192/1/2'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'BigTao' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''

try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    port_1, port_2 = reserve_port(Locations=locations[:2])

    # 创建raw stream
    stream_1 = add_stream(Ports=port_1)
    stream_2 = add_stream(Ports=port_2)
    edit_port_load_profile(Ports=[port_1, port_2],
                           TransmitMode='BURST',
                           BurstSize=100)

    # 订阅统计
    subscribe_result(Types=['PortStats'])

    ggroup = smart_scripter_global_group()

    # 使用智能脚本的loop命令
    loopcommand = smart_scripter_command(ParentGroup=ggroup,
                                         Command='LoopCommand',
                                         LoopCount=2)
    stream_handle_1 = get_object_attrs(stream_1)
    start_stream_1 = smart_scripter_command(ParentGroup=loopcommand,
                                            Command='StartStreamCommand',
                                            StreamList=stream_handle_1)
    stream_handle_2 = get_object_attrs(stream_2)
    start_stream_2 = smart_scripter_command(ParentGroup=loopcommand,
                                            Command='StartStreamCommand',
                                            StreamList=stream_handle_2)
    run_benchmark()
    result = get_port_statistic()
    print(result)
    assert result['TxStreamFrames'][0] == 100
    assert result['TxStreamFrames'][1] == 100

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
