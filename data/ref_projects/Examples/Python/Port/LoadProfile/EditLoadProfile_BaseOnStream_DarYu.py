# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表负载模式为Base On Stream负载配置设置成功
#
# Step			:	测试步骤1: 预约4个离线端口;
#                   测试步骤2: 设置端口负载模式：Base On Stream,并设置负载配置各个类型参数;
#
# Criteria    	:   预期结果1: 步骤2中端口负载配置设置成功;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :
# =================================================================================

from TesterLibrary.base import *


Product = 'DarYu'
locations = [
    '//10.0.11.191/1/1',
    '//10.0.11.191/1/2',
    '//10.0.11.191/1/3',
    '//10.0.11.191/1/4',
]
verdict = 'pass'
errInfo = ''
try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)
    # 创建端口，并预约端口
    Ports = reserve_port(Locations=locations, Debug=True)
    if Product.lower() == 'daryu':

        # =============== *设置模式1* ===============
        # 负载模式：Base On Stream,  传输模式：Continuous, （突发报文数：10, 突发间隔：100, 突发间隔单位: ns）
        edit_port_load_profile(Ports=Ports[0],
                               LoadProfileType='STREAM_BASE',
                               TransmitMode="CONTINUOUS",
                               BurstSize=10,
                               InterFrameGap=100,
                               InterFrameGapUnit='NS')
        # 创建流量
        stream = add_stream(Ports=Ports[0], FixedLength=256)
        # 负载单位：Percent(%) 速率：5
        edit_stream_load_profile(Streams=stream, Unit='PERCENT', Rate=5)

        # =============== *设置模式2* ===============
        # 负载模式：Base On Stream, 传输模式：Burst, （（突发报文数：15, 突发间隔：110, 突发间隔单位: us , 突发次数: 10）
        edit_port_load_profile(Ports=Ports[1],
                               LoadProfileType='STREAM_BASE',
                               TransmitMode="BURST",
                               BurstSize=15,
                               InterFrameGap=110,
                               InterFrameGapUnit='US',
                               BurstCount=10)
        # 创建流量
        stream = add_stream(Ports=Ports[1], FixedLength=256)
        # 负载单位：Frames per Second 速率：5
        edit_stream_load_profile(Streams=stream, Unit='FRAME_PER_SEC', Rate=10)
        
        # =============== *设置模式3* ===============
        # 负载模式：Base On Stream, 传输模式：Time, （突发报文数：20, 突发间隔：120, 突发间隔单位: ms, 发送时间：15）
        edit_port_load_profile(Ports=Ports[2],
                               LoadProfileType='STREAM_BASE',
                               TransmitMode="TIME",
                               BurstSize=15,
                               InterFrameGap=120,
                               InterFrameGapUnit='MS',
                               Seconds=15)
        # 创建流量
        stream = add_stream(Ports=Ports[2], FixedLength=256)
        # 负载单位：Byte per Second 速率：5
        edit_stream_load_profile(Streams=stream, Unit='BYTE_PER_SEC', Rate=15)
        
        # =============== *设置模式4* ===============
        # 负载模式：Base On Stream, 传输模式：Step, （突发报文数：25, 突发间隔：130, 突发间隔单位: sec, 发送帧数：20）
        edit_port_load_profile(Ports=Ports[3],
                               LoadProfileType='STREAM_BASE',
                               TransmitMode="STEP",
                               BurstSize=20,
                               InterFrameGap=130,
                               InterFrameGapUnit='SEC',
                               Frames=20)
        # 创建流量
        stream = add_stream(Ports=Ports[3], FixedLength=256)
        # 负载单位：Line Bits per Second 速率：5
        edit_stream_load_profile(Streams=stream, Unit='LINEBIT_PER_SEC', Rate=20)

    # 保存配置文件
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
