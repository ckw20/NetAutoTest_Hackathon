*** Settings ***
Force Tags        Header
Resource          ../Common.robot
*** Test Cases ***
Header_ICMPv4_AddressMaskReply
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 address mask reply报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 address mask reply头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    IcmpMaskReply
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 address mask reply头部
    edit_header_icmp_mask_reply    Stream=${Stream}    Level=0    Identifier=100    SequenceNumber=200    AddrMask=24
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=IcmpMaskReply_1.Identifier    Value=100    MaxValue=100
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=IcmpMaskReply_1.SequenceNumber    Value=100    MaxValue=200
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=IcmpMaskReply_1.AddrMask    Value=24    MaxValue=24
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv4_AddressMaskRequest
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 address mask requset报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 address mask requset头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    IcmpMaskRequest
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 address mask request头部
    edit_header_icmp_mask_request    Stream=${Stream}    Level=0    Identifier=100    SequenceNumber=200    AddrMask=24
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=IcmpMaskRequest_1.Identifier    Value=100    MaxValue=100
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=IcmpMaskRequest_1.SequenceNumber    Value=100    MaxValue=200
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=IcmpMaskRequest_1.AddrMask    Value=24    MaxValue=24
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv4_DestUnreach
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 dest unreach报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 dest unreach头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    DestUnreach
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 dest unreach头部
    edit_header_icmp_dest_unreach    Stream=${Stream}    Level=0    Unused=0    Ipv4HeaderTosPrecedence=000    Ipv4HeaderTosDelay=0    Ipv4HeaderTosThroughput=1    Ipv4HeaderTosReliability=0    Ipv4HeaderTosMonetaryCost=0    Ipv4HeaderTosReserved=0    Ipv4HeaderFlags=001    Ipv4HeaderOffset=0    Ipv4HeaderTTL=200    Ipv4HeaderSource=10.1.1.2    Ipv4HeaderDestination=20.1.1.2    Ipv4HeaderGateway=10.1.1.1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=destUnreach_1.headerData.ipv4Header.tos.tos.throughput    Value=1    MaxValue=1
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=destUnreach_1.headerData.ipv4Header.source    Value=10.1.1.2    MaxValue=10.1.1.2
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=destUnreach_1.headerData.ipv4Header.destination    Value=20.1.1.2    MaxValue=20.1.1.2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv4_EchoReply
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 echo reply报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 echo reply头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    Icmpv4EchoReply
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 echo reply头部
    edit_header_icmp_echo_reply    Stream=${Stream}    Level=0    Type=2    Code=4    Identifier=100    SequenceNumber=200
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4EchoReply_1.identifier    Value=100    MaxValue=100
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4EchoReply_1.sequenceNumber    Value=200    MaxValue=200
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_ICMPv4_EchoRequest
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 echo requset报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 echo requset头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    Icmpv4EchoRequest
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 echo request头部
    edit_header_icmp_echorequest    Stream=${Stream}    Level=0    Type=2    Code=4    Identifier=65535    SequenceNumber=65535
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4EchoRequest_1.identifier    Value=65535    MaxValue=65535
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4EchoRequest_1.sequenceNumber    Value=65535    MaxValue=65535
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_ICMPv4_InformationReply
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 information reply报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 information reply头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    InformationReply
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 information reply头部
    edit_header_icmp_information_reply    Stream=${Stream}    Level=0    Code=4    Identifier=65535    SequenceNumber=65535
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=informationReply_1.identifier    Value=65535    MaxValue=65535
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=informationReply_1.code    Value=4    MaxValue=4
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_ICMPv4_InformationRequest
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 information request报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 information request头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    InformationRequest
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 information request头部
    edit_header_icmp_information_request    Stream=${Stream}    Level=0    Code=4    Identifier=100    SequenceNumber=200
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=informationRequest_1.identifier    Value=100    MaxValue=100
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=informationRequest_1.SequenceNumber    Value=200    MaxValue=200
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_ICMPv4_ParameterProblem
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 parameter problem报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 parameter problem头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    Icmpv4ParameterProblem
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 parameter problem头部
    edit_header_icmp_parameter_problem    Stream=${Stream}    Level=0    Pointer=1    Ipv4HeaderDiffservDscp=CodePoint    Ipv4HeaderFlags=111    Ipv4HeaderSource=10.1.1.2    Ipv4HeaderDestination=11.1.1.2    Data=0000000000000001    Ipv4HeaderGateway=10.1.1.1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4ParameterProblem_1.pointer    Value=1    MaxValue=1
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4ParameterProblem_1.headerData.ipv4Header.flags    Value=111    MaxValue=111
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4ParameterProblem_1.headerData.ipv4Header.destination    Value=11.1.1.2    MaxValue=11.1.1.2
    ${pdu_pattern_4}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4ParameterProblem_1.headerData.data    Value=0000000000000001    MaxValue=0000000000000001
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3} && ${pdu_pattern_4}
    [Teardown]    teardown

Header_ICMPv4_Redirect
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 redirect报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 redirect头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    Icmpv4Redirect
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 redirect头部
    edit_header_icmp_redirect    Stream=${Stream}    Level=0    GatewayAddress=10.1.1.1    Ipv4HeaderTosDelay=1    Ipv4HeaderTTL=200    Ipv4HeaderDestination=20.1.1.2    Data=0000000000000002
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4Redirect_1.gatewayAddress    Value=10.1.1.1    MaxValue=10.1.1.1
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4Redirect_1.headerData.ipv4Header.tos.tos.delay    Value=1    MaxValue=1
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4Redirect_1.headerData.ipv4Header.ttl    Value=200    MaxValue=200
    ${pdu_pattern_4}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv4Redirect_1.headerData.ipv4Header.destination    Value=20.1.1.2    MaxValue=20.1.1.2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3} && ${pdu_pattern_4}
    [Teardown]    teardown

Header_ICMPv4_Source_Quench
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 source quench报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 source quench头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    SourceQuench
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 source quench头部
    edit_header_icmp_source_quench    Stream=${Stream}    Level=0    Code=2    Ipv4HeaderTosReserved=1    Ipv4HeaderOffset=1    Ipv4HeaderSource=10.1.1.2
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=sourceQuench_1.code    Value=2    MaxValue=2
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=sourceQuench_1.headerData.ipv4Header.offset    Value=1    MaxValue=1
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=sourceQuench_1.headerData.ipv4Header.source    Value=10.1.1.2    MaxValue=10.1.1.2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} || ${pdu_pattern_2} || ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv4_Time_Exceeded
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 time exceeded报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 time exceeded头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    TimeExceeded
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 time exceeded头部
    edit_header_icmp_time_exceeded    Stream=${Stream}    Level=0    Ipv4HeaderTosPrecedence=001    Ipv4HeaderID=100    Ipv4HeaderProtocol=1    Ipv4HeaderPadding=11
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timeExceeded_1.headerData.ipv4Header.tos.tos.precedence    Value=001    MaxValue=001
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timeExceeded_1.headerData.ipv4Header.id    Value=100    MaxValue=100
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timeExceeded_1.headerData.ipv4Header.protocol    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} || ${pdu_pattern_2} || ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv4_Time_Stamp_Reply
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 time stamp reply报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 time stamp reply头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    TimestampReply
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 time stamp reply头部
    edit_header_icmp_time_stamp_reply    Stream=${Stream}    Level=0    Identifier=100    SequenceNumber=200    OriginateTimestamp=111    ReceiveTimestamp=222    TransmitTimestamp=333
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timestampReply_1.identifier    Value=100    MaxValue=100
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timestampReply_1.sequenceNumber    Value=200    MaxValue=200
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} || ${pdu_pattern_2}
    [Teardown]    teardown

Header_ICMPv4_Time_Stamp_Request
    [Documentation]    测试目的 : 检查测试仪表发icmpv4 time stamp request报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv4 time stamp request头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    TimestampRequest
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv4 time stamp request头部
    edit_header_icmp_time_stamp_request    Stream=${Stream}    Level=0    Identifier=100    SequenceNumber=200    OriginateTimestamp=111    ReceiveTimestamp=222    TransmitTimestamp=333
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timestampRequest_1.identifier    Value=100    MaxValue=100
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timestampRequest_1.sequenceNumber    Value=200    MaxValue=200
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} || ${pdu_pattern_2}
    [Teardown]    teardown

