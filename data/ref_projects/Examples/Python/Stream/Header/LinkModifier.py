# =================================================================================
# Objective   	:   测试目的 : 检查测试仪表发ipv4报文统计正确
#
# Step			:	测试步骤1: 预约两个自环端口Port_1、Port_2;
#                   测试步骤2: 修改流量StreamTemplate_1的ipv4头部内容;;
#                   测试步骤3: 设置link Modifer;
#
# Criteria    	:   预期结果1: 配置无异常;
#
# Created by   	:  	Tester-001
#
# Bugs   	    :  	None
# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/13', '//10.0.11.191/1/14'] if len(sys.argv) < 2 else sys.argv[1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:
    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口
    port1, port2 = reserve_port(Locations=locations)
    # 创建流量
    stream = add_stream(Ports=port1, FixedLength=256)
    # 修改流量报文头部
    create_stream_header(Stream=stream, HeaderTypes=['EthernetII', 'IPv4'])
    # 修改ipv4头部
    HeaderOption = ['Security', 'RouterAlert']
    attribute_dict = edit_header_ipv4(Stream=stream, Level=0, TTL=200, Source='10.1.1.2', Destination='20.1.1.2',
                                      Flags=111, HeaderOption=HeaderOption)
    # ipv4头部Source字段添加Increment跳变
    modifier_1 = edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=attribute_dict['Source'],
                  Type='Increment', Count=10, Step=2)

    modifier_2 = edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=attribute_dict['Source'],
                  Type='Increment', Count=20, Step=2)

    modifier_3 = edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=attribute_dict['Destination'],
                               Type='Increment', Count=10, Step=2)

    modifier_4 = edit_modifier(Stream=stream, Level=0, HeaderType='IPv4', Attribute=attribute_dict['Destination'],
                               Type='Increment', Count=20, Step=2)
    # 设置流量link modifer
    link_modifier = [[modifier_1, modifier_2, modifier_3], [modifier_2, modifier_3, modifier_4], [modifier_3, modifier_4]]
    edit_modifier_link(Stream=stream, Link=link_modifier)

    # 保存配置
    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

    # 释放端口资源
    release_port(locations)


except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
