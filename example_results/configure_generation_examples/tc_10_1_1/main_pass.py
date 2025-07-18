import time
import sys
import os

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

    port_a, port_b = ports
    # 创建接口
    interface_a = create_interface(Port=port_a, Layers=['ipv4'])
    interface_b = create_interface(Port=port_b, Layers=['ipv4'])
    edit_interface(Interface=interface_a,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['mac_up_address']['default'])

    edit_interface(Interface=interface_b,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['mac_down_address']['default'])

    edit_interface(Interface=interface_a,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_up_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_up_gateway']['default'])

    edit_interface(Interface=interface_b,
                   Layer='IPv4Layer',
                   Address=cfg['arg']['interface']['default']['ipv4_down_address']['default'],
                   Gateway=cfg['arg']['interface']['default']['ipv4_down_gateway']['default'])

    # 创建流量
    src_point = get_layer_from_interfaces(Interfaces=[interface_a], Layer='ipv4')
    dst_point = get_layer_from_interfaces(Interfaces=[interface_b], Layer='ipv4')

    stream = add_stream(Type='binding', SrcPoints=src_point, DstPoints=dst_point, Bidirection=False)

    # 订阅StreamBlockStats统计视图
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试
        
        ipv4_ping(Interface=interface_a, IpAddr='192.168.1.1', PacketCount=5)
        ipv4_ping(Interface=interface_b, IpAddr='192.168.2.1', PacketCount=5)
        ipv4_ping(Interface=interface_a, IpAddr='192.168.1.100', PacketCount=5)
        ipv4_ping(Interface=interface_a, IpAddr='192.168.2.100', PacketCount=5)
    
        # 清空统计计数
        clear_result()
        # 启动流量测试
        start_protocol()
        time.sleep(5)
        start_stream()
        time.sleep(10)
        stop_stream()
        time.sleep(5)
        stop_protocol()
        
        # 获取流量统计结果
        Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'RxLossStreamFrames',
                                                                    'RealtimeLossRate'])
        if Result['RxStreamFrames'] > 0 and Result['RxLossStreamFrames'] == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'测试仪端口 B 处应可以观察到数据流量', step=1, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'测试仪端口 B 处没有观察到数据流量', step=1, result=False)
        

        # 在被测设备端口 2 上配置 ACL，拒绝该接口所有出方向流量
        cmd_cfg = '_'.join('DeviceA_Step2'.split('_')[1:])
        for _ in range(3):
            flag = device['DeviceA'].execute(row=cmd_cfg)
            if flag:
                break

        # 清空统计计数
        clear_result()
        # 启动流量测试
        start_protocol()
        time.sleep(5)
        start_stream()
        time.sleep(10)
        stop_stream()
        time.sleep(5)
        stop_protocol()
        time.sleep(5)
        # 获取流量统计结果
        Result = get_streamblock_statistic(Stream=stream, StaItems=['StreamBlockID', 'RxPortID', 'TxStreamFrames',
                                                                    'RxStreamFrames', 'RxLossStreamFrames',
                                                                    'RealtimeLossRate'])
        if Result['RxStreamFrames'] == 0:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'测试仪端口 B 处应无流量', step=2, result=True)
        else:
            CustomData.verdict, CustomData.errInfo = printf(
                message=f'测试仪端口 B 处仍有流量', step=2, result=False)

        # 释放端口资源
        release_port(locations)
        printf(message='Test completed')

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
