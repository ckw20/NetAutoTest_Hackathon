*** Settings ***
Force Tags        Protocol
Resource          ../Common.robot
*** Test Cases ***
Protocol_ISIS_IPv4
    [Documentation]    测试目的 : 检查ISIS协议IPv4绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 两个端口分别创建ISIS协议，并且创建路由;
    ...
    ...    测试步骤3: 创建绑定流量;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    ISIS    IPv4
    [Setup]    setup
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv4
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv4
    edit_interface    Interface=${Interface_1}    Layer=IPv4Layer    Address=192.168.1.3    Gateway=192.168.1.2
    edit_interface    Interface=${Interface_2}    Layer=IPv4Layer    Address=192.168.1.2    Gateway=192.168.1.3
    # 创建ISIS协议会话
    ${Session_1}    create_isis    Port=${Ports[0]}
    ${Session_2}    create_isis    Port=${Ports[1]}
    edit_isis    Session=${Session_1}    Level=L1L2    MtParams=1    PerPduAuthentication=1
    edit_isis    Session=${Session_2}    Level=L1L2    MtParams=1    PerPduAuthentication=1
    # 修改ISIS Mt参数
    ${MtFlags}    Create List    ABIT    OBIT
    edit_isis_mt_params    Session=${Session_1}    Index=0    MtId=IPV4    MtFlags=${MtFlags}
    edit_isis_mt_params    Session=${Session_2}    Index=0    MtId=IPV4    MtFlags=${MtFlags}
    # ${MtFlags} \ \ \ Create List \ \ \ NOSHOW
    # edit_isis_mt_params \ \ \ Session=${Session_1} \ \ \ Index=1 \ \ \ MtId=IPV4 \ \ \ MtFlags=${MtFlags}
    # edit_isis_mt_params \ \ \ Session=${Session_2} \ \ \ Index=1 \ \ \ MtId=IPV4 \ \ \ MtFlags=${MtFlags}
    # 修改ISIS PerPduAuthentication参数
    edit_isis_per_pdu    Session=${Session_1}    Index=0    PdusType=L1_HELLO    AuthMethod=SIMPLE    Password=test
    # edit_isis_per_pdu \ \ \ Session=${Session_1} \ \ \ Index=1 \ \ \ PdusType=L1_HELLO \ \ \ AuthMethod=NONE
    # edit_isis_per_pdu \ \ \ Session=${Session_1} \ \ \ Index=2 \ \ \ PdusType=L1_HELLO \ \ \ AuthMethod=MD5 \ \ \ Password=test
    # edit_isis_per_pdu \ \ \ Session=${Session_1} \ \ \ Index=3 \ \ \ PdusType=L1_HELLO \ \ \ AuthMethod=NONE
    edit_isis_per_pdu    Session=${Session_2}    Index=0    PdusType=L1_HELLO    AuthMethod=SIMPLE    Password=test
    # edit_isis_per_pdu \ \ \ Session=${Session_2} \ \ \ Index=1 \ \ \ PdusType=L1_HELLO \ \ \ AuthMethod=NONE
    # edit_isis_per_pdu \ \ \ Session=${Session_2} \ \ \ Index=2 \ \ \ PdusType=L1_HELLO \ \ \ AuthMethod=MD5 \ \ \ Password=test
    # edit_isis_per_pdu \ \ \ Session=${Session_2} \ \ \ Index=3 \ \ \ PdusType=L1_HELLO \ \ \ AuthMethod=NONE
    # ISIS协议会话与接口绑定
    select_interface    Session=${Session_1}    Interface=${Interface_1}
    select_interface    Session=${Session_2}    Interface=${Interface_2}
    # ISIS协议会话创建LSP
    ${Lsp_1}    create_isis_lsp    Session=${Session_1}    Level=L1
    ${Lsp_2}    create_isis_lsp    Session=${Session_2}    Level=L1
    # ISIS协议会话LSP创建IPv4 TLV
    ${Tlv_1}    create_isis_ipv4_tlv    Lsp=${Lsp_1}    RouteCount=10
    ${Tlv_2}    create_isis_ipv4_tlv    Lsp=${Lsp_2}    RouteCount=10
    # 获取ISIS协议绑定流端点对象
    ${Points_1}    get_isis_router_from_tlv    Configs=${Tlv_1}
    ${Points_2}    get_isis_router_from_tlv    Configs=${Tlv_2}
    # 创建ISIS绑定流
    ${Streams}    add_stream    Type=binding    SrcPoints=${Points_1}    DstPoints=${Points_2}    Bidirection=True
    # 订阅StreamBlockStats统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats    IsisSessionStats    IsisTlvStats
    subscribe_result    Types=${SubscribeTypes}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    # 启动协议
    start_protocol
    # 等待ISIS协议会话稳定状态
    wait_isis_state    Sessions=${Session_1}
    wait_isis_state    Sessions=${Session_2}
    wait_isis_l1_broadcast_adj_state    Sessions=${Session_1}
    wait_isis_l1_broadcast_adj_state    Sessions=${Session_2}
    wait_isis_l2_broadcast_adj_state    Sessions=${Session_1}
    wait_isis_l2_broadcast_adj_state    Sessions=${Session_2}
    # 发送流量
    start_stream
    sleep    10
    stop_stream
    stop_protocol
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    # 查看ISIS协议IsisSessionStats统计结果
    &{Result}    get_isis_session_stats    Session=${Session_1}
    &{Result}    get_isis_session_stats    Session=${Session_2}
    # 查看ISIS协议IsisTlvStats统计结果
    &{Result}    get_isis_tlv_stats    Session=${Session_1}
    &{Result}    get_isis_tlv_stats    Session=${Session_2}
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    &{Result}    get_streamblock_statistic    Stream=${Streams[0]}
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

Protocol_OSPFv2
    [Documentation]    测试目的 : 检查OSPFv2协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 两个端口分别创建OSPF协议，并且创建路由;
    ...
    ...    测试步骤3: 创建绑定流量;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    OSPF    OSPFv2    IPv4
    [Setup]    setup
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv4
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv4
    edit_interface    Interface=${Interface_1}    Layer=IPv4Layer    Address=192.168.1.3    Gateway=192.168.1.2
    edit_interface    Interface=${Interface_2}    Layer=IPv4Layer    Address=192.168.1.2    Gateway=192.168.1.3
    # 创建OSPFv2协议会话
    ${Session_1}    create_ospf    Port=${Ports[0]}
    ${Session_2}    create_ospf    Port=${Ports[1]}
    edit_ospf    Session=${Session_1}    Priority=1
    edit_ospf    Session=${Session_2}    Priority=1
    # OSPFv2协议会话与接口绑定
    select_interface    Session=${Session_1}    Interface=${Interface_1}
    select_interface    Session=${Session_2}    Interface=${Interface_2}
    # OSPFv2协议会话创建LSA
    ${Lsa_1}    create_ospf_external_lsa    Session=${Session_1}    RouteCount=10
    ${Lsa_2}    create_ospf_external_lsa    Session=${Session_2}    RouteCount=10
    # 获取OSPFv2协议绑定流端点对象
    ${Points_1}    get_ospf_router_from_lsa    Lsa=${Lsa_1}
    ${Points_2}    get_ospf_router_from_lsa    Lsa=${Lsa_2}
    # 创建OSPFv2绑定流
    ${Streams}    add_stream    Type=binding    SrcPoints=${Points_1}    DstPoints=${Points_2}    Bidirection=True
    # 订阅StreamBlockStats和Ospfv2SessionResultPropertySet统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats    Ospfv2SessionResultPropertySet
    subscribe_result    Types=${SubscribeTypes}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    # 启动协议
    start_protocol
    # 等待OSPF协议会话稳定状态
    wait_ospf_state    Sessions=${Session_1}
    wait_ospf_state    Sessions=${Session_2}
    wait_ospf_adjacency_state    Sessions=${Session_1}
    wait_ospf_adjacency_state    Sessions=${Session_2}
    # 发送流量
    start_stream
    sleep    10
    stop_stream
    stop_protocol
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    # 查看OSPFv2协议Ospfv2SessionResultPropertySet统计结果
    &{Result}    get_ospf_statistic    Session=${Session_1}
    &{Result}    get_ospf_statistic    Session=${Session_2}
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    &{Result}    get_streamblock_statistic    Stream=${Streams[0]}
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

