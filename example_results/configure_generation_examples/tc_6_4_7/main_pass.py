# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.4.7 Address Learning Rate
#
# Step			:	Test Step 1: According to RFC 2889, connect three ports of the switch to the tester, namely port 1 (test port), port 2 (learning port), port 3 (monitor port), see Figure 5;
#                   Test Step 2: The test method adopts the standard test method of RFC2889.
#
# Criteria    	:   Expected Result 1: The technical requirement is not less than 1000 frames/s.
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
    port_up, port_down, port_monitor = ports
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

    # =============== *选择测试项* ===============
    wizard, Config = create_benchmark(Type='RFC2889', Items=['addressLearningRate'])

    # =============== *选择端口* ===============
    relate_benchmark_ports(Config=wizard, Ports=[port_up, port_down, port_monitor])

    # =============== *配置端点* ===============
    interfaces_up = create_interface(Port=port_up, Layers=['eth'])
    interfaces_down = create_interface(Port=port_down, Layers=['eth'])
    edit_interface(Interface=interfaces_up,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['up']['default'])

    edit_interface(Interface=interfaces_down,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['down']['default'])

    # =============== *配置流* ===============
    point_1 = get_layer_from_interfaces(Interfaces=interfaces_up, Layer='eth')
    point_2 = get_layer_from_interfaces(Interfaces=interfaces_down, Layer='eth')
    streams = create_benchmark_streams(Config=wizard, Items=Config, Type='eth', SrcPoints=point_1, DstPoints=point_2, Monitors=port_monitor, Bidirectional=False)

    # =============== *配置测试选项* ===============
    edit_benchmark_latency(Configs=Config, Type='FIFO', DelayBefore=2, DelayAfter=10)

    # =============== *地址缓存容量参数设置* ===============
    # 试验次数
    edit_benchmark_duration(Config=Config, Trial=1)
    # 帧长设置
    edit_benchmark_frame(Config=Config, Type='custom', Custom=cfg['arg']['frame_size']['default'])

    # 地址学习速率和地址数量
    edit_benchmark_address_learning_rate(Config=Config,
                                         MinRateCount=cfg['arg']['learning_capacity']['default']['min_rate_count']['default'],
                                         MaxRateCount=cfg['arg']['learning_capacity']['default']['max_rate_count']['default'],
                                         InitRateCount=cfg['arg']['learning_capacity']['default']['init_rate_count']['default'],
                                         Resolution=cfg['arg']['learning_capacity']['default']['resolution']['default'],
                                         AgingTime=cfg['arg']['learning_capacity']['default']['aging_time']['default'],
                                         AddressCount=cfg['arg']['learning_capacity']['default']['address_count']['default'])

    # =============== *生成智能脚本* ===============
    expand_benchmark(Config=wizard)

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        # 执行测试
        printf(message='Test start')
        db = run_benchmark(Mode=0, Timer=3600, Analyzer=testbed['tester']['analyzer']['default'])
        df = get_benchmark_result(DB=db, Type='RFC2889', ReturnType='dataframe')
        # 使用tabulate库表格化输出DataFrame二维数据
        print('\n' + tabulate(df, headers='keys', tablefmt='psql') + '\n', flush=True)
        printf(message='Test completed')
        data.write_report(df)
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