Header_ICMPv6_Destination_Unreachable
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 destination unreachable报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 destination unreachable头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    destinationunreachable
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 destination unreachable头部
    edit_header_icmpv6_destination_unreachable    Stream=${Stream}    Level=0    Code=3    FlowLabel=2    HopLimit=250    Source=2022::2    Destination=2020::2    Gateway=2022::1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=destinationUnreachable_1.code    Value=3    MaxValue=3
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=destinationUnreachable_1.headerData.ipv6Header.hopLimit    Value=250    MaxValue=250
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=destinationUnreachable_1.headerData.ipv6Header.destination    Value=2020::2    MaxValue=2020::2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv6_Echo_Reply
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 echo reply报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 echo reply头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    icmpv6echoreply
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 echo reply头部
    edit_header_icmpv6_echo_reply    Stream=${Stream}    Level=0    Identifier=65535    SequenceNumber=65535
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv6EchoReply_1.identifier    Value=65535    MaxValue=65535
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv6EchoReply_1.sequenceNumber    Value=65535    MaxValue=65535
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_ICMPv6_Echo_Request
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 echo request报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 echo request头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    icmpv6echorequest
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 echo request头部
    edit_header_icmpv6_echo_request    Stream=${Stream}    Level=0    Identifier=65535    SequenceNumber=65535
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv6EchoRequest_1.identifier    Value=65535    MaxValue=65535
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv6EchoRequest_1.sequenceNumber    Value=65535    MaxValue=65535
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_ICMPv6_MLDv1_Done
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 mldv1 done报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 mldv1 done头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    mldv1done
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 mldv1 done头部
    edit_header_icmpv6_mldv1_done    Stream=${Stream}    Level=0    Type=132    MaxRespDelay=10    MulticastAddress=FF1E::1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Done_1.maxRespDelay    Value=10    MaxValue=10
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Done_1.multicastAddress    Value=FF1E::1    MaxValue=FF1E::1
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Done_1.type    Value=132    MaxValue=132
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv6_MLDv1_Query
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 mldv1 query报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 mldv1 query头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    mldv1query
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 mldv1 query头部
    edit_header_icmpv6_mldv1_query    Stream=${Stream}    Level=0    Code=2    Reserved=10    MulticastAddress=FF1E::1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Query_1.code    Value=2    MaxValue=2
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Query_1.reserved    Value=10    MaxValue=10
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Query_1.multicastAddress    Value=FF1E::1    MaxValue=FF1E::1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv6_MLDv1_Report
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 mldv1 report报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 mldv1 report头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    mldv1report
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 mldv1 report头部
    edit_header_icmpv6_mldv1_report    Stream=${Stream}    Level=0    Code=2    Reserved=10    MulticastAddress=FF1E::1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Report_1.code    Value=2    MaxValue=2
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Report_1.reserved    Value=10    MaxValue=10
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv1Report_1.multicastAddress    Value=FF1E::1    MaxValue=FF1E::1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv6_MLDv2_Query
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 mldv2 query报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 mldv2 query头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    mldv2query
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 mldv2 query头部
    edit_header_icmpv6_mldv2_query    Stream=${Stream}    Level=0    Code=2    Reserved=10    GroupAddress=FF1E::1    Qrv=111
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv2Query_1.code    Value=2    MaxValue=2
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv2Query_1.reserved    Value=10    MaxValue=10
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv2Query_1.Qrv    Value=111    MaxValue=111
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv6_MLDv2_Report
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 mldv2 report报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 mldv2 report头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    mldv2report
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 mldv2 report头部
    edit_header_icmpv6_mldv2_report    Stream=${Stream}    Level=0    Type=143    Reserved=20    NumberOfGroupRecords=2
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv2Report_1.type    Value=143    MaxValue=143
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv2Report_1.reserved2    Value=20    MaxValue=20
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mldv2Report_1.numberOfGroupRecords    Value=2    MaxValue=2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv6_Packet_Too_Big
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 packet too big报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 packet too big头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    packettoobig
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 packet too big头部
    edit_header_icmpv6_packet_too_big    Stream=${Stream}    Level=0    Mtu=500    FlowLabel=1111    HopLimit=255    Source=2020::2    Gateway=2020::1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=packetTooBig_1.headerData.ipv6Header.hopLimit    Value=255    MaxValue=255
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=packetTooBig_1.headerData.ipv6Header.source    Value=2020::2    MaxValue=2020::2
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=packetTooBig_1.mtu    Value=500    MaxValue=500
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv6_Parameter_Problem
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 parameter problem报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 parameter problem头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    icmpv6parameterproblem
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 parameter problem头部
    edit_header_icmpv6_parameter_problem    Stream=${Stream}    Level=0    Pointer=00000011    FlowLabel=1111    HopLimit=255    Source=2020::2    Gateway=2020::1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv6ParameterProblem_1.headerData.ipv6Header.hopLimit    Value=255    MaxValue=255
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv6ParameterProblem_1.headerData.ipv6Header.source    Value=2020::2    MaxValue=2020::2
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Icmpv6ParameterProblem_1.pointer    Value=00000011    MaxValue=00000011
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ICMPv6_Time_Exceed
    [Documentation]    测试目的 : 检查测试仪表发icmpv6 time exceed报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的icmpv6 time exceed头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ICMPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    timeexceed
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改icmpv6 time exceed头部
    edit_header_icmpv6_time_exceed    Stream=${Stream}    Level=0    Code=1    Reserve=11
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timeExceed_1.reserve    Value=11    MaxValue=11
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=timeExceed_1.code    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_IGMPv1_Query
    [Documentation]    测试目的 : 检查测试仪表发igmpv1 query报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的igmpv1 query头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IGMPv1
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    igmpv1query
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改igmpv1 query头部
    edit_header_igmpv1_query    Stream=${Stream}    Level=0    Type=99    Unused=255    Checksum=ffff    GroupAddress=10.1.1.1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1Query_1.type    Value=99    MaxValue=99
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1Query_1.unused    Value=255    MaxValue=255
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1Query_1.checksum    Value=ffff    MaxValue=ffff
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_IGMPv1_Report
    [Documentation]    测试目的 : 检查测试仪表发igmpv1 report报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的igmpv1 report头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IGMPv1
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    igmpv1
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改igmpv1 report头部
    edit_header_igmpv1_report    Stream=${Stream}    Level=0    Type=99    Unused=255    Checksum=ffff    GroupAddress=10.1.1.1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1_1.type    Value=99    MaxValue=99
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1_1.Unused    Value=255    MaxValue=255
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1_1.groupAddress    Value=10.1.1.1    MaxValue=10.1.1.1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_IGMPv2_Query
    [Documentation]    测试目的 : 检查测试仪表发igmpv2 query报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的igmpv2 query头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IGMPv2
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    IGMPv2Query
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改igmpv2 query头部
    edit_header_igmpv2_query    Stream=${Stream}    Level=0    Type=99    MaxResponseTime=255    Checksum=ffff    GroupAddress=10.1.1.1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv2_1.type    Value=99    MaxValue=99
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv2_1.maxResponseTime    Value=255    MaxValue=255
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv2_1.groupAddress    Value=10.1.1.1    MaxValue=10.1.1.1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_IGMPv2_Report
    [Documentation]    测试目的 : 检查测试仪表发igmpv2 report报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的igmpv2 report头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IGMPv2
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    igmpv2
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改igmpv2 report头部
    edit_header_igmpv2_report    Stream=${Stream}    Level=0    Type=99    MaxResponseTime=255    Checksum=ffff    GroupAddress=10.1.1.1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1_1.type    Value=99    MaxValue=99
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1_1.MaxResponseTime    Value=255    MaxValue=255
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv1_1.groupAddress    Value=10.1.1.1    MaxValue=10.1.1.1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_IGMPv3_Query
    [Documentation]    测试目的 : 检查测试仪表发igmpv3 query报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的igmpv3 query头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IGMPv3
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    igmpv3query
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改igmpv3 query头部
    edit_header_igmpv3_query    Stream=${Stream}    Level=0    Type=99    MaxResponseTime=255    Checksum=ffff    GroupAddress=10.1.1.1    SuppressFlag=1    Qrv=111    Qqic=255    NumberOfSources=65535
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv3Query_1.type    Value=99    MaxValue=99
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv3Query_1.MaxResponseTime    Value=255    MaxValue=255
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv3Query_1.groupAddress    Value=10.1.1.1    MaxValue=10.1.1.1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_IGMPv3_Report
    [Documentation]    测试目的 : 检查测试仪表发igmpv3 report报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的igmpv3 report头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IGMPv3
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    igmpv3report
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改igmpv3 report头部
    edit_header_igmpv3_report    Stream=${Stream}    Level=0    Type=99    Reserved1=ff    Checksum=ffff    NumGroupRecords=65535
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv3Report_1.type    Value=99    MaxValue=99
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv3Report_1.Checksum    Value=ffff    MaxValue=ffff
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=igmpv3Report_1.Reserved1    Value=ff    MaxValue=ff
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_IPv4
    [Documentation]    测试目的 : 检查测试仪表发ipv4报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv4头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    IPv4
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 创建列表
    ${HeaderOption}    Create List    Security    RouterAlert
    # 修改ipv4头部
    edit_header_ipv4    Stream=${Stream}    Level=0    TTL=200    Source=10.1.1.2    Destination=20.1.1.2    Flags=111    HeaderOption=${HeaderOption}
    # 修改ipv4头部，添加一个Security
    edit_header_ipv4_option    Stream=${Stream}    Index=0    Option=Security    Security=1
    # 修改ipv4头部，添加一个RouterAlert
    edit_header_ipv4_option    Stream=${Stream}    Index=1    Option=RouterAlert    Length=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv4_1.ttl    Value=200    MaxValue=200
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv4_1.ipv4HeaderOption.ipv4HeaderOptionList_0.optionSecurity.security    Value=1    MaxValue=1
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv4_1.ipv4HeaderOption.ipv4HeaderOptionList_1.optionRouterAlert.length    Value=10    MaxValue=10
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_IPv6
    [Documentation]    测试目的 : 检查测试仪表发ipv6报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv6头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    IPv6
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    ipv6fragmentheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ipv6头部
    edit_header_ipv6    Stream=${Stream}    Level=0    HopLimit=255    Source=2022::2    Destination=2020::2    Gateway=2022::1
    # 修改ipv6 fragment头部
    edit_header_ipv6_fragment    Stream=${Stream}    NextHeader=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6_1.hopLimit    Value=255    MaxValue=255
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6_1.source    Value=2022::2    MaxValue=2022::2
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6_1.destination    Value=2020::2    MaxValue=2020::2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_OSPFv2_Database_Description
    [Documentation]    测试目的 : 检查测试仪表发ospfv2 database description报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ospfv2 database description头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    OSPFv2
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    ospfv2databasedescription
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ospfv2 database description头部
    edit_header_ospfv2_dd    Stream=${Stream}    Level=0    RouterID=2.2.2.2    AuthType=SimplePassword    AuthValue1=123    AuthValue2=456    PacketOptionsDcBit=1    DdOptionsReserved3=1    SequenceNumber=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2DatabaseDescription_1.ddOptions.dcBit    Value=1    MaxValue=1
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2DatabaseDescription_1.ospfHeader.authSelect.hdrAuthSelectNone.authValue2    Value=456    MaxValue=456
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2DatabaseDescription_1.sequenceNumber    Value=10    MaxValue=10
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_Ospfv2Update_RouteLsa
    [Documentation]    测试目的 : 检查测试仪表发ospfv2 link state update报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ospfv2 link state update头部内容;
    ...
    ...    测试步骤3: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤4: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤5: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    OSPFv2
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    Ospfv2LinkstateUpdate
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    ${LsaHeaders}    Create List    Router
    # 修改ospfv2 link state update头部，添加一个Router LSA
    edit_header_ospfv2_update    Stream=${Stream}    RouterID=10.1.1.2    AreaID=10.1.1.2    AuthValue2=2    LsaHeaders=${LsaHeaders}
    # 修改ospfv2 link state update头部，Router LSA内容，并添加4个Lsa Link即RouterLsaLinkCount=4
    edit_header_ospfv2_update_lsa    Stream=${Stream}    Index=0    Type=Router    LinkStateId=10.1.0.1    AdvertisingRouter=10.1.0.2    RouterLsaLinkCount=4    eBitRouter=1
    # 修改ospfv2 link state update头部，Router LSA中，第一个RouterLsaLinkCount内容即Index=0
    edit_header_ospfv2_update_route_lsa_link    Stream=${Stream}    LsaIndex=0    Index=0    LinkStateId=10.1.0.1    LinkData=255.255.255.255    RouterLsaLinkType=3    NumRouterLsaTosMetrics=10
    # 修改ospfv2 link state update头部，Router LSA中，第二个RouterLsaLinkCount内容即Index=1
    edit_header_ospfv2_update_route_lsa_link    Stream=${Stream}    LsaIndex=0    Index=1    LinkStateId=10.2.0.1    LinkData=255.255.255.255    RouterLsaLinkType=2    NumRouterLsaTosMetrics=10
    # 修改ospfv2 link state update头部，Router LSA中，第三个RouterLsaLinkCount内容即Index=2
    edit_header_ospfv2_update_route_lsa_link    Stream=${Stream}    LsaIndex=0    Index=2    LinkStateId=10.3.0.1    LinkData=255.255.255.255    RouterLsaLinkType=1    NumRouterLsaTosMetrics=10
    # 修改ospfv2 link state update头部，Router LSA中，第四个RouterLsaLinkCount内容即Index=3
    edit_header_ospfv2_update_route_lsa_link    Stream=${Stream}    LsaIndex=0    Index=3    LinkStateId=10.4.0.1    LinkData=255.255.255.255    RouterLsaLinkType=4    NumRouterLsaTosMetrics=10
    [Teardown]    teardown