Protocol_BGP_IPv4
    [Documentation]    测试目的 : 检查BGP协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 两个端口分别创建BGP协议，并且创建路由;
    ...
    ...    测试步骤3: 创建绑定流量;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    BGP    IPv4
    [Setup]    setup
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv4
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv4
    edit_interface    Interface=${Interface_1}    Layer=IPv4Layer    Address=192.168.1.3    Gateway=192.168.1.2
    edit_interface    Interface=${Interface_2}    Layer=IPv4Layer    Address=192.168.1.2    Gateway=192.168.1.3
    # 创建BGP协议会话
    ${Session_1}    create_bgp    Port=${Ports[0]}
    ${Session_2}    create_bgp    Port=${Ports[1]}
    edit_bgp    Session=${Session_1}    AsNumber=100    DutAsNumber=200
    edit_bgp    Session=${Session_2}    AsNumber=200    DutAsNumber=100
    # BGP协议会话与接口绑定
    select_interface    Session=${Session_1}    Interface=${Interface_1}
    select_interface    Session=${Session_2}    Interface=${Interface_2}
    # BGP协议会话创建route pool
    ${RoutePool_1}    create_bgp_ipv4_route_pool    Session=${Session_1}    RouteCount=10
    ${RoutePool_2}    create_bgp_ipv4_route_pool    Session=${Session_2}    RouteCount=10
    # 获取BGP协议绑定流端点对象
    ${Points_1}    get_bgp_router_from_route_pool    Configs=${RoutePool_1}
    ${Points_2}    get_bgp_router_from_route_pool    Configs=${RoutePool_2}
    # 创建BGP绑定流
    ${Streams}    add_stream    Type=binding    SrcPoints=${Points_1}    DstPoints=${Points_2}    Bidirection=True
    # 订阅StreamBlockStats、BgpSessionStatistic、BgpSessionBlockStatistic统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats    BgpSessionStatistic    BgpSessionBlockStatistic
    subscribe_result    Types=${SubscribeTypes}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    # 启动协议
    start_protocol
    # 等待OSPF协议会话稳定状态
    wait_bgp_state    Sessions=${Session_1}
    wait_bgp_state    Sessions=${Session_2}
    wait_bgp_router_state    Sessions=${Session_1}
    wait_bgp_router_state    Sessions=${Session_2}
    # 发送流量
    start_stream
    sleep    10
    stop_stream
    stop_protocol
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    # 查看BGP协议会话统计结果
    &{Result}    get_bgp_session_statistic    Session=${Session_1}    Id=1
    &{Result}    get_bgp_session_statistic    Session=${Session_2}    Id=1
    &{Result}    get_bgp_session_block_statistic    Session=${Session_1}
    &{Result}    get_bgp_session_block_statistic    Session=${Session_2}
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    &{Result}    get_streamblock_statistic    Stream=${Streams[0]}
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

Protocol_BGP_IPv6
    [Documentation]    测试目的 : 检查BGP4+协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 两个端口分别创建BGP4+协议，并且创建路由;
    ...
    ...    测试步骤3: 创建绑定流量;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    BGP    BGP4+    IPv6
    [Setup]    setup
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv6
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv6
    edit_interface    Interface=${Interface_1}    Layer=IPv6Layer    Address=2000::2    Gateway=2000::3
    edit_interface    Interface=${Interface_2}    Layer=IPv6Layer    Address=2000::3    Gateway=2000::2
    # 创建BGP协议会话
    ${Session_1}    create_bgp    Port=${Ports[0]}
    ${Session_2}    create_bgp    Port=${Ports[1]}
    edit_bgp    Session=${Session_1}    AsNumber=100    DutAsNumber=200
    edit_bgp    Session=${Session_2}    AsNumber=200    DutAsNumber=100
    # BGP协议会话与接口绑定
    select_interface    Session=${Session_1}    Interface=${Interface_1}
    select_interface    Session=${Session_2}    Interface=${Interface_2}
    # BGP协议会话创建route pool
    ${RoutePool_1}    create_bgp_ipv6_route_pool    Session=${Session_1}    RouteCount=10
    ${RoutePool_2}    create_bgp_ipv6_route_pool    Session=${Session_2}    RouteCount=10
    # 获取BGP协议绑定流端点对象
    ${Points_1}    get_bgp_router_from_route_pool    Configs=${RoutePool_1}    Type=IPv6
    ${Points_2}    get_bgp_router_from_route_pool    Configs=${RoutePool_2}    Type=IPv6
    # 创建BGP绑定流
    ${Streams}    add_stream    Type=binding    SrcPoints=${Points_1}    DstPoints=${Points_2}    Bidirection=True
    # 订阅StreamBlockStats、BgpSessionStatistic、BgpSessionBlockStatistic统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats    BgpSessionStatistic    BgpSessionBlockStatistic
    subscribe_result    Types=${SubscribeTypes}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    # 启动协议
    start_protocol
    # 等待BGP协议会话稳定状态
    wait_bgp_state    Sessions=${Session_1}
    wait_bgp_state    Sessions=${Session_2}
    wait_bgp_router_state    Sessions=${Session_1}
    wait_bgp_router_state    Sessions=${Session_2}
    # 发送流量
    start_stream
    sleep    10
    stop_stream
    stop_protocol
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    # 查看BGP协议会话统计结果
    &{Result}    get_bgp_session_statistic    Session=${Session_1}    Id=1
    &{Result}    get_bgp_session_statistic    Session=${Session_2}    Id=1
    &{Result}    get_bgp_session_block_statistic    Session=${Session_1}
    &{Result}    get_bgp_session_block_statistic    Session=${Session_2}
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    &{Result}    get_streamblock_statistic    Stream=${Streams[0]}
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

Protocol_DHCPv4
    [Documentation]    测试目的 : 检查DHCPv4协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 两个端口分别创建DHCPv4 Clinet和Server协议;
    ...
    ...    测试步骤3: 创建绑定流量;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    DHCP    DHCPv4    IPv4
    [Setup]    setup
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv4
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv4
    edit_interface    Interface=${Interface_1}    Layer=IPv4Layer    Address=2.1.1.2    Gateway=2.1.1.1
    edit_interface    Interface=${Interface_2}    Layer=IPv4Layer    Address=2.1.2.2    Gateway=2.1.1.1
    # 创建DHCPv4协议会话
    ${client}    create_dhcp_client    Port=${Ports[0]}
    ${server}    create_dhcp_server    Port=${Ports[1]}
    # DHCPv4协议会话与接口绑定
    select_interface    Session=${client}    Interface=${Interface_1}
    select_interface    Session=${server}    Interface=${Interface_2}
    # 获取DHCP Server地址池
    ${configDict}    get_configs    Configs=Dhcpv4AddressPool
    ${dhcpv4AddressPool}    Get Dictionary Values    ${configDict}
    edit_configs    Configs=${dhcpv4AddressPool}    PoolAddressStart=2.1.2.3
    # 获取接口绑定流端点对象
    ${Points_1}    get_layer_from_interfaces    Interfaces=${Interface_1}
    ${Points_2}    get_layer_from_interfaces    Interfaces=${Interface_2}
    # 创建DHCPv4绑定流
    ${Streams}    add_stream    Type=binding    SrcPoints=${Points_1}    DstPoints=${Points_2}    Bidirection=True
    # 订阅StreamBlockStats和Ospfv2SessionResultPropertySet统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats    Dhcpv4ServerStats    Dhcpv4ClientBlockStats    Dhcpv4ClientStats    Dhcpv4PortStats    Dhcpv4LeaseStats
    subscribe_result    Types=${SubscribeTypes}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    # 启动协议
    start_protocol
    # 等待DHCPv4协议会话稳定状态
    wait_dhcp_client_state    Sessions=${client}
    wait_dhcp_server_state    Sessions=${server}
    # 发送流量
    start_stream
    sleep    10
    stop_stream
    stop_protocol
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    # 查看DHCPv4协议Dhcpv4PortStats统计结果
    &{Result}    get_dhcp_port_statistic    Port=${Ports[0]}
    &{Result}    get_dhcp_port_statistic    Port=${Ports[1]}
    # 获取DHCP客户端统计
    &{Result}    get_dhcp_client_statistic    Session=${client}
    &{Result}    get_dhcp_client_block_statistic    Session=${client}
    # 获取DHCP服务器统计
    &{Result}    get_dhcp_server_statistic    Session=${server}
    &{Result}    get_dhcp_server_lease_statistic    Session=${server}    ClientId=00:00:02:01:01:02
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    &{Result}    get_streamblock_statistic    Stream=${Streams[0]}
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

