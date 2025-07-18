# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   测试目的 : 6.4.3 端口吞吐量
#
# Step			:	测试步骤1: 按照 RFC 2544 中规定，将交换机任意两个同类型端口与测试仪相连接，见图 3；
#                   测试步骤2: 配置流量发生器：测试帧长度分别为（64、65、256、1024、1518）字节；
#                   测试步骤3: 测试时间为 60s。
#
# Criteria    	:   预期结果1: 技术要求吞吐量为100%。
#
# Created by   	:  	Tester-001
#
# Tags   	    :  	performance
# =================================================================================
import sys
import os
import time

start_time=time.time()

dirname, filename = os.path.split(os.path.abspath(__file__))
ntolibrary_path = os.path.join(dirname, os.path.pardir, os.path.pardir)

# 将库的路径添加到 sys.path
if ntolibrary_path not in sys.path:
    sys.path.append(ntolibrary_path)

from CustomLibrary.common import cfg, testbed, setup, teardown, printf, temp_dir, get_locations, CustomData, edit_port_params
# from NtoLibrary.common import NTO
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
    # if testbed['nto']['enable']['default']:
    #     nto = NTO(host=testbed['nto']['ip']['default'], port=testbed['nto']['port']['default'], username=testbed['nto']['username']['default'], password=testbed['nto']['password']['default'], content_type='multipart/form-data')
    #     nto.actions_import(os.path.join(dirname, 'topu.ata'))
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
    interfaces_up = create_interface(Port=port_up, Layers=['eth'])
    interfaces_down = create_interface(Port=port_down, Layers=['eth'])
    edit_interface(Interface=interfaces_up,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['up']['default'])

    edit_interface(Interface=interfaces_down,
                   Layer='EthIILayer',
                   Address=cfg['arg']['interface']['default']['down']['default'])

    # 创建绑定流
    point_1 = get_layer_from_interfaces(Interfaces=interfaces_up, Layer='eth')
    point_2 = get_layer_from_interfaces(Interfaces=interfaces_down, Layer='eth')
    streams = add_stream(Type='binding', SrcPoints=point_1, DstPoints=point_2, Bidirection=True)

    wizard, Config = create_benchmark(Type='rfc2544', Items=['throughput'])
    relate_benchmark_ports(Config=wizard, Ports=[port_up, port_down])
    benchmark_stream_use_exist(Config=wizard, Streams=streams)
    edit_benchmark_learning(Configs=Config, Frequency='once', EnableLearning=True)
    edit_benchmark_duration(Config=Config, Mode='second', Count=cfg['arg']['duration']['default'])
    edit_benchmark_frame(Config=Config, Type='custom', Custom=cfg['arg']['frame_size']['default'])
    edit_benchmark_search(Config=Config, Mode='binary', Init=cfg['arg']['search']['default']['init']['default'],
                          Lower=cfg['arg']['search']['default']['lower']['default'], Upper=cfg['arg']['search']['default']['upper']['default'])
    expand_benchmark(Config=wizard)

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        printf(message='Test start')
        # 执行测试
        db = run_benchmark(Mode=0, Timer=3600, Analyzer=testbed['tester']['analyzer']['default'])
        df = get_benchmark_result(DB=db, Type='RFC2544', ReturnType='dataframe')
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


end_time=time.time()
print("用时",end_time-start_time)