Header_OSPFv2_Hello
    [Documentation]    测试目的 : 检查测试仪表发ospfv2 hello报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ospfv2 hello头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    OSPFv2
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    ospfv2hello
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ospfv2 hello头部
    edit_header_ospfv2_hello    Stream=${Stream}    Level=0    RouterID=2.2.2.2    AuthType=MD5    NetworkMask=255.255.255.0    RouterDeadInterval=50
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2Hello_1.networkMask    Value=255.255.255.0    MaxValue=255.255.255.0
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2Hello_1.ospfHeader.routerID    Value=2.2.2.2    MaxValue=2.2.2.2
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2Hello_1.routerDeadInterval    Value=50    MaxValue=50
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_OSPFv2_Link_State_Acknowledge
    [Documentation]    测试目的 : 检查测试仪表发ospfv2 link state acknowledge报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ospfv2 link state acknowledge头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    OSPFv2
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    ospfv2linkstateacknowledge
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ospfv2 link state acknowledge头部
    edit_header_ospfv2_ack    Stream=${Stream}    Level=0    RouterID=2.2.2.2    AuthType=MD5
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2LinkStateAcknowledge_1.ospfHeader.routerID    Value=2.2.2.2    MaxValue=2.2.2.2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_OSPFv2_Link_State_Request
    [Documentation]    测试目的 : 检查测试仪表发ospfv2 link state request报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ospfv2 link state request头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    OSPFv2
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    ospfv2linkstaterequest
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ospfv2 link state request头部
    edit_header_ospfv2_request    Stream=${Stream}    Level=0    RouterID=2.2.2.2    AuthType=MD5
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2LinkStateRequest_1.ospfHeader.routerID    Value=2.2.2.2    MaxValue=2.2.2.2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_OSPFv2_Unknown
    [Documentation]    测试目的 : 检查测试仪表发ospfv2 unknown报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ospfv2 unknown头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    OSPFv2
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    ospfv2unknown
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ospfv2 link state request头部
    edit_header_ospfv2_unknown    Stream=${Stream}    Level=0    RouterID=2.2.2.2    AuthType=MD5    AuthValue1=111
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=Ospfv2Unknown_1.ospfHeader.authSelect.hdrAuthSelectNone.authValue1    Value=111    MaxValue=111
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_PPP
    [Documentation]    测试目的 : 检查测试仪表发ppp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ppp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    PPP
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    ppp
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ppp头部
    edit_header_ppp    Stream=${Stream}    Level=0    Protocol=0001
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ppp_1.protocol    Value=0001    MaxValue=0001
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Custom
    [Documentation]    测试目的 : 检查测试仪表发custom报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的custom头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    Custom
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    custom
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 添加一个Pattern头，一个Checksum头并修改
    edit_header_custom    Stream=${Stream}    Pattern=1212121212    Checksum=Auto
    # 添加一个Pattern头，一个Checksum头并修改
    edit_header_custom    Stream=${Stream}    Pattern=0343434343    Checksum=Auto
    # 添加一个Pattern头，一个Checksum头并修改
    edit_header_custom    Stream=${Stream}    Pattern=2323232323    Checksum=Auto
    # 修改custom头部，第一个Pattern内容即Index=0
    edit_header_custom    Stream=${Stream}    Index=0    Pattern=0565656565
    # 修改custom头部，第二个Pattern内容即Index=2
    edit_header_custom    Stream=${Stream}    Index=2    Pattern=0787878787
    [Teardown]    teardown

Header_Vlan
    [Documentation]    测试目的 : 检查测试仪表发vlan报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的vlan头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    Vlan
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    vlan
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改vlan头部
    edit_header_vlan    Stream=${Stream}    Level=0    ID=100    Priority=5    CFI=1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=vlan_1.cfi    Value=1    MaxValue=1
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=vlan_1.id    Value=100    MaxValue=100
    ${pdu_pattern_3}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=vlan_1.priority    Value=5    MaxValue=5
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2} && ${pdu_pattern_3}
    [Teardown]    teardown

Header_ARP
    [Documentation]    测试目的 : 检查测试仪表发arp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的arp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    ARP
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    ARP
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改arp头部
    edit_header_arp    Stream=${Stream}    Level=0    SendMac=00:00:00:00:00:01    SendIpv4=192.168.0.2    TargetIpv4=192.168.0.1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=arp_1.sendIpv4    Value=192.168.0.2    MaxValue=192.168.0.2
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=arp_1.sendMac    Value=00:00:00:00:00:01    MaxValue=00:00:00:00:00:01
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_EthernetII
    [Documentation]    测试目的 : 检查测试仪表发ethernetii报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ethernetii头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    EthernetII
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改EthernetII头部
    edit_header_ethernet    Stream=${Stream}    Level=0    DestMacAdd=00:00:00:00:00:01    SourceMacAdd=00:00:00:00:00:02
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ethernetII_1.sourceMacAdd    Value=00:00:00:00:00:02    MaxValue=00:00:00:00:00:02
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ethernetII_1.destMacAdd    Value=00:00:00:00:00:01    MaxValue=00:00:00:00:00:01
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_Ethernet_Raw_8023
    [Documentation]    测试目的 : 检查测试仪表发ethernet Raw 802.3报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ethernet Raw 802.3头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    EthernetII
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    Raw
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改EthernetII头部
    edit_header_raw_8023    Stream=${Stream}    Level=0    DestMacAdd=00:00:00:00:00:01    SourceMacAdd=00:00:00:00:00:02
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=raw_1.sourceMacAdd    Value=00:00:00:00:00:02    MaxValue=00:00:00:00:00:02
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=raw_1.destMacAdd    Value=00:00:00:00:00:01    MaxValue=00:00:00:00:00:01
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_MPLS
    [Documentation]    测试目的 : 检查测试仪表发mpls报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的mpls头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    MPLS
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    mpls
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改mpls头部
    edit_header_mpls    Stream=${Stream}    Level=0    Label=32    TTL=200
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mpls_1.label    Value=32    MaxValue=32
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mpls_1.ttl    Value=200    MaxValue=200
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_PPPoE
    [Documentation]    测试目的 : 检查测试仪表发pppoe报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的pppoe头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    PPPoE
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    pppoe
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改pppoe头部
    edit_header_pppoe    Stream=${Stream}    Level=0    Code=11    SessionId=2
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=pppoe_1.code    Value=11    MaxValue=11
    ${pdu_pattern_2}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=pppoe_1.sessionId    Value=2    MaxValue=2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1} && ${pdu_pattern_2}
    [Teardown]    teardown

Header_GRE
    [Documentation]    测试目的 : 检查测试仪表发gre报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的gre头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IPv4    GRE
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    gre
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改gre头部
    ${header}    edit_header_gre    Stream=${Stream}    Level=0    ChecksumPresent=1    Routing=1    Protocol=IPv4    Checksum=10    SequenceNumber=2    Key=1
    # 设置跳变
    ${attr}    get from dictionary    ${header}    Checksum
    edit_modifier    Stream=${Stream}    HeaderType=gre    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=gre_1.routing    Value=1    MaxValue=1
    # \ \ \ ${pdu_pattern_2} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=gre_1.checksum.GreChecksum_0.checksum \ \ \ Value=123 \ \ \ MaxValue=123
    # \ \ \ ${pdu_pattern_3} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=gre_1.sequenceNumber.GreSequenceNumber_0.sequenceNumber \ \ \ Value=2 \ \ \ MaxValue=2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_L2TPv2_Data
    [Documentation]    测试目的 : 检查测试仪表发l2tpv2 data报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的l2tpv2 data头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IPv4    UDP    L2TPv2Data
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    UDP    L2TPv2Data
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l2tpv2 data头部
    ${header}    edit_header_l2tpv2_data    Stream=${Stream}    Level=0    Type=1    LengthOption=2
    # 设置跳变
    ${attr}    get from dictionary    ${header}    LengthOption
    edit_modifier    Stream=${Stream}    HeaderType=L2TPv2Data    Attribute=${attr}    Type=Increment    Count=10
    ${header_option}    edit_header_l2tpv2_data_option    Stream=${Stream}    Level=0    Ns=1    Nr=2    Value=102030
    ${attr}    get from dictionary    ${header_option}    Ns
    edit_modifier    Stream=${Stream}    HeaderType=L2TPv2Data    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=l2tpv2Data_1.type    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    # 订阅StreamBlockStats统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats
    subscribe_result    Types=${SubscribeTypes}
    # 设置端口发送模式为突发包
    edit_port_load_profile    Ports=${Ports[1]}    TransmitMode=BURST    BurstCount=100
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    start_stream
    sleep    10
    stop_stream
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    [Teardown]    teardown

