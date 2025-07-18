*** Settings ***
Force Tags        RFC2889
Resource          ../../Common.robot
*** Variables ***
@{Locations}      //10.0.11.191/1/5    //10.0.11.191/1/6    //10.0.11.191/1/7    //10.0.11.191/1/8    # 测试仪表端口物理地址

*** Test Cases ***
RFC2889_AddressCachingCapacity
    [Documentation]    测试目的 : 确定局域网交换机设备的地址缓存容量
    [Tags]    Tester-001
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}    Force=True
    # =============== *选择测试项* ===============
    ${Wizard}    ${TestItem}    create_benchmark    Type=RFC2889    Items=addressCachingCapacity
    Set Test Variable    ${Wizard}
    # =============== *选择端口* ===============
    relate_benchmark_ports    Config=${Wizard}    Ports=${Ports}
    # =============== *配置端点* ===============
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=eth
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=eth
    # =============== *配置流* ===============
    @{SrcPoints}    get_layer_from_interfaces    Interfaces=${Interface_1}    Layer=eth
    @{DstPoints}    get_layer_from_interfaces    Interfaces=${Interface_2}    Layer=eth
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=eth    SrcPoints=${SrcPoints}    DstPoints=${DstPoints}    Bidirectional=False    Monitors=${Ports[2]}
    # =============== *配置测试选项* ===============
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    # =============== *地址缓存容量参数设置* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Count=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 提供学习的地址数和地址学习速率
    edit_benchmark_address_learning_capacity    Config=${TestItem}    MinAddressCount=1000    MaxAddressCount=5000    InitAddressCount=5000    Resolution=1    AgingTime=30    LearningRate=1000
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=addressCachingCapacity    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=addressCachingCapacity

RFC2889_AddressCachingRate
    [Documentation]    测试目的 : 确定局域网交换机设备的地址学习速率
    [Tags]    Tester-001
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}    Force=True
    # =============== *选择测试项* ===============
    ${Wizard}    ${TestItem}    create_benchmark    Type=RFC2889    Items=addressLearningRate
    Set Test Variable    ${Wizard}
    # =============== *选择端口* ===============
    relate_benchmark_ports    Config=${Wizard}    Ports=${Ports}
    # =============== *配置端点* ===============
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=eth
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=eth
    # =============== *配置流* ===============
    @{SrcPoints}    get_layer_from_interfaces    Interfaces=${Interface_1}    Layer=eth
    @{DstPoints}    get_layer_from_interfaces    Interfaces=${Interface_2}    Layer=eth
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=eth    SrcPoints=${SrcPoints}    DstPoints=${DstPoints}    Bidirectional=False    Monitors=${Ports[2]}
    # =============== *配置测试选项* ===============
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    # =============== *地址速率参数设置* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Count=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 地址学习速率和地址数量
    edit_benchmark_address_learning_rate    Config=${TestItem}    MinRateCount=1000    MaxRateCount=5000    InitRateCount=5000    Resolution=1    AgingTime=30    AddressCount=5000
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=addressLearningRate    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=addressLearningRate

RFC2889_BroadcastForwarding
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=broadcastForwarding
    # =============== *配置流* ===============
    ${Dests}    Combine Lists    ${Point_2}    ${Point_3}    ${Point_4}
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=eth    SrcPoints=${Point_1}    DstPoints=${Dests}
    # =============== *配置测试选项* ===============
    # 时延设置
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    edit_benchmark_learning    Configs=${TestItem}    Frequency=trial    EnableLearning=True    LearningRate=100    LearningRepeat=3    DelayBefore=5
    # =============== *广播帧转发参数设置* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Count=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 负载
    edit_benchmark_search    Config=${TestItem}    Mode=step    Lower=10    Upper=20    Step=10
    # 突发帧数
    ${Count}    Create List    100
    edit_benchmark_burst_count_loop    Config=${TestItem}    Mode=custom    Custom=${Count}
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=broadcastForwarding    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=broadcastForwarding

RFC2889_BroadcastLatency
    [Documentation]    测试目的 : 确定局域网交换机设备的广播帧时延
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=broadcastLatency
    # =============== *配置流* ===============
    ${Dests}    Combine Lists    ${Point_2}    ${Point_3}    ${Point_4}
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=eth    SrcPoints=${Point_1}    DstPoints=${Dests}
    # =============== *配置测试选项* ===============
    # 时延设置
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    edit_benchmark_learning    Configs=${TestItem}    Frequency=trial    EnableLearning=True    LearningRate=100    LearningRepeat=3    DelayBefore=5
    # =============== *广播帧时延参数设置* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Count=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=broadcastLatency    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=broadcastLatency

