# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.6.1 Layer 3 Forwarding Rate
#
# Step			:	Test Step 1: Build the test environment according to the topology diagram;
#                   Test Step 2: Tester port1 address is 192.168.1.100/24, port2 address is 192.168.2.100/24;
#                   Test Step 3: DUT port1 address is 192.168.1.1/24, port2 address is 192.168.2.1/24;
#                   Test Step 4: The tester sends data from the port at maximum load with different frame lengths (64, 128, 256, 512, 1024, 1518 bytes), and the test duration is 30 seconds.
#
# Criteria    	:   Expected Result 1: Record the forwarding rate.
#
# Created by   	:  	Tester-001
#
# Tags   	    :  	performance
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


dirname, filename = os.path.split(os.path.abspath(__file__))
data = CustomData()
# 测试前下发配罿
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

    # 创建绑定流
    point_1 = get_layer_from_interfaces(Interfaces=interfaces_up, Layer='ipv4')
    point_2 = get_layer_from_interfaces(Interfaces=interfaces_down, Layer='ipv4')
    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    # 负载模式：Base On Port, （端口负载：, 负载单位：PERCENT 传输模式：Time
    edit_port_load_profile(Ports=[port_up, port_down],
                           LoadProfileType='PORT_BASE',
                           Unit='PERCENT',
                           TransmitMode="TIME",
                           Rate=cfg['arg']['load_profile']['default']['rate']['default'],
                           Seconds=cfg['arg']['load_profile']['default']['seconds']['default'])

    # 订阅统计视图
    subscribe_result(Types=['PortStats', 'StreamBlockStats'])

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        # 初始化一个空的DataFrame来存储所有数据
        printf(message='Test start')
        all_data = pd.DataFrame()
        for frame_size in cfg['arg']['stream']['default']['frame_size']['default']:
            # 修改帧长
            for s in streams:
                s.edit(FixedLength=frame_size)
            # 发送流量
            start_stream()
            time.sleep(3)
            df = get_streamblock_statistic()
            wait_stream_state(TimeOut=cfg['arg']['load_profile']['default']['seconds']['default'] + 3)
            time.sleep(3)
            result = get_streamblock_statistic()
            # 使用 concat 拼接 DataFrame
            df = pd.concat([df, result])
            # 重置索引
            df = df.reset_index(drop=True)
            # 添加一列帧长，全部值为当前循环的frame_length，并命名为'frame_length'
            # 注意：这里我们假设原始DataFrame中没有名为'frame_length'的列，或者即使有，我们也想要覆盖它
            df['FrameSize'] = frame_size
            # 但是，由于我们想要将'frame_length'放在第二列，我们需要重新排列列
            # 首先获取当前列名列表
            columns = df.columns.tolist()
            # 如果'FrameSize'已经在列表中，移除它以便我们可以重新插入到正确的位置
            if 'FrameSize' in columns:
                columns.remove('FrameSize')
            # 将'frame_length'插入到第二列的位置（索引为1）
            columns.insert(1, 'FrameSize')
            # 重新排序DataFrame的列
            df = df.reindex(columns=columns)
            # 将当前循环的数据追加到所有数据的DataFrame中
            all_data = pd.concat([all_data, df])
            # 重置all_data的索引，虽然这不是严格必要的，但可以保持索引的连续性
            all_data = all_data.reset_index(drop=True)
        # 使用tabulate库表格化输出DataFrame二维数据
        print('\n' + tabulate(all_data, headers='keys', tablefmt='psql') + '\n', flush=True)
        printf(message='Test completed')
        data.write_report(all_data)
        printf(message='Test data save successfully')

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