Protocol_IGMP
    [Documentation]    测试目的 : 检查IGMP协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 两个端口分别创建IGMP和IGMP Querier协议，并且创建组播组;
    ...
    ...    测试步骤3: 创建绑定流量;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    IGMP    IPv4
    [Setup]    setup
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv4
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv4
    edit_interface    Interface=${Interface_1}    Layer=IPv4Layer    Address=2.1.1.2    Gateway=2.1.1.1
    edit_interface    Interface=${Interface_2}    Layer=IPv4Layer    Address=2.1.2.2    Gateway=2.1.1.1
    # 创建IGMP协议会话
    ${igmp}    create_igmp    Port=${Ports[0]}
    # IGMP协议会话与接口绑定
    select_interface    Session=${igmp}    Interface=${Interface_1}
    # 编辑igmp会话
    edit_igmp    Session=${igmp}    InitialJoin=True
    # 创建组播组
    ${multicast_group}    create_multicast_group    Start=225.0.1.2
    # IGMP协议会话创建组成员关系
    ${memberships}    create_memberships    Session=${igmp}    DeviceGroupMapping=ROUNDROBIN
    # 将组播组和IGMP组成员关系绑定
    binding_multicast_group    Session=${igmp}    Memberships=${memberships}    MulticastGroup=${multicast_group}
    # 创建IGMP Querier协议会话
    ${igmp_querier}    create_igmp_querier    Port=${Ports[1]}
    # IGMP协议会话与接口绑定
    select_interface    Session=${igmp_querier}    Interface=${Interface_2}
    # 编辑igmp querier会话
    edit_igmp_querier    Session=${igmp_querier}    RobustnessVariable=3
    # 创建IGMP绑定流
    ${point}    get_layer_from_interfaces    Interfaces=${Interface_2}
    ${streams}    add_stream    Type=binding    SrcPoints=${point}    DstPoints=${multicast_group}    Bidirection=False
    # 订阅统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats    IgmpHostResults    IgmpPortAggregatedResults    IgmpQuerierResults
    subscribe_result    Types=${SubscribeTypes}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    # 启动协议
    start_protocol
    # 等待IGMP和IGMP Querier协议会话稳定状态
    wait_igmp_state    Sessions=${igmp}
    wait_igmp_querier_state    Sessions=${igmp_querier}
    # 发送流量
    start_stream
    sleep    60
    stop_stream
    stop_protocol
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    # 查看IGMP协议IgmpHostResults统计结果
    &{Result}    get_igmp_host_statistic    Session=${igmp}
    # 查看IGMP协议IgmpPortAggregatedResults统计结果
    &{Result}    get_igmp_port_statistic    Port=${Ports[0]}
    # 查看IGMP Querier协议IgmpQuerierResults统计结果
    &{Result}    get_igmp_querier_statistic    Session=${igmp_querier}
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    &{Result}    get_streamblock_statistic    Stream=${Streams[0]}
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

Protocol_MLD
    [Documentation]    测试目的 : 检查MLD协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 两个端口分别创建MLD和MLD Querier协议，并且创建组播组;
    ...
    ...    测试步骤3: 创建绑定流量;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
    ...
    ...    预期结果1: 步骤6中流量StreamTemplate_1收发包相等;
    [Tags]    Tester-001    MLD    IPv6
    [Setup]    setup
    # 创建接口
    ${Interface_1}    create_interface    Port=${Ports[0]}    Layers=IPv6
    ${Interface_2}    create_interface    Port=${Ports[1]}    Layers=IPv6
    edit_interface    Interface=${Interface_1}    Layer=IPv6Layer    Address=2000::2    Gateway=2000::3
    edit_interface    Interface=${Interface_2}    Layer=IPv6Layer    Address=2000::3    Gateway=2000::2
    # 创建MLD协议会话
    ${mld}    create_mld    Port=${Ports[0]}
    # MLD协议会话与接口绑定
    select_interface    Session=${mld}    Interface=${Interface_1}
    # 编辑mld会话
    edit_mld    Session=${mld}    InitialJoin=True
    # 创建组播组
    ${multicast_group}    create_multicast_group    Start=ff1e::2    Version=IPv6
    # MLD协议会话创建组成员关系
    ${memberships}    create_memberships    Session=${mld}    DeviceGroupMapping=ROUNDROBIN
    # 将组播组和MLD组成员关系绑定
    binding_multicast_group    Session=${mld}    Memberships=${memberships}    MulticastGroup=${multicast_group}
    # 创建MLD Querier协议会话
    ${mld_querier}    create_mld_querier    Port=${Ports[1]}
    # MLD协议会话与接口绑定
    select_interface    Session=${mld_querier}    Interface=${Interface_2}
    # 编辑mld querier会话
    edit_mld_querier    Session=${mld_querier}    RobustnessVariable=3
    # 创建MLD绑定流
    ${point}    get_layer_from_interfaces    Interfaces=${Interface_2}    Layer=ipv6
    ${streams}    add_stream    Type=binding    SrcPoints=${point}    DstPoints=${multicast_group}    Bidirection=False
    # 订阅统计视图
    ${SubscribeTypes}    Create List    StreamBlockStats    MldHostResults    MldPortAggregatedResults    MldQuerierResults
    subscribe_result    Types=${SubscribeTypes}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动抓包，发送流量
    start_capture
    # 启动协议
    start_protocol
    # 等待MLD和MLD Querier协议会话稳定状态
    wait_mld_state    Sessions=${mld}
    wait_mld_querier_state    Sessions=${mld_querier}
    # 发送流量
    start_stream
    sleep    60
    stop_stream
    stop_protocol
    stop_capture
    sleep    3
    # 下载捕获到的报文
    ${PackagesPath}    download_packages    Port=${Ports[1]}    FileDir=${TestPcapPath}    FileName=${TEST NAME}    MaxCount=100
    # 查看MLD协议MldHostResults统计结果
    &{Result}    get_mld_host_statistic    Session=${mld}
    # 查看MLD协议MldPortAggregatedResults统计结果
    &{Result}    get_mld_port_statistic    Port=${Ports[0]}
    # 查看MLD Querier协议MldQuerierResults统计结果
    &{Result}    get_mld_querier_statistic    Session=${mld_querier}
    # 获取流量StreamBlockStats，并判断流量收发是否正确
    &{Result}    get_streamblock_statistic    Stream=${Streams[0]}
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

