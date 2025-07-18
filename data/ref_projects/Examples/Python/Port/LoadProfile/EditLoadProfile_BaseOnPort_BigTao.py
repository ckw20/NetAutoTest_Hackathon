# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表负载模式为Base On Port负载配置设置成功
#
# Step			:	测试步骤1: 预约6个离线端口;
#                   测试步骤2: 设置端口负载模式：Base On Port,并设置负载配置各个类型参数;
#
# Criteria    	:   预期结果1: 步骤2中端口负载配置设置成功;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :
# =================================================================================

from TesterLibrary.base import *


Product = 'BigTao'
locations = [
    '//10.0.11.191/1/1',
    '//10.0.11.191/1/2',
    '//10.0.11.191/1/3',
    '//10.0.11.191/1/4',
    '//10.0.11.191/1/5',
    '//10.0.11.191/1/6',
]
verdict = 'pass'
errInfo = ''
try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)
    # 创建端口，并预约端口
    Ports = reserve_port(Locations=locations, Debug=True)
    if Product.lower() == 'bigtao':

        # =============== *设置模式1* ===============
        # 负载模式：Base On Port, （端口负载：15, 负载单位：Percent(%)） 传输模式：Continuous,
        edit_port_load_profile(Ports=Ports[0],
                               LoadProfileType='PORT_BASE',
                               TransmitMode="CONTINUOUS",
                               Rate=15,
                               Unit='PERCENT')

        # =============== *设置模式2* ===============
        # 负载模式：Base On Port （端口负载：20, 负载单位：Inter Frame Gap(ns)）, 传输模式：Burst, （突发报文数：15, 突发间隔：2, 突发间隔单位: ms , 突发次数: 10）
        edit_port_load_profile(Ports=Ports[1],
                               LoadProfileType='PORT_BASE',
                               Rate=20,
                               Unit='NS',
                               TransmitMode="BURST",
                               BurstSize=15,
                               InterFrameGap=2,
                               InterFrameGapUnit='MS',
                               BurstCount=10)

        # =============== *设置模式3* ===============
        # 负载模式：Base On Port, （端口负载：25, 负载单位：Inter Frame Gap(byte)） 传输模式：Time, （发送时间：15）
        edit_port_load_profile(Ports=Ports[2],
                               LoadProfileType='PORT_BASE',
                               Rate=25,
                               Unit='INTER_FRAME_GAP_BYTE',
                               TransmitMode="TIME",
                               Seconds=15)

        # =============== *设置模式4* ===============
        # 负载模式：Base On Port, （端口负载：30, 负载单位：Frames per Second） 传输模式：Step, （发送帧数：20）
        edit_port_load_profile(Ports=Ports[3],
                               LoadProfileType='PORT_BASE',
                               Rate=30,
                               Unit='FRAME_PER_SEC',
                               TransmitMode="STEP",
                               Frames=20)

        # =============== *设置模式5* ===============
        # 负载模式：Base On Port, （端口负载：35, 负载单位：Byte per Second） 传输模式：On Stream, 流传输模式：Continuous
        edit_port_load_profile(Ports=Ports[4],
                               LoadProfileType='PORT_BASE',
                               Rate=35,
                               Unit='BYTE_PER_SEC',
                               TransmitMode="ONSTREAM")
        # 创建流量
        stream = add_stream(Ports=Ports[4], FixedLength=256)
        edit_stream_load_profile(Streams=stream, StreamTransmitMode='CONTINUOUS')

        # =============== *设置模式6* ===============
        # 负载模式：Base On Port, （端口负载：40, 负载单位：Data Bits per Second） 传输模式：On Stream, 流传输模式：Burst （突发间隔单位：MS, 突发次数：3, 突发间隔：4, 突发数量：10）
        edit_port_load_profile(Ports=Ports[5],
                               LoadProfileType='PORT_BASE',
                               Rate=40,
                               Unit='DATABIT_PER_SEC',
                               TransmitMode="ONSTREAM")
        # 创建流量
        stream = add_stream(Ports=Ports[5], FixedLength=256)
        edit_stream_load_profile(Streams=stream, StreamTransmitMode='BURST', BurstGapUnit='MS', BurstCount=3, BurstGap=4, FramePerBurst=10)

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
