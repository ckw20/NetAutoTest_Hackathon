*** Settings ***
Suite Setup       SuiteSetup
Force Tags        RFC3918
Resource          ../../Common.robot
*** Variables ***
@{Locations}      //10.0.11.191/1/5    //10.0.11.191/1/6    //10.0.11.191/1/7    //10.0.11.191/1/8

*** Test Cases ***
RFC3918_MixedThroughput
    [Documentation]    测试目的 : 如RFC2432规定，混合吞吐量测试是确定想一定数量的接口同时发送单播和组播流量时，DUT/SUT的吞吐量
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=mixedThroughput
    # 搜索算法
    edit_benchmark_search    Config=${TestItem}    Mode=step    Lower=10    Upper=20    Step=10
    # 组播流百分比
    edit_benchmark_multicast_traffic_ratio_loop    Config=${TestItem}    LoopMode=random    MinRatio=10    MaxRatio=50
    # 组播组
    edit_benchmark_multicast_group_count_loop    Config=${TestItem}    LoopMode=random    MinGroup=10    MaxGroup=50
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    ResultFileName=mixedThroughput    AddTimeStamp=True
    # =============== *配置单播流量* ===============
    ${unicast}    add_stream    Type=binding    SrcPoints=${Point_1}    DstPoints=${point_2}    Bidirection=True
    edit_benchmark_multicast_mixed_throughput_unicast_streams    Config=${TestItem}    Streams=${unicast}
    [Teardown]    CaseTeardown    testcase=mixedThroughput

RFC3918_MulticastGroupCapability
    [Documentation]    测试目的 : 确定再DUT/SUT能够正确转发数据包到注册在该DUT/SUT的组播组情况下，DUT/SUT能够支持的最大的组播组数量
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=multicastGroupCapacity
    # =============== *配置组播组容量* ===============
    # 组播搜索算法
    edit_benchmark_search    Config=${TestItem}    Mode=step    Lower=10    Upper=20    Step=10
    # 负载设置
    edit_benchmark_traffic_load_loop    Config=${TestItem}    LoadMode=random    LoadMin=10    LoadMax=50
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    ResultFileName=multicastGroupCapacity    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=multicastGroupCapacity

RFC3918_MulticastJoinLeaveLatency
    [Documentation]    测试目的 : 确定再DUT/SUT收到IGMP陈工加入离开组消息开始，DUT/SUT开始/停止转发多播帧需要的时间
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=multicastJoinLeaveLatency
    # =============== *配置加入离开组时延* ===============
    # 组播组
    edit_benchmark_multicast_group_count_loop    Config=${TestItem}    LoopMode=random    MinGroup=10    MaxGroup=50
    # 负载设置
    edit_benchmark_traffic_load_loop    Config=${TestItem}    LoadMode=random    LoadMin=10    LoadMax=50
    # 延迟设置
    edit_benchmark_multicast_join_leave_delay    Config=${TestItem}    DelayBetweenJoinAndStartStream=20    DelayBetweenJoinAndLeave=15
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    ResultFileName=multicastJoinLeaveLatency    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=multicastJoinLeaveLatency

RFC3918_MulticastLatency
    [Documentation]    测试目的 : 得到DUT/SUT一个端口到多个出端口的一组时延数据
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=multicastLatency
    # =============== *配置组播转发时延* ===============
    # 组播组
    edit_benchmark_multicast_group_count_loop    Config=${TestItem}    LoopMode=random    MinGroup=10    MaxGroup=50
    # 负载设置
    edit_benchmark_traffic_load_loop    Config=${TestItem}    LoadMode=random    LoadMin=10    LoadMax=50
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    ResultFileName=multicastLatency    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=multicastLatency

RFC3918_MulticastThroughput
    [Documentation]    测试目的 : 确定再DUT/SUT在一定数量端口加入不同数量的组播组时的转发率
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=multicastThroughput
    # =============== *配置聚合组播吞吐量* ===============
    # 组播搜索算法
    edit_benchmark_search    Config=${TestItem}    Mode=step    Lower=10    Upper=20    Step=10
    # 组播组
    edit_benchmark_multicast_group_count_loop    Config=${TestItem}    LoopMode=random    MinGroup=10    MaxGroup=50
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    ResultFileName=multicastThroughput    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=multicastThroughput

RFC3918_ScaledGroupForwarding
    [Documentation]    测试目的 : 确定再DUT/SUT在一定数量端口加入不同数量的组播组时的转发率
    [Tags]    Tester-002
    [Setup]    CaseSetup    testcase=scaledGroupForwarding
    # =============== *配置组转发矩阵* ===============
    # 组播组
    edit_benchmark_multicast_group_count_loop    Config=${TestItem}    LoopMode=random    MinGroup=10    MaxGroup=50
    # 负载设置
    edit_benchmark_traffic_load_loop    Config=${TestItem}    LoadMode=random    LoadMin=10    LoadMax=50
    # 配置自定义测试结果名称
    edit_benchmark_result_file_name    Config=${TestItem}    ResultFileName=scaledGroupForwarding    AddTimeStamp=True
    [Teardown]    CaseTeardown    testcase=scaledGroupForwarding