Protocol_BFD
    [Documentation]    测试目的 : 检查BFD与ISIS协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建ISIS协议，并且创建路由
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    BFD
    [Setup]    setup
    # 创建接口
    ${interface1}    Create Interface    Port=${Ports[0]}
    ${interface2}    Create Interface    Port=${Ports[1]}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建BFD协议会话
    ${bfd1}    Create Bfd    Port=${Ports[0]}
    ${bfd2}    Create Bfd    Port=${Ports[1]}    RouterRole=PASSIVE
    Select Interface    Session=${bfd1}    Interface=${interface1}
    Select Interface    Session=${bfd2}    Interface=${interface2}
    # 创建ISIS协议会话及Tlv
    ${isis1}    Create Isis    Port=${Ports[0]}    EnableBFD=True
    ${isis2}    Create Isis    Port=${Ports[1]}    EnableBFD=True
    Select Interface    Session=${isis1}    Interface=${interface1}
    Select Interface    Session=${isis2}    Interface=${interface2}
    ${lsp1}    Create Isis Lsp    Session=${isis1}    Level=L1
    ${lsp2}    Create Isis Lsp    Session=${isis2}    Level=L1
    ${tlv1}    Create Isis Ipv4 Tlv    Lsp=${lsp1}    RouteCount=10    StartIpv4Prefix=2.0.0.1
    ${tlv2}    Create Isis Ipv4 Tlv    Lsp=${lsp2}    RouteCount=10    StartIpv4Prefix=3.0.0.1
    # 获取接口绑定流端点对象
    ${point1}    Get Isis Router From Tlv    Configs=${tlv1}
    ${point2}    Get Isis Router From Tlv    Configs=${tlv2}
    # 创建数据流量
    ${streams}    Add Stream    Type=binding    SrcPoints=${point1}    DstPoints=${point2}    Bidirection=True
    # 订阅统计
    @{Types}=    Create List    StreamBlockStats    IsisBfdSessionResult
    Subscribe Result    Types=${Types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待ISIS协议协议会话状态正确
    ${isissessions}    Create List    ${isis1}    ${isis2}
    Wait Isis State    Sessions=${isissessions}    State=UP
    Sleep    5
    # 发送流量
    Start Stream
    Sleep    10
    Stop Stream
    Stop Protocol
    Sleep    3
    # 获取BFD ISIS统计
    &{bfd_isis_ipv4_result_1}    Get Bfd Isis Session Result    BfdSession=${bfd1}    IsisSession=${isissessions[0]}    SessionId=${1}
    &{bfd_isis_ipv4_result_2}    Get Bfd Isis Session Result    BfdSession=${bfd2}    IsisSession=${isissessions[1]}    SessionId=${1}
    Log Many    ${bfd_isis_ipv4_result_1}
    Log Many    ${bfd_isis_ipv4_result_2}
    # 获取流量1统计
    &{Result}    Get Streamblock Statistic    Stream=${Streams[0]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    IF    ${TxStreamFrames} != 0 and ${TxStreamFrames} == ${RxStreamFrames}
    Log    html=True    console=True    message=TxStreamFrames(${TxStreamFrames}) is equal to RxStreamFrames(${RxStreamFrames})
    ELSE
    Log    html=True    console=True    message=TxStreamFrames(${TxStreamFrames}) is not equal to RxStreamFrames(${RxStreamFrames})
    Run Keyword And Continue On Failure    Fail    msg==TxStreamFrames(${TxStreamFrames}) is not equal to RxStreamFrames(${RxStreamFrames})
    END
    # 获取流量2统计
    &{Result}    Get Streamblock Statistic    Stream=${Streams[1]}
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

Protocol_OSPFv3
    [Documentation]    测试目的 : 检查OSPFv3协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建OSPFv3协议，并且创建路由
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    OSPFv3
    [Setup]    setup
    # 创建接口
    @{layers}=    Create List    ipv6
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers}
    Edit Interface    Interface=${interface1}    Layer=IPv6Layer    Address=2001::1    Gateway=2001::2
    Edit Interface    Interface=${interface2}    Layer=IPv6Layer    Address=2001::2    Gateway=2001::1
    # 创建OSPFv3协议会话
    ${session_1}    Create Ospfv3    Port=${Ports[0]}    Priority=${1}
    ${session_2}    Create Ospfv3    Port=${Ports[1]}    Priority=${2}
    # OSPFv3协议会话与接口绑定
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # OSPFv3协议会话1创建Summary Lsa
    ${inter_lsa_1}    Create Ospfv3 Inter Area Prefix Lsa    Session=${session_1}
    # OSPFv3协议会话2创建External Lsa
    ${inter_lsa_2}    Create Ospfv3 Inter Area Prefix Lsa    Session=${session_2}
    # 获取OSPFv3协议绑定流端点对象
    ${point_1}    Get Ospf Router From Lsa    Lsa=${inter_lsa_1}
    ${point_2}    Get Ospf Router From Lsa    Lsa=${inter_lsa_2}
    # 创建OSPFv3绑定流
    ${streams}    Add Stream    Type=binding    SrcPoints=${point_1}    DstPoints=${point_2}    Bidirection=True
    # 订阅统计
    @{types}    Create List    Ospfv3SessionResultPropertySet    StreamBlockStats
    subscribe_result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待OSPFv3协议会话达到Full状态
    @{sessions}    Create List    ${session_1}    ${session_2}
    Wait Ospf Adjacency State    Sessions=${sessions}
    @{inter_lsas}    Create List    ${inter_lsa_1}    ${inter_lsa_2}
    Advertise Ospf Lsa    Lsa=${inter_lsas}
    Sleep    5
    # 发送流量
    Start Stream
    Sleep    10
    Stop Stream
    Withdraw Ospf Lsa    Lsa=${inter_lsas}
    Sleep    5
    # \ \ \ Stop Protocol
    # \ \ \ Sleep \ \ \ 3
    # 获取OSPFv3会话1统计
    &{result}    Get Ospfv3 Statistic    Session=${session_1}
    ${TxInterAreaPrefixLsa}    Get From Dictionary    dictionary=&{Result}    key=TxInterAreaPrefixLsa
    ${RxInterAreaPrefixLsa}    Get From Dictionary    dictionary=&{Result}    key=RxInterAreaPrefixLsa
    Should Be Equal    ${TxInterAreaPrefixLsa}    ${RxInterAreaPrefixLsa}
    # 获取OSPFv3会话2统计
    &{result}    Get Ospfv3 Statistic    Session=${session_2}
    ${TxInterAreaPrefixLsa}    Get From Dictionary    dictionary=&{Result}    key=TxInterAreaPrefixLsa
    ${RxInterAreaPrefixLsa}    Get From Dictionary    dictionary=&{Result}    key=RxInterAreaPrefixLsa
    Should Be Equal    ${TxInterAreaPrefixLsa}    ${RxInterAreaPrefixLsa}
    # 获取流量1统计
    &{result}    Get Streamblock Statistic    Stream=${streams[0]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 获取流量2统计
    &{result}    Get Streamblock Statistic    Stream=${streams[1]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_PIM
    [Documentation]    测试目的 : 检查PIM协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建PIM协议及组播组
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    PIM
    [Setup]    setup
    # 创建接口
    @{layers}=    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建pim协议会话
    ${pim_1}    Create Pim    Port=${Ports[0]}
    ${pim_2}    Create Pim    Port=${Ports[1]}
    ${pim_group_1}    Create Pim Group    Session=${pim_1}    GroupAddr=225.0.0.1
    ${pim_group_2}    Create Pim Group    Session=${pim_2}    GroupAddr=225.0.0.2
    # 选择接口
    Select Interface    Session=${pim_1}    Interface=${interface1}
    Select Interface    Session=${pim_2}    Interface=${interface2}
    # 创建组播组
    ${multicast_group_1}    Create Multicast Group    Start=225.0.0.1
    ${multicast_group_2}    Create Multicast Group    Start=225.0.0.2
    # 创建DHCP绑定流
    ${point_1}    Get Layer From Interfaces    Interfaces=${interface1}
    ${point_2}    Get Layer From Interfaces    Interfaces=${interface2}
    ${stream1}    Add Stream    Type=binding    SrcPoints=${point_1}    DstPoints=${multicast_group_1}
    ${stream2}    Add Stream    Type=binding    SrcPoints=${point_2}    DstPoints=${multicast_group_2}
    # 订阅统计
    @{types}    Create List    StreamBlockStats    PimSessionStats    PimGroupStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待DHCP协议协议会话状态正确
    @{Sessions}    Create List    ${pim_1}    ${pim_2}
    Wait Pim State    Sessions=${Sessions}
    Sleep    5
    #发送流量
    Start Stream
    Sleep    10
    Stop Stream
    # \ \ \ Stop Protocol
    # \ \ \ Sleep \ \ \ 3
    # 获取PIM会话统计
    &{result}    Get Pim Session Stats    Session=${pim_1}
    Log Many    ${result}
    &{result}    Get Pim Session Stats    Session=${pim_2}
    Log Many    ${result}
    # 获取PIM Group统计
    &{result}    Get Pim Group Stats    Session=${pim_1}    Group=${pim_group_1}
    Log Many    ${result}
    &{result}    Get Pim Group Stats    Session=${pim_1}    Group=${pim_group_1}
    Log Many    ${result}
    # 获取流量1统计
    &{result}    Get Streamblock Statistic    Stream=${stream1}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 获取流量2统计
    &{result}    Get Streamblock Statistic    Stream=${stream2}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_RIP
    [Documentation]    测试目的 : 检查RIP协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建RIP协议及组播组
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    RIP
    [Setup]    setup
    # 创建接口
    @{layers}=    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=192.168.1.1    Gateway=192.168.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=192.168.1.2    Gateway=192.168.1.1
    # 创建RIP协议会话
    ${session_1}    Create Rip    Port=${Ports[0]}
    ${session_2}    Create Rip    Port=${Ports[1]}
    # RIP协议会话与接口绑定
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # RIP协议会话1创建IPv4 Route
    ${ipv4_route_1}    Create Rip Ipv4 Route    Session=${session_1}
    # RIP协议会话2创建IPv4 Route
    ${ipv4_route_2}    Create Rip Ipv4 Route    Session=${session_2}
    # 获取RIP协议绑定流端点对象
    ${point_1}    Get Rip Router From Route    Route=${ipv4_route_1}
    ${point_2}    Get Rip Router From Route    Route=${ipv4_route_2}
    # 创建RIP绑定流
    ${streams}    Add Stream    Type=binding    SrcPoints=${point_1}    DstPoints=${point_2}    Bidirection=True
    # 订阅统计
    @{types}    Create List    RipSessionBlockStats    RipSessionStats    StreamBlockStats
    subscribe_result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待RIP协议会话达到Full状态
    @{sessions}    Create List    ${session_1}    ${session_2}
    Wait Rip State    Sessions=${sessions}
    Advertise Rip    Sessions=${sessions}
    Sleep    5
    # 发送流量
    Start Stream
    Sleep    10
    Stop Stream
    # \ \ \ Withdraw Rip \ \ \ Sessions=${sessions}
    Sleep    5
    # \ \ \ Stop Protocol
    # \ \ \ Sleep \ \ \ 3
    # 获取RIP会话1统计
    &{result}    Get Rip Session Block Statistic    Session=${session_1}
    ${TxAdvertised}    Get From Dictionary    dictionary=&{Result}    key=TxAdvertised
    ${RxAdvertised}    Get From Dictionary    dictionary=&{Result}    key=RxAdvertised
    Log Many    ${result}
    # 获取RIP会话2统计
    &{result}    Get Rip Session Block Statistic    Session=${session_2}
    ${TxAdvertised}    Get From Dictionary    dictionary=&{Result}    key=TxAdvertised
    ${RxAdvertised}    Get From Dictionary    dictionary=&{Result}    key=RxAdvertised
    Log Many    ${result}
    # 获取流量1统计
    &{result}    Get Streamblock Statistic    Stream=${streams[0]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 获取流量2统计
    &{result}    Get Streamblock Statistic    Stream=${streams[1]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_PPPOE
    [Documentation]    测试目的 : 检查PPPOE协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建PPPOE协议及组播组
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    PPPOE
    [Setup]    setup
    # 创建接口
    @{layers1}=    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    @{layers2}=    Create List    eth    pppoe
    Edit Interface Stack    Interfaces=${interfaces}    Layers=${layers2}    Tops=${layers1}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=192.168.1.1    Gateway=192.168.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=192.168.1.2    Gateway=192.168.1.1
    # 创建pppoe协议会话
    ${session_1}    Create Pppoe    Port=${Ports[0]}    EmulationMode=client
    ${session_2}    Create Pppoe    Port=${Ports[1]}    EmulationMode=server
    # pppoe协议会话与接口绑定
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # 获取接口绑定流端点对象
    ${point_1}    Get Layer From Interfaces    Interfaces=${interface1}
    ${point_2}    Get Layer From Interfaces    Interfaces=${interface2}
    # 创建接口绑定流
    ${streams}    Add Stream    Type=binding    SrcPoints=${point_1}    DstPoints=${point_2}    Bidirection=True
    # 订阅统计
    @{types}    Create List    PppoePortStatistic    PppoeServerBlockStatistic    PppoeServerStatistic    PppoeClientBlockStatistic    PppoeClientStatistic    StreamBlockStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待PPPoE协议会话达到CONNECTED状态
    @{sessions}    Create List    ${session_1}    ${session_2}
    Wait Pppoe Ipcp State    Sessions=${sessions}
    Sleep    5
    # 发送流量
    Start Stream
    Sleep    10
    Stop Stream
    # \ \ \ Stop Protocol
    Sleep    3
    # 获取PPPOE端口统计
    &{result}    Get Pppoe Port Statistic    Port=${Ports[0]}
    Log Many    ${result}
    &{result}    Get Pppoe Port Statistic    Port=${Ports[1]}
    Log Many    ${result}
    # 获取PPPOE客户端 服务端统计
    &{result}    Get Pppoe Client Block Statistic    Session=${session_1}
    Log Many    ${result}
    &{result}    Get Pppoe Client Statistic    Session=${session_1}
    Log Many    ${result}
    &{result}    Get Pppoe Server Block Statistic    Session=${session_2}
    Log Many    ${result}
    &{result}    Get Pppoe Server Statistic    Session=${session_2}
    Log Many    ${result}
    # 获取流量1统计
    &{result}    Get Streamblock Statistic    Stream=${streams[0]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 获取流量2统计
    &{result}    Get Streamblock Statistic    Stream=${streams[1]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_DHCPV6
    [Documentation]    测试目的 : 检查DHCPV6协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建DHCPV6协议及组播组
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    DHCPV6
    [Setup]    setup
    # 创建接口
    @{layers1}=    Create List    ipv6
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv6Layer    Address=2011::2    Gateway=2011::1
    Edit Interface    Interface=${interface2}    Layer=IPv6Layer    Address=2011::1    Gateway=2011::2
    # 创建DHCPv6协议会话
    ${client}    Create Dhcpv6 Client    Port=${Ports[0]}
    ${server}    Create Dhcpv6 Server    Port=${Ports[1]}
    # DHCPv6协议会话与接口绑定
    Select Interface    Session=${client}    Interface=${interface1}
    Select Interface    Session=${server}    Interface=${interface2}
    # 获取DHCP Server地址池
    ${pool}    Create Dhcpv6 Server Address Pool    Sessions=${server}    StartAddress=2011::2
    # 获取接口绑定流端点对象
    ${point_1}    Get Layer From Interfaces    Interfaces=${interface1}    Layer=ipv6
    ${point_2}    Get Layer From Interfaces    Interfaces=${interface2}    Layer=ipv6
    # 创建DHCP绑定流
    ${streams}    Add Stream    Type=binding    SrcPoints=${point_1}    DstPoints=${point_2}    Bidirection=True
    # 订阅统计
    @{types}    Create List    StreamBlockStats    Dhcpv6PortStatistics    Dhcpv6ClientBlockStatistics    Dhcpv6ServerStatistics    Dhcpv6LeaseStatistics
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待PPPoE协议会话达到CONNECTED状态
    Wait Dhcpv6 Client State    Sessions=${client}
    Wait Dhcp Server State    Sessions=${server}
    Sleep    5
    # 发送流量
    Start Stream
    Sleep    10
    Stop Stream
    # \ \ \ Stop Protocol
    Sleep    3
    # 获取DHCP端口统计
    &{result}    Get Dhcpv6 Port Statistic    Port=${Ports[0]}
    Log Many    ${result}
    &{result}    Get Dhcpv6 Port Statistic    Port=${Ports[1]}
    Log Many    ${result}
    # 获取DHCP客户端统计
    &{result}    Get Dhcpv6 Client Block Statistic    Session=${client}
    Log Many    ${result}
    # 获取DHCP服务器统计
    &{result}    Get Dhcpv6 Server Statistic    Session=${server}
    Log Many    ${result}
    &{result}    Get Dhcpv6 Server Lease Statistic    Session=${server}    Pool=${pool}
    Log Many    ${result}
    # 获取流量1统计
    &{result}    Get Streamblock Statistic    Stream=${streams[0]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 获取流量2统计
    &{result}    Get Streamblock Statistic    Stream=${streams[1]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_L2TP
    [Documentation]    测试目的 : 检查L2TP协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建L2TP协议及组播组
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    L2TP
    [Setup]    setup
    # 创建接口
    @{layers1}    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    @{layers2}    Create List    eth    l2tp    ipv4
    Edit Interface Stack    Interfaces=${interface1}    Layers=${layers2}    Tops=${layers1}
    Edit Interface Stack    Interfaces=${interface2}    Layers=${layers2}    Tops=${layers1}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建L2TP协议会话
    ${l2tp_1}    Create L2tp    Port=${Ports[0]}
    ${l2tp_2}    Create L2tp    Port=${Ports[1]}    EmulationMode=LNS
    Select Interface    Session=${l2tp_1}    Interface=${interface1}
    Select Interface    Session=${l2tp_2}    Interface=${interface2}
    ${pppoe_1}    Create Pppoe    Port=${Ports[0]}    EmulationMode=CLIENT
    ${pppoe_2}    Create Pppoe    Port=${Ports[1]}    EmulationMode=SERVER
    Edit Pppoe    Session=${pppoe_1}    EmulationMode=PPPoL2TP
    Edit Pppoe    Session=${pppoe_2}    EmulationMode=PPPoL2TP
    Select Interface    Session=${pppoe_1}    Interface=${interface1}
    Select Interface    Session=${pppoe_2}    Interface=${interface2}
    # 获取接口绑定流端点对象
    ${point_1}    Get Layer From Interfaces    Interfaces=${interface1}
    ${point_2}    Get Layer From Interfaces    Interfaces=${interface2}
    # 创建接口绑定流
    ${streams}    Add Stream    Type=binding    SrcPoints=${point_1}    DstPoints=${point_2}    Bidirection=True
    # 订阅统计
    @{types}    Create List    L2tpPortStatistic    L2tpBlockStatistic    L2tpSessionStatistic    L2tpTunnelStatistic    PppoeClientStatistic    StreamBlockStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待PPPoE协议会话达到CONNECTED状态
    @{sessions}    Create List    ${l2tp_1}    ${l2tp_2}
    Wait L2tp State    Sessions=${sessions}
    Sleep    5
    # 发送流量
    Start Stream
    Sleep    10
    Stop Stream
    # \ \ \ Stop Protocol
    Sleep    3
    # 获取L2TP会话1统计
    &{result}    Get L2tp Port Statistic    Port=${Ports[0]}
    Log Many    ${result}
    &{result}    Get L2tp Port Statistic    Port=${Ports[1]}
    Log Many    ${result}
    &{result}    Get L2tp Session Statistic    Session=${l2tp_1}    NodeIndexInBlock=${1}
    Log Many    ${result}
    &{result}    Get L2tp Session Statistic    Session=${l2tp_2}    NodeIndexInBlock=${1}
    Log Many    ${result}
    &{result}    Get L2tp Block Statistic    Session=${l2tp_1}
    Log Many    ${result}
    &{result}    Get L2tp Block Statistic    Session=${l2tp_2}
    Log Many    ${result}
    &{result}    Get L2tp Tunnel Statistic    Session=${l2tp_1}    NodeIndexInBlock=${1}
    Log Many    ${result}
    &{result}    Get L2tp Tunnel Statistic    Session=${l2tp_2}    NodeIndexInBlock=${1}
    Log Many    ${result}
    # 获取流量1统计
    &{result}    Get Streamblock Statistic    Stream=${streams[0]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 获取流量2统计
    &{result}    Get Streamblock Statistic    Stream=${streams[1]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_802.1X
    [Documentation]    测试目的 : 检查802.1x协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建802.1x协议及组播组
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    802.1x
    [Setup]    setup
    # 创建接口
    @{layers1}=    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建802.1x协议会话
    ${session_1}    Create Dot1x    Port=${Ports[0]}
    ${session_2}    Create Dot1x    Port=${Ports[1]}
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # 订阅统计
    @{types}    Create List    Dot1xBlockStatistics    Dot1xPortStatistics    Dot1xStatistics
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待dotiq会话达到AUTHENTICATING状态
    @{sessions}    Create List    ${session_1}    ${session_2}
    Wait Dot1x State    Sessions=${sessions}    State=AUTHENTICATING
    Sleep    5
    # 获取802.1x会话1统计
    &{result}    Get Dot1x Port Statistic    Port=${Ports[0]}
    Log Many    ${result}
    &{result}    Get Dot1x Port Statistic    Port=${Ports[1]}
    Log Many    ${result}
    &{result}    Get Dot1x Block Statistic    Session=${session_1}
    Log Many    ${result}
    &{result}    Get Dot1x Block Statistic    Session=${session_2}
    Log Many    ${result}
    &{result}    Get Dot1x Statistic    Session=${session_1}    Index=${1}
    Log Many    ${result}
    &{result}    Get Dot1x Statistic    Session=${session_2}    Index=${1}
    Log Many    ${result}
    Stop Protocol
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_LDP
    [Documentation]    测试目的 : 检查LDP协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建LDP协议
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-004    LDP
    [Setup]    setup
    # 创建接口
    @{layers1}=    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建LDP协议会话
    ${session_1}    Create Ldp    Port=${Ports[0]}    DutIpv4Address=1.1.1.2
    ${session_2}    Create Ldp    Port=${Ports[1]}    DutIpv4Address=1.1.1.1
    # LDP协议会话与接口绑定
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # 创建LSP
    ${lsp_1}    Create Ldp Ipv4 Egress    Session=${session_1}
    ${lsp_2}    Create Ldp Ipv4 Egress    Session=${session_2}
    # 获取接口绑定流端点对象
    ${lsps}    Create List    ${lsp_1}    ${lsp_2}
    ${point}    Get Ldp Point From Lsp    Configs=${lsps}
    # 创建LDP绑定流
    ${streams}    Add Stream    Type=binding    SrcPoints=${point[0]}    DstPoints=${point[1]}    Bidirection=True
    # 订阅统计
    @{types}    Create List    StreamBlockStats    LdpSessionStatistic    LdpLspStatistic
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    #等待LDP协议协议会话状态正确
    @{sessions}    Create List    ${session_1}    ${session_2}
    Wait Ldp State    Sessions=${sessions}
    Sleep    5
    # 发送流量
    Start Stream
    Sleep    10
    Stop Stream
    # \ \ \ Stop Protocol
    Sleep    3
    # 获取LDP端口统计
    &{result}    Get Ldp Session Statistic    Session=${session_1}
    Log Many    ${result}
    &{result}    Get Ldp Session Statistic    Session=${session_2}
    Log Many    ${result}
    # 获取LDP客户端统计
    &{result}    Get Ldp Lsp Statistic    Session=${session_1}
    Log Many    ${result}
    &{result}    Get Ldp Lsp Statistic    Session=${session_2}
    Log Many    ${result}
    # 获取流量1统计
    &{result}    Get Streamblock Statistic    Stream=${streams[0]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 获取流量2统计
    &{result}    Get Streamblock Statistic    Stream=${streams[1]}
    ${TxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=TxStreamFrames
    ${RxStreamFrames}    Get From Dictionary    dictionary=&{Result}    key=RxStreamFrames
    Should Be Equal    ${TxStreamFrames}    ${RxStreamFrames}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_PCEP
    [Documentation]    测试目的 : 配置PCEP协议，检查统计
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建PCEP协议
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅SPCEP统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看PCEP统计信息
    ...
    ...    预期结果1: 步骤6中统计获取正常
    [Tags]    Tester-004    PCEP
    [Setup]    setup
    # 创建接口
    @{layers1}=    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建PCEP协议会话
    ${session_1}    Create Pcep    Port=${Ports[0]}    Role=PCC    Negotiation=True
    ${session_2}    Create Pcep    Port=${Ports[1]}    Role=PCE    Negotiation=False
    # PCEP协议会话与接口绑定
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # 创建LSP
    ${lsp_1}    Create Pcep Pcc Lsp    Sessions=${session_1}
    ${lsp_2}    Create Pcep Pce Lsp    Sessions=${session_2}
    # 订阅统计
    ${types}    Create List    PcepLspStatistic    PcepLspBlockStatistic    PcepPortStatistic    PcepSessionStatistic    PcepSessionBlockStatistic
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    #等待LDP协议协议会话状态正确
    @{sessions}    Create List    ${session_1}    ${session_2}
    Wait Pcep State    Sessions=${sessions}
    Sleep    5
    # 发送流量
    Start Stream
    Sleep    10
    Stop Stream
    # \ \ \ Stop Protocol
    Sleep    3
    # 获取PCEP端口统计
    &{result}    Get Pcep Lsp Statistic    Session=${session_1}    SessionId=${1}    Lsp=${lsp_1}    LspId=${1}
    Log Many    ${result}
    &{result}    Get Pcep Lsp Statistic    Session=${session_2}    SessionId=${1}    Lsp=${lsp_2}    LspId=${1}
    Log Many    ${result}
    # 获取PCEP客户端统计
    &{result}    Get Pcep Lsp Block Statistic    Session=${session_1}    SessionId=${1}    Lsp=${lsp_1}
    Log Many    ${result}
    &{result}    Get Pcep Lsp Block Statistic    Session=${session_2}    SessionId=${1}    Lsp=${lsp_2}
    Log Many    ${result}
    # 获取PCEP客户端统计
    &{result}    Get Pcep Port Statistic    Port=${Ports[0]}
    Log Many    ${result}
    &{result}    Get Pcep Port Statistic    Port=${Ports[1]}
    Log Many    ${result}
    # 获取PCEP客户端统计
    &{result}    Get Pcep Session Statistic    Session=${session_1}    SessionId=${1}
    Log Many    ${result}
    &{result}    Get Pcep Session Statistic    Session=${session_2}    SessionId=${1}
    Log Many    ${result}
    # 获取PCEP客户端统计
    &{result}    Get Pcep Session Block Statistic    Session=${session_1}
    Log Many    ${result}
    &{result}    Get Pcep Session Block Statistic    Session=${session_2}
    Log Many    ${result}

Protocol_802.3ah
    [Documentation]    测试目的 : 检查802.3ah协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建802.3ah协议及组播组
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-003    802.3ah
    [Setup]    setup
    # 创建接口
    @{layers1}=    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建802.3ah协议会话
    ${session_1}    Create Dot3ah    Port=${Ports[0]}
    ${session_2}    Create Dot3ah    Port=${Ports[1]}
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # 订阅统计
    @{types}    Create List    Dot3ahErrorEventStats    Dot3ahSessionStatistic
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待dot3ah会话达到AUTHENTICATING状态
    @{sessions}    Create List    ${session_1}    ${session_2}
    Wait Dot3ah State    Sessions=${sessions}    State=AUTHENTICATING
    Sleep    5
    # 获取802.3ah会话1统计
    ${result}    Get Dot3ah Error Event Stats    Session=${session_1}
    Log Many    ${result}
    ${result}    Get Dot3ah Error Event Stats    Session=${session_2}
    Log Many    ${result}
    ${result}    Get Dot3ah Session Statistic    Session=${session_1}
    Log Many    ${result}
    ${result}    Get Dot3ah Session Statistic    Session=${session_2}
    Log Many    ${result}
    Stop Protocol
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_802.1ag
    [Documentation]    测试目的 : 检查802.1ag协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建802.1ag协议及组播组
    ...
    ...    测试步骤3: 创建绑定流量
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息
    ...
    ...    预期结果1: 步骤6中所有流量收发包相等
    [Tags]    Tester-003    802.1ag
    [Setup]    setup
    # 创建接口
    @{layers1}    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建802.1ag协议会话
    ${session_1}    Create Dot1ag    Port=${Ports[0]}
    ${session_2}    Create Dot1ag    Port=${Ports[1]}
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # 创建802.1ag ma
    ${Ma}    Create Dot1ag Ma
    # 创建802.1ag mp
    Create Dot1ag Mp    Session=${session_1}    SelectMa=${Ma}
    Create Dot1ag Mp    Session=${session_2}    SelectMa=${Ma}
    # 订阅统计
    @{types}    Create List    Dot1agMpStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待dot1ag会话达到RUNNING状态
    @{sessions}    Create List    ${session_1}    ${session_2}
    Wait Dot1ag State    Sessions=${sessions}    State=RUNNING
    Sleep    5
    # 获取802.1ag会话1统计
    &{result}    Get Dot1ag Mp Stats    Session=${session_1}
    Log Many    &{result}
    ${result}    Get Dot1ag Mp Stats    Session=${session_2}
    Log Many    ${result}
    Stop Protocol
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_VXLAN
    [Documentation]    测试目的 : 检查VXLAN协议绑定流发送正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2;
    ...
    ...    测试步骤2: 创建VXLAN协议及组播组;
    ...
    ...    测试步骤3: 创建绑定流量;
    ...
    ...    测试步骤4: 订阅StreamBlockStats统计;
    ...
    ...    测试步骤5: 发送所有流量，等待一段时间;
    ...
    ...    测试步骤6: 停止所有流量，查看StreamBlockStats统计信息;
    [Tags]    Tester-002
    [Setup]    setup
    # 创建接口
    @{layers1}    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    ${interface3}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface4}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    Edit Interface    Interface=${interface3}    Layer=IPv4Layer    Address=2.1.1.1    Gateway=2.1.1.2
    Edit Interface    Interface=${interface4}    Layer=IPv4Layer    Address=2.1.1.2    Gateway=2.1.1.1
    # 创建VXLAN协议会话
    ${session_1}    create_vxlan    Port=${Ports[0]}
    ${session_2}    create_vxlan    Port=${Ports[1]}
    ${sessions}    Create List    ${session_1}    ${session_2}
    # VXLAN协议会话与接口绑定
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # 创建VXLAN Segment
    ${segment}    create_vxlan_segment    StartVni=10
    # 绑定VXLAN VM
    binding_vxlan_vm    Segments=${segment}    Interfaces=${interface3}
    binding_vxlan_vm    Segments=${segment}    Interfaces=${interface4}
    binding_vxlan_vtep    Vteps=${session_1}    Interfaces=${interface3}
    binding_vxlan_vtep    Vteps=${session_2}    Interfaces=${interface4}
    # 创建VXLAN绑定流
    ${point_1}    get_vxlan_vm_point    Vxlan=${session_1}
    ${point_2}    get_vxlan_vm_point    Vxlan=${session_2}
    ${stream}    add_stream    Type=binding    SrcPoints=${point_1}    DstPoints=${point_2}    Bidirection=True
    # 订阅统计
    @{types}    Create List    VxlanBindingStats    StreamBlockStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    start_protocol
    # 等待VXLAN协议会话达到STARTED状态
    wait_vxlan_state    Sessions=${sessions}
    # 发送流量
    start_stream
    Sleep    10
    stop_stream
    stop_protocol
    # 获取VXLAN会话统计
    ${result}    get_vxlan_statistic    Session=${session_1}
    Log Many    ${result}
    ${result}    get_vxlan_statistic    Session=${session_2}
    Log Many    ${result}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_Saa
    [Documentation]    测试目的 : 检查saa协议统计获取正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建saa协议;
    ...
    ...    测试步骤3: 启动协议，查看协议统计;
    ...
    ...    预期结果1: 步骤3中统计获取正确
    [Tags]    Tester-002
    [Setup]    setup
    # 创建接口
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=eth    Tops=ipv6
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=eth    Tops=ipv6
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv6Layer    Address=2022::2    Gateway=2022::3
    Edit Interface    Interface=${interface2}    Layer=IPv6Layer    Address=2022::3    Gateway=2022::2
    # 创建协议会话
    ${session_1}    Create Saa    Port=${Ports[0]}
    ${session_2}    Create Saa    Port=${Ports[1]}
    @{sessions}    Create List    ${session_1}    ${session_2}
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    # 订阅统计
    @{types}    Create List    SaaPortStatistics    SaaSessionBlockStatistics    SaaSessionStatistics
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待会话达到状态
    Wait Saa State    Sessions=${sessions}    State=IDLE
    Sleep    5
    # 获取统计
    &{result}    Get Saa Port Statistic    Port=${Ports[0]}
    Log Many    ${result}
    &{result}    Get Saa Session Block Statistic    Session=${session_1}
    Log Many    ${result}
    &{result}    Get Saa Session Statistic    Session=${session_1}    SessionId=1
    Log Many    ${result}
    Stop Protocol
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_Y1731
    [Documentation]    测试目的 : 检查y1731协议统计获取正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建y1731协议;
    ...
    ...    测试步骤3: 启动协议，查看协议统计;
    ...
    ...    预期结果1: 步骤3中统计获取正确
    [Tags]    Tester-002
    [Setup]    setup
    # 创建接口
    ${interface1}    Create Interface    Port=${Ports[0]}
    ${interface2}    Create Interface    Port=${Ports[1]}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    # 创建协议会话
    ${session_1}    Create Y1731    Port=${Ports[0]}
    ${session_2}    Create Y1731    Port=${Ports[1]}
    @{sessions}    Create List    ${session_1}    ${session_2}
    Select Interface    Session=${session_1}    Interface=${interface1}
    Select Interface    Session=${session_2}    Interface=${interface2}
    ${mp_1}    create_y1731_mp    Sessions=${session_1}
    ${mp_2}    create_y1731_mp    Sessions=${session_2}
    ${meg}    create_y1731_meg
    edit_y1731_mp    ${mp_1}    Meg=${meg}
    edit_y1731_mp    ${mp_2}    Meg=${meg}
    # 订阅统计
    @{types}    Create List    Y1731MegStats    Y1731MpStats    Y1731PortStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    Start Protocol
    # 等待会话达到状态
    wait_y1731_state    Sessions=${sessions}
    Sleep    5
    # 获取统计
    &{result}    get_y1731_port_statistic    Port=${Ports[0]}
    Log Many    ${result}
    &{result}    get_y1731_meg_statistic    Meg=${meg}    Port=${Ports[0]}
    Log Many    ${result}
    &{result}    get_y1731_mp_statistic    Mp=${mp_1}
    Log Many    ${result}
    Stop Protocol
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_LACP
    [Documentation]    测试目的 : 检查LACP统计获取正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建LACP;
    ...
    ...    测试步骤3: 启动协议，查看协议统计;
    ...
    ...    预期结果1: 步骤3中统计获取正确
    [Tags]    Tester-002
    [Setup]    setup
    #创建LACP
    ${Lacp_1}    create_lacp    Ports=${Ports[0]}
    ${Lacp_2}    create_lacp    Ports=${Ports[1]}
    # 订阅统计
    @{types}    Create List    LacpPortStats    LagPortStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    start_lacp_port    Ports=${Ports}
    Sleep    5
    # 获取统计
    ${result}    get_lacp_port_statistic    Port=${Ports[0]}
    Log Many    ${result}
    ${result}    get_lag_port_statistic    Lacp=${Lacp_1}
    Log Many    ${result}
    # 停止协议
    stop_lacp_port    Ports=${Ports}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_OpenFlow
    [Documentation]    测试目的 : 检查openflow统计获取正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建switch controller;
    ...
    ...    测试步骤3: 启动协议，查看协议统计;
    ...
    ...    预期结果1: 步骤3中统计获取正确
    [Tags]    Tester-002
    [Setup]    setup
    # 创建接口
    ${interface1}    Create Interface    Port=${Ports[0]}
    ${interface2}    Create Interface    Port=${Ports[1]}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    #创建协议
    ${switch}    create_openflow_switch    Port=${Ports[0]}
    ${controller}    create_openflow_controller    Port=${Ports[1]}
    select_interface    Session=${switch}    Interface=${interface1}
    select_interface    Session=${controller}    Interface=${interface2}
    # 创建desc
    ${controller_desc}    edit_controller_desc    Sessions=${switch}
    ${switch_desc}    edit_switch_desc    Sessions=${controller}
    # 订阅统计
    @{types}    Create List    OfpControllerStats    OfpSwitchDescStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    start_protocol
    Sleep    5
    # 获取统计
    ${result}    get_openflow_controller_statistic    Controller=${controller}
    Log Many    ${result}
    ${result}    get_openflow_switch_statistic    Switch=${switch_desc}
    Log Many    ${result}
    # 停止协议
    stop_protocol    Ports=${Ports}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_Ovsdb
    [Documentation]    测试目的 : 检查ovsdb统计获取正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 创建ovsdb;
    ...
    ...    测试步骤3: 启动协议，查看协议统计;
    ...
    ...    预期结果1: 步骤3中统计获取正确
    [Tags]    Tester-002
    [Setup]    setup
    # 创建接口
    @{layers1}    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    #创建协议
    ${ovsdb}    create_ovsdb    Port=${Ports[0]}
    select_interface    Session=${ovsdb}    Interface=${interface1}
    # 订阅统计
    @{types}    Create List    OvsdbResults
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    start_protocol
    wait_ovsdb_state    Sessions=${ovsdb}
    Sleep    2
    # 获取统计
    ${result}    get_ovsdb_statistic    Sessions=${ovsdb}
    Log Many    ${result}
    # 停止协议
    stop_protocol    Ports=${Ports}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}

Protocol_TWAMP
    [Documentation]    测试目的 : 检查TWAMP统计获取正常
    ...
    ...    测试步骤1: 预约两个自环端口Port_1、Port_2
    ...
    ...    测试步骤2: 两个端口分别创建client server;
    ...
    ...    测试步骤3: 启动协议，查看协议统计;
    ...
    ...    预期结果1: 步骤3中统计获取正确
    [Tags]    Tester-002
    [Setup]    setup
    # 创建接口
    @{layers1}    Create List    ipv4
    ${interface1}    Create Interface    Port=${Ports[0]}    Layers=${layers1}
    ${interface2}    Create Interface    Port=${Ports[1]}    Layers=${layers1}
    @{interfaces}    Create List    ${interface1}    ${interface2}
    Edit Interface    Interface=${interface1}    Layer=IPv4Layer    Address=1.1.1.1    Gateway=1.1.1.2
    Edit Interface    Interface=${interface2}    Layer=IPv4Layer    Address=1.1.1.2    Gateway=1.1.1.1
    #创建协议
    ${client}    create_twamp    Port=${Ports[0]}    ActiveClient=True    PeerIpv4Address=1.1.1.2
    ${server}    create_twamp    Port=${Ports[1]}    ActiveServer=True
    select_interface    Session=${client}    Interface=${interface1}
    select_interface    Session=${server}    Interface=${interface2}
    ${twamps}    Create List    ${client}    ${server}
    # 创建test session
    ${session_1}    edit_twamp_test_session    Twamps=${client}
    ${session_2}    edit_twamp_test_session    Twamps=${client}
    # 订阅统计
    @{types}    Create List    TwampClientStats    TwampServerStats
    Subscribe Result    Types=${types}
    # 保存配置文件
    save_case    Path=${TestFilePath}${TEST NAME}.xcfg
    # 启动协议
    twamp_start    Sessions=${twamps}
    wait_twamp_state    Sessions=${client}
    wait_twamp_state    Sessions=${server}    State=STARTED
    Sleep    2
    # 获取统计
    ${result}    get_twamp_client_statistic    Sessions=${client}
    Log Many    ${result}
    ${result}    get_twamp_server_statistic    Sessions=${server}
    Log Many    ${result}
    # 停止协议
    twamp_stop    Sessions=${twamps}
    # 释放端口资源
    ${Ports}    release_port    Locations=${Locations}
*** Keywords ***
setup
    # 初始化仪表
    init_tester    Product=${TesterProduct}
    # 创建端口，并预约端口
    ${Ports}    reserve_port    Locations=${Locations}    Force=True
    set suite variable    ${Ports}
