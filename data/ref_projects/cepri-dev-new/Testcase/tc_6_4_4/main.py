# -*- coding: utf-8 -*-
# =================================================================================
# Objective   	:   Test Objective : 6.4.4 Store-and-Forward Latency
#
# Step			:	Test Step 1: According to Figure 4, connect any two same-type ports of the switch to the tester;
#                   Test Step 2: Both ports simultaneously send data to each other under corresponding loads, test frame lengths are (64, 65, 256, 1024, 1518) bytes, test duration is 60s; set load rates: heavy load 95%, light load 10%;
#                   Test Step 3: Record the average store-and-forward latency for different frame lengths.
#
# Criteria    	:   Expected Result 1: The technical requirement is that the average latency should be less than 10μs.
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
        print("111",testbed['tester']['rtsm']['ip'])
        init_tester(Rtsm=testbed['tester']['rtsm']['ip'])
    else:
        init_tester()

    locations = get_locations(cfg['port'])
    # 创建端口，并预约端口
    ports = reserve_port(Locations=locations, Force=testbed['tester']['force']['default'], Debug=testbed['tester']['debug']['default'], WaitForStatusUp=False)
    port_up, port_down = ports
    print("port_up",port_up)
    print("port_down", port_down)
    # if testbed['nto']['enable']['default']:
    #     nto = NTO(host=testbed['nto']['ip']['default'], port=testbed['nto']['port']['default'], username=testbed['nto']['username']['default'], password=testbed['nto']['password']['default'], content_type='multipart/form-data')
    #     nto.actions_import(os.path.join(dirname, 'topu.ata'))
    for k, v in testbed['tester'].items():
        edit_port_kwargs = {}
        if k in edit_port_params:
            edit_port_kwargs.update({k: v['default']})
        if edit_port_kwargs:
            edit_port(Ports=ports, **edit_port_kwargs)
            time.sleep(10)

    # 创建接口
    interfaces_up = create_interface(Port=port_up, Layers=['eth'])
    interfaces_down = create_interface(Port=port_down, Layers=['eth'])
    print("interfaces_up", interfaces_up)
    print("interfaces_down", interfaces_down)
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

    wizard, Config = create_benchmark(Type='rfc2544', Items=['latency'])
    relate_benchmark_ports(Config=wizard, Ports=[port_up, port_down])
    benchmark_stream_use_exist(Config=wizard, Streams=streams)
    edit_benchmark_learning(Configs=Config, Frequency='once', EnableLearning=True)
    edit_benchmark_duration(Config=Config, Mode='second', Count=cfg['arg']['duration']['default'])
    edit_benchmark_frame(Config=Config, Type='custom', Custom=cfg['arg']['frame_size']['default'])
    edit_benchmark_traffic_load_loop(Config=Config, LoadUnit=cfg['arg']['traffic_load_loop']['default']['load_unit']['default'],
                                     LoadMode='custom', LoadCustom=cfg['arg']['traffic_load_loop']['default']['load_custom']['default'])
    expand_benchmark(Config=wizard)

    # 保存配置文件
    save_case(Path=os.path.join(temp_dir, 'xcfg', '{}.xcfg'.format(cfg['tc_no'])))
    printf(message='Save case to xcfg')

    if not testbed['tester']['debug']['default']:
        # 执行测试
        printf(message='Test start')
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