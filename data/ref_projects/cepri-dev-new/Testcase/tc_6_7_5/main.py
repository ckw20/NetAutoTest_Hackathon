# =================================================================================
# Objective   	:   Test Objective : 6.7.5 Routing Information Protocol (RIP)
#
# Step			:	Test Step 1: According to Figure 4, arbitrarily select two switch ports as test ports;
#                   Test Step 2: tester port1 IP address is 192.168.1.100/24, port2 is 192.168.2.100/24;
#                   Test Step 3: DUT1 port1 IP address is 192.168.1.1/24, port2 IP address is 192.168.2.1/24;
#                   Test Step 4: Configure RIPv2 routing protocol on DUT;
#                   Test Step 5: tester port1 sends RIPv2 response packets with destination multicast address 224.0.0.9 and UDP port 520, route tag 2, RIP entry 192.168.4.0/255.255.255.0/8, period 1s; observe DUT routing table changes and whether tester port2 receives routing update packets;
#                   Test Step 6: Stop sending packets from step 5, tester port1 sends RIPv2 response packets with route tag 2, RIP entry 192.168.4.0/255.255.255.0/6, period 1s; observe DUT routing table changes and whether tester port2 receives routing update packets;
#                   Test Step 7: Stop sending packets from step 6, tester port1 sends RIPv2 response packets with route tag 2, RIP entry 192.168.4.0/255.255.255.0/10, period 1s; observe DUT routing table changes and whether tester port2 receives routing update packets.
#
# Criteria    	:   Expected Result 1:
#
# Created by   	:  	Tester-006
#
# Bugs   	    :  	None
# =================================================================================
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
    ports = reserve_port(Locations=locations, Force=testbed['tester']['force']['default'], Debug=testbed['tester']['debug']['default'], WaitForStatusUp=False)
    port_up, port_down = ports
    if testbed['nto']['enable']['default']:
        nto = NTO(host=testbed['nto']['ip']['default'], port=testbed['nto']['port']['default'], username=testbed['nto']['username']['default'], password=testbed['nto']['password']['default'], content_type='multipart/form-data')
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
    interfaces_down = create_interface(Port=port_down, Layers=['ipv4'])
    edit_interface(Interface=interfaces_up,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['mac_up_address']['default'])

    edit_interface(Interface=interfaces_down,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['mac_down_address']['default'])

    edit_interface(Interface=interfaces_up,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_up_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    edit_interface(Interface=interfaces_down,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_down_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_down_gateway']['default'])

    # 创建RIP协议会话
    session_1 = create_rip(Port=port_up)
    session_2 = create_rip(Port=port_down)

    # RIP协议会话与接口绑定
    select_interface(Session=session_1, Interface=interfaces_up)
    select_interface(Session=session_2, Interface=interfaces_down)

    #创建流量
    port1, port2 = ports

    # 订阅统计视图
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')


    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试
        # 启动协议

        route = create_rip_ipv4_route(Session=session_1, StartIpv4Prefix='192.168.4.0', Increment=8)
        start_protocol()
        wait_rip_state(Sessions=[session_1, session_2])
        start_capture(Ports=port2)
        advertise_rip(Sessions=session_1)
        time.sleep(3)
        stop_capture(Ports=port2)
        time.sleep(3)
        # 下载捕获到的报文
        packages_path = download_packages(Port=port2, FileDir=f'{dirname}/pcap', FileName='step6', MaxCount=100)
        print(f'packages_path: {packages_path}')
        cap = pyshark.FileCapture(packages_path, keep_packets=True, display_filter='rip.version == 1')
        for pkt in cap:
            if pkt.rip.ip == '192.168.4.0':
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'tester port2 收到路由更新报文',
                    step=6, result=True)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'tester port2 没有收到路由更新报文',
                    step=6, result=False)

        stop_protocol()
        route.Increment = 6
        save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
        start_protocol()
        wait_rip_state(Sessions=[session_1, session_2])
        start_capture(Ports=port2)
        advertise_rip(Sessions=session_1)
        time.sleep(3)
        stop_capture(Ports=port2)
        time.sleep(3)
        # 下载捕获到的报文
        packages_path = download_packages(Port=port2, FileDir=f'{dirname}/pcap', FileName='step7', MaxCount=100)
        print(f'packages_path: {packages_path}')
        cap = pyshark.FileCapture(packages_path, keep_packets=True, display_filter='rip.version == 1')
        for pkt in cap:
            if pkt.rip.ip == '192.168.4.0':
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'tester port2 收到路由更新报文',
                    step=6, result=True)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'tester port2 没有收到路由更新报文',
                    step=6, result=False)

        stop_protocol()
        route.Increment = 10
        start_protocol()
        wait_rip_state(Sessions=[session_1, session_2])
        start_capture(Ports=port2)
        advertise_rip(Sessions=session_1)
        time.sleep(3)
        stop_capture(Ports=port2)
        time.sleep(3)
        # 下载捕获到的报文
        packages_path = download_packages(Port=port2, FileDir=f'{dirname}/pcap', FileName='step8', MaxCount=100)
        print(f'packages_path: {packages_path}')
        cap = pyshark.FileCapture(packages_path, keep_packets=True, display_filter='rip.version == 1')
        for pkt in cap:
            if pkt.rip.ip == '192.168.4.0':
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'tester port2 收到路由更新报文',
                    step=6, result=True)
            else:
                CustomData.verdict, CustomData.errInfo = printf(
                    message=f'tester port2 没有收到路由更新报文',
                    step=6, result=False)
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
