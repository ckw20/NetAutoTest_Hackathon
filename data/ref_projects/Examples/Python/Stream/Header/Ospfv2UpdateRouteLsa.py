# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发ospfv2 link state update报文统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 端口Port_1创建一条流量StreamTemplate_1;
#                   测试步骤3: 修改流量StreamTemplate_1的ospfv2 link state update头部内容;
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

locations = ['//10.0.11.191/1/13', '//10.0.11.191/1/14'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口

    Port_UP, Port_Down = reserve_port(Locations=locations)

    # 创建流量

    stream = add_stream(Ports=Port_UP, FixedLength=256)

    # 修改流量报文头部

    create_stream_header(Stream=stream, HeaderTypes=['EthernetII', 'IPv4', 'ospfv2linkstateupdate'])

    # 修改ospfv2 link state update头部，添加一个Router LSA

    LsaHeaders = ['Router']
    edit_header_ospfv2_update(Stream=stream, Level=0,
                              RouterID='10.1.1.2',
                              AreaID='0.0.0.2',
                              AuthValue2=1,
                              LsaHeaders=LsaHeaders,
                              )

    # 修改ospfv2 link state update头部，Router LSA内容，并添加4个Lsa Link即RouterLsaLinkCount=4

    edit_header_ospfv2_update_lsa(Stream=stream, Level=0,
                                  Index=0,
                                  Type='Router',
                                  LinkStateId='10.1.0.1',
                                  AdvertisingRouter='10.1.0.2',
                                  RouterLsaLinkCount=4,
                                  )

    # 修改ospfv2 link state update头部，Router LSA中，第一个RouterLsaLinkCount内容即Index=0

    edit_header_ospfv2_update_route_lsa_link(Stream=stream, Level=0,
                                             LsaIndex=0,
                                             Index=0,
                                             LinkId='10.1.0.0',
                                             LinkData='255.255.255.255',
                                             RouterLsaLinkType=3,
                                             NumRouterLsaTosMetrics=10,
                                             )

    # 修改ospfv2 link state update头部，Router LSA中，第二个RouterLsaLinkCount内容即Index=1

    edit_header_ospfv2_update_route_lsa_link(Stream=stream, Level=0,
                                             LsaIndex=0,
                                             Index=1,
                                             LinkId='10.2.0.0',
                                             LinkData='255.255.0.0',
                                             RouterLsaLinkType=2,
                                             NumRouterLsaTosMetrics=10,
                                             )

    # 修改ospfv2 link state update头部，Router LSA中，第三个RouterLsaLinkCount内容即Index=2

    edit_header_ospfv2_update_route_lsa_link(Stream=stream, Level=0,
                                             LsaIndex=0,
                                             Index=2,
                                             LinkId='10.3.0.0',
                                             LinkData='255.255.0.0',
                                             RouterLsaLinkType=4,
                                             NumRouterLsaTosMetrics=10,
                                             )

    # 修改ospfv2 link state update头部，Router LSA中，第四个RouterLsaLinkCount内容即Index=3

    edit_header_ospfv2_update_route_lsa_link(Stream=stream, Level=0,
                                             LsaIndex=0,
                                             Index=3,
                                             LinkId='10.4.0.0',
                                             LinkData='255.255.0.0',
                                             RouterLsaLinkType=1,
                                             NumRouterLsaTosMetrics=10,
                                             )

    # 订阅StreamBlockStats统计视图

    subscribe_result(Types=['StreamBlockStats'])

    # 保存配置文件

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 启动抓包，发送流量

    start_capture()

    start_stream()

    time.sleep(10)

    stop_stream()

    stop_capture()

    time.sleep(3)

    # 下载捕获到的报文
    packages_path = download_packages(Port=Port_Down, FileDir=f'{dirname}/pcap', FileName=filename, MaxCount=100)
    print(f'packages_path: {packages_path}')

    # 获取流量StreamBlockStats，并判断流量收发是否正确

    result = get_streamblock_statistic(Stream=stream)
    print(result)
    TxStreamFrames = result['TxStreamFrames']
    RxStreamFrames = result['RxStreamFrames']
    print('TxStreamFrames: {}'.format(TxStreamFrames))
    print('RxStreamFrames: {}'.format(RxStreamFrames))

    if TxStreamFrames != RxStreamFrames:
        verdict = 'fail'
        errInfo += '{} TxStreamFrames({}) is not equal to RxStreamFrames({})\n'.format(stream, TxStreamFrames,
                                                                                       RxStreamFrames)

    # 释放端口资源

    result = release_port(Locations=locations)

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
