
import sys
import os
import time

dirname, filename = os.path.split(os.path.abspath(__file__))
ntolibrary_path = os.path.join(dirname, os.path.pardir, os.path.pardir)

# 将库的路径添加到 sys.path
if ntolibrary_path not in sys.path:
    sys.path.append(ntolibrary_path)

from CustomLibrary.common import cfg, testbed, setup, teardown, printf, temp_dir, get_locations, CustomData, edit_port_params
from TesterLibrary.base import *

dirname, filename = os.path.split(os.path.abspath(__file__))
data = CustomData()
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
    port_up = ports[0]

    if not testbed['tester']['debug']['default']:
        for k, v in testbed['tester'].items():
            edit_port_kwargs = {}
            if k in edit_port_params:
                edit_port_kwargs.update({k: v['default']})
        if edit_port_kwargs:
            edit_port(Ports=ports, **edit_port_kwargs)
            time.sleep(10)
        if testbed['tester']['wait_for_status_up']['default']:
            wait_port_state(ports, State="UP")

    # 创建接口
    interfaces_up = create_interface(Port=port_up, Layers=['ipv4'])

    edit_interface(Interface=interfaces_up,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['mac_up_address']['default'])

    edit_interface(Interface=interfaces_up,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_up_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    # 创建OSPFv2协议会话对象
    session_1 = create_ospf(Port=port_up)
    
    # 修改OSPF HelloInterval值
    edit_ospf(Session=session_1, HelloInterval=cfg['arg']['hello_interval']['default']['tester_hello_interval']['default'])

    # OSPFv2协议会话与接口绑定
    select_interface(Session=session_1, Interface=interfaces_up)

    # 订阅统计视图
    subscribe_result(Types=['Ospfv2SessionResultPropertySet'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        
        # 启动OSPF协议
        start_protocol()
        
        # 等待OSPF邻接状态达到指定状态 (应保持在DOWN或INIT)
        adjacency_established = wait_ospf_adjacency_state(
            Sessions=[session_1],
            State=["FULL", "DOWN", "INIT"],
            Interval=1,
            TimeOut=60
        )
        time.sleep(60)

        if adjacency_established:
            verdict = 'fail'
            errInfo += 'OSPF adjacency was established unexpectedly.\n'
        else:
            printf(message='OSPF adjacency was NOT established as expected.')

        # 获取OSPF统计信息
        result = get_ospf_statistic(Session=session_1)
        print(result)
        AdjacencyState = result.get('AdjacencyState', 'UNKNOWN')
        print(f'AdjacencyState: {AdjacencyState}')

        if AdjacencyState not in ['Down', 'Init']:
            verdict = 'fail'
            errInfo += f'Unexpected AdjacencyState: {AdjacencyState}\n'

        # 停止协议
        stop_protocol()

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