RFC2889_Congestion
    [Documentation]    测试目的 : 确定局域网交换机设备的拥塞控制
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=congestionControl
    # =============== *配置流* ===============
    ${Srcs}    Combine Lists    ${Point_1}    ${Point_2}
    ${Dests}    Combine Lists    ${Point_3}    ${Point_4}
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=eth    SrcPoints=${Srcs}    DstPoints=${Dests}    Mode=congestion
    # =============== *配置测试选项* ===============
    # 时延设置
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    edit_benchmark_learning    Configs=${TestItem}    Frequency=trial    EnableLearning=True    LearningRate=100    LearningRepeat=3    DelayBefore=5
    # =============== *拥塞控制参数设置* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Count=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 突发帧数
    ${Count}    Create List    100
    edit_benchmark_burst_count_loop    Config=${TestItem}    Mode=custom    Custom=${Count}
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=congestionControl    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=congestionControl

RFC2889_ErorFrameFilter
    [Documentation]    测试目的 : 确定局域网交换机设备的错误帧过滤
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=erroredFrameFilter
    # =============== *配置流* ===============
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=eth    SrcPoints=${Point_1}    DstPoints=${Point_2}
    # =============== *配置测试选项* ===============
    # 时延设置
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    edit_benchmark_learning    Configs=${TestItem}    Frequency=trial    EnableLearning=True    LearningRate=100    LearningRepeat=3    DelayBefore=5
    # =============== *错误帧过滤参数设置* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Count=1
    # 错误以太帧、突发和帧长设置
    edit_benchmark_errored_frame_filtering    Config=${TestItem}    CrcTested=True    CrcFrameLength=128
    # 负载
    edit_benchmark_traffic_load_loop    Config=${TestItem}    LoadMode=step    LoadStart=10    LoadEnd=20    LoadStep=10
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=erroredFrameFilter    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=errorFrameFilter

RFC2889_Forwarding
    [Documentation]    测试目的 : 确定局域网交换机设备的转发
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=forwarding
    # =============== *配置流* ===============
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=eth    SrcPoints=${Point_1}    DstPoints=${Point_2}
    # =============== *配置测试选项* ===============
    # 时延设置
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO    DelayBefore=2    DelayAfter=10
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    edit_benchmark_learning    Configs=${TestItem}    Frequency=trial    EnableLearning=True    LearningRate=100    LearningRepeat=3    DelayBefore=5
    # =============== *转发参数设置* ===============
    # 试验次数
    edit_benchmark_duration    Config=${TestItem}    Count=1
    # 帧长设置
    ${FrameSize}    Create List    128
    edit_benchmark_frame    Config=${TestItem}    Type=custom    Custom=${FrameSize}
    # 负载
    edit_benchmark_search    Config=${TestItem}    Mode=step    Lower=10    Upper=20    Step=10
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    EnableCustomResult=True    ResultFileName=forwarding    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=forwarding
*** Keywords ***
CaseSetup
    [Arguments]    ${testcase}
    [Documentation]    RFC2889 Case Setup
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}    Force=True
    # 创建接口
    ${layers}    Create List    eth
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=${layers}
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=${layers}
    ${Interface_3}    create_interface    Port=${Ports[2]}    Layers=${layers}
    ${Interface_4}    create_interface    Port=${Ports[3]}    Layers=${layers}
    ${Point_1}    get_layer_from_interfaces    Interfaces=${Interface_1}    Layer=eth
    ${Point_2}    get_layer_from_interfaces    Interfaces=${Interface_2}    Layer=eth
    ${Point_3}    get_layer_from_interfaces    Interfaces=${Interface_3}    Layer=eth
    ${Point_4}    get_layer_from_interfaces    Interfaces=${Interface_4}    Layer=eth
    # =============== *选择测试项* ===============
    ${Wizard}    ${TestItem}    create_benchmark    Type=RFC2889    Items=${testcase}
    # =============== *选择端口* ===============
    relate_benchmark_ports    Config=${Wizard}    Ports=${Ports}
    Set Test Variable    ${Point_1}
    Set Test Variable    ${Point_2}
    Set Test Variable    ${Point_3}
    Set Test Variable    ${Point_4}
    Set Test Variable    ${Wizard}
    Set Test Variable    ${TestItem}

CaseTeardown
    [Arguments]    ${testcase}
    [Documentation]    RFC2889 Case Teardown
    # =============== *生成智能脚本* ===============
    expand_benchmark    Config=${Wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # =============== *执行智能脚本测试* ===============
    ${DB}    run_benchmark    Mode=0    Timer=3600    Analyzer=True
    ${Result}    get_benchmark_result    DB=${DB}    Type=RFC2889    Item=${testcase}
    ${PutResult}    format_benchmark_result    Result=${Result}
    Log To Console    message=${PutResult}
    del_benchmark
    # Shutdown Tester