Header_L2TPv2_Control
    [Documentation]    测试目的 : 检查测试仪表发l2tpv2 control报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的l2tpv2 control头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IPv4    UDP    L2TPv2Control
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    UDP    l2tpv2Control
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l2tpv2 control头部
    ${header}    edit_header_l2tpv2_control    Stream=${Stream}    Level=0    Type=1    Reserved1=11    Ns=5    Nr=6
    # 设置跳变
    ${attr}    get from dictionary    ${header}    Nr
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv2Control    Attribute=${attr}    Type=Increment    Count=10
    # 修改l2tpv2 control头部，添加一个Option头部
    ${header_option}    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=0    Types=generalTLV    AttributeValue=11
    ${attr}    get from dictionary    ${header_option}    AttributeValue
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv2Control    Attribute=${attr}    Type=Increment    Count=10
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=1    Types=messageType    MessageType=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=2    Types=resultCode    ErrorCode=1    ErrorMessage=01
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=3    Types=protocolVersion    Ver=1    Rev=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=4    Types=framingCapabilities    Abit=1    Sbit=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=5    Types=bearerCapabilities    Abit=1    Dbit=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=6    Types=tieBreaker    TieBreakerValue=0000000000000001
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=7    Types=firmwareRevision    FirmwareRevision=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=8    Types=assignedTunnelId    TunnelId=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=9    Types=receiveWindowSize    WindowSize=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=10    Types=assignedSessionId    SessionId=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=11    Types=response    ResponseValue=00000000000000000000000000000001
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=12    Types=callSerialNumber    CallSerialNumber=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=13    Types=minimumBps    MinimumBps=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=14    Types=maximumBps    MaximumBps=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=15    Types=bearerType    Abit=1    Dbit=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=16    Types=framingType    Abit=1    Sbit=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=17    Types=txConnectSpeed    Bps=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=18    Types=rxConnectSpeed    HighBPS=1    LowBPS=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=19    Types=physicalChannelId    PhysicalChannelId=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=20    Types=proxyAuthenType    AuthenType=1
    # 修改l2tpv2 control头部，再添加一个Option头部
    edit_header_l2tpv2_control_option    Stream=${Stream}    Level=0    Index=21    Types=proxyAuthenId    AuthenId=1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=l2tpv2Control_1.ns    Value=5    MaxValue=5
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_L2TPv3_Control_Over_Ip
    [Documentation]    测试目的 : 检查测试仪表发l2tpv3 control over ip报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的l2tpv3 control over ip头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IPv4    L2TPv3ControlOverIp
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    l2tpv3ControlOverIp
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l2tpv3 control over ip头部
    ${header}    edit_header_l2tpv3_control_over_ip    Stream=${Stream}    Level=0    SessionId=1    Type=1    UseLength=1    ExcludeSessionLength=1
    # 设置跳变
    ${attr}    get from dictionary    ${header}    ExcludeSessionLength
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv3ControlOverIp    Attribute=${attr}    Type=Increment    Count=10
    # 修改l2tpv3 control over ip头部，添加一个Option头部
    ${header_option}    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=0    Types=generalTLV    AttributeValue=11
    ${attr}    get from dictionary    ${header_option}    AttributeValue
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv3ControlOverIp    Attribute=${attr}    Type=Increment    Count=10
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=1    Types=messageType    MessageType=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=2    Types=resultCode    ErrorCode=1    ErrorMessage=01
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=3    Types=tieBreaker    TieBreakerValue=0000000000000001
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=4    Types=receiveWindowSize    WindowSize=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=5    Types=callSerialNumber    CallSerialNumber=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=6    Types=physicalChannelId    PhysicalChannelId=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=7    Types=circuitError    AlignmentOverruns=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=8    Types=routeId    RouteId=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=9    Types=assignedConnection    ConnectionId=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=10    Types=localSessionId    SessionId=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=11    Types=remoteSessionId    SessionId=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=12    Types=assignedCookie    Cookie4Byte=00000001
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=13    Types=pwType    PwType=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=14    Types=l2SpecificSub    L2SpecificSublayer=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=15    Types=dataSequencing    DataSequencing=1
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=16    Types=txConnectSpeed    SpeedBps=0000000000000001
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=17    Types=rxConnectSpeed    SpeedBps=0000000000000001
    # 修改l2tpv3 control over ip头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=18    Types=circuitStatus    Nbit=1    Abit=1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=l2tpv3ControlOverIp_1.type    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_L2TPv3_Control_Over_Udp
    [Documentation]    测试目的 : 检查测试仪表发l2tpv3 control over udp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的l2tpv3 control over udp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IPv4    UDP    L2TPv3ControlOverUdp
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    UDP    l2tpv3ControlOverUdp
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l2tpv3 control over udp头部
    ${header}    edit_header_l2tpv3_control_over_udp    Stream=${Stream}    Level=0    Type=1    UseLength=1    Length=1
    # 设置跳变
    ${attr}    get from dictionary    ${header}    Length
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv3ControlOverUdp    Attribute=${attr}    Type=Increment    Count=10
    # 修改l2tpv3 control over udp头部，添加一个Option头部
    ${header_option}    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=0    Types=generalTLV    AttributeValue=11
    ${attr}    get from dictionary    ${header_option}    AttributeValue
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv3ControlOverUdp    Attribute=${attr}    Type=Increment    Count=10
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=1    Types=messageType    MessageType=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=2    Types=resultCode    ErrorCode=1    ErrorMessage=01
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=3    Types=tieBreaker    TieBreakerValue=0000000000000001
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=4    Types=receiveWindowSize    WindowSize=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=5    Types=callSerialNumber    CallSerialNumber=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=6    Types=physicalChannelId    PhysicalChannelId=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=7    Types=circuitError    AlignmentOverruns=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=8    Types=routeId    RouteId=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=9    Types=assignedConnection    ConnectionId=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=10    Types=localSessionId    SessionId=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=11    Types=remoteSessionId    SessionId=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=12    Types=assignedCookie    Cookie4Byte=00000001
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=13    Types=pwType    PwType=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=14    Types=l2SpecificSub    L2SpecificSublayer=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=15    Types=dataSequencing    DataSequencing=1
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=16    Types=txConnectSpeed    SpeedBps=0000000000000001
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=17    Types=rxConnectSpeed    SpeedBps=0000000000000001
    # 修改l2tpv3 control over udp头部，再添加一个Option头部
    edit_header_l2tpv3_control_option    Stream=${Stream}    Level=0    Index=18    Types=circuitStatus    Nbit=1    Abit=1
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=l2tpv3ControlOverUdp_1.type    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_L2TPv3_Data_Over_Ip
    [Documentation]    测试目的 : 检查测试仪表发l2tpv3 data over ip报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的l2tpv3 data over ip头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-003    IPv4    l2tpv3DataOverIp
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    l2tpv3DataOverIp
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l2tpv3 data over ip头部
    ${Atmspecificsublayer}    Create Dictionary    xbit=1    ebit=1    gbit=1
    ${header}    Edit Header L2tpv3 Data Over Ip    Stream=${Stream}    Level=0    SessionId=1    Cookie8Byte=0000000000000001    Atmspecificsublayer=1
    # 设置跳变
    ${attr}    get from dictionary    ${header}    Cookie8Byte
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv3DataOverIp    Attribute=${attr}    Type=Increment    Count=10
    # 修改l2tpv3 data over ip头部选项
    ${header_option}    edit_header_l2tpv3_data_sublayer    Stream=${Stream}    Type=Atmspecificsublayer    Xbit=1    Sequence=10
    ${attr}    get from dictionary    ${header_option}    Sequence
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv3DataOverIp    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=l2tpv3DataOverIp_1.sessionId    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_L2TPv3_Data_Over_Udp
    [Documentation]    测试目的 : 检查测试仪表发l2tpv3 data over udp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的l2tpv3 data over udp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Stream    Header    IPv4    UDP    l2tpv3DataOverUdp
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    UDP    l2tpv3DataOverUdp
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l2tpv3 data over udp头部
    ${Atmspecificsublayer}    Create Dictionary    xbit=1    ebit=1    gbit=1
    ${header}    Edit Header L2tpv3 Data Over Udp    Stream=${Stream}    Level=0    SessionId=1    Cookie8Byte=0000000000000001    Atmspecificsublayer=1
    # 设置跳变
    ${attr}    get from dictionary    ${header}    Cookie8Byte
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv3DataOverUdp    Attribute=${attr}    Type=Increment    Count=10
    # 修改l2tpv3 data over ip头部选项
    ${header_option}    edit_header_l2tpv3_data_sublayer    Stream=${Stream}    Type=Atmspecificsublayer    Xbit=1    Sequence=10
    ${attr}    get from dictionary    ${header_option}    Sequence
    edit_modifier    Stream=${Stream}    HeaderType=l2tpv3DataOverUdp    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=l2tpv3DataOverUdp_1.sessionId    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_DHCPv4_Server
    [Documentation]    测试目的 : 检查测试仪表发dhcpv4 server报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的dhcpv4 server头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Stream    Header    IPv4    UDP    dhcpv4Server
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    UDP    dhcpv4Server
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改dhcpv4 server头部
    ${header}    edit_header_dhcpv4_server    Stream=${Stream}    Level=0    MessageType=1    HardwareType=1    Hops=1    Bootpflags=0001
    # 设置跳变
    ${attr}    get from dictionary    ${header}    Bootpflags
    edit_modifier    Stream=${Stream}    HeaderType=dhcpv4Server    Attribute=${attr}    Type=Increment    Count=10
    # 修改dhcpv4 server 头部，添加一个Option头部
    ${header_option}    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=0    Types=serverId    ReqAddr=1.1.1.1
    ${attr}    get from dictionary    ${header_option}    ReqAddr
    edit_modifier    Stream=${Stream}    HeaderType=dhcpv4Server    Attribute=${attr}    Type=Increment    Count=10
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=1    Types=message    Value=01
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=2    Types=leaseTime    LeaseTime=1
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=3    Types=endOfOptions    Type=01
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=4    Types=messageSize    Value=01
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=5    Types=clientIdHW    IdType=01    ClientHWA=00:00:00:00:00:01
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=6    Types=clientIdNoneHW    IdType=01    Value=01
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=7    Types=hostName    Value=01
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=8    Types=paramReqList    Value=01
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=9    Types=reqAddr    ReqAddr=1.1.1.1
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=10    Types=optionOverload    Overload=1
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=11    Types=customOption    Overload=01
    # 修改dhcpv4 server 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=12    Types=generalTLV    Value=01
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=dhcpv4Server_1.hops    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    # 订阅StreamBlockStats统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats
    subscribe_result    Types=${SubscribeTypes}
    [Teardown]    teardown

