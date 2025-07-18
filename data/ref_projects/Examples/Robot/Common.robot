*** Settings ***
Library           Collections    # 内建库用于处理列表和字典
Library           TesterLibrary    # 测试仪表封装库

*** Variables ***
${TesterProduct}    DARYU    # 测试仪表产品类型支持BITAO和DARYU
${TestFilePath}    ${CURDIR}${/}xcfg${/}    # 测试过程中仪表生成的配置文件保存路径
${TestPcapPath}    ${CURDIR}${/}pcap${/}    # 测试过程中仪表下载的pcap报文文件保存路径
@{Locations}      //10.0.11.191/1/5    //10.0.11.191/1/6    # 测试仪表端口物理地址

*** Keywords ***
Case Setup
    init_tester

Case Teardown
    Shutdown Tester
