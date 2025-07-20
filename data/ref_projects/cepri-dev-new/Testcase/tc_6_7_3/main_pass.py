# =================================================================================
# Objective   	:   Test Objective : 6.7.3 Dynamic Host Configuration Protocol (DHCP)
#
# Step			:	Test Step 1: Build the test environment according to Figure 10
#                   Test Step 2: DUT port1 address is 192.168.1.1/24, enable DHCP server on DUT, set as DHCP server, configure address pool 192.168.1.2~192.168.1.254;
#                   Test Step 3: tester port1 acts as DHCP client, sends DHCP request
#                   Test Step 4: Observe whether the client can receive the correct address configuration
#
# Criteria    	:   Expected Result 1: The client can receive the correct address configuration
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

from CustomLibrary.common import cfg, testbed, setup, teardown, printf, temp_dir, get_locations, CustomData, \
    edit_port_params
from NtoLibrary.common import NTO
from TesterLibrary.base import *
import pandas

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
        if testbed['tester']['wait_for_status_up']['default']:
            wait_port_state(ports)

    # 创建接口
    interfaces_up = create_interface(Port=port_up, Layers=['ipv4'])

    edit_interface(Interface=interfaces_up,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_up_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])
    # 创建DHCPv4协议会话
    client = create_dhcp_client(Port=port_up)

    # DHCPv4协议会话与接口绑定
    select_interface(Session=client, Interface=interfaces_up)

    # # 获取DHCP Server地址池
    # configDict = get_configs(Configs='Dhcpv4AddressPool')
    # dhcpv4AddressPool = list(configDict.values())[0]
    # edit_configs(Configs=dhcpv4AddressPool, PoolAddressStart='192.168.1.2', PrefixLength=19, PoolAddressCount=253)

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试
        # 启动协议
        start_protocol()
        # dhcp_bind(Sessions=client)
        # 等待DHCP协议协议会话状态正确
        result = wait_dhcp_client_state(Sessions=client)

        if result:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'The State Of Dhcp is Bound', step=4, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'The State Of Dhcp is not Bound', step=4, result=False)

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
