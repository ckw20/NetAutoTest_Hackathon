*** Settings ***
Suite Setup       SuiteSetup
Force Tags        RFC2544
Resource          ../../Common.robot
*** Variables ***
@{Locations}      //10.0.11.191/1/5    //10.0.11.191/1/6

*** Test Cases ***
RFC2544_BackToBack
    [Documentation]    测试目的 : 局域网交换机设备背靠背测试
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=backtoback
    # =============== *配置rfc2544* ===============
    edit_benchmark_learning    Configs=${TestItem}    Frequency=once    EnableArp=False
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_transport_layer    Configs=${TestItem}    HeaderType=tcp
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    # =============== *配置背靠背* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Trial=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 时间阈值
    edit_benchmark_backtoback_binary_search    Config=${TestItem}    MinDuration=0.01
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=backtoback    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=backtoback

RFC2544_Frameloss
    [Documentation]    测试目的 : 局域网交换机设备丢包率测试
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=frameloss
    # =============== *配置rfc2544* ===============
    edit_benchmark_learning    Configs=${TestItem}    Frequency=once    EnableArp=False
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_transport_layer    Configs=${TestItem}    HeaderType=tcp
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    # =============== *配置丢包率* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Trial=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 负载
    edit_benchmark_traffic_load_loop    Config=${TestItem}    LoadMode=step    LoadStart=10    LoadEnd=20    LoadStep=10
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=frameloss    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=frameloss

RFC2544_Latency
    [Documentation]    测试目的 : 局域网交换机设备时延测试
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=latency
    # =============== *配置rfc2544* ===============
    edit_benchmark_learning    Configs=${TestItem}    Frequency=once    EnableArp=False
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_transport_layer    Configs=${TestItem}    HeaderType=tcp
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    # =============== *配置时延* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Trial=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 负载
    edit_benchmark_traffic_load_loop    Config=${TestItem}    LoadMode=step    LoadStart=10    LoadEnd=20    LoadStep=10
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=latency    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=latency

RFC2544_throughput
    [Documentation]    测试目的 : 确定局域网交换机设备的吞吐量
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=throughput
    # =============== *配置rfc2544* ===============
    edit_benchmark_learning    Configs=${TestItem}    Frequency=once    EnableArp=False
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_transport_layer    Configs=${TestItem}    HeaderType=tcp
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    # =============== *配置吞吐量* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Trial=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 负载
    edit_benchmark_search    Config=${TestItem}    Mode=step    Lower=10    Upper=20    Step=10
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=latency    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=throughput
*** Keywords ***
SuiteSetup
    [Documentation]    RFC2544 Suite Setup
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}    Force=True
    # 创建接口
    ${layers}    Create List    eth    ipv4
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=${layers}
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=${layers}
    @{SrcPoints}    get_layer_from_interfaces    Interfaces=${Interface_1}    Layer=ipv4
    @{DstPoints}    get_layer_from_interfaces    Interfaces=${Interface_2}    Layer=ipv4
    Set Suite Variable    @{SrcPoints}
    Set Suite Variable    @{DstPoints}

CaseSetup
    [Arguments]    ${testcase}
    [Documentation]    RFC2544 case setup
    # 创建测试套件及流量
    @{TestCase}    Create List    ${testcase}
    ${Wizard}    ${TestItem}    create_benchmark    Type=RFC2544    Items=@{TestCase}
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=ipv4    SrcPoints=@{SrcPoints}    DstPoints=@{DstPoints}
    Set Test Variable    ${Wizard}
    Set Test Variable    ${TestItem}

CaseTeardown
    [Arguments]    ${testcase}
    [Documentation]    RFC2544 Case Teardown
    # =============== *生成智能脚本* ===============
    expand_benchmark    Config=${Wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # =============== *执行智能脚本测试* ===============
    ${DB}    run_benchmark    Mode=0    Timer=3600    Analyzer=True
    ${Result}    get_benchmark_result    DB=${DB}    Type=RFC2544    Item=${testcase}
    ${PutResult}    format_benchmark_result    Result=${Result}
    Log To Console    message=${PutResult}
    del_benchmark
    # Shutdown Tester
