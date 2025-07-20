
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
# 测试前下发配置
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
    port_tester_a_1 = ports[0]

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
    interface_tester_a_1 = create_interface(Port=port_tester_a_1, Layers=['ipv4'])

    # 配置接口Mac地址和IPv4地址
    edit_interface(Interface=interface_tester_a_1,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['mac_up_address']['default'])

    edit_interface(Interface=interface_tester_a_1,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_up_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    # 创建OSPF协议会话
    ospf_session = create_ospf(Port=port_tester_a_1)

    # 配置OSPF Area ID为合法值
    edit_ospf(Session=ospf_session,
              AreaId=cfg['arg']['ospf']['default']['area_id_valid']['default']
    )

    # OSPF协议会话与接口绑定
    select_interface(Session=ospf_session, Interface=interface_tester_a_1)

    # 订阅统计视图
    subscribe_result(Types=['Ospfv2SessionResultPropertySet'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 启动协议
        start_protocol()

        # 等待OSPF协议会话达到Full状态
        wait_ospf_adjacency_state(Sessions=[ospf_session], State='FULL')

        # 获取OSPF会话统计结果
        result = get_ospf_statistic(Session=ospf_session)
        print(result)

        adjacency_state = result.get('AdjacencyState', None)
        print('AdjacencyState: {}'.format(adjacency_state))

        if adjacency_state != 'Full':
            CustomData.verdict = 'fail'
            CustomData.errInfo += 'OSPF adjacency state is not FULL\n'

        # 停止协议
        stop_protocol()
        time.sleep(3)

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
