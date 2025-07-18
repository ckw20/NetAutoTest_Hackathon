# =================================================================================
# Objective   	:   测试目的 : 配置PCEP协议，检查统计
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 两个端口分别创建PCEP协议;
#                   测试步骤4: 订阅PCEP相关统计;
#                   测试步骤5: 启动协议;
#                   测试步骤6: 查看统计信息;
#
# Criteria    	:   预期结果1: 步骤6中统计获取正常;
#
# Created by   	:  	Tester-002
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

    interfaces_1 = create_interface(Port=Port_UP)

    interfaces_2 = create_interface(Port=Port_Down)

    edit_interface(Interface=interfaces_1,
                   Layer='IPv4Layer',
                   Address='1.1.1.1',
                   Gateway='1.1.1.2')

    edit_interface(Interface=interfaces_2,
                   Layer='IPv4Layer',
                   Address='1.1.1.2',
                   Gateway='1.1.1.1')

    # 创建PCEP协议会话

    session_1 = create_pcep(Port=Port_UP, Role='PCC', Negotiation=True)

    session_2 = create_pcep(Port=Port_Down, Role='PCE', Negotiation=False)

    # PCEP协议会话与接口绑定

    select_interface(Session=session_1, Interface=interfaces_1)

    select_interface(Session=session_2, Interface=interfaces_2)

    # 创建LSP

    lsp_1 = create_pcep_pcc_lsp(Sessions=session_1)

    lsp_2 = create_pcep_pce_lsp(Sessions=session_2)

    # 订阅统计

    subscribe_result(Types=['PcepLspStatistic', 'PcepLspBlockStatistic', 'PcepPortStatistic',
                            'PcepSessionStatistic', 'PcepSessionBlockStatistic'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动协议

    start_protocol()

    # 等待PCEP协议协议会话状态正确

    wait_pcep_state(Sessions=[session_1, session_2])

    time.sleep(5)

    # 发送流量

    start_stream()

    time.sleep(10)

    stop_stream()

    stop_protocol()

    time.sleep(3)

    # 获取PCEP端口统计
    import pandas
    result = get_pcep_lsp_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_pcep_lsp_statistic(Session=session_1, SessionId=1, Lsp=lsp_1, LspId=1)
    print(result)
    result = get_pcep_lsp_statistic(Session=session_2, SessionId=1, Lsp=lsp_2, LspId=1)
    print(result)

    # 获取PCEP客户端统计
    result = get_pcep_lsp_block_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_pcep_lsp_block_statistic(Session=session_1, SessionId=1, Lsp=lsp_1)
    print(result)
    result = get_pcep_lsp_block_statistic(Session=session_2, SessionId=1, Lsp=lsp_2)
    print(result)

    # 获取PCEP客户端统计
    result = get_pcep_port_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_pcep_port_statistic(Port=Port_UP)
    print(result)
    result = get_pcep_port_statistic(Port=Port_Down)
    print(result)

    # 获取PCEP客户端统计
    result = get_pcep_session_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_pcep_session_statistic(Session=session_1, SessionId=1)
    print(result)
    result = get_pcep_session_statistic(Session=session_2, SessionId=1)
    print(result)

    # 获取PCEP客户端统计
    result = get_pcep_session_block_statistic()
    print(result)
    if not isinstance(result, pandas.DataFrame):
        verdict = 'fail'

    result = get_pcep_session_block_statistic(Session=session_1)
    print(result)
    result = get_pcep_session_block_statistic(Session=session_2)
    print(result)

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