*** Keywords ***
SuiteSetup
    [Documentation]    RFC3918 Suite Setup
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}    Force=True
    Set Suite Variable    ${Ports}
    # 创建接口
    ${layers}    Create List    eth    ipv4
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=${layers}
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=${layers}
    ${Interface_3}    create_interface    Port=${Ports[2]}    Layers=${layers}
    ${Interface_4}    create_interface    Port=${Ports[3]}    Layers=${layers}
    edit_interface    Interface=${Interface_1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    edit_interface    Interface=${Interface_2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    edit_interface    Interface=${Interface_3}    Layer=IPv4Layer    Address=1.1.1.3    Gateway=1.1.1.4
    edit_interface    Interface=${Interface_4}    Layer=IPv4Layer    Address=1.1.1.4    Gateway=1.1.1.3
    ${Point_1}    get_layer_from_interfaces    Interfaces=${Interface_1}    Layer=ipv4
    ${Point_2}    get_layer_from_interfaces    Interfaces=${Interface_2}    Layer=ipv4
    ${Point_3}    get_layer_from_interfaces    Interfaces=${Interface_3}    Layer=ipv4
    ${Point_4}    get_layer_from_interfaces    Interfaces=${Interface_4}    Layer=ipv4
    Set Suite Variable    ${Point_1}
    Set Suite Variable    ${Point_2}
    Set Suite Variable    ${Point_3}
    Set Suite Variable    ${Point_4}

CaseSetup
    [Arguments]    ${testcase}
    [Documentation]    RFC3918 Case Setup
    # 创建测试套件
    @{TestCase}    Create List    ${testcase}
    ${Wizard}    ${TestItem}    create_benchmark    Type=RFC3918    Items=@{TestCase}
    relate_benchmark_ports    Config=${Wizard}    Ports=${Ports}
    Set Test Variable    ${Wizard}
    Set Test Variable    ${TestItem}
    # =============== *创建组播流量* ===============
    create_benchmark_streams    Config=${Wizard}    Items=${TestItem}    Type=ipv4    SrcPoints=${Point_1}    DstPoints=${Point_2}    Mode=m2m    Monitors=${Point_3}
    # =============== *配置组播参数* ===============
    edit_benchmark_multicast_base_parameters    Configs=${TestItem}    Version=igmpv2    Ipv4GroupAddressStart=225.0.0.1    Ipv4GroupAddressStep=0.1.0.0    Ipv4PrefixLength=32    GroupIncrement=1    JoinGroupDelay=10    LeaveGroupDelay=20    JoinLeaveSendRate=100    GroupDistributeMode=even
    # 传输层配置
    edit_benchmark_transport_layer    Configs=${TestItem}    HeaderType=tcp    EnableRandomPort=True
    # 流配置
    edit_benchmark_multicast_stream_tos    Configs=${TestItem}    Tos=2    TTL=11    Priority=1
    # =============== *配置测试选项* ===============
    edit_benchmark_learning    Configs=${TestItem}    Frequency=frame    EnableLearning=True    LearningRate=1000    LearningRepeat=5    DelayBefore=2    EnableArp=True    ArpRate=1000    ArpRepeat=3
    edit_benchmark_duration    Config=${TestItem}    Trial=1    Mode=burst    Count=1
    edit_benchmark_frame    Config=${TestItem}    Type=step    Min=128    Max=256    Step=128
    edit_benchmark_latency    Configs=${TestItem}    Type=FIFO
    edit_benchmark_multicast_other    Configs=${TestItem}    StopTestWhenFailed=True    VerifyFreq=topo_changed    DurationMode=second    TimeDurationCount=2    TxFrameRate=1000
    edit_benchmark_path    Configs=${TestItem}    Path=${TestFilePath}
    edit_benchmark_latency    Configs=${TestItem}    DelayAfter=20

CaseTeardown
    [Arguments]    ${testcase}
    [Documentation]    RFC3918 Case Teardown
    # =============== *生成智能脚本* ===============
    expand_benchmark    Config=${Wizard}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # =============== *执行智能脚本测试* ===============
    ${DB}    run_benchmark    Mode=0    Timer=3600    Analyzer=True
    ${Result}    get_benchmark_result    DB=${DB}    Type=RFC3918    Item=${testcase}
    ${PutResult}    format_benchmark_result    Result=${Result}
    Log To Console    message=${PutResult}
    del_benchmark
    # Shutdown Tester