Header_DHCPv4_Client
    [Documentation]    测试目的 : 检查测试仪表发dhcpv4 client报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的dhcpv4 client头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Stream    Header    IPv4    UDP    dhcpv4Client
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv4    UDP    dhcpv4Client
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改dhcpv4 client头部
    ${header}    edit_header_dhcpv4_client    Stream=${Stream}    Level=0    MessageType=1    HardwareType=1    Hops=1    Bootpflags=0001
    # 设置跳变
    ${attr}    get from dictionary    ${header}    MessageType
    edit_modifier    Stream=${Stream}    HeaderType=dhcpv4Client    Attribute=${attr}    Type=Increment    Count=10
    # 修改dhcpv4 client 头部，添加一个Option头部
    ${header_option}    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=0    Types=serverId    ReqAddr=1.1.1.1
    ${attr}    Get From Dictionary    ${header_option}    ReqAddr
    edit_modifier    Stream=${Stream}    HeaderType=dhcpv4Client    Attribute=${attr}    Type=Increment    Count=10
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=1    Types=message    Value=01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=2    Types=leaseTime    LeaseTime=1
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=3    Types=endOfOptions    Type=01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=4    Types=messageSize    Value=01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=5    Types=clientIdHW    IdType=01    ClientHWA=00:00:00:00:00:01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=6    Types=clientIdNoneHW    IdType=01    Value=01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=7    Types=hostName    Value=01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=8    Types=paramReqList    Value=01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=9    Types=reqAddr    ReqAddr=1.1.1.1
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=10    Types=optionOverload    Overload=1
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=11    Types=customOption    Overload=01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=12    Types=generalTLV    Value=01
    # 修改dhcpv4 client 头部，添加一个Option头部
    edit_header_dhcpv4_option    Stream=${Stream}    Level=0    Index=13    Types=messageType    Code=4
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=dhcpv4Client_1.hops    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_DHCPv6_Client
    [Documentation]    测试目的 : 检查测试仪表发dhcpv6 client报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的dhcpv6 client头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Stream    Header    IPv6    UDP    dhcpv6Client
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    UDP    dhcpv6Client
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 将IaOption以字典方式传入
    ${IaOptionone}    Create Dictionary    type=5    length=5    ipv6Address=2020::1    preferredLifetime=1    validLifetime=1
    ${IaOptiontwo}    Create Dictionary    type=7    length=7    preferredLifetime=1    validLifetime=1    prefixLength=128    ipv6Address=2022::3
    # 修改dhcpv6 client头部
    ${header}    edit_header_dhcpv6_client    Stream=${Stream}    Level=0    MessageType=2    TransId=2
    # 设置跳变
    ${attr}    Get From Dictionary    ${header}    TransId
    edit_modifier    Stream=${Stream}    HeaderType=dhcpv6Client    Attribute=${attr}    Type=Increment    Count=10
    # 修改dhcpv6 client 头部，添加一个Option头部
    ${header_option}    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=0    Types=clientIdOption    Duid=01
    ${attr}    Get From Dictionary    ${header_option}    Duid
    edit_modifier    Stream=${Stream}    HeaderType=dhcpv6Client    Attribute=${attr}    Type=Increment    Count=10
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=1    Types=serverIdOption    DuidType=2    HardwareType=2    LinkAddress=00:00:00:00:00:02
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=2    Types=ianaOption    Iaid=00000003    T1=3    T2=3    IaOption=1
    edit_header_dhcpv6_option_ia_address    Stream=${Stream}    Level=0    Index=2    Type=5    Length=5    Ipv6Address=2020::1    PreferredLifetime=1    ValidLifetime=1
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=3    Types=requestOption    Value=04
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=4    Types=elapsedTimeOption    ElapseTime=5
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=5    Types=serverUnicastOption    ServerAddress=2022::1
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=6    Types=statusCodeOption    StatusCode=7    StatusMsg=0000000007
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=7    Types=rapidCommitOption    Length=8
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=8    Types=interfaceIdOption    InterfaceId=0000000009
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=9    Types=reconfigureAcceptOption    Type=10
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=10    Types=iapdOption    Iaid=00000011    T1=11    T2=11    IaOption=1
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=11    Types=customOption    Value=12
    # 修改dhcpv6 client 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=12    Types=generalTLV    Value=13
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=dhcpv6Client_1.messageType    Value=2    MaxValue=2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_DHCPv6_Server
    [Documentation]    测试目的 : 检查测试仪表发dhcpv6 server报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的dhcpv6 server头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Stream    Header    IPv6    UDP    dhcpv6Server
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    UDP    dhcpv6Server
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 将IaOption以字典方式传入
    ${IaOptionone}    Create Dictionary    type=5    length=5    ipv6Address=2020::1    preferredLifetime=1    validLifetime=1
    ${IaOptiontwo}    Create Dictionary    type=7    length=7    preferredLifetime=1    validLifetime=1    prefixLength=128    ipv6Address=2022::3
    # 修改dhcpv6 server头部
    ${header}    edit_header_dhcpv6_server    Stream=${Stream}    Level=0    MessageType=2    TransId=2
    # 设置跳变
    ${attr}    Get From Dictionary    ${header}    TransId
    edit_modifier    Stream=${Stream}    HeaderType=dhcpv6Server    Attribute=${attr}    Type=Increment    Count=10
    # 修改dhcpv6 server 头部，添加一个Option头部
    ${header_option}    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=0    Types=clientIdOption    Duid=01
    ${attr}    Get From Dictionary    ${header_option}    Duid
    edit_modifier    Stream=${Stream}    HeaderType=dhcpv6Server    Attribute=${attr}    Type=Increment    Count=10
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=1    Types=serverIdOption    DuidType=2    HardwareType=2    LinkAddress=00:00:00:00:00:02
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=2    Types=ianaOption    Iaid=00000003    T1=3    T2=3    IaOption=1
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=3    Types=requestOption    Value=04
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=4    Types=elapsedTimeOption    ElapseTime=5
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=5    Types=serverUnicastOption    ServerAddress=2022::1
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=6    Types=statusCodeOption    StatusCode=7    StatusMsg=0000000007
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=7    Types=rapidCommitOption    Length=8
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=8    Types=interfaceIdOption    InterfaceId=0000000009
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=9    Types=reconfigureAcceptOption    Type=10
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=10    Types=iapdOption    Iaid=00000011    T1=11    T2=11    IaOption=1
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=11    Types=customOption    Value=12
    # 修改dhcpv6 server 头部，添加一个Option头部
    edit_header_dhcpv6_option    Stream=${Stream}    Level=0    Index=12    Types=generalTLV    Value=13
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=dhcpv6Server_1.messageType    Value=2    MaxValue=2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS-L1_CSNP_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS-L1_CSNP_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS-L1_CSNP_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS-L1_CSNP_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    l1csnpheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l1csnpheader头部
    @{CsnpDataTlvOptionHeader}    Create List    IsIsLspEntries    AuthentionInfo
    Edit Header Isis Csnp    Stream=${Stream}    CsnpDataTlvOptionHeader=${CsnpDataTlvOptionHeader}
    Edit Header Isis Tlv Header    Stream=${stream}    Option=IsIsLspEntries    LspEntries=${2}
    Edit Header Isis Lsp Entry    Stream=${Stream}    TlvIndex=0    LspIndex=1    RemainTime=10
    # 配置过滤抓包
    # \ \ \ ${pdu_pattern_1} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime \ \ \ Value=10 \ \ \ MaxValue=10
    # \ \ \ edit_capture_filter \ \ \ Port=${Ports[1]} \ \ \ Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS-L1_Hello_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS-L1_Hello_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS-L1_Hello_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS-L1_Hello_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    isisl1helloheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l1csnpheader头部
    @{isIsTlv}    Create List    IsIsAreaAddress    Padding    AuthentionInfo    ProtocolSupport    IpInterfaceAddress    Neighbor    RestartSignal    Ipv6InterfaceAddress
    Edit Header Isis L1l2 Hello    Stream=${Stream}    IsIsTlv=${isIsTlv}
    Edit Header Isis Tlv Header    Stream=${stream}    Option=IsIsAreaAddress    AreaAddressEntries=${2}
    # \ \ \ Edit Header Isis Area Address Entry \ \ \ Stream=${Stream} \ \ \ TlvIndex=${0} \ \ \ InEntrydex=${1}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=Padding    Index=${1}    TlvLength=${10}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=AuthentionInfo    Index=${2}    AuthenticationLength=${20}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=ProtocolSupport    Index=${3}    NlPIDEntriesField=${2}
    Edit Header Isis Nlpid Entry    Stream=${Stream}    TlvIndex=${3}    NlpidIndex=${0}    TlvLength=${30}
    # 配置过滤抓包
    # \ \ \ ${pdu_pattern_1} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime \ \ \ Value=10 \ \ \ MaxValue=10
    # \ \ \ edit_capture_filter \ \ \ Port=${Ports[1]} \ \ \ Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS-L1_LSP_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS-L1_LSP_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS-L1_LSP_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS-L1_LSP_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    l1lspheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l1lspheader头部
    @{LspisIsTlvOptionSet}    Create List    IsIsAreaAddress    IsIsReachability    ExtendedReachability    IsIsIpInterReachability    IsIsProtocolsSupported    IsIsIPExternalReachability    IpInterfaceAddress    Ipv6InterfaceAddress    IsIsIpv6Reachability
    Edit Header Isis Lsp    Stream=${Stream}    LspisIsTlvOptionSet=${LspisIsTlvOptionSet}
    Edit Header Isis Tlv Header    Stream=${stream}    Option=IsIsAreaAddress    AreaAddressEntries=${2}
    Edit Header Isis Area Address Entry    Stream=${Stream}    TlvLength=${1}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=IsIsReachability    Index=${1}    MetricEntries=${1}
    Edit Header Isis Metric Entry    Stream=${Stream}    TlvIndex=${1}    EntryIndex=${1}    DefaultMetricIEbit=${1}
    @{iisNeighborSubTlv}    Create List    AdGroupSubtlv    Ipv4InterfaceAddressSubtlv    Ipv4NeighborAddressSubtlv    MaxLinkBandwidthSubtlv    ReservableLinkBandwidthSubtlv    UnReservedBandwidthSubtlv    InterfaceIpv6Subtlv    NeigbhorIpv6Subtlv
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=ExtendedReachability    Index=${2}    IisNeighborSubTlv=${iisNeighborSubTlv}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=AdGroupSubtlv    TlvIndex=${2}    SubTlvIndex=${0}    TlvCode=${20}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=Ipv4InterfaceAddressSubtlv    TlvIndex=${2}    SubTlvIndex=${1}    Ipv4InterfaceAddressValue=1.1.1.1
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=Ipv4NeighborAddressSubtlv    TlvIndex=${2}    SubTlvIndex=${2}    Ipv4NeighborAddressValue=2.2.2.2
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=MaxLinkBandwidthSubtlv    TlvIndex=${2}    SubTlvIndex=${3}    MaxBandwidthValue=${30}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=ReservableLinkBandwidthSubtlv    TlvIndex=${2}    SubTlvIndex=${4}    ReservableLinkBandwidthValue=${40}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=UnReservedBandwidthSubtlv    TlvIndex=${2}    SubTlvIndex=${5}    ResBandwidth0Value=${50}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=InterfaceIpv6Subtlv    TlvIndex=${2}    SubTlvIndex=${6}    InterfaceIpv6Value=2022::2
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=NeigbhorIpv6Subtlv    TlvIndex=${2}    SubTlvIndex=${7}    Neighboripv6Value=2033::3
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=IsIsIpInterReachability    Index=${3}    InternalmetricEntries=${1}
    Edit Header Isis Internal Metric Entry    Stream=${Stream}    TlvIndex=${3}    EntryIndex=${1}    DefaultMetricIEbit=${1}
    @{ipv4InterfaceAddress}    Create List    1.1.1.1    2.2.2.2
    Edit Header Isis Tlv Header    Stream=${stream}    Option=ipInterfaceAddress    Index=${6}    Ipv4InterfaceAddress=${ipv4InterfaceAddress}
    @{ipv6InterfaceAddress}    Create List    2022::2    2033::3
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=Ipv6InterfaceAddress    Index=${7}    Ipv6InterfaceAddress=${ipv6InterfaceAddress}
    # 配置过滤抓包
    # \ \ \ ${pdu_pattern_1} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime \ \ \ Value=10 \ \ \ MaxValue=10
    # \ \ \ edit_capture_filter \ \ \ Port=${Ports[1]} \ \ \ Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS_L1_PSNP_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS_L1_PSNP_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS_L1_PSNP_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS-L1_LSP_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    l1psnpHeader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l1psnpHeader头部
    @{CsnpDataTlvOptionHeader}    Create List    IsIsLspEntries    AuthentionInfo
    Edit Header Isis Psnp    Stream=${Stream}    CsnpDataTlvOptionHeader=${CsnpDataTlvOptionHeader}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=IsIsLspEntries    LspEntries=${2}
    Edit Header Isis Lsp Entry    Stream=${Stream}    TlvIndex=${0}    LspIndex=${1}    RemainTime=${10}
    # 配置过滤抓包
    # \ \ \ ${pdu_pattern_1} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime \ \ \ Value=10 \ \ \ MaxValue=10
    # \ \ \ edit_capture_filter \ \ \ Port=${Ports[1]} \ \ \ Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS-L2_CSNP_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS-L2_CSNP_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS-L2_CSNP_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS-L1_LSP_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    l2csnpheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ISIS-L2_CSNP_Config头部
    @{CsnpDataTlvOptionHeader}    Create List    IsIsLspEntries    AuthentionInfo
    Edit Header Isis Csnp    Stream=${Stream}    CsnpDataTlvOptionHeader=${CsnpDataTlvOptionHeader}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=IsIsLspEntries    LspEntries=${2}
    Edit Header Isis Lsp Entry    Stream=${Stream}    TlvIndex=${0}    LspIndex=${1}    RemainTime=${10}
    # 配置过滤抓包
    # \ \ \ ${pdu_pattern_1} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime \ \ \ Value=10 \ \ \ MaxValue=10
    # \ \ \ edit_capture_filter \ \ \ Port=${Ports[1]} \ \ \ Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS-L2_Hello_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS-L2_Hello_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS-L2_Hello_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS-L2_Hello_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    isisl2helloheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改isisl2helloheader头部
    @{isIsTlv}    Create List    AreaAddress    Padding    AuthentionInfo    ProtocolSupport    IpInterfaceAddress    Neighbor    RestartSignal    Ipv6InterfaceAddress
    Edit Header Isis L1l2 Hello    Stream=${Stream}    IsIsTlv=${isIsTlv}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=areaAddress    AreaAddressEntries=${2}
    Edit Header Isis Area Address Entry    Stream=${Stream}    TlvIndex=${0}    EntryIndex=${1}    AreaAddress=ff
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=Padding    Index=${1}    TlvLength=${10}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=AuthentionInfo    Index=${2}    AuthenticationLength=${20}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=ProtocolSupport    Index=${3}    NlPIDEntriesField=${2}
    Edit Header Isis Nlpid Entry    Stream=${Stream}    TlvIndex=${3}    NlpidIndex=${0}    TlvLength=${30}
    # 配置过滤抓包
    # \ \ \ ${pdu_pattern_1} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime \ \ \ Value=10 \ \ \ MaxValue=10
    # \ \ \ edit_capture_filter \ \ \ Port=${Ports[1]} \ \ \ Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS-L2_LSP_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS-L2_LSP_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS-L2_LSP_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS-L2_LSP_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    l2lspheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l2lspheader头部
    @{LspisIsTlvOptionSet}    Create List    IsIsAreaAddress    IsIsReachability    ExtendedReachability    IsIsIpInterReachability    IsIsProtocolsSupported    IsIsIPExternalReachability    IpInterfaceAddress    Ipv6InterfaceAddress    IsIsIpv6Reachability
    Edit Header Isis Lsp    Stream=${Stream}    LspisIsTlvOptionSet=${LspisIsTlvOptionSet}
    Edit Header Isis Tlv Header    Stream=${stream}    Option=IsIsAreaAddress    AreaAddressEntries=${2}
    Edit Header Isis Area Address Entry    Stream=${Stream}    TlvLength=${1}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=IsIsReachability    Index=${1}    MetricEntries=${1}
    Edit Header Isis Metric Entry    Stream=${Stream}    TlvIndex=${1}    EntryIndex=${1}    DefaultMetricIEbit=${1}
    @{iisNeighborSubTlv}    Create List    AdGroupSubtlv    Ipv4InterfaceAddressSubtlv    Ipv4NeighborAddressSubtlv    MaxLinkBandwidthSubtlv    ReservableLinkBandwidthSubtlv    UnReservedBandwidthSubtlv    InterfaceIpv6Subtlv    NeigbhorIpv6Subtlv
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=extendedReachability    Index=${2}    IisNeighborSubTlv=${iisNeighborSubTlv}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=adGroupSubtlv    TlvIndex=${2}    SubTlvIndex=${0}    TlvCode=${20}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=ipv4InterfaceAddressSubtlv    TlvIndex=${2}    SubTlvIndex=${1}    Ipv4InterfaceAddressValue=1.1.1.1
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=ipv4NeighborAddressSubtlv    TlvIndex=${2}    SubTlvIndex=${2}    Ipv4NeighborAddressValue=2.2.2.2
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=maxLinkBandwidthSubtlv    TlvIndex=${2}    SubTlvIndex=${3}    MaxBandwidthValue=${30}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=ReservableLinkBandwidthSubtlv    TlvIndex=${2}    SubTlvIndex=${4}    ReservableLinkBandwidthValue=${40}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=unReservedBandwidthSubtlv    TlvIndex=${2}    SubTlvIndex=${5}    ResBandwidth0Value=${50}
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=interfaceIpv6Subtlv    TlvIndex=${2}    SubTlvIndex=${6}    InterfaceIpv6Value=2022::2
    Edit Header Isis Sub Tlv    Stream=${Stream}    SubTlv=neigbhorIpv6Subtlv    TlvIndex=${2}    SubTlvIndex=${7}    Neighboripv6Value=2033::3
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=isIsIpInterReachability    Index=${3}    InternalmetricEntries=${1}
    Edit Header Isis Internal Metric Entry    Stream=${Stream}    TlvIndex=${3}    EntryIndex=${1}    DefaultMetricIEbit=${1}
    @{ipv4InterfaceAddress}    Create List    1.1.1.1    2.2.2.2
    Edit Header Isis Tlv Header    Stream=${stream}    Option=ipInterfaceAddress    Index=${6}    Ipv4InterfaceAddress=${ipv4InterfaceAddress}
    @{ipv6InterfaceAddress}    Create List    2022::2    2033::3
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=Ipv6InterfaceAddress    Index=${7}    Ipv6InterfaceAddress=${ipv6InterfaceAddress}
    ## 配置过滤抓包
    # \ \ \ ${pdu_pattern_1} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime \ \ \ Value=10 \ \ \ MaxValue=10
    # \ \ \ edit_capture_filter \ \ \ Port=${Ports[1]} \ \ \ Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS_L2_PSNP_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS_L2_PSNP_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS_L2_PSNP_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS_L2_PSNP_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    l2psnpHeader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l1psnpHeader头部
    @{CsnpDataTlvOptionHeader}    Create List    IsIsLspEntries    AuthentionInfo
    Edit Header Isis Psnp    Stream=${Stream}    CsnpDataTlvOptionHeader=${CsnpDataTlvOptionHeader}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=IsIsLspEntries    LspEntries=${2}
    Edit Header Isis Lsp Entry    Stream=${Stream}    TlvIndex=${0}    LspIndex=${1}    RemainTime=${10}
    # 配置过滤抓包
    # \ \ \ ${pdu_pattern_1} \ \ \ create_capture_pdu_pattern \ \ \ Port=${Ports[1]} \ \ \ HeaderTypes=${HeaderTypes} \ \ \ FieldName=IsIsL1Csnp_1.CsnpDataHeader.CsnpDataTlvOptionHeader.csnpisIsTlvs_0.isIsLspEntries.lspEntries.LSPEntry_0.remainTime \ \ \ Value=10 \ \ \ MaxValue=10
    # \ \ \ edit_capture_filter \ \ \ Port=${Ports[1]} \ \ \ Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_ISIS_P2P_Hello_Config
    [Documentation]    测试目的 : 检查测试仪表发ISIS_P2P_Hello_Config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ISIS_P2P_Hello_Config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-004    ISIS_P2P_Hello_Config
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    p2phelloheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改l1psnpHeader头部
    @{isIsTlv}    Create List    AreaAddress    Padding    AuthentionInfo    ProtocolSupport    IpInterfaceAddress    P2pAdjacencyState    RestartSignal    Ipv6InterfaceAddress
    Edit Header Isis P2p Hello    Stream=${Stream}    IsIsTlv=${isIsTlv}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=AreaAddress    AreaAddressEntries=${1}
    Edit Header Isis Area Address Entry    Stream=${Stream}    TlvIndex=${0}    EntryIndex=${1}    AreaAddress=ff
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=Padding    Index=${1}    TlvLength=${10}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=AuthentionInfo    Index=${2}    AuthenticationLength=${20}
    Edit Header Isis Tlv Header    Stream=${Stream}    Option=ProtocolSupport    Index=${3}    NlPIDEntriesField=${2}
    Edit Header Isis Nlpid Entry    Stream=${Stream}    TlvIndex=${3}    NlpidIndex=${0}    TlvLength=${30}
    [Teardown]    teardown

