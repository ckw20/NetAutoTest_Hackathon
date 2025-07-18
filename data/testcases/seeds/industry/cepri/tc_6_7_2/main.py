# =================================================================================
# Objective   	:   测试目的 :  6.7.2互联网控制消息协议（ICMP）
#
# Step			:	测试步骤1: ：按图10搭建测试环境
#                   测试步骤2: tester port1 地址为 192.168.1.100/24，port2 地址为192.168.2.100/24
#                   测试步骤3: DUT port1 地址为192.168.1.1/24，port2 地址为192.168.2.1/24
#                   测试步骤4: tester port1 向 192.168.1.1 发送 ping 包，观察是否能收到正确的响应；
#                   测试步骤5: tester port1 向 192.168.3.1 发送 ip 包，观察是否能收到正确的响应（网络不可达，类型为3，编码为0）；
#                   测试步骤6: tester port1 向 192.168.1.1 发送 ip 包，协议号为100，观察是否能收到正确的响应（协议不可达，类型为3，编码为2）
#                   测试步骤7: tester port1 向 192.168.1.1 发送 ip 包，协议号为17端口为100，观察是否能收到正确的响应（端口不可达，类型为3，编码为3）
#
# Criteria    	:   预期结果1: 客户端能接收到正确的地址配置
#
# Created by   	:  	Tester-006
#
# Bugs   	    :  	None
# =================================================================================
import time
import sys
import os

dirname, filename = os.path.split(os.path.abspath(__file__))
ntolibrary_path = os.path.join(dirname, os.path.pardir, os.path.pardir)

# 将库的路径添加到 sys.path
if ntolibrary_path not in sys.path:
    sys.path.append(ntolibrary_path)

from CustomLibrary.common import cfg, testbed, setup, teardown, printf, temp_dir, get_locations, CustomData, edit_port_params
from NtoLibrary.common import NTO
from TesterLibrary.base import *
import pandas
import pyshark


dirname, filename = os.path.split(os.path.abspath(__file__))
data = CustomData()
# 测试前下发配罿
device = setup(cfg, testbed)

verdict = 'pass'
errInfo = ''