Header_Tcp
    [Documentation]    测试目的 : 检查测试仪表发tcp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的tcp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    ipv4    tcp
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改tcp头部
    ${header}    edit_header_tcp    Stream=${Stream}    SourcePort=1000    DestPort=2000
    ${attr}    Get From Dictionary    ${header}    SourcePort
    edit_modifier    Stream=${Stream}    HeaderType=tcp    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=tcp_1.destPort    Value=2000    MaxValue=2000
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Udp
    [Documentation]    测试目的 : 检查测试仪表发udp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的udp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    ipv4    udp
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改tcp头部
    ${header}    edit_header_udp    Stream=${Stream}    SourcePort=1000    DestPort=2000
    ${attr}    Get From Dictionary    ${header}    SourcePort
    edit_modifier    Stream=${Stream}    HeaderType=udp    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=udp_1.destPort    Value=2000    MaxValue=2000
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Gtpv1
    [Documentation]    测试目的 : 检查测试仪表发gtpv1报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的gtpv1头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    ipv4    udp    gtpv1    gtpv1opt    gtpv1ext
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改gtpv1头部
    ${gtp}    edit_header_gtpv1    Stream=${Stream}    Teid=10
    ${opt}    edit_header_gtpv1_optional    Stream=${Stream}    Sequence=20
    ${optext}    edit_header_gtpv1_optional_extension    Stream=${Stream}    NPDUNumber=30
    ${attr}    Get From Dictionary    ${gtp}    Teid
    edit_modifier    Stream=${Stream}    HeaderType=gtpv1    Attribute=${attr}    Type=Increment    Count=10
    ${attr}    Get From Dictionary    ${opt}    Sequence
    edit_modifier    Stream=${Stream}    HeaderType=gtpv1opt    Attribute=${attr}    Type=Increment    Count=10
    ${attr}    Get From Dictionary    ${optext}    NPDUNumber
    edit_modifier    Stream=${Stream}    HeaderType=gtpv1ext    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=gtpv1_1.version    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_8021ah_CustomerStagEthernet
    [Documentation]    测试目的 : 检查测试仪表发802.1ah报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的802.1ah头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    sTag    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改Customer Stag Ethernet头部
    ${stag}    edit_header_8021ah_CustomerStagEthernet    Stream=${Stream}    Vid=101010101010
    ${attr}    Get From Dictionary    ${stag}    Vid
    edit_modifier    Stream=${Stream}    HeaderType=sTag    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=sTag_1.tag.sTagOption_0.sTag.vid    Value=101010101010    MaxValue=101010101010
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_8021ah_EncapsulatedCustomerEtherntII
    [Documentation]    测试目的 : 检查测试仪表发802.1ah报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的802.1ah头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 创建流量
    ${Stream}    add_stream    Ports=${Ports[0]}
    # 修改流量报文头部
    ${HeaderTypes}    Create List    encapEthernetII    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改Customer Stag Ethernet头部
    edit_header_8021ah_EncapsulatedCustomerEthernetII    Stream=${Stream}    ServiceTag=True    CustomerTag=True
    ${server}    edit_header_8021ah_EncapsulatedCustomerEthernetII_serviceTag    Stream=${Stream}    Vid=101010101010
    ${customer}    edit_header_8021ah_EncapsulatedCustomerEthernetII_customerTag    Stream=${Stream}    Id=110011001100
    ${attr_server}    Get From Dictionary    ${server}    Vid
    ${attr_customer}    Get From Dictionary    ${customer}    Id
    edit_modifier    Stream=${Stream}    HeaderType=encapEthernetII    Attribute=${attr_server}    Type=Increment    Count=10
    edit_modifier    Stream=${Stream}    HeaderType=encapEthernetII    Attribute=${attr_customer}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=encapEthernetII_1.etherType    Value=0800    MaxValue=0800
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_8021ah_EncapsulatedBackboneEthernet
    [Documentation]    测试目的 : 检查测试仪表发802.1ah报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的802.1ah头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    encapbackboneeth    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改Customer Stag Ethernet头部
    ${eth}    edit_header_8021ah_EncapsulatedBackboneEthernet    Stream=${Stream}    Vid=200
    ${attr}    Get From Dictionary    ${eth}    Vid
    edit_modifier    Stream=${Stream}    HeaderType=encapbackboneeth    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=encapBackboneEth_1.bVLANTag.tagOption_0.btag.vid    Value=200    MaxValue=200
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_8021ah_Itag
    [Documentation]    测试目的 : 检查测试仪表发802.1ah报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的802.1ah头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    itag    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改itag头部
    ${itag}    edit_header_8021ah_iTag    Stream=${Stream}    EncapCusDstAddr=22:00:00:00:00:00
    ${attr}    Get From Dictionary    ${itag}    EncapCusDstAddr
    edit_modifier    Stream=${Stream}    HeaderType=itag    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=itag_1.pcp    Value=000    MaxValue=000
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_8021ah_MacInMac
    [Documentation]    测试目的 : 检查测试仪表发802.1ah报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的802.1ah头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    mac-in-mac    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改itag头部
    ${macInMac}    edit_header_8021ah_MacInMac    Stream=${Stream}    DestMacAdd=22:00:00:00:00:00
    ${attr}    Get From Dictionary    ${macInMac}    DestMacAdd
    edit_modifier    Stream=${Stream}    HeaderType=mac-in-mac    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mac-in-mac_1.sourceMacAdd    Value=00:00:00:12:30:10    MaxValue=00:00:00:12:30:10
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_8021ah_EncapsulatedCustomerEthernet
    [Documentation]    测试目的 : 检查测试仪表发802.1ah报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的802.1ah头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    mac-in-mac    itag    encapCustomerEth
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改Encapsulated Customer Ethernet头部
    ${eth}    edit_header_8021ah_EncapsulatedCustomerEthernet    Stream=${Stream}    EtherType=ffff
    ${attr}    Get From Dictionary    ${eth}    EtherType
    edit_modifier    Stream=${Stream}    HeaderType=encapCustomerEth    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=mac-in-mac_1.sourceMacAdd    Value=00:00:00:12:30:10    MaxValue=00:00:00:12:30:10
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Ancp
    [Documentation]    测试目的 : 检查测试仪表发ancp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ancp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    portManagement
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ancp头部
    ${ancp}    edit_header_ancp    Stream=${Stream}    Version=20    AccessLineIdentifyingTlvs=${${1}}    TestingRelatedTlvs=${${1}}    StatusInfoTlvs=${${1}}
    ${attr}    Get From Dictionary    ${ancp}    Version
    edit_modifier    Stream=${Stream}    HeaderType=portManagement    Attribute=${attr}    Type=Increment    Count=10
    ${access}    edit_header_ancp_access_line_identifying_tlv    Stream=${Stream}    Value=102030
    ${access_attr}    Get From Dictionary    ${access}    Value
    edit_modifier    Stream=${Stream}    HeaderType=portManagement    Attribute=${access_attr}    Type=Increment    Count=10
    ${testing}    edit_header_ancp_testing_related_tlv    Stream=${Stream}    Value1=405060
    ${testing_attr}    Get From Dictionary    ${testing}    Value1
    edit_modifier    Stream=${Stream}    HeaderType=portManagement    Attribute=${testing_attr}    Type=Increment    Count=10
    edit_header_ancp_status_info_tlv    Stream=${Stream}    OptionalSubTLV=${${1}}
    ${option}    edit_header_ancp_status_info_tlv_optional_sub_tlv    Stream=${Stream}    Data=708090
    ${option_attr}    Get From Dictionary    ${option}    Data
    edit_modifier    Stream=${Stream}    HeaderType=portManagement    Attribute=${option_attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=portManagement_1.tcpipEncapHeaderField.id    Value=880c    MaxValue=880c
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Pppoe_Discovery
    [Documentation]    测试目的 : 检查测试仪表发pppoe discovery报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的pppoe discovery头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    pppoediscovery
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改pppoe discovery头部
    ${pppoe}    edit_header_pppoe_discovery    Stream=${Stream}    SessionId=10    EndOfListTag=${${1}}    RelaySessionIdTag=${${1}}
    ${attr}    Get From Dictionary    ${pppoe}    SessionId
    edit_modifier    Stream=${Stream}    HeaderType=pppoediscovery    Attribute=${attr}    Type=Increment    Count=10
    ${end}    edit_header_pppoe_discovery_end_of_list_tag    Stream=${Stream}    Length=10
    ${end_attr}    Get From Dictionary    ${end}    Length
    edit_modifier    Stream=${Stream}    HeaderType=pppoediscovery    Attribute=${end_attr}    Type=Increment    Count=10
    ${relay}    edit_header_pppoe_discovery_relay_session_id_tag    Stream=${Stream}    TagIndex=1    Value=102030
    ${relay_attr}    Get From Dictionary    ${relay}    Value
    edit_modifier    Stream=${Stream}    HeaderType=pppoediscovery    Attribute=${relay_attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=pppoeDiscovery_1.version    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Bier
    [Documentation]    测试目的 : 检查测试仪表发bier报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的bier头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    bier
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改bier头部
    ${bier}    edit_header_bier    Stream=${Stream}    BiftId=10    BierbitString=${${1}}
    ${attr}    Get From Dictionary    ${bier}    BiftId
    edit_modifier    Stream=${Stream}    HeaderType=bier    Attribute=${attr}    Type=Increment    Count=10
    ${bit_string}    edit_header_bier_bit_string    Stream=${Stream}    BitString=11111111111111111111111111111111
    ${string_attr}    Get From Dictionary    ${bit_string}    BitString
    edit_modifier    Stream=${Stream}    HeaderType=bier    Attribute=${string_attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=bier_1.biftId    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Eoam
    [Documentation]    测试目的 : 检查测试仪表发Eoam报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的eoam头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    CCM
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改eoam头部
    ${tlvs}    Create List    SenderIDTLV    PortStatusTLV    InterfaceStatusTLV    OrgSpecTLV    EndTLV
    ${eoam}    edit_header_eoam    Stream=${Stream}    MDlevel=7    Tlvs=${tlvs}
    ${attr}    Get From Dictionary    ${eoam}    MDlevel
    edit_modifier    Stream=${Stream}    HeaderType=CCM    Attribute=${attr}    Type=Increment    Count=10
    ${sender}    edit_header_eoam_sender_id_tlv    Stream=${Stream}    Type=FF    theChassisID=ChassisComponent    theManagementAddressDomain=MADtDU4
    ${sender_attr}    Get From Dictionary    ${sender}    Type
    edit_modifier    Stream=${Stream}    HeaderType=CCM    Attribute=${sender_attr}    Type=Increment    Count=10
    edit_header_eoam_sender_id_tlv_chassis_id    Stream=${Stream}    Type=ChassisComponent    ChassisID=TEST
    edit_header_eoam_sender_id_tlv_management_address_domain    Stream=${Stream}    Type=MADtDU4    IPv4=1.1.1.1
    edit_header_eoam_end_tlv    Stream=${Stream}    Index=4    Type=FF
    # 配置过滤抓包
    Comment    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ccm_1.OpCode    Value=01    MaxValue=01
    Comment    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Hdlc
    [Documentation]    测试目的 : 检查测试仪表发Hdlc报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的Hdlc头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 创建流量
    ${Stream}    add_stream    Ports=${Ports[0]}
    # 修改流量报文头部
    ${HeaderTypes}    Create List    chdlc    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改hdlc头部
    ${hdlc}    edit_header_hdlc    Stream=${Stream}    Address=FF
    ${attr}    Get From Dictionary    ${hdlc}    Address
    edit_modifier    Stream=${Stream}    HeaderType=chdlc    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=chdlc_1.protocol    Value=0800    MaxValue=0800
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Control_Word
    [Documentation]    测试目的 : 检查测试仪表发Control Word报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的control word头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    cw    ethernetii    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改control word头部
    ${cw}    edit_header_control_word    Stream=${Stream}    Sn=65535
    ${attr}    Get From Dictionary    ${cw}    Sn
    edit_modifier    Stream=${Stream}    HeaderType=cw    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=cw_1.rsvd    Value=0000    MaxValue=0000
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Fcoe
    [Documentation]    测试目的 : 检查测试仪表发Fcoe报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ELS FLOGI头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 创建流量
    ${Stream}    add_stream    Ports=${Ports[0]}
    edit_stream    Stream=${Stream}    FrameLengthType=AUTO
    # 修改流量报文头部
    ${HeaderTypes}    Create List    elsflogi
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改ELS FLOGI 头部
    ${fcoe}    edit_header_els_flogi    Stream=${Stream}    Bbscn=255
    ${attr}    Get From Dictionary    ${fcoe}    Bbscn
    edit_modifier    Stream=${Stream}    HeaderType=elsflogi    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=elsFLOGI_1.commandCode    Value=04000000    MaxValue=04000000
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_8023
    [Documentation]    测试目的 : 检查测试仪表发802.3报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的802.3头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    8023
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改802.3头部
    ${header}    edit_header_8023    Stream=${Stream}    Oui=102030
    ${attr}    Get From Dictionary    ${header}    Oui
    edit_modifier    Stream=${Stream}    HeaderType=8023    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=8023_1.length    Value=46    MaxValue=46
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Goose
    [Documentation]    测试目的 : 检查测试仪表发goose报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的goose头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    ethernetII    goose
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改goose头部
    ${header}    edit_header_goose    Stream=${Stream}    Apdu=102030405060
    ${attr}    Get From Dictionary    ${header}    Apdu
    edit_modifier    Stream=${Stream}    HeaderType=goose    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=goose_1.appid    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Llc
    [Documentation]    测试目的 : 检查测试仪表发llc报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的llc头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    ethernetII    ipv4    udp    logicLinkControl
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改llc头部
    ${header}    edit_header_llc    Stream=${Stream}    Dsap=FF
    ${attr}    Get From Dictionary    ${header}    Dsap
    edit_modifier    Stream=${Stream}    HeaderType=logicLinkControl    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=logicLinkControl_1.ssap    Value=AA    MaxValue=AA
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Mstp_Config
    [Documentation]    测试目的 : 检查测试仪表发mstp config报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的mstp config头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    ethernetII    logicLinkControl    cfg
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改mstp头部
    ${header}    edit_header_mstp_config    Stream=${Stream}    RootBridgeSystemID=22:11:11:11:11:11    MstInstances=${${1}}
    ${attr}    Get From Dictionary    ${header}    RootBridgeSystemID
    edit_modifier    Stream=${Stream}    HeaderType=cfg    Attribute=${attr}    Type=Increment    Count=10
    ${ins}    edit_header_mstp_config_mst_instance    Stream=${Stream}    RemainingHops=255
    ${attr_ins}    Get From Dictionary    ${ins}    RemainingHops
    edit_modifier    Stream=${Stream}    HeaderType=cfg    Attribute=${attr_ins}    Type=Increment    Count=10
    [Teardown]    teardown

Header_Pause
    [Documentation]    测试目的 : 检查测试仪表发pause报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的pause头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    ethernetII    pause
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改pause头部
    ${header}    edit_header_pause    Stream=${Stream}    PauseCode=FFFF
    ${attr}    Get From Dictionary    ${header}    PauseCode
    edit_modifier    Stream=${Stream}    HeaderType=pause    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=pause_1.pauseTime    Value=0000    MaxValue=0000
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Pfc
    [Documentation]    测试目的 : 检查测试仪表发pfc报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的pfc头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    ethernetII    pfc
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改pfc头部
    ${header}    edit_header_pfc    Stream=${Stream}    OpCode=FFFF
    ${attr}    Get From Dictionary    ${header}    OpCode
    edit_modifier    Stream=${Stream}    HeaderType=pfc    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=pfc_1.time0    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Vntag
    [Documentation]    测试目的 : 检查测试仪表发vntag报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的vntag头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    ethernetII    vntag    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改vntag头部
    ${header}    edit_header_vntag    Stream=${Stream}    Ver=11
    ${attr}    Get From Dictionary    ${header}    Ver
    edit_modifier    Stream=${Stream}    HeaderType=vntag    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=vnTag_1.res    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Fibre_Channel
    [Documentation]    测试目的 : 检查测试仪表发fc报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的fc头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    fc    elsflogi
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改fc头部
    ${header}    edit_header_fibre_channel    Stream=${Stream}    DestAddr=112233
    ${attr}    Get From Dictionary    ${header}    DestAddr
    edit_modifier    Stream=${Stream}    HeaderType=fc    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=fc_1.rctl    Value=22    MaxValue=22
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Ipv6_Authentication
    [Documentation]    测试目的 : 检查测试仪表发ipv6 authentication报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv6 authentication头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    ipv6authenticationheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_ipv6_authentication    Stream=${Stream}    AuthData=abcd
    ${attr}    Get From Dictionary    ${header}    AuthData
    edit_modifier    Stream=${Stream}    HeaderType=ipv6authenticationheader    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6AuthenticationHeader_1.length    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Ipv6_Destination
    [Documentation]    测试目的 : 检查测试仪表发ipv6 destination报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv6 destination头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    ipv6destinationheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_ipv6_destination    Stream=${Stream}    Length=10    OptionHeaders=bierv6
    ${attr}    Get From Dictionary    ${header}    Length
    edit_modifier    Stream=${Stream}    HeaderType=ipv6destinationheader    Attribute=${attr}    Type=Increment    Count=10
    ${bier}    edit_header_ipv6_destination_option    Stream=${Stream}    Option=bierv6    Optiontype=20    BierbitString=${${1}}
    ${attr_bier}    Get From Dictionary    ${bier}    Optiontype
    edit_modifier    Stream=${Stream}    HeaderType=ipv6destinationheader    Attribute=${attr_bier}    Type=Increment    Count=10
    ${bit_string}    edit_header_ipv6_destination_bier_bit_string    Stream=${Stream}    BitString=11001100110011001100110011001100
    ${attr_bit_string}    Get From Dictionary    ${bit_string}    BitString
    edit_modifier    Stream=${Stream}    HeaderType=ipv6destinationheader    Attribute=${attr_bit_string}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6DestinationHeader_1.length    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Ipv6_Encapsulation
    [Documentation]    测试目的 : 检查测试仪表发ipv6 encapsulation报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv6 encapsulation头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    ipv6encapsulationheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_ipv6_encapsulation    Stream=${Stream}    Spi=10
    ${attr}    Get From Dictionary    ${header}    Spi
    edit_modifier    Stream=${Stream}    HeaderType=ipv6encapsulationheader    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6EncapsulationHeader_1.seqNum    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Ipv6_Fragment
    [Documentation]    测试目的 : 检查测试仪表发ipv6 fragment报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv6 fragment头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    ipv6fragmentheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_ipv6_fragment    Stream=${Stream}    Ident=10
    ${attr}    Get From Dictionary    ${header}    Ident
    edit_modifier    Stream=${Stream}    HeaderType=ipv6fragmentheader    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6FragmentHeader_1.reserved1    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Ipv6_Hopbyhop
    [Documentation]    测试目的 : 检查测试仪表发ipv6 hopbyhop报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv6 hopbyhop头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    ipv6hopbyhopheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_ipv6_hopbyhop    Stream=${Stream}    Length=10    OptionHeaders=routerAlert
    ${attr}    Get From Dictionary    ${header}    Length
    edit_modifier    Stream=${Stream}    HeaderType=ipv6hopbyhopheader    Attribute=${attr}    Type=Increment    Count=10
    ${routealert}    edit_header_ipv6_hopbyhop_option    Stream=${Stream}    Option=routerAlert    Value=1020
    ${attr_route}    Get From Dictionary    ${routealert}    Value
    edit_modifier    Stream=${Stream}    HeaderType=ipv6hopbyhopheader    Attribute=${attr_route}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6HopByHopHeader_1.nextHeader    Value=59    MaxValue=59
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Ipv6_Routing
    [Documentation]    测试目的 : 检查测试仪表发ipv6 routing报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv6 routing头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    ipv6routingheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${address}    Create List    2022::2    2033::3
    ${header}    edit_header_ipv6_routing    Stream=${Stream}    Nodes=${address}
    ${attr}    Get From Dictionary    ${header}    Nodes_2022::2
    edit_modifier    Stream=${Stream}    HeaderType=ipv6routingheader    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6RoutingHeader_1.length    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Ipv6_Sr
    [Documentation]    测试目的 : 检查测试仪表发ipv6 sr报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的ipv6 sr头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    IPv6    ipv6srheader
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${options}    Create List    sRSegment    sRSegment
    ${header}    edit_header_ipv6_sr    Stream=${Stream}    SRHeaderFlag=10101010    SRHOption=${options}
    ${attr}    Get From Dictionary    ${header}    SRHeaderFlag
    edit_modifier    Stream=${Stream}    HeaderType=ipv6srheader    Attribute=${attr}    Type=Increment    Count=10
    ${srOption}    edit_header_ipv6_sr_option    Stream=${Stream}    Option=sRSegment    Index=${${1}}    Segment=2033::3
    ${attr}    Get From Dictionary    ${srOption}    Segment
    edit_modifier    Stream=${Stream}    HeaderType=ipv6srheader    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ipv6SrHeader_1.length    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Vxlan
    [Documentation]    测试目的 : 检查测试仪表发vxlan报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的vxlan头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    vlan    ipv4    udp    vxlan
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_vxlan    Stream=${Stream}    Vni=1000
    ${attr}    Get From Dictionary    ${header}    Vni
    edit_modifier    Stream=${Stream}    HeaderType=vxlan    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=vxlan_1.reserved1    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Lldp_ChassisIdTlv
    [Documentation]    测试目的 : 检查测试仪表发lldp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的lldp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    chassisidtlv
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_lldp_chassis_id_tlv    Stream=${Stream}    ChassisId=1.1.1.1
    ${attr}    Get From Dictionary    ${header}    ChassisId
    edit_modifier    Stream=${Stream}    HeaderType=chassisidtlv    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=chassisIdTlv_1.type    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Lldp_PortIdTlv
    [Documentation]    测试目的 : 检查测试仪表发lldp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的lldp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    portidtlv
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_lldp_port_id_tlv    Stream=${Stream}    PortId=22:22:22:22:22:22
    ${attr}    Get From Dictionary    ${header}    PortId
    edit_modifier    Stream=${Stream}    HeaderType=portidtlv    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=portIdTlv_1.type    Value=2    MaxValue=2
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Lldp_TtlTlv
    [Documentation]    测试目的 : 检查测试仪表发lldp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的lldp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    portidtlv    ttltlv
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_lldp_ttl_tlv    Stream=${Stream}    Ttl=10
    ${attr}    Get From Dictionary    ${header}    Ttl
    edit_modifier    Stream=${Stream}    HeaderType=ttltlv    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=ttlTlv_1.type    Value=3    MaxValue=3
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Lldp_EndTlv
    [Documentation]    测试目的 : 检查测试仪表发lldp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的lldp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    EthernetII    portidtlv    ttltlv    endtlv
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_lldp_end_tlv    Stream=${Stream}    Length=10
    ${attr}    Get From Dictionary    ${header}    Length
    edit_modifier    Stream=${Stream}    HeaderType=endtlv    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=endTlv_1.type    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Hsr
    [Documentation]    测试目的 : 检查测试仪表发hsr报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的hsr头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    hsrtag    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_hsr_tag    Stream=${Stream}    LsduSize=4095
    ${attr}    Get From Dictionary    ${header}    LsduSize
    edit_modifier    Stream=${Stream}    HeaderType=hsrtag    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=hsrtag_1.seqnum    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Prp
    [Documentation]    测试目的 : 检查测试仪表发prp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的prp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    prptag    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_prp_tag    Stream=${Stream}    SequenceNumber=4095
    ${attr}    Get From Dictionary    ${header}    SequenceNumber
    edit_modifier    Stream=${Stream}    HeaderType=prptag    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=prptag_1.lsdusize    Value=52    MaxValue=52
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Rtag
    [Documentation]    测试目的 : 检查测试仪表发r tag报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的r tag头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    rtag    ipv4
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_r_tag    Stream=${Stream}    Reserved=1010
    ${attr}    Get From Dictionary    ${header}    Reserved
    edit_modifier    Stream=${Stream}    HeaderType=rtag    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=rtag_1.seqnum    Value=0    MaxValue=0
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Sctp
    [Documentation]    测试目的 : 检查测试仪表发sctp报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的sctp头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    ethernetii    ipv4    sctp
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_sctp    Stream=${Stream}    SourcePort=1000    DestPort=2000
    ${attr}    Get From Dictionary    ${header}    SourcePort
    edit_modifier    Stream=${Stream}    HeaderType=sctp    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=sctp_1.header.verTag    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown

Header_Trill
    [Documentation]    测试目的 : 检查测试仪表发Trill报文统计正确
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 修改流量StreamTemplate_1的trill头部内容;
    ...
    ...    测试步骤3: 配置过滤抓包;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 设置端口发送模式为突发包;
    ...
    ...    测试步骤6: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤7: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 修改流量报文头部
    ${HeaderTypes}    Create List    ethernetii    trill
    create_stream_header    Stream=${Stream}    HeaderTypes=${HeaderTypes}
    # 修改头部
    ${header}    edit_header_trill    Stream=${Stream}    EgressRBridge=1000    IngressBridge=2000
    ${attr}    Get From Dictionary    ${header}    IngressBridge
    edit_modifier    Stream=${Stream}    HeaderType=trill    Attribute=${attr}    Type=Increment    Count=10
    # 配置过滤抓包
    ${pdu_pattern_1}    create_capture_pdu_pattern    Port=${Ports[1]}    HeaderTypes=${HeaderTypes}    FieldName=trill_1.version    Value=1    MaxValue=1
    edit_capture_filter    Port=${Ports[1]}    Expression= ${pdu_pattern_1}
    [Teardown]    teardown
*** Keywords ***
setup
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}    Force=True
    # 创建流量
    ${Stream}    add_stream    Ports=${Ports[0]}
    edit_stream    Stream=${Stream}    FrameLengthType=AUTO
    set suite variable    ${Ports}
    set suite variable    ${Stream}

teardown
    # 订阅StreamBlockStats统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats
    subscribe_result    Types=${SubscribeTypes}
    # 设置端口发送模式为突发包
    edit_port_load_profile    Ports=${Ports[0]}    TransmitMode=BURST    BurstCount=100
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    start_stream
    sleep    10
    stop_stream
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    &{Result}    get_streamblock_statistic    Stream=${Stream[0]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    IF    ${TxStreamFrames} != 0 and ${TxStreamFrames} == ${RxStreamFrames}
    Log    html=True    console=True    message=TxStreamFrames(${TxStreamFrames}) is equal to RxStreamFrames(${RxStreamFrames})
    ELSE
    Log    html=True    console=True    message=TxStreamFrames(${TxStreamFrames}) is not equal to RxStreamFrames(${RxStreamFrames})
    Run Keyword And Continue On Failure    Fail    msg==TxStreamFrames(${TxStreamFrames}) is not equal to RxStreamFrames(${RxStreamFrames})
    END
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}
    Shutdown Tester