try:
    # 初始化仪表
    printf(message='Initialize tester')
    if testbed['tester']['rtsm']['ip']:
        init_tester(Rtsm=testbed['tester']['rtsm']['ip'])
    else:
        init_tester()

    locations = get_locations(cfg['port'])
    # 创建端口，并预约端口
    ports = reserve_port(Locations=locations, Force=testbed['tester']['force']['default'],
                         Debug=testbed['tester']['debug']['default'],
                         WaitForStatusUp=testbed['tester']['wait_for_status_up']['default'])
    port_up, port_down = ports
    if testbed['nto']['enable']['default']:
        nto = NTO(host=testbed['nto']['ip']['default'], port=testbed['nto']['port']['default'],
                  username=testbed['nto']['username']['default'], password=testbed['nto']['password']['default'],
                  content_type='multipart/form-data')
        nto.actions_import(os.path.join(dirname, 'topu.ata'))
    if not testbed['tester']['debug']['default']:
        for k, v in testbed['tester'].items():
            edit_port_kwargs = {}
            if k in edit_port_params:
                edit_port_kwargs.update({k: v['default']})
        if edit_port_kwargs:
            edit_port(Ports=ports, **edit_port_kwargs)
            time.sleep(10)
        if  testbed['tester']['wait_for_status_up']['default']:
            wait_port_state(ports)

    # 创建接口
    interfaces_up = create_interface(Port=port_up, Layers=['ipv4'])

    edit_interface(Interface=interfaces_up,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_up_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    # edit_port_load_profile(Ports=port_up, TransmitMode='TIME', Rate=1, Seconds=30)
    edit_port_load_profile(Ports=ports,
                           LoadProfileType='PORT_BASE',
                           Unit='FRAME_PER_SEC',
                           TransmitMode="CONTINUOUS",
                           Rate=100)
    sip_address_list = ['192.168.1.100']
    dip_address_list = ['192.168.3.1 ','192.168.1.1']

    # step5：tester port1 向 192.168.3.1 发送 ip 包，观察是否能收到正确的响应（网络不可达，类型为3，编码为0）；
    stream = add_stream(Ports=port_up, Names=f'step5')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ipv4(Stream=stream, Source=sip_address_list[0], Destination=dip_address_list[0], Gateway='192.168.1.1')

    # step6 tester port1 向 192.168.1.1 发送 ip 包，协议号为100，观察是否能收到正确的响应（协议不可达，类型为3，编码为2）
    stream = add_stream(Ports=port_up, Names=f'step6')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4'])
    edit_header_ipv4(Stream=stream, Source=sip_address_list[0], Destination=dip_address_list[1],Protocol=100, Gateway='192.168.1.1')

    # step7 tester port1 向 192.168.1.1 发送 ip 包，协议号为17端口为100，观察是否能收到正确的响应（端口不可达，类型为3，编码为3）
    stream = add_stream(Ports=port_up, Names=f'step7')
    edit_stream(Stream=stream, FixedLength=128)
    create_stream_header(Stream=stream, HeaderTypes=['ethernetii', 'ipv4', 'udp'])
    edit_header_ipv4(Stream=stream, Source=sip_address_list[0], Destination=dip_address_list[1],Protocol=17, Gateway='192.168.1.1')
    edit_header_udp(Stream=stream, SourcePort=100)

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')
    # 订阅统计
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试
        # tester port1 向 192.168.1.1 发送 ping 包，观察是否能收到正确的响应；
        ping = ipv4_ping(Interface=interfaces_up, IpAddr='192.168.1.1', PacketCount=5)
        if ping:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'ping is avalible',
                step=4, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'ping is not avalible',
                step=4, result=False)

        stream1, stream2, stream3 = get_streams(Ports=port_up)
        # 端口1测试
        net_unreached_pkt = []
        start_l3_learning()
        time.sleep(5)
        start_capture(Ports=port_up)
        # 启动流量测试
        start_stream(Type='stream', Objects=stream1)
        time.sleep(10)
        stop_stream()
        stop_capture(Ports=port_up)
        time.sleep(3)
        # 下载捕获到的报文
        packages_path = download_packages(Port=port_up, FileDir=f'{dirname}/pcap', FileName='step5', MaxCount=100)
        print(f'packages_path: {packages_path}')
        cap = pyshark.FileCapture(packages_path, keep_packets=True, display_filter='icmp.type == 3')
        for pkt in cap:
            if pkt.icmp.code == '0' and pkt.icmp.type == '3':
                net_unreached_pkt.append(pkt)

        if len(net_unreached_pkt) > 1:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'tester port1 收到网络不可达报文，类型为 3，编码为 0',
                step=5, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'tester port1 没有收到网络不可达报文',
                step=5, result=False)

        protocol_unreached_pkt = []
        start_l3_learning()
        time.sleep(5)
        start_capture(Ports=port_up)
        # 启动流量测试
        start_stream(Type='stream', Objects=stream2)
        time.sleep(10)
        stop_stream()
        stop_capture(Ports=port_up)
        time.sleep(3)
        # 下载捕获到的报文
        packages_path = download_packages(Port=port_up, FileDir=f'{dirname}/pcap', FileName='step6', MaxCount=100)
        print(f'packages_path: {packages_path}')
        cap = pyshark.FileCapture(packages_path, keep_packets=True, display_filter='icmp.type == 3')
        for pkt in cap:
            if pkt.icmp.code == '2' and pkt.icmp.type == '3':
                protocol_unreached_pkt.append(pkt)
        if len(protocol_unreached_pkt) > 1:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'tester port1 收到协议不可达报文，类型为 3，编码为 2',
                step=6, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'tester port1 没有收到协议不可达报文',
                step=6, result=False)

        port_unreached_pkt = []
        start_l3_learning()
        time.sleep(5)
        start_capture(Ports=port_up)
        # 启动流量测试
        start_stream(Type='stream', Objects=stream3)
        time.sleep(10)
        stop_stream()
        stop_capture(Ports=port_up)
        time.sleep(3)
        # 下载捕获到的报文
        packages_path = download_packages(Port=port_up, FileDir=f'{dirname}/pcap', FileName='step7', MaxCount=100)
        print(f'packages_path: {packages_path}')
        cap = pyshark.FileCapture(packages_path, keep_packets=True, display_filter='icmp.type == 3')
        for pkt in cap:
            if pkt.icmp.code == '3' and pkt.icmp.code == '3':
                port_unreached_pkt.append(pkt)

        if len(port_unreached_pkt) > 1:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'tester port1 收到端口不可达报文，类型为 3，编码为 3',
                step=7, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'tester port1 没有收到端口不可达报文',
                step=7, result=False)

        # 测试结束
        printf(message='Test completed')

        # 释放端口资源
        release_port(locations)

except Exception as e:
    CustomData.verdict = 'fail'
    CustomData.errInfo = repr(e)
finally:
    # 关闭仪表进程
    shutdown_tester()
    # 测试结束清除配置
    teardown(cfg, testbed)
    print(f'errInfo:\n{CustomData.errInfo}', flush=True)
    print(f'verdict:{CustomData.verdict}', flush=True)
