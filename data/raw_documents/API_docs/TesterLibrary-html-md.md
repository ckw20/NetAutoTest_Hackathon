Library scope:	GLOBAL
Introduction
Documentation for library TesterLibrary.

Importing
Arguments
logLevel
=
20
logHandle
=
LOG_FILE
Documentation
Initialize self. See help(type(self)) for accurate signature.

Keywords
Abort Dot1x
Arguments
Sessions
Documentation
中断802.1x会话

Args:

Sessions (:obj:Dot1x): 802.1x会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Abort Dot1x	Sessions=${Sessions}
Abort L2tp
Arguments
Sessions
Documentation
中断L2tp协议会话

Args:

Sessions (:obj:L2tp): L2tp协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Abort L2tp	Sessions=${Sessions}
Abort Pppoe
Arguments
Sessions
Documentation
中断PPPoE协议会话

Args:

Sessions (list (:obj:PppoeClent)): PPPoE协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Abort Pppoe	Sessions=${Sessions}
Abort Request Ldp Label
Arguments
Configs
Documentation
中止LDP协议会话LSP请求标签

Args:

Configs (list): LDP LSP对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Abort Request Ldp Label	Configs=${Configs}
Add Imix Distribution Frame
Arguments
IMix
Type
=
fixed
Length
=
None
Min
=
None
Max
=
None
Weight
=
None
Documentation
在Imix模板添加自定义帧长

Args:

IMix (:obj:Imix): 测试仪表Imix模板对象

Type (str): 测试仪表Imix模板自定义帧长类型 fixed random

Length (int): 测试仪表Imix模板自定义帧长长度，random时有效

Min (int): 测试仪表Imix模板自定义帧长最小帧长，random时有效

Max (int): 测试仪表Imix模板自定义帧长最大帧长，random时有效

Weight (int): 测试仪表Imix模板自定义帧长权重

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

${Imix}	Create Imix	Name=Imix_1	Seed=10121112		
Add IMix Distribution Frame	IMix=${Imix}	Type=random	Min=64	Max=128	Weight=50
Add IMix Distribution Frame	IMix=${Imix}	Type=random	Min=128	Max=256	Weight=50
Bind Stream Imix	Stream=${Stream}	Imix=${Imix}			
Add Stream
Arguments
Type
=
raw
Ports
=
None
Names
=
None
FilePath
=
None
IncludeCrc
=
True
SrcPoints
=
None
DstPoints
=
None
SrcInterface
=
None
DstInterface
=
None
Bidirection
=
None
Direction
=
None
Layer
=
None
TrafficMeshMode
=
None
EndpointMapping
=
None
AutoCreateTunnel
=
False
StreamOnly
=
None
** kwargs
Documentation
测试仪表创建流量

Args:

Type (str): 创建绑定流类型，支持raw流、binding流以及pcap文件导入流:

raw

binding

pcap

Ports (list (:obj:Port)): raw流和pcap流参数，端口对象, 测试仪表端口对象object列表

Names (list): raw流参数，流量名称, 流量名称列表

FilePath (str): pcap流参数，当Type为pcap需要指定导入pcap文件的路径

IncludeCrc (bool): pcap流参数，当Type为pcap指定导入方式是否携带CRC, 布尔值Bool (范围：True / False)

SrcInterface (list): binding流参数，指定源接口

DstInterface (list): binding流参数，指定目的接口

SrcPoints (list): binding流参数，指定源端点

DstPoints (list): binding流参数，指定目的端点

Bidirection (bool): 是否是能双向流量, 布尔值Bool (范围：True / False)

Direction (str): binding流参数

Layer (str): binding流参数，指定接口网络层，默认值：IPV4，支持值：

ETHERNETII

VLAN

GRE

IPV4

IPV6

TrafficMeshMode (str): binding流参数, 默认值：MANY_TO_MANY，支持值：

ONE_TO_ONE

MANY_TO_MANY

FULL_MESH

CONGESTION

LEARNING

BACK_BONE

PAIR

EndpointMapping (str): binding流参数, 默认值：ROUND_ROBIN，支持值：

ROUND_ROBIN

MANY_TO_MANY

AutoCreateTunnel (bool): binding流参数, 自动绑定隧道, 默认值：False

StreamOnly (bool): True为每个flow创建一个stream, False为多个flow创建一个stream, 默认值：False

Returns:

list (:obj:StreamTemplate): 创建的流量对象object列表

Examples: .. code:: RobotFramework

# raw流

${Streams}	add_stream	Port=${Port}
# pcap流

${Streams}	add_stream	Type=pcap	Port=${Port}	FilePath=${Pcap_File_Path}	IncludeCrc=True
# binding流

${Streams}	add_stream	Type=binding	SrcPoints=${Points_1}	DstPoints=${Points_2}	Bidirection=True
Advertise Bgp
Arguments
Sessions
Documentation
通告BGP协议会话lsa

Args:

Sessions (:obj:BgpRouter): BGP协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Advertise Bgp	Sessions=${Sessions}
Advertise Bgp Route
Arguments
Routes
Documentation
通告BGP协议指定lsa

Args:

Routes (list): BGP协议路由对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Advertise Bgp Route	Routes=${Routes}
Advertise Isis
Arguments
Lsps
Documentation
通告Isis协议会话lsp

Args:

Lsps (:obj:IsisLspConfig): ISIS LSP对象, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Advertise Isis	Lsp=${Lsp}
Advertise Ldp Label
Arguments
Configs
Documentation
通告LDP协议会话LSP标签

Args:

Configs (list): LDP LSP对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Advertise Ldp Label	Configs=${Configs}
Advertise Ospf Lsa
Arguments
Sessions
=
None
Type
=
None
Lsa
=
None
Documentation
通告OSPFv2协议会话lsa

Args:

Sessions (list(:obj:OspfRouter)): OSPFv2协议会话对象列表, 类型为：list

Type (str): OSPFv2 lsa类型, 类型为：string, 支持的lsa类型：

Router

Network

Summary

AsbrSummary

External

Lsa (list): OSPFv2 lsa列表, 类型为：list, 当Type=None时参数生效

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Advertise Ospf Lsa	Sessions=${Sessions}	Type=router
Advertise Ospf Lsa	Sessions=${Sessions}	Lsa=${Lsas}
Advertise Ospfv3 Lsa
Arguments
Sessions
=
None
Type
=
None
Lsa
=
None
Documentation
通告OSPFv3协议会话lsa

Args:

Sessions (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：list

Type (str): OSPFv3 lsa类型, 类型为：string, 支持的lsa类型：

Router

Network

InterAreaPrefix

InterAreaRouter

AsExternal

Link

Lsa (int): OSPFv3 lsa列表, 类型为：list, 当Type=None时参数生效

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Advertise Ospfv3 Lsa	Sessions=${Sessions}	Type=router
Advertise Ospfv3 Lsa	Sessions=${Sessions}	Lsa=${Lsas}
Advertise Rip
Arguments
Sessions
Documentation
通告RIP协议路由

Args:

Sessions(:obj:RipRouter): RIP协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Advertise Rip	Sessions=${Sessions}
Apply Igmp Querier
Arguments
Sessions
Documentation
IGMP Querier增量配置下发到后台

Args:

Sessions (list (:obj:IgmpQuerier)): IGMP Querier协会话对象, 类型为：object

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Apply Igmp Querier
Apply Mld Querier
Arguments
Sessions
Documentation
MLD Querier增量配置下发到后台

Args:

Sessions (list (:obj:MldQuerier)): MLD Querier协会话对象, 类型为：object

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Apply Mld Querier
Benchmark Stream Use Exist
Arguments
Config
Streams
Documentation
编辑测试套件使用已存在流量

Args:

Config (:obj:wizard): 仪表测试测试套件对象object

Streams (list (:obj:StreamTemplate)): 仪表测试流模板对象object列表

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

@{Items}	Create List	throughput	frameloss		
@{FrameSize}	Create List	256	1024	16383	
${Streams}	Add Stream	Type=binding		SrcPoints=@{SrcPoints}	DstPoints=@{SrcPoints}
${Wizard}	${Config}	Create Benchmark	Type=rfc2544	Items=${Items}	
Edit Benchmark Path	Configs=${Config}	Path=C:/test			
Relate Benchmark Ports	Config=${Wizard}	Ports=${Ports}			
Benchmark Stream Use Exist	Config=${Wizard}	Streams=${Streams}			
Edit Benchmark Learning	Configs=${Config}	Frequency=once			
Edit Benchmark Duration	Config=${Config}	Count=1000			
Edit Benchmark Frame	Config=${Config}	Type=custom	Custom=@{FrameSize}		
Edit Benchmark Search	Config=${Config}	Init=100			
Expand Benchmark	Config=${Wizard}				
Bfd Admin Down
Arguments
Sessions
Documentation
设置BFD会话状态AdminDown

Args:

Sessions (list (:obj:BfdRouter)): BFD协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Bfd Admin Down	Sessions=${Sessions}
Bfd Admin Up
Arguments
Sessions
Documentation
设置BFD会话状态AdminUp

Args:

Sessions (list (:obj:BfdRouter)): BFD协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Bfd Admin Up	Sessions=${Sessions}
Bfd Disable Demand Mode
Arguments
Sessions
Documentation
关闭BFD demand模式

Args:

Sessions (list (:obj:BfdRouter)): BFD协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Bfd Disable Demand Mode	Sessions=${Sessions}
Bfd Enable Demand Mode
Arguments
Sessions
Documentation
开启BFD Demand模式

Args:

Sessions (list (:obj:BfdRouter)): BFD协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Bfd Enable Demand Mode	Sessions=${Sessions}
Bfd Initiate Poll
Arguments
Sessions
Documentation
发送BFD poll Sequence

Args:

Sessions (list (:obj:BfdRouter)): BFD协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Bfd Initiate Poll	Sessions=${Sessions}
Bfd Resume Pdus
Arguments
Sessions
Documentation
恢复发送BFD PDU

Args:

Sessions (list (:obj:BfdRouter)): BFD协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Bfd Resume Pdus	Sessions=${Sessions}
Bfd Set Diagnostic State
Arguments
Sessions
State
Documentation
设置BFD状态诊断码

Args:

Sessions (list (:obj:BfdRouter)): BFD协议会话对象列表, 类型为：list

State (str):设置状态诊断码, 类型为：string, 默认值：NO_DIAGNOSTIC, 支持的状态诊断码：

NO_DIAGNOSTIC

CONTROL_DETECTION_TIME_EXPIRED

ECHO_FUNCTION_FAILED

NEIGHBOR_SIGNAL_SESSION_DOWN

FORWARDING_PLANE_RESET

PATH_DOWN

CONCATENATED_PATH_DOWN

ADMINISTRATIVELY_DOWN

REVERSE_CONCATENATED_PATH_DOWN

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Bfd Set Diagnostic State	Sessions=${Sessions}
Bfd Stop Pdus
Arguments
Sessions
Documentation
停止发送BFD PDU

Args:

Sessions (list (:obj:BfdRouter)): BFD协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Bfd Stop Pdus	Sessions=${Sessions}
Bind Stream Imix
Arguments
Stream
IMix
Documentation
将Imix模板和流量模板绑定

Args:

Stream (:obj:StreamTemplate): 测试仪表流量模板StreamTemplate对象

IMix (:obj:Imix): 测试仪表Imix模板对象

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

${Imix}	Create Imix	Name=Imix_1	Seed=10121112
Bind Stream Imix	Stream=${Stream}	Imix=${Imix}	
Binding Multicast Group
Arguments
Session
Memberships
MulticastGroup
Documentation
将全局组播组绑定到组播协议会话上

Args:

Session (:obj:Mld, Igmp): IGMP/MLD协会话对象, 类型为：object

Memberships (:obj:MldMembershipsConfig): 组播协议和组播组绑定关系对象, 类型为：object

MulticastGroup (:obj:MldSelectMulticastGroupCommand): 全局组播组对象, 类型为：object

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

${Group}	Create Multicast Group	Version=IPV4	Start=225.0.1.1	Number=20
${Session}	Create Igmp	Port=${Port}	Version=IGMPV3	
${Memberships}	Create Memberships	Session=${Session}	Start=225.0.1.1	DeviceGroupMapping=ONETOONE
binding_multicast_group	Session=${Session}	Memberships=${Memberships}	MulticastGroup=${Group}	
Binding Vxlan Multicast Group
Arguments
Segments
MulticastGroups
Documentation
创建Vxlan Multicast Group对象

Args:

Segments (:obj:VxlanSegmentConfig): Vxlan Segment对象, 类型：object

MulticastGroups (:obj:Ipv4MulticastGroup): Vxlan Multicast Group对象, 类型：object

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Binding Vxlan Multicast Group	Segments=${Segments}	MulticastGroups=${MulticastGroups}
Binding Vxlan Vm
Arguments
Segments
Vms
Documentation
绑定Vxlan Vm对象

Args:

Segments (:obj:VxlanSegmentConfig): Vxlan Segment对象, 类型：object

Vms (:obj:'VxlanVmProperty'): Vxlan Vm对象, 类型：object

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Binding Vxlan Vm	Segments=${Segments}	Vms=${Vms}
Binding Vxlan Vtep
Arguments
Vteps
Vms
Documentation
绑定Vxlan Vtep对象

Args:

Vteps (:obj:Vxlan): Vxlan协议会话对象, 类型：object

Vms (:obj:'VxlanVmProperty'): Vxlan Vm对象, 类型：object

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Binding Vxlan Vtep	Vteps=${Vxlan}	Vms=${Vms}
Clear Result
Arguments
All
=
True
Objects
=
None
Documentation
清除测试仪表统计

Args:

All (bool): 是否清除所有已经订阅的统计视图的数据, 默认位: True

Objects (list): 指定需要清空视图的对象

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Subscribe Result	
Start Stream	
Sleep	10
Stop Stream	
Sleep	3
Clear Result	
Connect Bgp
Arguments
Sessions
Documentation
连接BGP协议会话

Args:

Sessions (:obj:BgpRouter): BGP协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Connect Bgp	Sessions=${Sessions}
Connect Chassis
Arguments
Chassis
Documentation
连接测试仪表机箱后台.

Args:

Chassis (str): 机箱主机IP地址列表

Returns:

list: Chassis对象列表

Examples: robotframework:

.. code:: robotframework

${Hosts}=	Create List	192.168.0.10	192.168.0.10
${Chassis}	Connect Chassis	Chassis=${Hosts}	
Connect L2tp
Arguments
Sessions
Documentation
建立L2tp协议会话

Args:

Sessions (:obj:L2tp): L2tp协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Connect L2tp	Sessions=${Sessions}
Connect Pppoe
Arguments
Sessions
Documentation
连接PPPoE协议会话

Args:

Sessions (list (:obj:PppoeClent)): PPPoE协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Connect Pppoe	Sessions=${Sessions}
Create Benchmark
Arguments
Type
=
rfc2544
Items
=
None
Documentation
创建测试仪表测试套件

Args:

Type (str): 测试仪表测试套件类型, 支持的类型:

rfc2544

rfc2889

rfc3918

Asymmetric

Items (list): 测试仪表测试套件中的测试项, 测试套件中的测试项列表, 支持测试项目如下:

throughput: rfc2544吞吐量测试

backtoback: rfc2544背靠背测试

frameloss: rfc2544丢包率测试

latency: rfc2544时延测试

addressCachingCapacity: rfc2889地址缓存容量测试

addressLearningRate: rfc2889地址学习速率测试

broadcastLatency: rfc2889广播帧转发测试

broadcastForwarding: rfc2889广播帧时延测试

congestion: rfc2889拥塞控制测试

erroredFrameFilter: rfc2889错误帧过滤测试

forwarding: rfc2889转发测试

forwardPressure:

maxForwarding:

mixedThroughput: rfc3918混合吞吐量测试

scaledGroupForwarding: rfc3918组转发矩阵测试

multicastThroughput: rfc3918聚合组播吞吐量测试

multicastGroupCapacity: rfc3918组播组容量测试

multicastLatency: rfc3918组播转发时延测试

multicastJoinLeaveLatency: rfc3918加入离开时延测试

Returns:

(:obj:wizard_config): 仪表测试测试套件对象object

(list (:obj:test_config)): 仪表测试测试套件测试项对象object列表

Examples: robotframework:

.. code:: robotframework

${Items}	Create List	throughput	frameloss				
${Wizard}	${Config}	Create Benchmark	Type=rfc2544	Items=${Items}			
Relate Benchmark Ports	Config=${Wizard}	Ports=${Ports}					
Create Benchmark Streams	Config=${Wizard}	Items=@{RFC2544Items}	Type=eth	SrcPoints=@{SrcPoints}	DstPoints=@{SrcPoints}	Mode=meshed	Mapping=roundrobin
Edit Benchmark Learning	Configs=${Config}	Frequency=once					
Edit Benchmark Duration	Config=${Config}	Count=${L2_TestTime}					
Edit Benchmark Frame	Config=${Config}	Type=custom	Custom=@{L2_FrameSize}				
Edit Benchmark Search	Config=${Config}	Init=100					
Expand Benchmark	Config=${Wizard}						
Create Benchmark Streams
Arguments
Config
Items
Type
SrcPoints
DstPoints
Bidirectional
=
False
Mode
=
1v1
Mapping
=
roundrobin
Monitors
=
()
Documentation
创建测试仪表测试套件流量

Args:

Config (:obj:wizard_config): 仪表测试测试套件对象object

Items (list): 测试仪表测试套件中的测试项, 测试套件中的测试项列表, 支持测试项目如下:

throughput

backtoback

frameloss

latency

addressCachingCapacity

addressCachingRate

broadcastLatency

broadcastForwarding

congestion

erroredFrameFilter

forwarding

forwardPressure

maxForwarding

mixedThroughput

scaledGroupForwarding

multicastThroughput

multicastGroupCapacity

multicastLatency

multicastJoinLeaveLatency

Type (str): 创建绑定流类型, 支持类型有:

eth

ipv4

ipv6

SrcPoints (list): 创建绑定流类型源端点对象object列表

DstPoints (list): 创建绑定流类型目的端点, 目的端点对象object列表

Bidirectional (bool): 是否使能双向流量, 默认值: False

Mode (str): 创建绑定流topo类型

1v1

m2m

meshed

Mapping (str): 创建绑定流端点模式, 支持类型

roundrobin

manytomany

Monitors (list): 作为镜像端口的测试仪表端口对象object列表

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

${Items}	Create List	throughput	frameloss				
${Wizard}	${Config}	Create Benchmark	Type=rfc2544	Items=${Items}			
Relate Benchmark Ports	Config=${Wizard}	Ports=${Ports}					
Create Benchmark Streams	Config=${Wizard}	Items=@{RFC2544Items}	Type=eth	SrcPoints=@{SrcPoints}	DstPoints=@{SrcPoints}	Mode=meshed	Mapping=roundrobin
Edit Benchmark Learning	Configs=${Config}	Frequency=once					
Edit Benchmark Duration	Config=${Config}	Count=${L2_TestTime}					
Edit Benchmark Frame	Config=${Config}	Type=custom	Custom=@{L2_FrameSize}				
Edit Benchmark Search	Config=${Config}	Init=100					
Expand Benchmark	Config=${Wizard}						
Create Bfd
Arguments
Port
** kwargs
Documentation
创建BFD协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): BFD协议会话名称, 类型为：string

Enable (bool): 使能BFD协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

RouterRole (str): BFD会话的角色, 类型为：string, 默认值：Active, 支持角色：

Active

Passive

TimeIntervalUnit (str): 时间间隔的单位。 类型为：string, 默认值：milliseconds, 支持单位：

milliseconds

microseconds

DesiredMinTXInterval (int): 期望的最小发送时间间隔。 类型为：number, 取值范围：1-10000 (milliseconds); 1-10000000 (microseconds), 默认值：50

RequiredMinRXInterval (int): 需要的最小接收时间间隔。 类型为：number, 取值范围：1-10000 (milliseconds); 1-10000000 (microseconds), 默认值：50

RequiredMinEchoRXInterval (int): 需要的最小Echo报文接收时间间隔。 类型为：number, 取值范围：1-10000 (milliseconds); 1-10000000 (microseconds), 默认值：0

DetectMultiple (int): 用于检测超时的时间因子, 类型为：number, 取值范围：2-100, 默认值：3

AuthenticationType (str): 认证方式, 类型为：string, 默认值：None, 支持的方式：

NONE

SIMPLE_PASSWORD

KEYED_MD5

METICULOUS_KEYED_MD5

KEYED_SHA1

METICULOUS_KEYED_SHA1

Password (str): 当认证方式不为NONE时，在该单元格输入认证密码。密码可以是数字、字母或者数字和字母的组合，最长为16位。 类型为：string, 默认值：Xinertel

KeyID (int): 当认证方式不为NONE时，在该单元格输入Key ID, 类型为：number, 取值范围：0-255, 默认值：1

Returns:

(:obj:BfdRouter): BFD协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create bfd	Port=${Port}	TimeIntervalUnit=microseconds
Create Bfd Ipv4 Session
Arguments
Session
** kwargs
Documentation
创建BFD IPv4会话对象

Args:

Session(:obj:BfdRouter): BFD协议会话对象列表, 类型为：object

Keyword Args:

Name (str): BFD IPv4会话名称, 类型为：string

Enable (bool): 使能BFD IPv4会话, 类型为：bool, 取值范围：True或False, 默认值：True

NumberOfSessions (str): BFD IPv4会话的数目, 类型为：string, 取值范围：1-4294967295, 默认值：1

StartDestinationAddress (str): 指定第一个目的IPv4地址, 类型为：string, 取值范围：有效的ipv4地址, 默认值：192.0.1.0

DestinationAddressIncrement (str): 指定下一个目的IPv4地址的增量, 类型为：string, 取值范围：有效的ipv4地址, 默认值：0.0.0.1

EnableMyDiscriminator (bool): 是否指定本地标识符, 类型为：bool, 取值范围：True或False, 默认值：False

MyDiscriminator (int): 指定本地标识符的初始值。只有使能本地标识符被选中才可编辑, 类型为：number, 取值范围：1-4294967295, 默认值：1

MyDiscriminatorIncrement (int): 指定下一个本地标识符的增量。只有使能本地标识符被选中才可编辑。 类型为：number, 取值范围：1-4294967295, 默认值：1

EnableYourDiscriminator (bool): 是否指定对端标识符, 类型为：bool, 取值范围：True或False, 默认值：False

YourDiscriminator (int): 指定对端标识符的初始值。只有使能本地标识符被选中才可编辑, 类型为：number, 取值范围：1-4294967295, 默认值：1

YourDiscriminatorIncrement (int): 指定下一个对端标识符的增量。只有使能本地标识符被选中才可编辑。 类型为：number, 取值范围：1-4294967295, 默认值：1

Returns:

(:obj:BfdIpv4SessionConfig): BFD IPv4会话对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Bfd	Port=${Port}
Create Bfd Ipv4 Session	Session=${Session}	NumberOfSessions=10
Create Bfd Ipv6 Session
Arguments
Session
** kwargs
Documentation
创建BFD IPv6路由对象

Args:

Session(:obj:BfdRouter): BFD协议会话对象列表, 类型为：object

Keyword Args:

Name (str): BFD IPv6路由名称, 类型为：string

Enable (bool): 使能BFD IPv6路由, 类型为：bool, 取值范围：True或False, 默认值：True

NumberOfSessions (str): BFD IPv6会话的数目, 类型为：string, 取值范围：1-4294967295, 默认值：1

StartDestinationAddress (str): 指定第一个目的IPv6地址, 类型为：string, 取值范围：有效的ipv6地址, 默认值：2000::1

DestinationAddressIncrement (str): 指定下一个目的IPv4地址的增量, 类型为：string, 取值范围：有效的ipv4地址, 默认值：::1

EnableMyDiscriminator (bool): 是否指定本地标识符, 类型为：bool, 取值范围：True或False, 默认值：False

MyDiscriminator (int): 指定本地标识符的初始值。只有使能本地标识符被选中才可编辑, 类型为：number, 取值范围：1-4294967295, 默认值：1

MyDiscriminatorIncrement (int): 指定下一个本地标识符的增量。只有使能本地标识符被选中才可编辑。 类型为：number, 取值范围：1-4294967295, 默认值：1

EnableYourDiscriminator (bool): 是否指定对端标识符, 类型为：bool, 取值范围：True或False, 默认值：False

YourDiscriminator (int): 指定对端标识符的初始值。只有使能本地标识符被选中才可编辑, 类型为：number, 取值范围：1-4294967295, 默认值：1

YourDiscriminatorIncrement (int): 指定下一个对端标识符的增量。只有使能本地标识符被选中才可编辑。 类型为：number, 取值范围：1-4294967295, 默认值：1

Returns:

(:obj:BfdIpv6SessionConfig): BFD IPv6会话对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Bfd	Port=${Port}
Create Bfd Ipv6 Session	Session=${Session}	
Create Bgp
Arguments
Port
** kwargs
Documentation
创建BGP协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): BGP协会话名称, 类型为：string

Enable (bool): 使能BGP协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

IpVersion (str): IP版本, 类型为：string, 默认值：BOTH, 支持版本：

BOTH

IPV4

IPV6

BgpInitiator (bool): BGP会话发起者, 类型为：bool, 取值范围：True或False, 默认值：True

AsNumber (int): 自治域, 类型为：number, 取值范围：1-65535, 默认值：1

AsNumberStep (int): 自治域跳变, 类型为：number, 取值范围：0-65535, 默认值：1

Enable4ByteAs (bool): 使能4字节自治域, 类型为：bool, 取值范围：True或False, 默认值：False

AsNumber4Byte (int): 4字节自治域, 类型为：number, 取值范围：0.1-65535.65535, 默认值：1.1

AsNumber4ByteStep (int): 4字节自治域跳变, 类型为：number, 取值范围：0.1-65535.65535, 默认值：0.1

DutAsNumber (int): DUT自治域, 类型为：number, 取值范围：1-65535, 默认值：1

DutAsNumberStep (int): DUT自治域跳变, 类型为：number, 取值范围：1-65535, 默认值：1

Enable4ByteDutAs (bool): 使能DUT4字节自治域, 类型为：bool, 取值范围：True或False, 默认值：False

Dut4ByteAsNumber (int): DUT4字节自治域, 类型为：number, 取值范围：0.1-65535.65535, 默认值：1.1

Dut4ByteAsNumberStep (int): DUT4字节自治域跳变, 类型为：number, 取值范围：0.1-65535.65535, 默认值：0.1

BgpType (str): BGP类型, 类型为：string, 取值范围：EBGP, IBGP, 默认值：IBGP

UseGatewayAsDutIp (bool): 使用网关地址作为DUT地址, 类型为：bool, 取值范围：True或False, 默认值：True

BgpSessionIpAddressType (str): 会话IP类型, 类型为：string, 取值范围：INTERFACE_IP, ROUTE_ID, 默认值：INTERFACE_IP

DutIpv4Address (str): DUT IPv4地址, 当IP版本为IPv4，并且使用网关地址作为DUT地址未选中时，需配置该选项指定DUT的Router ID, 类型为：string, 取值范围：IPv4地址, 默认值：2.1.1.1

DutIpv4AddressStep (str): DUT IPv4地址跳变, 当IP版本为IPv4，并且使用网关地址作为DUT地址未选中时，需配置该选项指定DUT的Router ID增量步长, 类型为：string, 取值范围：IPv4地址, 默认值：0.0.0.1

DutIpv6Address (str): DUT IPv4地址, 当IP版本为IPv6，并且使用网关地址作为DUT地址未选中时，需配置该选项指定DUT的Router ID, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

DutIpv6AddressStep (str): DUT IPv4地址跳变, 当IP版本为IPv6，并且使用网关地址作为DUT地址未选中时，需配置该选项指定DUT的Router ID增量步长, 类型为：string, 取值范围：IPv6地址, 默认值：::1

HoldTime (int): Hold Time间隔 (sec), 类型为：number, 取值范围：3-65535, 默认值：90

KeepaliveTime (int): Keep Alive间隔 (sec), 类型为：number, 取值范围：1-65535, 默认值：30

ConnectRetryCount (int): 重连次数, 取值范围：0-65535, 默认值：0

ConnectRetryInterval (int): 重连间隔 (sec), 取值范围：10-300, 默认值：30

MaxRoutesPerUpdateMessage (int): Update报文中最大路由数量, 取值范围：10-300, 默认值：2000

RouteRefreshMode (str): Route Refresh模式, 类型为：string, 取值范围：None; Route Refresh, 默认值：None

EnableGracefulRestart (bool): 使能平滑重启, 类型为：bool, 取值范围：True或False, 默认值：False

RestartTime (int): 平滑重启时间（秒）, 取值范围：3-4095, 默认值：90

EnableViewRoutes (bool): 使能查看路由, 类型为：bool, 取值范围：True或False, 默认值：False

Authentication (str): 使用的认证类型, 类型为：string, 取值范围：None或MD5, 默认值：None

Password (str): 认证密码, 类型为：类型为：string, 取值范围：字符串，由1-255个数字、字母或特殊字符组成, 默认值：xinertel

EnableBfd (bool): 使能BFD, 类型为：bool, 取值范围：True或False, 默认值：False

EnableSr (bool): 使能SR, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:BgpRouter): BGP协议会话对, 类型：object

Examples: .. code:: RobotFramework

Create Bgp	Port=${Port}
Create Bgp Capability
Arguments
Session
** kwargs
Documentation
创建BGP Capability对象

Args:

Session (:obj:BgpRouter): Bgp协议会话对象列表, 类型为：object

Keyword Args:

Name (str): BGP Capability名称, 类型为：string

Enable (bool): 使能BGP Capability, 类型为：bool, 取值范围：True或False, 默认值：True

CapabilityCode (int): Capability Code, 类型为：number, 默认值：1, 取值范围：1-255

CapabilityValue (str): Capability 值 类型为：list

Returns:

(:obj:BgpCapabilityConfig): BGP Capability对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}				
${CapabilityValue}	Create List	1	2	3	4	5
Create Bgp Capability	Session=${Session}	CapabilityCode=5	CapabilityValue=${CapabilityValue}			
Create Bgp Evpn Ethernet Segment Routes
Arguments
Session
** kwargs
Documentation
创建Bgp Evpn Ethernet Segment Routes对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

Keyword Args:

Origin (str): 指定路由属性中的ORIGIN值, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳地址, 类型为：bool, 默认值：True

NextHop (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv4地址, 默认值：100.0.0.1

NextHopIpv6 (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv6地址, 默认值：2001::1

EnableLinkLocalNextHop (bool): 使能IPv6 Link Local下一跳, 类型为：bool, 默认值：False

LinkLocalNextHop (str): IPv6 Link Local下一跳地址, 类型为：有效的ipv6地址, 默认值：fe80::1

EnableOriginatorId (bool): 是否启用Originator ID, 当仿真路由器作为BGP路由反射器时使用该属性, 类型为：bool, 默认值：False

OriginatorId (str): 指定originator ID的值。该值用于标识路由发起者的router id, 类型为：有效的ipv4地址, 默认值：192.0.0.1

VrfRouteTarget (str): 指定VRF路由目标起始值, 类型为：string, 默认值：100:1

VrfRouteTargetStep (str): 指定VRF路由目标的跳变步长, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：10.0.0.2:1

VrfRouteDistinguisherStep (str): 指定VRF路由标识的跳变步长, 类型为：string, 默认值：0:1

EthernetSegmentType (str): 类型为：string, 默认值：OPERATOR, 取值范围：

OPERATOR

IEEE802

BRIDGEDLAN

MACBASED

ROUTEID

AS

EthernetSegmentIdentifier (str): 类型为：string, 默认值：00:00:00:00:00:00:00:00:00

EviCount (int): 创建的EVI （EVPN instance，EVPN实例）数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

DataPlanEncapsulation (str): 指定路由属性中的ORIGIN值, 类型为：string, 默认值：NONE, 取值范围：

NONE

VXLAN

MPLS

SRv6

EsImportRoute (str): 类型为：有效的mac地址, 默认值：00:00:00:00:00:00

Returns:

(:obj:EvpnRouteEthernetSegmentConfig): Bgp Evpn Ethernet Segment Routes对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Evpn Ethernet Segment Routes	Session=${Session}	
Create Bgp Evpn Inclusive Multicast Routes
Arguments
Session
** kwargs
Documentation
创建Bgp Evpn Inclusive Multicast Routes对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

Keyword Args:

Origin (str): 指定路由属性中的ORIGIN值, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳地址, 类型为：bool, 默认值：True

NextHop (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv4地址, 默认值：100.0.0.1

NextHopIpv6 (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv6地址, 默认值：2001::1

EnableLinkLocalNextHop (bool): 使能IPv6 Link Local下一跳, 类型为：bool, 默认值：False

LinkLocalNextHop (str): IPv6 Link Local下一跳地址, 类型为：有效的ipv6地址, 默认值：fe80::1

EnableOriginatorId (bool): 是否启用Originator ID, 当仿真路由器作为BGP路由反射器时使用该属性, 类型为：bool, 默认值：False

OriginatorId (str): 指定originator ID的值。该值用于标识路由发起者的router id, 类型为：有效的ipv4地址, 默认值：192.0.0.1

VrfRouteTarget (str): 指定VRF路由目标起始值, 类型为：string, 默认值：100:1

VrfRouteTargetStep (str): 指定VRF路由目标的跳变步长, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：10.0.0.2:1

VrfRouteDistinguisherStep (str): 指定VRF路由标识的跳变步长, 类型为：string, 默认值：0:1

EviCount (int): 创建的EVI （EVPN instance，EVPN实例）数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

EthernetTagId (int): 类型为：number, 取值范围：1-4294967295, 默认值：1

PmsiTunnelType (str): 指定多播报文传输所使用隧道的类型。只支持INGRESS_REPLICATION（头端复制隧道。隧道标识携带本地PE的单播隧道目的端IP地址）。类型为：string, 默认值：INGRESS_REPLICATION

DataPlanEncapsulation (str): 指定路由属性中的ORIGIN值, 类型为：string, 默认值：NONE, 取值范围：

NONE

VXLAN

MPLS

SRv6

Label1 (int): 封装标签（VNI/VSID）, 数据平面封装为VXLAN时可见, 指定转发二层业务流量所使用封装标签的起始值, 类型为：number, 取值范围：1-16777215, 默认值：0

Label1Step (int): 指定转发二层业务流量所使用封装标签的跳变步长, 类型为：number, 取值范围：1-16777215, 默认值：1

EnableCustomMplsLabel (bool): 使能自定义MPLS标签, 类型为：bool, 默认值：False

MplsLabel (int): MPLS标签, 类型为：number, 取值范围：1-1048575, 默认值：0

MplsLabelStep (int): MPLS标签跳变, 类型为：number, 取值范围：1-1048575, 默认值：0

Returns:

(:obj:EvpnRouteInclusiveMulticastConfig): Bgp Evpn Inclusive Multicast Routes对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Evpn Inclusive Multicast Routes	Session=${Session}	
Create Bgp Evpn Ip Prefix Routes
Arguments
Session
** kwargs
Documentation
创建Bgp Evpn Ip Prefix Routes对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

Keyword Args:

Origin (str): 指定路由属性中的ORIGIN值, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳地址, 类型为：bool, 默认值：True

NextHop (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv4地址, 默认值：100.0.0.1

NextHopIpv6 (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv6地址, 默认值：2001::1

EnableLinkLocalNextHop (bool): 使能IPv6 Link Local下一跳, 类型为：bool, 默认值：False

LinkLocalNextHop (str): IPv6 Link Local下一跳地址, 类型为：有效的ipv6地址, 默认值：fe80::1

EnableOriginatorId (bool): 是否启用Originator ID, 当仿真路由器作为BGP路由反射器时使用该属性, 类型为：bool, 默认值：False

OriginatorId (str): 指定originator ID的值。该值用于标识路由发起者的router id, 类型为：有效的ipv4地址, 默认值：192.0.0.1

VrfRouteTarget (str): 指定VRF路由目标起始值, 类型为：string, 默认值：100:1

VrfRouteTargetStep (str): 指定VRF路由目标的跳变步长, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：10.0.0.2:1

VrfRouteDistinguisherStep (str): 指定VRF路由标识的跳变步长, 类型为：string, 默认值：0:1

EthernetSegmentType (str): 指定以太网段标识的类型，用于确定以太网段标识的格式 , 类型为：string, 默认值：OPERATOR, 取值范围：

OPERATOR

IEEE802

BRIDGEDLAN

MACBASED

ROUTEID

AS

EthernetSegmentIdentifier (str): 指定CE和PE之间连接的标识, 类型为：string, 默认值：00:00:00:00:00:00:00:00:00

EthernetTagId (int): 指定广播域（例如VLAN）的标识, 类型为：number, 取值范围：1-4294967295, 默认值：0

NetWorkCount (int): 指定要创建的网络数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

EviCount (int): 创建的EVI （EVPN instance，EVPN实例）数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

VpnDistributionType (str): RT、RD以及VNI值在VPN之间的分配方式, 类型为：string, 默认值：ROUNDROBIN, 取值范围：

ROUNDROBIN

LINEAR

DataPlanEncapsulation (str): 封装有效负载所使用的头部类型, 类型为：string, 默认值：NONE, 取值范围：

NONE

VXLAN

MPLS

SRv6

EnableCustomMplsLabel (bool): 使能自定义MPLS标签, 类型为：bool, 默认值：False

Label1 (int): 封装标签（VNI/VSID）, 数据平面封装为VXLAN时可见, 指定转发二层业务流量所使用封装标签的起始值, 类型为：number, 取值范围：1-16777215, 默认值：0

Label1Step (int): 指定转发二层业务流量所使用封装标签的跳变步长, 类型为：number, 取值范围：1-16777215, 默认值：1

IpType (str): 类型为：string, 默认值：IPV4, 取值范围：

IPV4

IPV6

StartIpv4Address (str): 起始IPv4地址, 类型为：有效的ipv4地址, 默认值：100.0.0.2

Ipv4Increment (str): IPv4地址跳变, 类型为：有效的ipv4地址, 默认值：0.0.0.1

Ipv4PrefixLength (int): IPv4地址前缀, 类型为：number, 取值范围：1-32, 默认值：24

GatewayIp (str): 类型为：有效的ipv4地址, 默认值：0.0.0.0

StartIpv6Address (str): 起始IPv6地址, 类型为：有效的ipv6地址, 默认值：2001::1

Ipv6Increment (str): IPv6地址跳变, 类型为：有效的ipv6地址, 默认值：::1

Ipv6PrefixLength (int): IPv6地址前缀, 类型为：number, 取值范围：1-128, 默认值：64

GatewayIpv6 (str): 类型为：有效的ipv6地址, 默认值：'::'

EnableIncludeRouterMac (bool): 是否包含路由MAC, 类型为：bool, 默认值：False

RouterMac (str): 路由MAC地址, 类型为：有效的mac地址, 默认值：00:00:00:00:00:00

MplsLabel (int): MPLS标签, 类型为：number, 取值范围：1-1048575, 默认值：0

MplsLabelStep (int): MPLS标签跳变, 类型为：number, 取值范围：1-1048575, 默认值：0

Returns:

(:obj:EvpnRouteIpPrefixConfig): Bgp Evpn Ip Prefix Routes对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Evpn Ip Prefix Routes	Session=${Session}	
Create Bgp Evpn Mac Ip Routes
Arguments
Session
** kwargs
Documentation
创建Bgp Evpn Mac Ip Routes对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

Keyword Args:

Origin (str): 指定路由属性中的ORIGIN值, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳地址, 类型为：bool, 默认值：True

NextHop (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv4地址, 默认值：100.0.0.1

NextHopIpv6 (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv6地址, 默认值：2001::1

EnableLinkLocalNextHop (bool): 使能IPv6 Link Local下一跳, 类型为：bool, 默认值：False

LinkLocalNextHop (str): IPv6 Link Local下一跳地址, 类型为：有效的ipv6地址, 默认值：fe80::1

EnableOriginatorId (bool): 是否启用Originator ID, 当仿真路由器作为BGP路由反射器时使用该属性, 类型为：bool, 默认值：False

OriginatorId (str): 指定originator ID的值。该值用于标识路由发起者的router id, 类型为：有效的ipv4地址, 默认值：192.0.0.1

VrfRouteTarget (str): 指定VRF路由目标起始值, 类型为：string, 默认值：100:1

VrfRouteTargetStep (str): 指定VRF路由目标的跳变步长, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：10.0.0.2:1

VrfRouteDistinguisherStep (str): 指定VRF路由标识的跳变步长, 类型为：string, 默认值：0:1

EthernetSegmentType (str): 指定以太网段标识的类型，用于确定以太网段标识的格式 , 类型为：string, 默认值：OPERATOR, 取值范围：

OPERATOR

IEEE802

BRIDGEDLAN

MACBASED

ROUTEID

AS

EthernetSegmentIdentifier (str): 指定CE和PE之间连接的标识, 类型为：string, 默认值：00:00:00:00:00:00:00:00:00

EthernetTagId (int): 指定广播域（例如VLAN）的标识, 类型为：number, 取值范围：1-4294967295, 默认值：0

NetWorkCount (int): 指定要创建的网络数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

StartMacAddress (str): 指定路由块中的起始MAC地址, 类型为：有效的mac地址, 默认值：00:10:01:00:00:01

MacIncrement (str): 指定路由块中MAC地址的跳变步长, 类型为：有效的mac地址, 默认值：00:00:00:00:00:01

EviCount (int): 创建的EVI （EVPN instance，EVPN实例）数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

VpnDistributionType (str): RT、RD以及VNI值在VPN之间的分配方式, 类型为：string, 默认值：ROUNDROBIN, 取值范围：

ROUNDROBIN

LINEAR

AssociatedIpType (str): 指定通告路由中所携带主机IP路由的版本 , 类型为：string, 默认值：IPV4, 取值范围：

NONE

IPV4

IPV6

DataPlanEncapsulation (str): 封装有效负载所使用的头部类型, 类型为：string, 默认值：NONE, 取值范围：

NONE

VXLAN

MPLS

SRv6

EnableMacMobility (bool): 使能MAC地址迁移, 类型为：bool, 默认值：False

StickyStatic (bool): MAC地址是静态MAC地址, 类型为：bool, 默认值：False

SequenceNumber (int): 指定MAC迁移扩展团体属性TLV中的序列号起始值, 类型为：number, 取值范围：1-4294967295, 默认值：0

Label1 (int): 封装标签（VNI/VSID）, 数据平面封装为VXLAN时可见, 指定转发二层业务流量所使用封装标签的起始值, 类型为：number, 取值范围：1-16777215, 默认值：0

Label1Step (int): 指定转发二层业务流量所使用封装标签的跳变步长, 类型为：number, 取值范围：1-16777215, 默认值：1

StartIpv4Address (str): 起始IPv4地址, 类型为：有效的ipv4地址, 默认值：100.0.0.2

Ipv4Increment (str): IPv4地址跳变, 类型为：有效的ipv4地址, 默认值：0.0.0.1

Ipv4PrefixLength (int): IPv4地址前缀, 类型为：number, 取值范围：1-32, 默认值：24

StartIpv6Address (str): 起始IPv6地址, 类型为：有效的ipv6地址, 默认值：2001::1

Ipv6Increment (str): IPv6地址跳变, 类型为：有效的ipv6地址, 默认值：::1

Ipv6PrefixLength (int): IPv6地址前缀, 类型为：number, 取值范围：1-128, 默认值：64

EnableLabel2 (bool): 使能MPLS Label2, 类型为：bool, 默认值：False

Label2 (int): 封装2标签(L3 VNI), 类型为：number, 取值范围：1-16777215, 默认值：2000

Label2Step (int): 封装2标签跳变(L3 VNI Step), 类型为：number, 取值范围：1-16777215, 默认值：1

EnableIncludeRouterMac (bool): 是否包含路由MAC, 类型为：bool, 默认值：False

RouterMac (str): 路由MAC地址, 类型为：有效的mac地址, 默认值：00:00:00:00:00:00

EnableIncludeDefaultGateway (bool): 指定默认网关, 类型为：bool, 默认值：False

EnableCustomMplsLabel (bool): 使能自定义MPLS标签, 类型为：bool, 默认值：False

MplsLabel (int): MPLS标签, 类型为：number, 取值范围：1-1048575, 默认值：0

MplsLabelStep (int): MPLS标签跳变, 类型为：number, 取值范围：1-1048575, 默认值：0

EnableCustomMplsLabel2 (bool): 使能自定义MPLS Label2, 类型为：bool, 默认值：False

MplsLabel2 (int): MPLS标签2, 类型为：number, 取值范围：1-1048575, 默认值：0

MplsLabel2Step (int): MPLS标签2跳变, 类型为：number, 取值范围：1-1048575, 默认值：0

Returns:

(:obj:EvpnRouteMacIpConfig): Bgp Evpn Mac Ip Routes对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Evpn Mac Ip Routes	Session=${Session}	
Create Bgp Evpn Route Ad
Arguments
Session
** kwargs
Documentation
创建BGP EVPN以太自动发现路由对象

Args:

Session (:obj:BgpRouter): Bgp协议会话对象列表, 类型为：object

Keyword Args:

Name (str): BGP EVPN以太自动发现路由名称, 类型为：string

Enable (bool): 使能BGP EVPN以太自动发现路由, 类型为：bool, 默认值：True, 取值范围：True或False,

Origin (str): ORIGIN, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): AS路径的值, 类型为：list

AdRouteType (str): 以太自动发现路由类型, 类型为：string, 默认值：ESI, 取值范围：

EVI

ESI

VPWS

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳地址, 类型为：bool, 默认值：True, 取值范围：True或False

NextHop (str): 下一跳, 类型为：string, 默认值：100.0.0.1, 取值范围：IPv4地址

NextHopIpv6 (str): IPv6下一跳, 类型为：string, 默认值：2001::1, 取值范围：IPv6地址

EnableLinkLocalNextHop (bool): 使能IPv6 Link Local下一跳, 类型为：bool, 默认值：False, 取值范围：True或False

LinkLocalNextHop (str): IPv6 Link Local下一跳, 类型为：string, 默认值：fe80::1, 取值范围：IPv6地址

EnableOriginatorId (bool): 使能Originator ID, 类型为：bool, 默认值：False, 取值范围：True或False

OriginatorId (str): Originator ID, 类型为：string, 默认值：192.0.0.1, 取值范围：IPv4地址

VrfRouteTarget (str): VRF路由目标, 类型为：string, 默认值：100:1, 取值范围：AS:Number

VrfRouteTargetStep (str): VRF路由目标跳变, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：10.0.0.2:1, 取值范围：AS:Number或IPv4:Number

VrfRouteDistinguisherStep (str): VRF路由标识跳变, 类型为：string, 默认值：0:1

EthernetSegmentType (str):以太网段类型, 类型为：string, 默认值：OPERATOR, 取值范围：

OPERATOR

IEEE802

BRIDGEDLAN

MACBASED

ROUTEID

AS

EthernetSegmentIdentifier (str): 以太网段标识, 类型为：string, 默认值：OPERATOR

EthernetTagId (str): 以太网标签ID, 类型为：string, 默认值：00:00:00:00:00:00:00:00:00

EthernetTagIdStep (int): 太网标签ID跳变, 类型为：number, 默认值：1, 取值范围：0-4294967295

EthernetTagCountPerEvi (int): 每个EVI下以太网标签数, 类型为：number, 默认值：1, 取值范围：1-4294967295

ActiveStandbyMode (str): 主备方式, 类型为：string, 默认值：SINGLE, 取值范围：

ALL

SINGLE

EviCount (int): EVI数, 类型为：number, 默认值：1, 取值范围：1-4294967295

DataPlanEncapsulation (str): 数据平面封装, 类型为：string, 默认值：NONE, 取值范围：

NONE

VXLAN

MPLS

SRv6

Label1 (int):封装标签（VNI/VSID）, 类型为：number, 默认值：100, 取值范围：0-16777215

Label1Step (int): 封装标签跳变（VNI/VSID Step）, 类型为：number, 默认值：1, 取值范围：0-16777215

IncludeLayer2AttributeExtendedCommunity (bool): 以太自动发现路由类型为VPWS时可见, 类型为：bool, 默认值：False, 取值范围：True或False

PBit (bool): P Bit 多归单活场景中，该标志位置1表示该PE为主PE, 类型为：bool, 默认值：False, 取值范围：True或False

BBit (bool): B Bit 多归单活场景中，该标志位置1表示该PE为备PE, 类型为：bool, 默认值：False, 取值范围：True或False

CBit (bool): C Bit 置1时发送给该PE的EVPN报文必须携带控制字, 类型为：bool, 默认值：False, 取值范围：True或False

L2Mtu (bool): 指定最大传输单元，单位是字节, 类型为：bool, 默认值：False, 取值范围：True或False

EnableCustomMplsLabel (bool): 使能自定义MPLS标签, 类型为：bool, 默认值：False, 取值范围：True或False

MplsLabel (int): MPLS标签值, 类型为：number, 默认值：0, 取值范围：0-1048575

MplsLabelStep (int): MPLS标签步长, 类型为：number, 默认值：0, 取值范围：0-1048575

Returns:

(:obj:EvpnRouteAdConfig): BGP EVPN以太自动发现路由对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}		
Create Bgp Evpn Route Ad	Session=${Session}	EnableCustomMplsLabel=True	MplsLabel=1000	MplsLabelStep=2
Create Bgp Flow Spec Conponent Type
Arguments
FlowSpec
Types
** kwargs
Documentation
创建Bgp Flow Specs Conponent Type对象, 类型为：object / list

Args:

FlowSpec(:obj:BgpIpv4FlowSpecConfig): BGP Flow Spec对象, 类型为：object / list

Types (int): BGP IPv4 FLowSpec Type序号, 类型为：number, 取值范围：1-12

Keyword Args:

IpValue (str): 指定起始地址, 类型为有效的ipv4地址, 默认值: "192.0.1.0"

PrefixLength (int): 指定前缀长度, 类型为：number, 取值范围：1-32, 默认值：24

AddressList (str): 类型为列表时, 指定地址列表, 类型为有效的ipv4地址, 默认值: ""

InputType (str): 指定类型, 类型为：string, 默认值：RANGE, 取值范围：

RANGE

LIST

RFC_4814

Count (int): 地址数量, 类型为：number, 取值范围：1-99, 默认值：1

Step (int): 地址跳变步长, 类型为：number, 取值范围：1-4294967295, 默认值：1

EqualBit (bool): 数据与指定值相等表示匹配, 类型为：bool, 取值范围：True或False, 默认值：False

LessThanBit (bool): 数据小于指定值表示匹配, 类型为：bool, 取值范围：True或False, 默认值：False

MoreThanBit (bool): 数据大于指定值表示匹配, 类型为：bool, 取值范围：True或False, 默认值：False

AndBit (bool): 如果选中And Bit，则该{option/value}组与前一个{option/value}组之间的关系是逻辑与（AND）；如果未选中And Bit，则该{option/value}组与前一个{option/value}组之间的关系是逻辑或（OR）。类型为：bool, 取值范围：True或False, 默认值：False

ValueField (int): 类型为：number, 取值范围：1-15, 默认值：1

Count (int): 类型为：number, 取值范围：0-99, 默认值：1

ValueIncrement (int): 类型为：number, 取值范围：0-65535, 默认值：1

ValueList (int): 类型为：number, 取值范围：0-65535, 默认值：""

ValueType (str): 指定值的类型, 类型为：string, 默认值：Increment, 取值范围：

Increment

List

NotBit (bool): 选中Not Bit时，对计算结果按位取反。类型为：bool, 取值范围：True或False, 默认值：False

MatchBit (bool): 选中Match Bit时，(data & value) == value表示按位匹配；未选中Match Bit时，如果数据中包含值掩码，则(data & value) == True表示匹配。其中，data是发送的数据，value是给定的值掩码。类型为：bool, 取值范围：True或False, 默认值：False

DSCPValue (int): 类型为：number, 取值范围：0-63, 默认值：0

Returns:

(:obj:BgpIpv4FlowSpecType1Component): Bgp Flow Spec Conponent Type对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${FlowSpec}	Create Bgp Ipv4 Flow Specs	Session=${Session}
Create Bgp Flow Spec Conponent Type	FlowSpec=${FlowSpec}	Type=1
Create Bgp Flow Spec Custom Path Attribute
Arguments
FlowSpec
** kwargs
Documentation
创建BGP Flow Spec Custom Path Attribute对象, 类型为：object / list

Args:

FlowSpec(:obj:BgpIpv4FlowSpecConfig): 所属的Bgp Flow Spec对象, 类型为：object / list

Keyword Args:

PathAttributeType (int): 路径属性的类型, 类型为：number, 取值范围：1-255, 默认值：1

OptionalFlag (str): 指定Optional Flag的值, 类型为：string, 默认值：OPTION, 取值范围：

WELL_KNOWN

OPTION

TransitiveFlag (str): 指定Transitive Flag的值, 类型为：string, 默认值：NONTRANSITIVE, 取值范围：

NONTRANSITIVE

TRANSITIVE

PartialFlag (str): 指定Partial Flag的值, 类型为：string, 默认值：PARTIAL, 取值范围：

COMPLETE

PARTIAL

ExtendedLengthFlag (bool): 是否启用Extended Length Flag, 类型为：bool, 默认值：False

AttributeValue (str): 指定路径属性的值, 类型为：string, 默认值：""

Returns:

(:obj:BgpFlowSpecPathAttributeConfig): Bgp Route Pool Custom Path Attribute对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${FlowSpecs}	Create Bgp Ipv4 Flow Specs	Session=${Session}
Create Bgp Flow Spec Custom Path Attribute	FlowSpec=${FlowSpecs}	
Create Bgp Flow Specs Actions
Arguments
FlowSpec
** kwargs
Documentation
创建Bgp Ipv4 Flow Specs Actions对象, 类型为：object / list

Args:

FlowSpec(:obj:BgpIpv4FlowSpecConfig): BGP Flow Spec对象, 类型为：object / list

Keyword Args:

EnableTrafficRate (bool): 启用流量限速动作。类型为：bool, 取值范围：True或False, 默认值：True

TrafficRate (int): 类型为：number, 取值范围：1-4294967295, 默认值：0

AsNum (int): 指定AS号。类型为：number, 取值范围：1-4294967295, 默认值：1

EnableTrafficAction (bool): 启用Traffic action。类型为：bool, 取值范围：True或False, 默认值：True

SampleBit (bool): 启用流量抽样记录。类型为：bool, 取值范围：True或False, 默认值：True

TerminateBit (bool): 撤销已生效的匹配规则。类型为：bool, 取值范围：True或False, 默认值：True

EnableRedirect: 启用流量重定向到指定的路由目标动作。类型为：bool, 取值范围：True或False, 默认值：False

RouteTarget (str): 指定重定向的路由目标。类型为：string, 默认值："100:1"

EnableTrafficMarking (bool): 启用重新标记报文DSCP值的动作。类型为：bool, 取值范围：True或False, 默认值：True

DSCPValue (int): 以十六进制形式指定重新标记报文所使用的DSCP值。类型为：number, 取值范围：1-4294967295, 默认值：0

EnableRedirectToIpNextHop (bool): 启用重定向到下一跳动作, 类型为：bool, 取值范围：True或False, 默认值：False

NextHop (str): 指定下一跳IP, 类型为有效的ipv4地址, 默认值: "0.0.1.0"

CopyBit (bool): 复制一份规则匹配的流量，并执行重定向到下一跳动作。类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:BgpIpv4FlowSpecAction): Bgp Ipv4 Flow Specs Actions对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${FlowSpec}	Create Bgp Ipv4 Flow Specs	Session=${Session}
Create Bgp Ipv4 Flow Specs Action	FlowSpec=${FlowSpec}	
Create Bgp Ipv4 Flow Specs
Arguments
Session
** kwargs
Documentation
创建Bgp Ipv4 Flow Specs对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

Keyword Args:

RouteCount (int): 类型为：number, 取值范围：1-8000000, 默认值：1

FlowSpecSubAfi (str): 指定SubAFI的值, 类型为：string, 默认值：FlowSpec, 取值范围：

FlowSpec

FlowSpecVpn

Origin (str): 指定ORIGIN的值, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

AsPathType (str): AS Path类型, 类型为：string, 默认值：SEQUENCE, 取值范围：

SET

SEQUENCE

EnableLocalPref (bool): 类型为：bool, 取值范围：True或False, 默认值：True

LocalPref (int): 类型为：number, 默认值：10

EnableMed (bool): 类型为：bool, 取值范围：True或False, 默认值：False

MultExitDisc (int): 类型为：number, 取值范围：1-4294967295, 默认值：0

EnableClusterIdList (bool): 是否启用Cluster ID List, 类型为：bool, 取值范围：True或False, 默认值：False

ClusterIdList (str): 指定cluster ID list的值, 类型为：有效的ipv4地址, 默认值：""

EnableCommunity (bool): 类型为：bool, 取值范围：True或False, 默认值：False

CommunityType (str): 团体类型, 类型为：string, 默认值：AA_NN, 取值范围：

AA_NN

NO_EXPORT

NO_ADVERTISE

LOCAL_AS

CommunityAsNumber (int): 当Type为AA:NN时，指定团体的AS号, 类型为：number, 取值范围：1-65535, 默认值：1

CommunityId (int): 当Type为AA:NN时，指定团体的ID值, 类型为：number, 取值范围：1-65535, 默认值：1

Community (str): 当Type为NO_EXPORT时，团体值为0xffffff01；当Type为NO_ADVERTISE时，团体值为0xffffff02；当Type为LOCAL_AS时，团体值为0xffffff03, 类型为：string, 默认值：""

ExtendedCommunity (str): 扩展团体, 类型为：string, 默认值：""

ComponentType (list): 过滤规则, 类型为：list, 默认值：Type1, 取值范围：

Type1

Type2

Type3

Type4

Type5

Type6

Type7

Type8

Type9

Type10

Type11

Type12

VrfNum (int): VRF数量, 类型为：number, 默认值：1

VrfRouteTarget (str): 指定VRF路由目标起始值, 类型为：string, 默认值：100:1

VrfRouteTargetStep (str): 指定VRF路由目标的跳变步长, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：1:1

VrfRouteDistinguisherStep (str): 指定VRF路由标识的跳变步长, 类型为：string, 默认值：0:1

Returns:

(:obj:BgpIpv4FlowSpecConfig): Bgp Ipv4 Flow Specs对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Ipv4 Flow Specs	Session=${Session}	
Create Bgp Ipv4 Flowspec Performance
Arguments
Session
MaxRouteCount
SourcePrefix
DestPrefix
Documentation
创建bgpflowspec性能条目

Args:

Session: bgp session

MaxRouteCount: 支持最大bgpls数量

SourcePrefix: 接口列表

DestPrefix: BGP ipv4路由列表

Returns:

bool: 布尔值Bool (范围：True / False)

Examples:

Create Bgp Ipv4 Route Pool
Arguments
Session
** kwargs
Documentation
创建BGP IPv4路由对象

Args:

Session (:obj:BgpRouter): Bgp协议会话对象列表, 类型为：object

Keyword Args:

Name (str): BGP IPv4路由名称, 类型为：string

Enable (bool): 使能BGP IPv4路由, 类型为：bool, 取值范围：True或False, 默认值：True

SubAfi (str): Sub-AFI, 类型为：string, 默认值：UNICAST, 支持类型：

UNICAST

MULTICAST

VPN

LABELED

Origin (str): 路由属性中的ORIGIN值, 类型为：string, 取值范围：Incomplete; IGP; EGP, 默认值：IGP

AsPath (int): AS Path, 类型为：number, 取值范围：1-255,

AsPathType (str): AS Path类型, 类型为：string, 取值范围：Incomplete; IGP; EGP, 默认值：IGP

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳, 类型为：bool, 取值范围：True或False, 默认值：True

EnableLocalPref (bool): 使能Local Preference, 类型为：bool, 取值范围：True或False, 默认值：True

LocalPref (int): LocalPref, 当使能Local Preference为选中状态时配置该选项, 类型为：number, 取值范围：0-4294967295, 默认值：10

EnableMed (bool): 使能Multi Exit Discriminator, 类型为：bool, 取值范围：True或False, 默认值：False

MultExitDisc (int): Multi Exit Discriminator, 当使能Multi Exit Discriminator为选中状态时配置该选项, 类型为：number, 取值范围：0-4294967295, 默认值：0

AtomicAggregate (bool): 使能Atomic Aggregate, 类型为：bool, 取值范围：True或False, 默认值：False

EnableAggregator (bool): 使能Aggregator, 类型为：bool, 取值范围：True或False, 默认值：False

AggregatorAsNumber (int): Aggregator自治域, 类型为：number, 取值范围：1-4294967295, 默认值：1

AggregatorIp (str): Aggregator IP, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.1.0

EnableOriginatorId (bool): 使能Originator ID, 类型为：bool, 取值范围：True或False, 默认值：False

OriginatorId (str): Originator ID, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.1.0

EnableClusterIdList (bool): 使能Cluster ID List, 类型为：bool, 取值范围：True或False, 默认值：False

ClusterIdList (str): Cluster ID List, 类型为：string, 取值范围：IPv4地址, 默认值：空

EnableCommunity (bool): 使能团体, 类型为：bool, 取值范围：True或False, 默认值：False

CommunityType (str): 团体类型, 类型为：string默认值：AA:NN, 取值范围：

AA_NN

NO_EXPORT

NO_ADVERTISE

LOCAL_AS

CommunityAsNumber (int): 团体自治域, 当Type为AA:NN时，指定团体的AS号, 类型为：number, 取值范围：1-65535, 默认值：1

CommunityId (int): 团体ID, 当Type为AA:NN时，指定团体的ID值, 类型为：number, 取值范围：1-65535, 默认值：1

Community (str): 团体, 类型为：list, 默认值：[]

CommunityIncrement (str): 团体跳变, 类型为：list, 默认值：[]

CommunityPerBlockCount (int): 每个路由组团体数量, 类型为：number, 取值范围：1-65535, 默认值：1

ExtendedCommunity (str): 扩展团体, 类型为：list, 默认值：[], 例如：['0x00:0x02:1:1', '0x01:0x02:1:2', '0x02:0x02:1:3']

VrfRd (str): VRF路由标识, 类型为：string, 取值范围：AS:Number或IPv4:Number, 默认值：1:1

VrfRdStep (str): VRF路由标识跳变, 类型为：string, 取值范围：AS:Number或IPv4:Number, 默认值：0:1

VrfRt (str): VRF路由目标, 类型为：string, 取值范围：AS:Number, 默认值：100:1

VrfRtStep (str): VRF路由目标跳变, 类型为：string, 取值范围：AS:Number, 默认值：0:1

VrfCount (int) (int): VRF数量, 类型为：number, 取值范围：1-65535, 默认值：1

StartingLabel (int): 起始标签, 类型为：number, 取值范围：0-1048575, 默认值：16

LabelType (str): 路由标签类型, 类型为：类型为：string, 取值范围：Fixed; Incrementa; Explicit Nul; Implicit Null, 默认值：Fixed

FirstRoute (str): IPv4路由起始值, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.1.0

RandomRoute (bool): 随机路由, 类型为：bool, 取值范围：True或False, 默认值：False

RouteCount (int): 每个会话路由数量, 类型为：number, 取值范围：1-8000000, 默认值：1

RouteStep (str): IPv4路由跳变步长, 类型为：string, 取值范围：IPv4地址, 默认值：0.0.1.0

Ipv4RouteStep (int): IPv4路由跳变步长, 类型为：number, 取值范围：1-4294967295, 默认值：1

PrefixLength (int): IPv4路由前缀长度, 类型为：number, 取值范围：1-32, 默认值：24

NextHopAddrType (str): 下一跳地址类型, 类型为：string, 取值范围：IPv4; IPv6, 默认值：IPv4

NextHop (str): 下一跳地址, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.1.0

NextHopStep (str): 下一跳步长, 类型为：string, 取值范围：IPv4地址, 默认值：0.0.0.1

IPv6NextHop (str): IPv6下一跳地址, 类型为：string, 取值范围：IPv4地址, 默认值：2000::1

IPv6NextHopStep (str): IPv6下一跳步长, 类型为：string, 取值范围：IPv6地址, 默认值：::1

EnableLinkLocalNextHop (bool): 使能Link Local地址作为下一跳, 类型为：bool, 取值范围：True或False, 默认值：False

Ipv6LinkLocalNextHop (str): IPv6 Link Local下一跳地址, 类型为：string, 取值范围：IPv4地址, 默认值：2000::1

Ipv6LinkLocalNextHopStep (str): IPv6 Link Local下一跳步长, 类型为：string, 取值范围：IPv6地址, 默认值：::1

EncodeSrTlvs (list): 编码SR TLV, 类型为：list, 默认值：0, 取值范围：

LABEL_INDEX

SRGB

SRV6_VPN_SID

SRV6_SERVICES

OverrideGlobalSrgb (bool): 覆盖全局SRGB, 类型为：bool, 取值范围：True或False, 默认值：False

SrgbBase (int): SRGB起始值, 类型为：number, 取值范围：0-16777215, 默认值：16000

SrgbRange (int): SRGB范围, 类型为：number, 取值范围：0-16777215, 默认值：1000

LabelIndex (int): 标签序号, 类型为：number, 取值范围：0-4294967295, 默认值：0

LabelStep (int): 标签步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

Srv6SidInfoSubTlvType (int): SRv6 SID Information Sub TLV类型, 类型为：number, 取值范围：1-255, 默认值：1

Srv6LocatorBlockLength (int): SRv6 Locator Block长度, 类型为：number, 取值范围：0-128, 默认值：32

Srv6LocatorNodeLength (int): SRv6 Locator Node长度, 类型为：number, 取值范围：1-128, 默认值：32

Srv6FuncLength (int): SRv6 Function长度, 类型为：number, 取值范围：0-128, 默认值：32

Srv6FuncOpcode (str): SRv6 Function Opcode, 类型为：string, 取值范围：格式：ff:ff:ff, 默认值：0

Srv6ArguLength (int): SRv6 Argument长度, 类型为：number, 取值范围：1-128, 默认值：32

Srv6Argument (str): SRv6 Argument, 类型为：string, 取值范围：格式：ff:ff:ff, 默认值：0

EncodedSrv6ServiceDataSubTlvs (list): 编码SRv6 Service Data Sub TLVs, 类型为：list, 默认值：NO_SHOW, 取值范围：

NO_SHOW

SRV6_ID_STRUCTURE

Srv6TranspositionLength (int): SRv6 Transposition长度, 类型为：number, 取值范围：0-24, 默认值：0

Srv6TranspositionOffset (int): SRv6 Transposition偏移, 类型为：number, 取值范围：0-15, 默认值：0

Srv6Locator (str): 使用的认证类型, 类型为：string, 取值范围：None或MD5, 默认值：None

Srv6LocatorStep (str): 认证密码, 类型为：类型为：string, 取值范围：字符串，由1-255个数字、字母或特殊字符组成, 默认值：xinertel

Srv6EndpointBehavior (str): SRv6 Endpoint Behavior, 类型为：string, 默认值：CUSTOM, 支持的值：

END_DX6

END_DX4

END_DT6

END_DT4

END_DT46

END_DX2

END_DX2V

END_DT2U

END_DT2M

CUSTOM

Srv6CustomEndpointBehavior (int): 自定义SRv6 Endpoint Behavior, 类型为：hex number, 取值范围：0x0-0xFFFF, 默认值：0xFFFF

Returns:

(:obj:BgpIpv4RoutepoolConfig): BGP IPv4路由对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}			
${Community}	Create List	AA_NN	NO_EXPORT	NO_ADVERTISE	LOCAL_AS
${CommunityIncrement}	Create List	1:1	1:2	1:3	1:4
${ExtendedCommunity}	Create List	0x00:0x02:1:1	0x01:0x02:1:2	0x02:0x02:1:3	
${RoutePool}	Create Bgp Ipv4 Route Pool	Session=${Session}	Community=${Community}	CommunityIncrement=${CommunityIncrement}	ExtendedCommunity=${ExtendedCommunity}
${Community}	Create List	AA_NN	NO_EXPORT		
${CommunityIncrement}	Create List	2:1	2:2		
Edit Configs	Configs=${RoutePool}	Community=${Community}	CommunityIncrement=${CommunityIncrement}	CommunityPerBlockCount=2	
Create Bgp Ipv4 Vpls
Arguments
Session
** kwargs
Documentation
创建Bgp Ipv4 Vpls对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

Keyword Args:

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

AsPathType (str): AS Path类型, 类型为：string, 默认值：SEQUENCE, 取值范围：

SET

SEQUENCE

CONFED_SEQUENCE

CONFED_SET

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳地址, 类型为：bool, 默认值：True

NextHop (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv4地址, 默认值：100.0.0.1

MultExitDisc (int): 类型为：number, 取值范围：1-4294967295, 默认值：0

LocalPreference (int): Local优先级, 类型为：number, 取值范围：1-4294967295, 默认值：10

VeId (int): 类型为：number, 取值范围：1-65535, 默认值：0

VeIdStep (int): 类型为：number, 取值范围：1-65535, 默认值：1

BlockOffset (int): 类型为：number, 取值范围：1-65535, 默认值：0

BlockOffsetStep (int): 类型为：number, 取值范围：1-65535, 默认值：0

BlockSize (int): 类型为：number, 取值范围：1-65535, 默认值：5

MtuSize (int): 类型为：number, 取值范围：64-9000, 默认值：1500

EncapType (str): 封装类型, 类型为：string, 默认值：VLAN, 取值范围：

VLAN

ETHERNET

VPLS

ControlFlag (int): 控制标识。以十进制表示。类型为：number, 取值范围：1-255, 默认值：0

VrfRouteTarget (str): 指定VRF路由目标起始值, 类型为：string, 默认值：100:1

VrfRouteTargetStep (str): 指定VRF路由目标的跳变步长, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：10.0.0.2:1

VrfRouteDistinguisherStep (str): 指定VRF路由标识的跳变步长, 类型为：string, 默认值：0:1

VrfCount (int): 类型为：number, 取值范围：1-65535, 默认值：1

Returns:

(:obj:BgpIpv4VplsConfig): Bgp Ipv4 Vpls对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Ipv4 Vpls	Session=${Session}	
Create Bgp Ipv6 Flow Spec
Arguments
Session
** kwargs
Documentation
创建BGP Ipv6 Flow Spec对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象, 类型为：object / list

Keyword Args:

RouteCount (int): 类型为：number, 取值范围：1-8000000, 默认值：1

FlowSpecSubAfi (str): 指定SubAFI的值, 类型为：string, 默认值：FlowSpec, 取值范围：

FlowSpec

FlowSpecVpn

FlowSpecActionType (str): 指定Optional Flag的值, 类型为：string, 默认值：RedirectRT, 取值范围：

RedirectRT

ComponentType (list): 指定Transitive Flag的值, 类型为：list, 默认值：Type1, 取值范围：

Type1

Type2

DestinationPrefix (str): 指定Partial Flag的值, 类型为：有效的ipv6地址, 默认值：2000::1

DestinationPrefixLength (bool): 是否启用Extended Length Flag, 类型为：bool, 默认值：False

DestinationPrefixIncrement (int): 指定路径属性的长度, 类型为：number, 取值范围：1-128, 默认值：64

DestinationPrefixCount (int): 指定路径属性的值, 类型为：number, 取值范围：1-65535, 默认值：1

DestinationPrefixOffset (int): 目的IP前缀偏移, 类型为：number, 默认值：0

SourcePrefix (str): 源IP前缀, 类型为：有效的ipv6地址, 默认值：2000::1

SourcePrefixLength (int): 源IP前缀长度, 类型为：number, 取值范围：1-128, 默认值：64

SourcePrefixIncrement (int): 源IP前缀偏移, 类型为：number, 取值范围：1-4294967295, 默认值：1

SourcePrefixCount (int): 源IP前缀个数, 类型为：number, 取值范围：1-65535, 默认值：1

SourcePrefixOffset (int): 源IP前缀偏移, 类型为：number, 取值范围：0-255, 默认值：0

Origin (str): 指定ORIGIN的值, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

AsPathType (str): AS Path类型, 类型为：string, 默认值：SEQUENCE, 取值范围：

SET

SEQUENCE

EnableLocalPref (bool): 是否启用Local_PREF属性。类型为：bool, 取值范围：True或False, 默认值：True

LocalPref (int): 指定Local_PREF的值。类型为：number, 取值范围：1-4294967295, 默认值：10

EnableMed (bool): 是否启用MULTI_EXIT_DISC属性。类型为：bool, 取值范围：True或False, 默认值：False

MultExitDisc (int): 指定Multi Exit Discriminator的值。类型为：number, 取值范围：1-4294967295, 默认值：0

EnableClusterIdList (bool): 是否启用Cluster ID List, 类型为：bool, 取值范围：True或False, 默认值：False

ClusterIdList (str): 指定cluster ID list的值, 类型为：有效的ipv4地址, 默认值：""

EnableCommunity (bool): 类型为：bool, 取值范围：True或False, 默认值：False

CommunityType (str): 团体类型, 类型为：string, 默认值：AA_NN, 取值范围：

AA_NN

NO_EXPORT

NO_ADVERTISE

LOCAL_AS

CommunityAsNumber (int): 当Type为AA:NN时，指定团体的AS号, 类型为：number, 取值范围：1-65535, 默认值：1

CommunityId (int): 当Type为AA:NN时，指定团体的ID值, 类型为：number, 取值范围：1-65535, 默认值：1

Community (str): 当Type为NO_EXPORT时，团体值为0xffffff01；当Type为NO_ADVERTISE时，团体值为0xffffff02；当Type为LOCAL_AS时，团体值为0xffffff03, 类型为：string, 默认值：""

ExtendedCommunity (str): 扩展团体, 类型为：string, 默认值：""

VrfNum (int): VRF数量, 类型为：number, 默认值：1

VrfRouteTarget (str): 指定VRF路由目标起始值, 类型为：string, 默认值：100:1

VrfRouteTargetStep (str): 指定VRF路由目标的跳变步长, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：1:1

VrfRouteDistinguisherStep (str): 指定VRF路由标识的跳变步长, 类型为：string, 默认值：0:1

Returns:

(:obj:BgpIpv6FlowSpecConfig): Bgp Ipv6 Flow Spec对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${FlowSpecs}	Create Bgp Ipv6 Flow Specs	Session=${Session}
Create Bgp Ipv6 Flow Spec Action
Arguments
FlowSpec
** kwargs
Documentation
创建Bgp Ipv6 Flow Specs Actions对象, 类型为：object / list

Args:

FlowSpec(:obj:BgpIpv6FlowSpecConfig): BGP Flow Spec对象, 类型为：object / list

Keyword Args:

EnableTrafficRate (bool): 启用流量限速动作。类型为：bool, 取值范围：True或False, 默认值：True

TrafficRate (int): 指定流量的最大传输速率, 类型为：number, 取值范围：1-4294967295, 默认值：0

AsNum (int): 指定AS号。类型为：number, 取值范围：1-4294967295, 默认值：1

EnableTrafficAction (bool): 启用Traffic action。类型为：bool, 取值范围：True或False, 默认值：True

SampleBit (bool): 启用流量抽样记录。类型为：bool, 取值范围：True或False, 默认值：True

TerminateBit (bool): 撤销已生效的匹配规则。类型为：bool, 取值范围：True或False, 默认值：True

EnableRedirect (bool): 启用流量重定向到指定的路由目标动作。类型为：bool, 取值范围：True或False, 默认值：False

RedirectIpv6RouteTarget (str): 指定重定向的路由目标。类型为：string, 默认值："100:1"

EnableRedirectToIpv6NextHop (bool): 启用重定向到下一跳动作, 类型为：bool, 取值范围：True或False, 默认值：False

Type (str): 类型为：string, 默认值："TYPE_0x000c", 取值范围：

TYPE_0x0800

TYPE_0x000c

NextHop (str): 指定下一跳IP, 类型为有效的ipv6地址, 默认值: "2000::1"

CopyBit (bool): 复制一份规则匹配的流量，并执行重定向到下一跳动作。类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:BgpIpv6FlowSpecAction): Bgp Ipv6 Flow Specs Actions对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${FlowSpec}	Create Bgp Ipv6 Flow Specs	Session=${Session}
Create Bgp Ipv6 Flow Specs Action	FlowSpec=${FlowSpec}	
Create Bgp Ipv6 Route Pool
Arguments
Session
** kwargs
Documentation
创建BGP IPv6路由对象

Args:

Session (:obj:BgpRouter): Bgp协议会话对象列表, 类型为：object

Keyword Args:

Name (str): BGP IPv6路由名称, 类型为：string

Enable (bool): 使能BGP IPv6路由, 类型为：bool, 取值范围：True或False, 默认值：True

SubAfi (str): Sub-AFI, 类型为：string, 默认值：UNICAST, 支持类型：

UNICAST

MULTICAST

VPN

LABELED

Origin (str): 路由属性中的ORIGIN值, 类型为：string, 取值范围：Incomplete; IGP; EGP, 默认值：IGP

AsPath (int): AS Path, 类型为：number, 取值范围：1-255,

AsPathType (str): AS Path类型, 类型为：string, 取值范围：Incomplete; IGP; EGP, 默认值：IGP

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳, 类型为：bool, 取值范围：True或False, 默认值：True

EnableLocalPref (bool): 使能Local Preference, 类型为：bool, 取值范围：True或False, 默认值：True

LocalPref (int): LocalPref, 当使能Local Preference为选中状态时配置该选项, 类型为：number, 取值范围：0-4294967295, 默认值：10

EnableMed (bool): 使能Multi Exit Discriminator, 类型为：bool, 取值范围：True或False, 默认值：False

MultExitDisc (int): Multi Exit Discriminator, 当使能Multi Exit Discriminator为选中状态时配置该选项, 类型为：number, 取值范围：0-4294967295, 默认值：0

AtomicAggregate (bool): 使能Atomic Aggregate, 类型为：bool, 取值范围：True或False, 默认值：False

EnableAggregator (bool): 使能Aggregator, 类型为：bool, 取值范围：True或False, 默认值：False

AggregatorAsNumber (int): Aggregator自治域, 类型为：number, 取值范围：1-4294967295, 默认值：1

AggregatorIp (str): Aggregator IP, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.1.0

EnableOriginatorId (bool): 使能Originator ID, 类型为：bool, 取值范围：True或False, 默认值：False

OriginatorId (str): Originator ID, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.1.0

EnableClusterIdList (bool): 使能Cluster ID List, 类型为：bool, 取值范围：True或False, 默认值：False

ClusterIdList (str): Cluster ID List, 类型为：string, 取值范围：IPv4地址, 默认值：空

EnableCommunity (bool): 使能团体, 类型为：bool, 取值范围：True或False, 默认值：False

CommunityType (str): 团体类型, 类型为：string, 取值范围：AA:NN; NO_EXPORT; NO_ADVERTISE; LOCAL_AS, 默认值：AA:NN

CommunityAsNumber (int): 当Type为AA:NN时，指定团体的AS号, 类型为：number, 取值范围：1-65535, 默认值：1

Community (str): 团体, 类型为：list, 默认值：[], 取值范围：

AA_NN

NO_EXPORT

NO_ADVERTISE

LOCAL_AS

CommunityIncrement (str): 团体跳变, 类型为：list, 默认值：[], 取值范围：AA:NN

CommunityPerBlockCount (int): 每个路由组团体数量, 类型为：number, 取值范围：1-65535, 默认值：1

ExtendedCommunity (str): 扩展团体, 类型为：list, 默认值：[], 例如：['0x00:0x02:1:1', '0x01:0x02:1:2', '0x02:0x02:1:3']

VrfRd (str): VRF路由标识, 类型为：string, 取值范围：AS:Number或IPv4:Number, 默认值：1:1

VrfRdStep (str): VRF路由标识跳变, 类型为：string, 取值范围：AS:Number或IPv4:Number, 默认值：0:1

VrfRt (str): VRF路由目标, 类型为：string, 取值范围：AS:Number, 默认值：100:1

VrfRtStep (str): VRF路由目标跳变, 类型为：string, 取值范围：AS:Number, 默认值：0:1

VrfCount (int): VRF数量, 类型为：number, 取值范围：1-65535, 默认值：1

StartingLabel (int): 起始标签, 类型为：number, 取值范围：0-1048575, 默认值：16

LabelType (str): 路由标签类型, 类型为：类型为：string, 取值范围：Fixed; Incrementa; Explicit Nul; Implicit Null, 默认值：Fixed

FirstIpv6Route (str): IPv6路由起始值, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

RouteCount (int): 每个会话路由数量, 类型为：number, 取值范围：1-8000000, 默认值：1

RouteStep (str): IPv6路由跳变步长, 类型为：string, 取值范围：IPv6地址, 默认值：'0:0:0:1::'

Ipv6RouteStep (int): IPv6路由跳变步长, 类型为：number, 取值范围：1-4294967295, 默认值：1

PrefixLength (int): IPv4路由前缀长度, 类型为：number, 取值范围：1-32, 默认值：24

NextHopAddrType (str): 下一跳地址类型, 类型为：string, 取值范围：IPv4; IPv6, 默认值：IPv4

NextHop (str): 下一跳地址, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.1.0

NextHopStep (str): 下一跳步长, 类型为：string, 取值范围：IPv4地址, 默认值：0.0.0.1

IPv6NextHop (str): IPv6下一跳地址, 类型为：string, 取值范围：IPv4地址, 默认值：2000::1

IPv6NextHopStep (str): IPv6下一跳步长, 类型为：string, 取值范围：IPv6地址, 默认值：::1

EnableLinkLocalNextHop (bool): 使能Link Local地址作为下一跳, 类型为：bool, 取值范围：True或False, 默认值：False

Ipv6LinkLocalNextHop (str): IPv6 Link Local下一跳地址, 类型为：string, 取值范围：IPv4地址, 默认值：2000::1

Ipv6LinkLocalNextHopStep (str): IPv6 Link Local下一跳步长, 类型为：string, 取值范围：IPv6地址, 默认值：::1

EncodeSrTlvs (list): 编码SR TLV, 类型为：list, 默认值：NO_SHOW, 取值范围：

NO_SHOW

SRV6_VPN_SID

SRV6_SERVICES

OverrideGlobalSrgb (bool): 覆盖全局SRGB, 类型为：bool, 取值范围：True或False, 默认值：False

SrgbBase (int): SRGB起始值, 类型为：number, 取值范围：0-16777215, 默认值：16000

SrgbRange (int): SRGB范围, 类型为：number, 取值范围：0-16777215, 默认值：1000

LabelIndex (int): 标签序号, 类型为：number, 取值范围：0-4294967295, 默认值：0

LabelStep (int): 标签步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

Srv6SidInfoSubTlvType (int): SRv6 SID Information Sub TLV类型, 类型为：number, 取值范围：1-255, 默认值：1

Srv6LocatorBlockLength (int): SRv6 Locator Block长度, 类型为：number, 取值范围：0-128, 默认值：32

Srv6LocatorNodeLength (int): SRv6 Locator Node长度, 类型为：number, 取值范围：1-128, 默认值：32

Srv6FuncLength (int): SRv6 Function长度, 类型为：number, 取值范围：0-128, 默认值：32

Srv6FuncOpcode (str): SRv6 Function Opcode, 类型为：string, 取值范围：格式：ff:ff:ff, 默认值：0

Srv6ArguLength (int): SRv6 Argument长度, 类型为：number, 取值范围：1-128, 默认值：32

Srv6Argument (str): SRv6 Argument, 类型为：string, 取值范围：格式：ff:ff:ff, 默认值：0

EncodedSrv6ServiceDataSubTlvs (list): 编码SRv6 Service Data Sub TLVs, 类型为：list, 默认值：NO_SHOW, 取值范围：

NO_SHOW

SRV6_ID_STRUCTURE

Srv6TranspositionLength (int): SRv6 Transposition长度, 类型为：number, 取值范围：0-24, 默认值：0

Srv6TranspositionOffset (int): SRv6 Transposition偏移, 类型为：number, 取值范围：0-15, 默认值：0

Srv6Locator (str): 使用的认证类型, 类型为：string, 取值范围：None或MD5, 默认值：None

Srv6LocatorStep (str): 认证密码, 类型为：类型为：string, 取值范围：字符串，由1-255个数字、字母或特殊字符组成, 默认值：xinertel

Srv6EndpointBehavior (str): SRv6 Endpoint Behavior, 类型为：string, 默认值：CUSTOM, 支持的值：

END_DX6

END_DX4

END_DT6

END_DT4

END_DT46

END_DX2

END_DX2V

END_DT2U

END_DT2M

CUSTOM

Srv6CustomEndpointBehavior (int): 自定义SRv6 Endpoint Behavior, 类型为：hex number, 取值范围：0x0-0xFFFF, 默认值：0xFFFF

Returns:

(:obj:BgpIpv6RoutepoolConfig): BGP IPv6路由对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}			
${Community}	Create List	AA_NN	NO_EXPORT	NO_ADVERTISE	LOCAL_AS
${CommunityIncrement}	Create List	1:1	1:2	1:3	1:4
${ExtendedCommunity}	Create List	0x00:0x02:1:1	0x01:0x02:1:2	0x02:0x02:1:3	
${RoutePool}	Create Bgp Ipv6 Route Pool	Session=${Session}	Community=${Community}	CommunityIncrement=${CommunityIncrement}	ExtendedCommunity=${ExtendedCommunity}
${Community}	Create List	AA_NN	NO_EXPORT		
${CommunityIncrement}	Create List	2:1	2:2		
Edit Configs	Configs=${RoutePool}	Community=${Community}	CommunityIncrement=${CommunityIncrement}	CommunityPerBlockCount=2	
Create Bgp Ipv6 Vpls
Arguments
Session
** kwargs
Documentation
创建Bgp Ipv6 Vpls对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

Keyword Args:

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳地址, 类型为：bool, 默认值：True

NextHop (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv6地址, 默认值：2000::1

LinkLocalNextHop (str): 类型为：有效的ipv6地址, 默认值：fe80::1

MultExitDisc (int): 类型为：number, 取值范围：1-4294967295, 默认值：0

LocalPreference (int): Local优先级, 类型为：number, 取值范围：1-4294967295, 默认值：10

VeId (int): 类型为：number, 取值范围：1-65535, 默认值：1

VeIdStep (int): 类型为：number, 取值范围：1-65535, 默认值：0

BlockOffset (int): 类型为：number, 取值范围：1-65535, 默认值：0

BlockOffsetStep (int): 类型为：number, 取值范围：1-65535, 默认值：0

BlockSize (int): 类型为：number, 取值范围：1-65535, 默认值：5

MtuSize (int): 类型为：number, 取值范围：64-65535, 默认值：1500

EncapType (str): 封装类型, 类型为：string, 默认值：VLAN, 取值范围：

VLAN

ETHERNET

VPLS

EnableRfc4761 (bool): 类型为：bool, 默认值：True

ControlFlag (int): 控制标识。以十进制表示。类型为：number, 默认值：0

StripVlan (bool): 类型为：bool, 默认值：False

VeFlooding (bool): 类型为：bool, 默认值：False

VrfRouteTarget (str): 指定VRF路由目标起始值, 类型为：string, 默认值：100:1

VrfRouteTargetStep (str): 指定VRF路由目标的跳变步长, 类型为：string, 默认值：0:1

VrfRouteDistinguisher (str): 指定VRF路由标识起始值, 类型为：string, 默认值：10.0.0.2:1

VrfRouteDistinguisherStep (str): 指定VRF路由标识的跳变步长, 类型为：string, 默认值：0:1

VrfCount (int): 类型为：number, 取值范围：1-65535, 默认值：1

Returns:

(:obj:BgpIpv6VplsConfig): Bgp Ipv6 Vpls对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Ipv6 Vpls	Session=${Session}	
Create Bgp Link States
Arguments
Session
** kwargs
Documentation
创建Bgp Link States对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

Keyword Args:

Origin (str): 路由产生源, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): 自治域路径, 类型为：string, 默认值：""

AsPathType (str): 自治域路径类型, 类型为：string, 默认值：SEQUENCE, 取值范围：

SET

SEQUENCE

CONFED_SEQUENCE

CONFED_SET

NextHop (str): 下一跳, 类型为：有效的ipv4地址, 默认值：10.0.0.1

IPv6NextHop (str): IPv6下一跳, 类型为：有效的ipv6地址, 默认值：2001::1

EnableLinkLocalNextHop (bool): 使能下一跳本地链路地址, 类型为：bool, 取值范围：True或False, 默认值：True

LinkLocalNextHop (str): 下一跳本地链路地址, 类型为：有效的ipv6地址, 默认值：fe80::1

LocalPreference (int): 本地优先级, 类型为：number, 默认值：10

Community (str): 团体, 当Type为NO_EXPORT时，团体值为0xffffff01；当Type为NO_ADVERTISE时，团体值为0xffffff02；当Type为LOCAL_AS时，团体值为0xffffff03, 类型为：string, 默认值：""

ExtendedCommunity (str): 扩展团体, 类型为：string, 默认值：""

ProtocolID (str): 协议ID, 类型为：string, 默认值：DIRECT, 取值范围：

ISIS_LEVEL_1

ISIS_LEVEL_2

OSPFV2

DIRECT

STATIC

OSPFV3

BGP

IdentifierType (str): 标识符类型, 类型为：string, 默认值：CUSTOMIZED, 取值范围：

DEFAULT_LAYER3

CUSTOMIZED

Identifier (int): 标识符, 类型为：number, 取值范围：1-1048575, 默认值：0

EnableNodeNLRI (bool): 使能节点NLRI, 类型为：bool, 取值范围：True或False, 默认值：True

LocalNodeDescriptorFlag (list): 本地节点描述符标志, 类型为：list, 默认值：IGP_ROUTER_ID, 取值范围：

AS_NUMBER

BGPLS_IDENTIFIER

OSPF_AREA_ID

IGP_ROUTER_ID

BGP_ROUTER_ID

MEMBER_ASN

AsNumber (int): 自治域, 类型为：number, 取值范围：1-4294967295, 默认值：1

BgpLsIdentifier (str): BGP-LS标识符, 类型为：有效的ipv4地址, 默认值：1.0.0.1

OspfAreaId (str): OSPF区域ID, 类型为：有效的ipv4地址, 默认值：0.0.0.0

IGPRouterIdType (str): IGP路由ID类型, 类型为：string, 默认值：OSPF_NONPSEUDONODE, 取值范围：

ISIS_NONPSEUDONODE

ISIS_PSEUDONODE

OSPF_NONPSEUDONODE

OSPF_PSEUDONODE

IsisNonPseud (str): ISIS非伪节点路由ID, 类型为：string, 默认值："00:10:12:00:00:01"

IsisPseud (str): ISIS伪节点路由ID, 类型为：string, 默认值："00:10:12:00:00:01.02"

OspfNonPseud (str): OSPF非伪节点路由ID, 类型为：有效的ipv4地址, 默认值：192.0.0.1

OspfPseud (str): OSPF伪节点路由ID, 类型为：string, 默认值："192.0.0.1:192.0.0.1"

BgpRouterId: BGP路由ID, 类型为：有效的ipv4地址, 默认值：0.0.0.0

MemberAsn (int): 自治域成员, 类型为：number, 取值范围：1-4294967295, 默认值：0

LocalNodeAttributeFlag (str): 本地节点描述符标志 类型为：string, 默认值：NODE_FLAG_BITS, 取值范围：

MULTI_TOPO_ID

NODE_FLAG_BITS

NODE_NAME

ISIS_AREA_ID

IPV4_LOCAL_NODE_ROUTERID

IPV6_LOCAL_NODE_ROUTERID

SR_CAPABILITIES

SR_ALGORITHM

SR_LOCAL_BLOCK

SR_SRMA_PREF

SRV6_CAPABILITIES

SRV6_NODE_MSD

MultiTopoId (str): 多拓扑ID, 类型为：string, 取值范围：1-4095, 默认值：""

NodeFlagBitIsis (str): 节点标志（ISIS）, 类型为：string, 默认值：ATTACHED, 取值范围：

OVERLOAD

ATTACHED

NodeFlagBitOspfv2 (list): 节点标志（OSPFv2）, 类型为：list, 默认值：ABR, 取值范围：

EXTERNAL

ABR

NodeFlagBitOspfv3 (list): 节点标志（OSPFv3）, 类型为：list, 默认值：ABR, 取值范围：

EXTERNAL ABR ROUTER V6

NodeName (str): 节点名称, 类型为：string, 默认值：""

IsisAreaId (int): IS-IS区域ID, 类型为：number, 取值范围：1-4294967295, 默认值：0

LocalIpv4RouterIds (str): 本端IPv4路由IDs, 类型为：有效的ipv4地址, 默认值：""

LocalIpv6RouterIds (str): 本端IPv6路由IDs, 类型为：有效的ipv6地址, 默认值：""

SidLabelType (str): SID/Label类型, 类型为：string, 默认值：BIT20_LABEL, 取值范围：

BIT20_LABEL

BIT32_SID

SrCapabilitiesFlags (list): SR能力标志, 类型为：list, 默认值：MPLS_IPv4, 取值范围：

MPLS_IPv4

MPLS_IPv6

SrCapabilities (str): SR能力, 类型为：string, 默认值："16:100"

SrAlgorithm (int): SR算法, 类型为：number, 取值范围：1-255, 默认值：0

SrLocalBlock (str): SRLB范围, 类型为：string, 默认值："16:100"

SrmsPref (int): SRMS优先级, 类型为：number, 取值范围：1-255, 默认值：0

Srv6CapabilitiesFlags (list): SRv6能力标志, 类型为：list, 默认值：O_FLAG, 取值范围：

UNUSED0

O_FLAG

UNUSED2

UNUSED3

UNUSED4

UNUSED5

UNUSED6

UNUSED7

UNUSED8

UNUSED9

UNUSED10

UNUSED11

UNUSED12

UNUSED13

UNUSED14

UNUSED15

Srv6MsdFlags (list): SRv6节点MSD类型, 类型为：list, 默认值：NONE, 取值范围：

NONE

MAX_SEGMENTS_LELT

MAX_END_POP

MAX_T_INSERT_SRH

MAX_T_ENCAPS_SRH

MAX_END_D_SRH

Srv6MsdMaxSegmentLeft (int): 最大Segments Left, 类型为：number, 取值范围：1-255, 默认值：8

Srv6MsdMaxEndPop (int): 最大End Pop, 类型为：number, 取值范围：1-255, 默认值：8

Srv6MsdMaxInsert (int): 最大T.Insert SRH, 类型为：number, 取值范围：1-255, 默认值：8

Srv6MsdMaxEncap (int): 最大T.Encaps SRH, 类型为：number, 取值范围：1-255, 默认值：8

Srv6MsdMaxEndD (int): 最大End D SRH, 类型为：number, 取值范围：1-255, 默认值：8

Returns:

(:obj:BgpLsNodeConfig): Bgp Link States对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Link States	Session=${Session}	
Create Bgp Link States Link
Arguments
Session
LinkState
** kwargs
Documentation
创建Bgp Link States Link对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

LinkState(:obj:BgpLsNodeConfig): Bgp Link States对象列表, 类型为：object / list

Keyword Args:

LinkLocalRemoteIdFlag (str): 链路本端/远端ID位置, 类型为：string, 默认值：NONE, 取值范围：

NONE

LINK_DESCRIPTOR

LINK_ATTRIBUTE

LinkLocalId (int): 链路本端ID, 类型为：number, 取值范围：1-4294967295, 默认值：0

LinkRemoteId (int): 链路远端ID, 类型为：number, 取值范围：1-4294967295, 默认值：0

RemoteNodeDescriptorFlag (str): 远端节点描述符标志, 类型为：string, 默认值：IGP_ROUTER_ID, 取值范围：

AS_NUMBER

BGPLS_IDENTIFIER

OSPF_AREA_ID

IGP_ROUTER_ID

BGP_ROUTER_ID

MEMBER_ASN

AsNumber (int): 自治域, 类型为：number, 取值范围：1-4294967295, 默认值：1

BgpLsIdentifier (str): BGP-LS标识符, 类型为：有效的ipv4地址, 默认值：1.0.0.1

OspfAreaId (str): OSPF区域ID, 类型为：有效的ipv4地址, 默认值：0.0.0.0

IGPRouterIdType (str): IGP路由ID类型, 类型为：string, 默认值：OSPF_NONPSEUDONODE, 取值范围：

ISIS_NONPSEUDONODE

ISIS_PSEUDONODE

OSPF_NONPSEUDONODE

OSPF_PSEUDONODE

IsisNonPseud (str): ISIS非伪节点路由ID, 类型为：string, 默认值："00:10:12:00:00:01"

IsisPseud (str): OSPF伪节点路由ID, 类型为：string, 默认值："00:10:12:00:00:01.02"

OspfNonPseud (str): OSPF非伪节点路由ID, 类型为：有效的ipv4地址, 默认值：192.0.0.1

OspfPseud (str): OSPF伪节点路由ID, 类型为：string, 默认值："192.0.0.1:192.0.0.1"

BgpRouterId (str): BGP路由ID, 类型为：有效的ipv4地址, 默认值：0.0.0.0

MemberAsn (int): 自治域成员, 类型为：number, 取值范围：1-1048575, 默认值：0

LinkDescriptorFlag (list): 链路描述符标志, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

LINK_IDENTIFIES

IPV4_INTERFACE

IPV4_NEIGHBOR

IPV6_INTERFACE

IPV6_NEIGHBOR

MULTI_TOPOLOGY

Ipv4InterfaceAddr (str): IPv4接口地址, 类型为：有效的ipv4地址, 默认值：192.168.0.1

Ipv4NeighborAddr (str): IPv4邻接地址, 类型为：有效的ipv4地址, 默认值：192.168.0.2

Ipv6InterfaceAddr (str): IPv6接口地址, 类型为：有效的ipv6地址, 默认值：2001::1

Ipv6NeighborAddr (str): IPv6邻接地址, 类型为：有效的ipv6地址, 默认值：2001::2

MultiTopologyId (int): 多拓扑ID, 类型为：number, 取值范围：1-4095, 默认值：“”

LinkAttributeFlag (list): 链路属性标志, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

IPV4_LOCAL_NODE

IPV4_REMOTE_NODE

IPV6_LOCAL_NODE

IPV6_REMOTE_NODE

LINK_IDENTIFIES

LINK_PROTECTION_TYPE

IGP_METRIC

SHARED_RISE

ADI_SID

LAN_ADJ_SID

PEERNODE_SID

PEERADJ_SID

PEERSET_SID

SRV6_LINK_MSD

SRV6_END_X_SID

SRV6_LAN_END_X_SID

LocalIpv4RouterIds (str): 本端IPv4路由IDs, 类型为：有效的ipv4地址, 默认值：""

RemoteIpv4RouterIds (str): 远端IPv4路由IDs, 类型为：有效的ipv4地址, 默认值：""

LocalIpv6RouterIds (str): 本端IPv6路由IDs, 类型为：有效的ipv6地址, 默认值：""

RemoteIpv6RouterIds (str): 远端IPv6路由IDs, 类型为：有效的ipv6地址, 默认值：""

IgpMetricType (str): IGP度量类型, 类型为：string, 默认值：UNKNOWN, 取值范围：

ISIS_NARROW

OSPFv2_LINK

ISIS_WIDE

IgpMetricValue (int): IGP度量值, 类型为：number, 取值范围：IS-IS Narrow Metrics：0-255, OSPFv2 Link Metrics：0-65535, IS-IS Wide Metrics：0-16777215, 默认值：0

LinkProteType (list): 链路保护类型, 类型为：list, 默认值：UNKNOWN, 取值范围：

EXTRA_TRAFFIC

UNPROTECTED

SHARED

DEDICATED1

DEDICATED2

ENHANCED

RESERVED4

RESERVED8

ShareRiskGroup (int): SRLG信息, 类型为：number, 取值范围：1-4294967295, 默认值：""

OspfAdjSidFlag (list): OSPF SR邻接SID标志, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

BACKUP

VALUE

LOCAL

GROUP

PERSISTENT

IsisAdjSidFlag (list): ISIS SR邻接SID标志, 类型为：list, 默认值：NOSHOW, 取值范围：

NOSHOW

ADDRESS

BACKUP

VALUE

LOCAL

SET

PERSISTENT

AdjSidWeight (int): 权重, 类型为：number, 取值范围：1-255, 默认值：1

AdjSidLabel (int): SID/Label, 类型为：number, 取值范围：1-255, 默认值：16

OspfNeighborId (str): OSPF邻居ID, 类型为：有效的ipv4地址, 默认值：192.0.1.0

IsisSystemId (str): ISIS系统ID, 类型为：有效的mac地址, 默认值：00:00:00:00:00:00

PeerNodeFlag (list): Peer Node标志, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

VALUE

LOCAL

BACKUP

PERSISTENT

PeerNodeWeight (int): Peer Node权重, 类型为：number, 取值范围：1-255, 默认值：1

PeerNodeSidLabel (int): Peer Node SID/Index/Label, 类型为：number, 取值范围：1-255, 默认值：16

PeerAdjFlag (list): Peer Adj标志, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

VALUE

LOCAL

BACKUP

PERSISTENT

PeerAdjWeight (int): Peer Adj权重, 类型为：number, 取值范围：1-255, 默认值：1

PeerAdjSidLabel (int): Peer Adj权重, 类型为：number, 取值范围：1-255, 默认值：16

PeerSetFlag (list): Peer Set标志, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

VALUE

LOCAL

BACKUP

PERSISTENT

PeerSetWeight (int): Peer Set权重, 类型为：number, 取值范围：1-255, 默认值：1

PeerSetSidLabel (int): Peer Set SID/Index/Label, 类型为：number, 取值范围：1-255, 默认值：16

Srv6MsdFlags (list): SRv6链路MSD类型, 类型为：list, 默认值：NONE, 取值范围：

NONE

MAX_SEGMENTS_LELT

MAX_END_POP

MAX_T_INSERT_SRH

MAX_T_ENCAPS_SRH

MAX_END_D_SRH

Srv6MsdMaxSegmentLeft (int): 最大Segments Left, 类型为：number, 取值范围：1-255, 默认值：8

Srv6MsdMaxEndPop (int): 最大End Pop, 类型为：number, 取值范围：1-255, 默认值：8

Srv6MsdMaxInsert (int): 最大T.Insert SRH, 类型为：number, 取值范围：1-255, 默认值：8

Srv6MsdMaxEncap (int): 最大T.Encaps SRH, 类型为：number, 取值范围：1-255, 默认值：8

Srv6MsdMaxEndD (int): 最大End D SRH, 类型为：number, 取值范围：1-255, 默认值：8

Srv6EndXSidEndpointBehavior (str): SRv6 Endpoint功能指令类型, 类型为：string, 默认值：CUSTOM, 取值范围：

END

END_WITH_PSP

END_WITH_USP

END_WITH_PSP_USP

END_X

END_X_WITH_PSP

END_X_WITH_USP

END_X_WITH_PSP_USP

END_T

END_T_WITH_PSP

END_T_WITH_USP

END_T_WITH_PSP_USP

END_B6_ENCAPS

END_BM

END_DX6

END_DX4

END_DT6

END_DT4

END_DT46

END_DX2

END_DX2V

END_DT2U

END_DT2M

END_B6_ENCAPS_RED

END_WITH_USD

END_WITH_PSP_USD

END_WITH_USP_USD

END_WITH_PSP_USP_USD

END_X_WITH_USD

END_X_WITH_PSP_USD

END_X_WITH_USP_USD

END_X_WITH_PSP_USP_USD

END_T_WITH_USD

END_T_WITH_PSP_USD

END_T_WITH_USP_USD

END_T_WITH_PSP_USP_USD

CUSTOM

Srv6EndXSidFlag (list): SRv6 End.X SID标志, 类型为：list, 默认值：NONE, 取值范围：

NONE

BACKUP_FLAG

SET_FLAG

PERSISTENT_FLAG

Srv6EndXSidAlgorithm (int): SRv6 End.X SID算法, 类型为：number, 取值范围：1-255, 默认值：8

Srv6EndXSidWeight (int): SRv6 End.X SID权重, 类型为：number, 取值范围：1-255, 默认值：1

Srv6EndXSidSid (str): SRv6 End.X SID, 类型为：有效的ipv6地址, 默认值：::1

Srv6LanEndXSidSystemId (str): ISIS邻居ID, 类型为：有效的mac地址, 默认值：00:00:00:00:00:00

Srv6LanEndXSidRouterId (str): OSPFv3邻居ID, 类型为：有效的ipv4地址, 默认值：192.0.0.1

EnableInterfaceIp (bool): 启用本端IPv4地址, 类型为：bool, 取值范围：True或False, 默认值：False

InterfaceIp (str): 本端IPv4地址, 类型为：有效的ipv4地址, 默认值：0.0.0.0

EnableNeighborIp (bool): 启用远端IPv4地址, 类型为：bool, 取值范围：True或False, 默认值：False

NeighborIp (str): 远端IPv4地址, 类型为：有效的ipv4地址, 默认值：0.0.0.0

EnableInterfaceIpv6 (bool): 启用本端IPv6地址, 类型为：bool, 取值范围：True或False, 默认值：False

InterfaceIpv6 (str): 本端IPv6地址, 类型为：有效的ipv4地址, 默认值：2000::1

EnableNeighborIpv6 (bool): 启用远端IPv6地址, 类型为：bool, 取值范围：True或False, 默认值：False

NeighborIpv6 (str): 启用远端IPv6地址, 类型为：有效的ipv6地址, 默认值：2000::1

EnableGroup (bool): 启用组, 类型为：bool, 取值范围：True或False, 默认值：False

Group (int): 组, 类型为：number, 取值范围：1-4294967295, 默认值：1

EnableUniLinkLoss (bool): 启用单向链路损耗, 类型为：bool, 取值范围：True或False, 默认值：False

LinkLoss (int): 链路损耗, 类型为：number, 取值范围：1-100, 默认值：3

LinkLossAflag (bool): 链路损耗的A-flag, 类型为：bool, 取值范围：True或False, 默认值：False

EnableUniDelay (bool): 启用单向延迟, 类型为：bool, 取值范围：True或False, 默认值：False

UniDelay (int): 单向延迟, 类型为：number, 取值范围：1-4294967295, 默认值：100000

UniAflag (bool): 单向延迟的A-flag, 类型为：bool, 取值范围：True或False, 默认值：False

EnableUniMinMaxDelay (bool): 启用单向延迟最小/最大值, 类型为：bool, 取值范围：True或False, 默认值：False

UniMinMaxAflag (bool): 启用单向延迟最小/最大值的A-flag类型为：bool, 取值范围：True或False, 默认值：False

UniMinDelay (int): 单向最小延迟, 类型为：number, 取值范围：1-4294967295, 默认值：100000

UniMaxDelay (int): 单向最大延迟, 类型为：number, 取值范围：1-4294967295, 默认值：100000

EnableUniDelayVariation (bool): 启用单向延迟变化, 类型为：bool, 取值范围：True或False, 默认值：False

UniVarDelay (int): 单向延迟变化, 类型为：number, 取值范围：1-4294967295, 默认值：100000

EnableUniResidual (bool): 启用单向剩余带宽, 类型为：bool, 取值范围：True或False, 默认值：False

UniResBandwidth (int): 单向剩余带宽, 类型为：number, 取值范围：1-4294967295, 默认值：100000

EnableUniAva (bool): 启用单向可用带宽, 类型为：bool, 取值范围：True或False, 默认值：False

UniAvaBandwidth (int): 单向可用带宽, 类型为：number, 取值范围：1-4294967295, 默认值：100000

EnableUniUtilized (bool): 启用单向已用带宽, 类型为：bool, 取值范围：True或False, 默认值：False

UniUtilized (int): 单向已用带宽, 类型为：number, 取值范围：1-4294967295, 默认值：100000

EnableMaximum (bool): 启用最大带宽(字节/秒), 类型为：bool, 取值范围：True或False, 默认值：False

Maximum (int): 最大带宽(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

EnableReservable (bool): 启用预留带宽(字节/秒), 类型为：bool, 取值范围：True或False, 默认值：False

Reservable (int): 预留带宽(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

EnableUnreserved (bool): 启用未预留带宽优先级(字节/秒), 类型为：bool, 取值范围：True或False, 默认值：False

UnreservedBandwidth0 (int): 未预留带宽优先级(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

UnreservedBandwidth1 (int): 未预留带宽优先级(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

UnreservedBandwidth2 (int): 未预留带宽优先级(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

UnreservedBandwidth3 (int): 未预留带宽优先级(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

UnreservedBandwidth4 (int): 未预留带宽优先级(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

UnreservedBandwidth5 (int): 未预留带宽优先级(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

UnreservedBandwidth6 (int): 未预留带宽优先级(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

UnreservedBandwidth7 (int): 未预留带宽优先级(字节/秒), 类型为：number, 取值范围：1-4294967295, 默认值：100000

EnableTeDefaultMetric (bool): 启用TE默认度量, 类型为：bool, 取值范围：True或False, 默认值：False

TeDefaultValue (int): TE默认度量, 类型为：number, 取值范围：1-4294967295, 默认值：0

Returns:

(:obj:BgpLsLinkConfig): Bgp Link States Link对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${LinkState}	Create Bgp Link States	Sessions=${Session}
Create Bgp Link States Link	Sessions=${Session}	LinkState=${LinkState}
Create Bgp Link States Prefix
Arguments
Session
LinkState
** kwargs
Documentation
创建Bgp Link States Prefix对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

LinkState(:obj:BgpLsNodeConfig): Bgp Link States对象列表, 类型为：object / list

Keyword Args:

PrefixDescriptorFlag (list): LS前缀描述符标志, 类型为：list, 默认值：IP_REACH_INFO, 取值范围：

MULTI_TOPOLOGY

OSPF_ROUTE_TYPE

IP_REACH_INFO

OspfRouteType (str): OSPF路由类型, 类型为：string, 默认值：INTRA_AREA, 取值范围：

INTRA_AREA

INTER_AREA

EXTERNAL1

EXTERNAL2

NSSA1

NSSA2

PrefixCount (int): 地址前缀个数, 类型为：number, 取值范围：1-65535, 默认值：1

PrefixType (str): 地址前缀类型, 类型为：string, 默认值：IPV4, 取值范围：

IPV4

IPV6

Ipv4Prefix (str): IPv4地址前缀, 类型为：有效的ipv4地址, 默认值：1.0.0.0

Ipv4PrefixLength (int): IPv4地址前缀步长, 类型为：number, 取值范围：1-32, 默认值：24

Ipv4PrefixStep (int): IPv4地址前缀步长, 类型为：number, 取值范围：1-65535, 默认值：1

Ipv6Prefix (str): IPv6地址前缀, 类型为：有效的ipv6地址, 默认值：2000::1

Ipv6PrefixLength (int): IPv6地址前缀步长, 类型为：number, 取值范围：1-128, 默认值：64

Ipv6PrefixStep (int): IPv6地址前缀长度, 类型为：number, 取值范围：1-65535, 默认值：1

MultiTopologyId (int): 多拓扑ID, 类型为：number, 取值范围：1-4095, 默认值：“”

OspfSrPrefixSidFlag (list): OSPF SR前缀SID标志, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

NO_PHP

MAPPING_SERVER

EXPLICIT_NULL

VALUE

LOCAL

IsisSrPrefixSidFlag (list): ISIS SR前缀SID标志, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

RE_ADVER

NODESID

NO_PHP

EXPLICIT_NULL

VALUE

LOCAL

PrefixAttributeFlag (str): LS前缀描述符标志, 类型为：string, 默认值：UNKNOWN|IGP_FLAGS, 取值范围：

UNKNOWN

IGP_FLAGS

PREFIX_METRIC

OSPF_FORWARDING

SR_PREFIX_SID

SR_RANGE

SR_ATTRIBUTE_FLAG

SR_SOURCE

SRV6_LOCATOR_TLV

IgpFlag (str): IGP标志, 类型为：string, 默认值：UNKNOWN, 取值范围：

UNKNOWN

ISIS_UP_DOWN

OSPF_NO_UNICAST

OSPF_LOCAL_ADDRESS

OSPF_PROPAGATE_NSSA

PrefixMetric (int): 前缀度量, 类型为：number, 取值范围：1-4294967295, 默认值：0

OspfForwardtype (str): OSPF转发地址类型, 类型为：string, 默认值：OSPFV2, 取值范围：

OSPFV2

OSPFV3

Ospfv2ForwardAddr (str): OSPFv2转发地址, 类型为：有效的ipv4地址, 默认值：192.168.1.1

Ospfv3ForwardAddr (str): OSPFv3转发地址, 类型为：有效的ipv6地址, 默认值：2000::1

OspfSrPrefixFlag (str): OSPF SR前缀SID标志, 类型为：string, 默认值：UNKNOWN, 取值范围：

UNKNOWN

NO_PHP

MAPPING_SERVER

EXPLICIT_NULL

VALUE

LOCAL

IsisSrPrefixFlag (str): ISIS SR前缀SID标志, 类型为：string, 默认值：UNKNOWN, 取值范围：

UNKNOWN

RE_ADVER

NODESID

NO_PHP

EXPLICIT_NULL

VALUE

LOCAL

Algorithm (int): 算法, 类型为：number, 取值范围：1-255, 默认值：0

SidLabelIndex (int): SID/Label/Index, 类型为：number, 取值范围：0-1048575 (20比特值), 0-4294967295 (32比特值), 默认值：0

Ospfv2SrPrefixAttributeFlag (list): OSPFv2 SR前缀属性标志, 类型为：list, 默认值：NODE, 取值范围：

ATTACH

NODE

Ospfv3SrPrefixAttributeFlag (list): OSPFv3 SR前缀属性标志, 类型为：list, 默认值：NO_UNICAST, 取值范围：

NO_UNICAST

LOCAL_ADDRESS

MULTICAST

PROPAGATE

RE_ADVER

HOST

IsisSrPrefixAttributeFlag (list): ISIS SR前缀属性标志, 类型为：list, 默认值：NODE, 取值范围：

EXTERNAL_PREFIX

RE_ADVER

NODE

SrSourceIpv4Id (str): SR IPv4源路由ID, 类型为：有效的ipv4地址, 默认值：192.168.1.0

SrSourceIpv6Id (str): SR IPv6源路由ID, 类型为：有效的ipv6地址, 默认值：2000::1

Ospfv2SrRangeFlag (list): OSPFv2 SR范围标志, 类型为：list, 默认值：INTER_AREA, 取值范围：

INTER_AREA

IsisSrRangeFlag (list): ISIS SR范围标志, ISIS SR前缀SID标志, 类型为：list, 默认值：ATTACHED, 取值范围：

ADDRESS_FAMILY

MIRROR_CONTEXT

S_FLAG

D_FLAG

ATTACHED

SrRangeSubTlv (str): SR范围Sub-TLVs, 类型为：string, 默认值："0 Range Sub-TLV"

Srv6LocatorFlag (str): SRv6 Locator标志, 类型为：string, 默认值：NONE, 取值范围：

NONE

D_FLAG

Srv6LocatorAlgorithm (int): SRv6 Locator算法, 类型为：number, 取值范围：1-255, 默认值：0

Srv6LocatorMetric (int): SRv6 Locator度量值, 类型为：number, 取值范围：1-4294967295, 默认值：0

Returns:

(:obj:BgpLsPrefixConfig): Bgp Link States Prefix对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${LinkState}	Create Bgp Link States	Sessions=${Session}
Create Bgp Link States Prefix	Sessions=${Session}	LinkState=${LinkState}
Create Bgp Link States Prefix Sr Range Sub Tlv
Arguments
Session
LinkStatePrefix
** kwargs
Documentation
创建Bgp Link States Prefix Sr Range Sub Tlv对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

LinkStatePrefix(:obj:BgpLsPrefixConfig): Bgp Link States prefix对象列表, 类型为：object / list

Keyword Args:

Algorithm (int): 算法, 类型为：number, 取值范围：1-255, 默认值：0

OspfSrPrefixSidFlag (list): OSPF SR Prefix SID Flags, 类型为：list, 默认值：UNKNOWN, 取值范围:

UNKNOWN

NO_PHP

MAPPING_SERVER

EXPLICIT_NULL

VALUE

LOCAL

IsisSrPrefixSidFlag (list): ISIS SR Prefix SID Flags, 类型为：list, 默认值：UNKNOWN, 取值范围:

UNKNOWN

RE_ADVER

NODESID

NO_PHP

EXPLICIT_NULL

VALUE

LOCAL

SidLabelIndex (int): SID/Label/Index, 类型为：number, 取值范围：1-255, 默认值：0

Returns:

(:obj:BgpLsSrRangeSubTlvConfig): Bgp Link States Prefix Sr Range Sub Tlv对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${LinkState}	Create Bgp Link States	Sessions=${Session}
${prefix}	Create Bgp Link States Prefix	LinkState=${LinkState}
Create Bgp Link States Prefix Sr Range Sub Tlv	Sessions=${Session}	LinkStatePrefix=${prefix}
Create Bgp Link States Srv6 Sid
Arguments
Session
LinkState
** kwargs
Documentation
创建Bgp Link States Srv6 Sid对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

LinkState(:obj:BgpLsNodeConfig): Bgp Link States对象列表, 类型为：object / list

Keyword Args:

Srv6AttributeFlag (list): SRv6 SID属性标志, 类型为：list, 默认值：SRV6_ENDPOINT_BEHAVIOR, 取值范围：

SRV6_ENDPOINT_BEHAVIOR

SRV6_BGP_PEER_NODE_SID

SRV6_SID_STRUCTURE

Srv6EndpointBehavior (str): SRv6 Endpoint功能指令类型, 类型为：string, 默认值：CUSTOM, 取值范围：

END

END_WITH_PSP

END_WITH_USP

END_WITH_PSP_USP

END_X

END_X_WITH_PSP

END_X_WITH_USP

END_X_WITH_PSP_USP

END_T

END_T_WITH_PSP

END_T_WITH_USP

END_T_WITH_PSP_USP

END_B6_ENCAPS

END_BM

END_DX6

END_DX4

END_DT6

END_DT4

END_DT46

END_DX2

END_DX2V

END_DT2U

END_DT2M

END_B6_ENCAPS_RED

END_WITH_USD

END_WITH_PSP_USD

END_WITH_USP_USD

END_WITH_PSP_USP_USD

END_X_WITH_USD

END_X_WITH_PSP_USD

END_X_WITH_USP_USD

END_X_WITH_PSP_USP_USD

END_T_WITH_USD

END_T_WITH_PSP_USD

END_T_WITH_USP_USD

END_T_WITH_PSP_USP_USD

CUSTOM

Srv6EndpointBehaviorFlag (list): SRv6 Endpoint功能指令标志, 类型为：list, 默认值：NONE, 取值范围：

NONE

UNUSED0

UNUSED1

UNUSED2

UNUSED3

UNUSED4

UNUSED5

UNUSED6

UNUSED7

Srv6EndpointBehaviorAlgorithm (int): SRv6 Endpoint功能指令算法, 类型为：number, 取值范围：1-255, 默认值：0

Srv6BgpPeerNodeSidFlag (list): EPE Peer Node SID标志, 类型为：list, 默认值：0, 取值范围：

NONE

BACKUP_FLAG

SET_FLAG

PERSISTENT_FLAG

Srv6BgpPeerNodeSidWeight (int): EPE Peer Node SID权重, 类型为：number, 取值范围：1-255, 默认值：0

Srv6BgpPeerNodeSidPeerAsNumber (int): Peer自治域, 类型为：number, 取值范围：1-4294967295, 默认值：1001

Srv6BgpPeerNodeSidPeerBgpId (int): Peer BGP标识符, 类型为：number, 取值范围：1-4294967295, 默认值：0

Srv6SidStructureLbLength (int): SRv6 Locator Block长度, 类型为：number, 取值范围：1-255, 默认值：32

Srv6SidStructureLnLength (int): SRv6 Locator Node长度, 类型为：number, 取值范围：1-255, 默认值：32

Srv6SidStructureFunLength (int): SRv6 Function长度, 类型为：number, 取值范围：1-255, 默认值：32

Srv6SidStructureArgLength (int): SRv6 Argument长度, 类型为：number, 取值范围：1-255, 默认值：32

Srv6Sid (str): 类型为：有效的ipv6地址, 默认值：::1

MultiTopologyId (int): 多拓扑ID, 类型为：number, 取值范围：1-4095, 默认值：“”

Returns:

(:obj:BgpLsSrv6SidConfig): Bgp Link States Srv6 Sid对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${LinkState}	Create Bgp Link States	Sessions=${Session}
Create Bgp Link States Srv6 Sid	Sessions=${Session}	LinkState=${LinkState}
Create Bgp Random Route
Arguments
PortNumber
Type
=
None
Ipv4RouteNumber
=
300000
Ipv6RouteNumber
=
100000
Ipv4StartMask
=
23
Ipv6StartMask
=
32
Ipv4StartRoute
=
60.0.0.0
Ipv6StartRoute
=
60::
** kwargs
Create Bgp Route Pool Custom Path Attribute
Arguments
RoutePool
** kwargs
Documentation
创建BGP Route Pool Custom Path Attribute对象, 类型为：object / list

Args:

RoutePool(:obj:BgpIpv4RoutepoolConfig): 所属的Bgp Route Pool对象, 类型为：object / list

Keyword Args:

PathAttributeType (int): 路径属性的类型, 类型为：number, 取值范围：1-255, 默认值：1

OptionalFlag (str): 指定Optional Flag的值, 类型为：string, 默认值：OPTION, 取值范围：

WELL_KNOWN

OPTION

TransitiveFlag (str): 指定Transitive Flag的值, 类型为：string, 默认值：NONTRANSITIVE, 取值范围：

NONTRANSITIVE

TRANSITIVE

PartialFlag (str): 指定Partial Flag的值, 类型为：string, 默认值：PARTIAL, 取值范围：

COMPLETE

PARTIAL

ExtendedLengthFlag (bool): 是否启用Extended Length Flag, 类型为：bool, 默认值：False

AttributeExtendedLength (int): 指定路径属性的长度, 类型为：number, 默认值：0

AttributeValue (str): 指定路径属性的值, 类型为：string, 默认值：""

Returns:

(:obj:BgpPathAttributeConfig): Bgp Route Pool Custom Path Attribute对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${RoutePool}	Create Bgp Ipv4 Route Pool	Session=${Session}
${AttributeValue}	Set Variable	0500220001001E00AAAA000100010001000000000000000100001300010006301014000000
Create Bgp Route Pool Custom Path Attribute	RoutePool=${RoutePool}	AttributeValue=${AttributeValue}
Create Bgp Segement Sub Tlv
Arguments
Session
SegementList
Types
** kwargs
Documentation
创建Bgp Segement Sub Tlv对象, 类型为：object

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

SegementList(:obj:BgpSrTePolicySegmentList): BGP Sr Te Policy Segement List对象, 类型为：object

Types (str): BGP Sr Te Policy Segement Sub Tlv类型, 类型为string, 默认值: A, 取值范围：A-K

Keyword Args:

Flags (list): 选择一个或多个Flag, 类型为：list, 默认值：NO_SHOW, 取值范围：

NO_SHOW

V_FLAG

A_FLAG

S_FLAG

B_FLAG

Label (int): 指定标签, 类型为：number, 取值范围：1-1048575, 默认值：1600

LabelStep (int): 指定标签跳变, 类型为：number, 取值范围：1-1048575, 默认值：1

Tc (int): 指定TC（Traffic Class，通信量类）值, 类型为：number, 取值范围：0-7, 默认值：0

Sbit (int): 指定栈底标志（S）的值, 类型为：number, 取值范围：0-1, 默认值：1

Ttl (int): 指定TTL值, 类型为：number, 取值范围：1-1048575, 默认值：255

Srv6Sid (str): 指定SRv6 SID, 类型为：有效的ipv6地址, 默认值：2000::1

Srv6SidStep (str): 指定SRv6 SID的跳变步长, 类型为：有效的ipv6地址, 默认值：::1

EndpointBehavior (int): 指定SRv6 Endpoint Behavior, 类型为：number, 取值范围：1-1048575, 默认值：0

LbLength (int): SRv6 SID Locator Block长度, 类型为：number, 取值范围：1-1048575, 默认值：0

LnLength (int): SRv6 SID Locator Node长度, 类型为：number, 取值范围：1-1048575, 默认值：0

FunLength (int): SRv6 SID Function长度, 类型为：number, 取值范围：1-1048575, 默认值：0

ArgLength (int): SRv6 SID参数长度, 类型为：number, 取值范围：1-1048575, 默认值：0

SrAlgorithm (int): SR算法, 类型为：number, 取值范围：1-1048575, 默认值：0

Ipv4NodeAddress (str): IPv4节点地址, 类型为：有效的ipv4地址, 默认值：192.0.0.1

Ipv4NodeAddressStep (str): IPv4节点地址跳变, 类型为：有效的ipv4地址, 默认值：0.0.0.1

Ipv6NodeAddress (str): IPv6节点地址, 类型为：有效的ipv6地址, 默认值：2000::1

Ipv6NodeAddressStep (str): IPv6节点地址跳变, 类型为：有效的ipv6地址, 默认值：::1

LocalInterfaceId: 本地Interface ID, 类型为：number, 取值范围：1-1048575, 默认值：0

LocalIpv4Address (str): IPv4节点地址, 类型为：有效的ipv4地址, 默认值：192.0.0.1

LocalIpv4AddressStep (str): IPv4节点地址跳变, 类型为：有效的ipv4地址, 默认值：0.0.0.1

RemoteIpv4Address (str): 远端IPv4地址, 类型为：有效的ipv4地址, 默认值：192.0.0.1

RemoteIpv4AddressStep (str): 远端IPv4地址跳变, 类型为：有效的ipv4地址, 默认值：0.0.0.1

LocalIpv6NodeAddress (str): IPv6本地节点地址, 类型为：有效的ipv6地址, 默认值：2000::1

LocalIpv6NodeAddressStep (str): IPv6本地节点地址跳变, 类型为：有效的ipv6地址, 默认值：::1

RemoteInterfaceId (int): 远端Interface ID, 类型为：number, 取值范围：1-1048575, 默认值：0

RemoteIpv6NodeAddress (str): IPv6远端节点地址, 类型为：有效的ipv6地址, 默认值：2000::1

RemoteIpv6NodeAddressStep (str): IPv6远端节点地址跳变, 类型为：有效的ipv6地址, 默认值：::1

Returns:

(:obj:BgpSegmentSubTlvTypeA): Bgp Segement Sub Tlv对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}	
${SrTe}	Create Bgp Sr Te Policy	Session=${Session}	
${SrTeSegmentList}	Create Bgp Sr Te Policy Segement List	Session=${Session}	SrTePolicys=${SrTe}
Create Bgp Segement Sub Tlv	Session=${Session}	SrTePolicys=${SrTe}	Types=B
Create Bgp Sr Te Policy
Arguments
Session
** kwargs
Documentation
创建Bgp Sr Te Policy对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：list

Keyword Args:

BindingSidCount (int): Binding SID数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

PolicyColor (int): 指定SR Policy的起始Color值, 类型为：number, 默认值：0

PolicyColorStep (int): 指定Policy Color的跳变步长, 类型为：number, 默认值：1

IpVersion (str): 指定IP前缀类型, 类型为：string, 默认值：IPV4, 取值范围：

IPV4

IPV6

EndpointCount (int): 指定目的节点的数量。该参数值不能大于Binding SID数量。类型为：number, 取值范围：1-4294967295, 默认值：1

Ipv4Endpoint (str): 指定Policy块中目的节点的起始IP地址, 类型为：有效的ipv4地址, 默认值：192.0.0.1

Ipv4EndpointStep (str): 指定Policy块中目的节点的IP地址的跳变步长, 类型为：有效的ipv4地址, 默认值：0.0.0.1

Ipv6Endpoint (str): 指定Policy目的节点的IP地址, 类型为：有效的ipv6地址, 默认值：2000::1

Ipv6EndpointStep (str): 指定Policy目的节点的IP地址, 类型为：有效的ipv6地址, 默认值：2000::1

EndpointIncrementMode (str): 指定Policy块中目的节点IP地址的生成方式, 类型为：string, 默认值：RoundRobin, 取值范围：

RoundRobin

Sequential

Origin (str): 指定ORIGIN的值, 类型为：string, 默认值：IGP, 取值范围：

IGP

EGP

INCOMPLETE

AsPath (str): 指定AS路径的值, 类型为：string, 默认值：""

AsPathType (str): AS Path类型, 类型为：string, 默认值：SEQUENCE, 取值范围：

SET

SEQUENCE

CONFED_SEQUENCE

CONFED_SET

LocalPref (int): 指定Local_PREF的值, 类型为：number, 默认值：10

UseSessionAddressAsNextHop (bool): 使用会话地址作为下一跳地址, 类型为：bool, 默认值：True

Ipv4NextHop (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv4地址, 默认值：192.0.0.1

Ipv6NextHop (str): 下一跳地址，即UPDATE消息中NEXT_HOP的值, 类型为：有效的ipv6地址, 默认值：2001::1

Distinguisher (int): 输入SR Policy标识, 类型为：number, 取值范围：1-4294967295, 默认值：0

RouteTarget (str): 指定重定向的路由目标。类型为：string, 默认值：""

Community (str): 当Type为NO_EXPORT时，团体值为0xffffff01；当Type为NO_ADVERTISE时，团体值为0xffffff02；当Type为LOCAL_AS时，团体值为0xffffff03, 类型为：string, 默认值：""

ExtendedCommunity (str): 扩展团体, 类型为：string, 默认值："0x03:0x0b:0:0"

SrTePolicySubTlv (list): 选择一个或多个TLV, 类型为：list, 默认值：NO_SHOW, 取值范围：

NO_SHOW

REMOTE_ENDPOINT

COLOR

PREFERENCE

BINDING_SID

ENLP

PRIORITY

EGRESS_ENDPOINT

POLICY_CP_NAME

SRV6_BSID

POLICY_NAME

RemoteEndpointAsn (int): 远端Endpoint自治域号, 类型为：number, 取值范围：1-4294967295, 默认值：0

Ipv4RemoteEndpoint (str): IPv6远端Endpoint, 类型为：有效的ipv4地址, 默认值：192.0.0.1

Ipv6RemoteEndpoint (str): IPv6远端Endpoint, 类型为：有效的ipv6地址, 默认值：2000::1

Color (int): 指定Color扩展团体中Color Value字段的值, 类型为：number, 取值范围：1-4294967295, 默认值：0

ColorFlags (list): 指定Color扩展团体中Flags字段的值, 类型为：list, 默认值：NO_SHOW, 取值范围：

NO_SHOW

C_FLAG

O_FLAG

Preference (int): 指定SR Policy中候选路径的优先级, 类型为：number, 取值范围：1-4294967295, 默认值：0

BsidFlags (str): Binding SID Flags, 类型为：string, 默认值：NO_SHOW, 取值范围：

NO_SHOW

S_FLAG

I_FLAG

BsidLength (str): Binding SID长度, 类型为：string, 默认值：NO_SHOW, 取值范围：

OCTET_0

OCTET_4

OCTET_16

BsidLabel (int): Binding SID标签, 类型为：number, 取值范围：1-4294967295, 默认值：0

BsidLabelStep (int): Binding SID标签跳变, 类型为：number, 取值范围：1-4294967295, 默认值：1

BsidTc (int): 指定BSID中的S字段值, 类型为：number, 取值范围：0-7, 默认值：0

BsidS (int): 指定BSID中的S字段值, 类型为：number, 取值范围：0-1, 默认值：0

BsidTtl (int): 指定BSID中的TTL字段值, 类型为：number, 默认值：0

Ipv6Bsid (str): 指定IPv6 BSID, 类型为：有效的ipv6地址, 默认值：2000::1

Ipv6BsidStep (str): 指定IPv6 BSID的跳变步长, 类型为：有效的ipv6地址, 默认值：::1

Enlp (str): 指定显式空标签策略, 类型为：string, 默认值：IPV4, 取值范围：

RESERVED0

IPV4

IPV6

PolicyPriority (int): 指定拓扑改变后重新计算SR Policy时的Policy优先级, 类型为：number, 取值范围：1-255, 默认值：0

Srv6BsidFlags (list): 指定SRv6 Binding SID sub-TLV中包含的Flag, 类型为：list, 默认值：NO_SHOW(0x0), 取值范围：

NO_SHOW

S_FLAG

I_FLAG

B_FLAG

Srv6Bsid (str): 指定SRv6 BSID, 类型为：有效的ipv6地址, 默认值：2000::1

Srv6BsidStep (str): 指定SRv6 BSID的跳变步长, 类型为：有效的ipv6地址, 默认值：::1

Srv6BsidEndpointBehavior (int): 指定SRv6 SID Endpoint Behavior, 类型为：number, 取值范围：1-65535, 默认值：0

Srv6BsidLbLength (int): 指定SRv6 SID Function长度。类型为：number, 取值范围：1-255, 默认值：0

Srv6BsidLnLength (int): 指定SRv6 SID Locator Node长度。单位：比特, 类型为：number, 取值范围：1-255, 默认值：0

Srv6BsidFunLength (int): 指定SRv6 SID Function长度。单位：比特, 类型为：number, 取值范围：1-255, 默认值：0

Srv6BsidArgLength (int): 指定SRv6 SID参数长度。单位：比特, 类型为：number, 取值范围：1-255, 默认值：0

CandidatePathName (str): Policy候选路径名称, 类型为：string, 默认值：""

PolicyName (str): 指定Policy的名称, 类型为：string, 默认值：""

TunnelEgressEndpointAfi (str): 隧道出口端点AFI, 类型为：string, 默认值：IPV4, 取值范围：

RESERVED0

IPV4

IPV6

Ipv4TunnelEgressEndpoint (str): IPv4远端Endpoint, 类型为：有效的ipv4地址, 默认值：192.0.0.1

Ipv6TunnelEgressEndpoint (str): IPv6远端Endpoint, 类型为：有效的ipv6地址, 默认值：2000::1

Returns:

(:obj:BgpSrTePolicyConfig): Bgp Sr Te Policy对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
Create Bgp Sr Te Policy	Session=${Session}	
Create Bgp Sr Te Policy Segement List
Arguments
Session
SrTePolicy
** kwargs
Documentation
创建Bgp Sr Te Policy Segement List对象, 类型为：object / list

Args:

Session (:obj:BgpRouter): BGP协议会话对象列表, 类型为：object / list

SrTePolicy(:obj:BgpSrTePolicyConfig): BGP Sr Te Policy对象, 类型为：object / list

Keyword Args:

SubTlvs (list): 选择一个或多个子TLV, 类型为：list, 默认值：NO_SHOW, 取值范围：

NO_SHOW

WEIGHT

Weight (int): 指定Segment List（SID列表）对应的权重, 类型为：number, 取值范围：1-4294967295, 默认值：1

Returns:

(:obj:BgpSrTePolicySegmentList): Bgp Sr Te Policy Segement List对象, 类型：object / list

Examples: .. code:: RobotFramework

${Session}	Create Bgp	Port=${Port}
${SrTe}	Create Bgp Sr Te Policy	Session=${Session}
Create Bgp Sr Te Policy Segement List	Session=${Session}	SrTePolicy=${SrTe}
Create Capture Byte Pattern
Arguments
Port
** kwargs
Documentation
在指定端口上创建Byte Pattern

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

CustomCapturePatternOperator (str): 表达式位运算符：, 类型为：string, 默认值：AND, 支持参数

AND OR XOR

CustomCapturePatternNot (bool): 表达式取反：, 类型为：bool, 取值范围：True或False, 默认值：False

UseFrameLength (bool): 使用Frame长度：, 类型为：bool, 取值范围：True或False, 默认值：False

Data (str): 最小值：, 类型为：string, 取值范围：十六进制字符串, 默认值：0x0,

MaxData (str): 最大值：, 类型为：string, 取值范围：十六进制字符串, 默认值：0xff,

Mask (str): 掩码：, 类型为：string, 取值范围：十六进制字符串, 默认值：0xff,

Offset (int): 偏移位：, 类型为：number, 取值范围：0-16378, 默认值：0

MinFrameLength (int): 最小长度,当UseFrameLength为True有效：, 类型为：number, 取值范围：64-16383, 默认值：64

MaxFrameLength (int): 最大长度,当UseFrameLength为True有效：, 类型为：number, 取值范围：64-16383, 默认值：16383

Returns:

str: Byte Pattern唯一索引字符串string，例如：CaptureBytePattern_1

Examples: robotframework:

.. code:: robotframework

Create Capture Byte Pattern	Port=${Port}	Data=0x0 0x01	Mask=0xff 0xff	Offset=0	CustomCapturePatternOperator=OR	CustomCapturePatternNot=True
Create Capture Pdu Pattern
Arguments
Port
HeaderTypes
FieldName
** kwargs
Documentation
在指定端口上创建Pdu Pattern

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

HeaderTypes (list): 指定报文结构 EthernetII Vlan IPv4 IPv6 Igmpv1 Igmpv1Query Igmpv2 Igmpv2Query Igmpv3Report Igmpv3Query Icmpv4EchoRequest Icmpv4EchoReply

FieldName (str): 过滤字段名

CustomCapturePatternOperator (str): 表达式位运算符：, 类型为：string, 默认值：AND, 支持参数

AND OR XOR

CustomCapturePatternNot (bool): 表达式取反：, 类型为：bool, 取值范围：True或False, 默认值：False

Value (str): 最小值：, 类型为：string

MaxValue (str): 最大值：, 类型为：string

Mask (str): 掩码：, 类型为：string

Returns:

str: Pdu Pattern唯一索引字符串string，例如：CapturePduPattern_1

Examples: robotframework:

.. code:: robotframework

${HeaderTypes}	Create List	EthernetII	IPv4	Icmpv4EchoReply	
Create Capture Pdu Pattern	Port=${Port}	HeaderTypes=${HeaderTypes}	FieldName=Icmpv4EchoReply_1.code	Value=4	MaxValue=5
Create Dhcp Client
Arguments
Port
** kwargs
Documentation
创建DHCPv4客户端协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象

Keyword Args:

Name (str): DHCP协议会话名称

Mode (str): DHCPv4客户端模式，默认值：CLIENT, 支持的参数：

CLIENT

RELAY_AGENT

HostName (str): 主机名字，默认值：XINERTEL

ParameterRequests (list): 主机请求选项, 默认值：['NONEOPTION', 'SUBNET_MASK', 'DOMAIN_NAME_SERVERS', 'DOMAIN_NAME', 'STATIC_ROUTES'], 支持的参数:

SUBNET_MASK

ROUTERS

DOMAIN_NAME_SERVERS

DOMAIN_NAME

STATIC_ROUTES

IP_LEASE_TIME

SERVER_IDENTIFIER

T1

T2

EnableRouterOption (bool): 启用路由选项, 默认值：False

VendorClassIdentifier (str): 供应商识别, 默认值：XINERTEL

BroadcastFlag (str): 默认值：BROADCAST, 支持参数：

UNICAST

BROADCAST

RelayAgentIp (str): 代理端IP, 取值范围：IPv4地址, 默认值：1.1.1.1

ServerIp (str): DHCPv4服务端IP, 取值范围：IPv4地址, 默认值：2.1.1.3

EnableRelayAgentCircuitID (bool): 使能代理电路标识, 默认值：False

RelayAgentCircuitID (str): 代理电路标识, 默认值：""

EnableRelayAgentRemoteID (str): 使能代理远程标识, 默认值：False

RelayAgentRemoteID (str): 代理远程标识, 默认值：""

EnableSyncAddressToInterface (bool): 使能同步地址到接口, 默认值：True

HostInterface (:obj:Interface): 客户端接口对象, 类型：object

Returns:

(:obj:DhcpClient): DHCP协议会话对象Object

Examples: .. code:: RobotFramework

${Session}	Create Dhcp Client	Port=${Port}	Name=DHCP_Client_1
Create Dhcp Client Custom Option
Arguments
Session
** kwargs
Documentation
创建测试仪表DHCP协议会话option对象

Args:

Session (:obj:DhcpClient): DHCPv4 Client协议对象, 类型为：object / list

Keyword Args:

OptionTag (number): 可选项类型标识, 默认值：0, 取值范围：0-255

OptionType (str): 可选项数据类型, 默认值：HEX, 支持以下参数：

HEX

STRING

BOOLEAN

INT8

INT16

INT32

IP

EnableOptionValueList (bool): 可选项值列表, 默认值：False

OptionValue (str): 可选项值, 默认值：""

MessageType (str): 携带Option消息类型, 默认值：DISCOVER, 支持以下参数：

DISCOVER

REQUEST

Returns:

(:obj:Dhcpv4ClientOption): 测试仪表DHCP协议会话option对象Object

Examples: .. code:: RobotFramework

Create Dhcp Client Custom Option	Session=${Sessions}
Create Dhcp Server
Arguments
Port
** kwargs
Documentation
创建DHCP Server会话对象

Args:

Port (:obj:Port): 测试仪表端口对象

Keyword Args:

Name (str): DHCP Server协议会话名称

LeaseTime (number): 租约时间（秒）, 默认值：600, 范围：1-4294967295

RenewTime (number): T1租约更新时间(%), 默认值：50, 范围：0-200

RebindTime (number): T2租约更新时间(%), 默认值：87.5, 范围：0-200

MinLeaseTime (number): 最小允许租约时间(秒), 默认值：10, 范围：1-4294967295

DeclineReserveTime (number): 资源释放等待时间(秒), 默认值：10, 范围：1-600

OfferReserveTime (number): 租约申请超时(秒), 默认值：10, 范围：1-600

ServerHostName (str): 服务端名字

DuplicateAddressDetection (bool): 重复地址检测（DAD）, 默认值：False

DuplicateAddressDetectionTimeout (number): DAD超时时间, 默认值：0.5, 范围：0-60

Returns:

(:obj:DhcpServer): DHCP Server会话对象Object

Examples: .. code:: RobotFramework

Create Dhcp Server	Port=${Port}	RenewTime=100
Create Dhcp Server Address Pool
Arguments
Sessions
** kwargs
Documentation
创建DHCP Server会话对象地址池

Args:

Sessions (:obj:DhcpServer): DHCPv4 Client协议对象, 类型为：object / list

Keyword Args:

Name (str): DHCP Server协议会话名称

PoolAddressStart (str): 开始地址, 取值范围：IPv4地址, 默认值：1.1.1.2

PoolAddressStep (str): 地址步长, 取值范围：IPv4地址, 默认值：0.0.0.1

PrefixLength (number): 前缀长度, 默认值：24, 范围：0-32

RouterList (str): 网关列表

LimitPoolCount (bool): 限制地址池个数, 默认值：True

PoolAddressCount (number): 地址池地址个数, 默认值：255, 范围：0-4294967295

DomainName (str): 域名

DnsList (str): DNS地址列表

Returns:

(:obj:Dhcpv4AddressPool): DHCP地址池对象列表list

Examples: .. code:: RobotFramework

Create Dhcp Server Address Pool	Sessions=${Sessions}	PoolAddressStart=2.2.2.2
Create Dhcp Server Custom Option
Arguments
Session
** kwargs
Documentation
创建测试仪表DHCP协议会话option对象

Args:

Session (:obj:DhcpClient): DHCPv4 Client协议对象, 类型为：object / list

Keyword Args:

OptionTag (number): 可选项类型标识, 默认值：0, 取值范围：0-255

OptionType (str): 可选项数据类型, 默认值：HEX, 支持以下参数：

HEX

STRING

BOOLEAN

INT8

INT16

INT32

IP

EnableOptionValueList (bool): 可选项值列表, 默认值：False

OptionValue (str): 可选项值, 默认值：""

MessageType (str): 携带Option消息类型, 默认值：DISCOVER, 支持以下参数：

DISCOVER

REQUEST

Returns:

(:obj:Dhcpv4ClientOption): 测试仪表DHCP协议会话option对象Object

Examples: .. code:: RobotFramework

Create Dhcp Server Custom Option	Session=${Sessions}
Create Dhcpv6 Client
Arguments
Port
** kwargs
Documentation
创建DHCPv6客户端会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): DHCPv6客户端会话名称, 类型为：string

Enable (bool): 使能DHCPv6客户端会话, 类型为：bool, 取值范围：True或False, 默认值：True

EmulationMode (str): 会话模式, 默认值：DHCPV6, 取值范围：

DHCPV6

DHCPV6PD

DHCPV6ANDPD

EnableRenewMsg (bool): 使能Renew消息, 默认值：True, 取值范围：True或False

EnableRebindMsg (bool): 使能Rebind消息, 默认值：True, 取值范围：True或False

EnableReconfigAccept (bool): 使能Reconfigure消息, 默认值：True, 取值范围：True或False

EnableSyncAddressInterface (bool): 默认值：True, 取值范围：True或False

T1Timer (int): T1时刻（秒）, 取值范围：0-2147483647, 默认值：302400

T2Timer (int): T2时刻（秒）, 取值范围：0-2147483647, 默认值：483840

PreferredLifetime (int): 首选生命周期（秒）, 取值范围：0-2147483647, 默认值：604800

ValidLifetime (int): 有效生命周期（秒）, 取值范围：0-2147483647, 默认值：2592000

RapidCommitOptMode (str): 快速交互模式, 默认值：DISABLE, 取值范围：

DISABLE

ENABLE

SERVERSET

DuidType (str): DUID类型, 默认值：LL, 取值范围：

LLT

EN

LL

CUSTOM

DuidCustomValue (int): 自定义DUID编号, 取值范围：0-65535, 默认值：1

DuidEnterpriseNumber (int): DUID企业编号, 取值范围：0-4294967295, 默认值：3456

DuidStartValue (str): DUID企业编号, 默认值：3456, 取值范围：匹配正则表达式"^([0-9a-fA-F]{1,256})$"

DuidStepValue (int): DUID标识符跳变, 取值范围：0-4294967295, 默认值：0x1

DestinationAddress (str): 目的地址, 默认值：ALL, 取值范围：

ALL

SERVER

EnableRelayAgent (bool): 使能中继代理, 默认值：False, 取值范围：True或False

RelayAgentIp (str): 中继代理IP, 默认值：2000::1, 取值范围：有效的ipv6地址

ServerIp (str): 服务IP, 默认值：2001::2, 取值范围：有效的ipv6地址

EnableUseRelayAgentMacForTraffic (bool): 默认值：True

RequestPrefixLength (int): 请求前缀长度, 取值范围：0-128, 默认值：64

RequestPrefixStartAddress (str): 请求前缀地址, 默认值：'::', 取值范围：有效的ipv6地址

ControlPlaneSrcIPv6Addr (str): 默认值：LINKLOCAL, 取值范围：

LINKLOCAL

ROUTEADVERTISEMENT

RequestStartAddress (str): 请求前缀地址, 默认值：'::', 取值范围：有效的ipv6地址

EnableAuthentication (bool): 使能认证, 默认值：False, 取值范围：True或False

AuthenticationProtocol (str): 认证协议, 默认值：DELAYED, 取值范围：

DELAYED

RECONFIGURATION

DhcpRealm (str): 认证域名称, 默认值：'xinertel.com'

AuthenticationKeyId (int): 取值范围：0-4294967295, 默认值：0

AuthenticationKey (str): 认证秘钥ID, 默认值：''

AuthenticationKeyType (str): 认证秘钥类型, 默认值：ASCII, 取值范围：

ASCII

HEX

EnableDad (bool): 使能重复地址检测（DAD）, 默认值：False, 取值范围：True或False

DadTimeout (int): DAD超时时间（秒）, 取值范围：1-4294967295, 默认值：2

DadTransmits (int): DAD传输次数, 取值范围：1-4294967295, 默认值：1

HostInterface (:obj:Interface): 接口对象, 类型：object

Returns:

(:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Dhcpv6 Client	Port=${Port}	DadTransmits=10
Create Dhcpv6 Client Custom Options
Arguments
Sessions
** kwargs
Documentation
创建DHCPv6 Client Custom Options对象

Args：

Session (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Keyword Args:

OptionVal (int): 选项标识, 取值范围：0-255, 默认值：0

IncludeMsg (list): 包含选项的消息类型, 默认值：['SOLICIT', 'REQUEST'], 取值范围：

SOLICIT

REQUEST

CONFIRM

RENEW

REBIND

RELEASE

INFOREQUEST

RELAYFORWARD

Wildcards (bool): 使能通配符, 默认值：False, 取值范围：True或False

StringIsHexadecimal (bool): 使能十六进制字符, 默认值：False, 取值范围：True或False

OptionPayload (str): 选项载荷, 默认值：'', 取值范围：string length in [0,512]

OptionHexPayload (int): 十六进制选项载荷, 默认值：""

RemoveOption (bool): 默认值：False, 取值范围：True或False

Returns:

(:obj:Dhcpv6ClientCustomOptionsConfig): DHCPv6 Client Custom Options对象, 类型：object / list

Examples: .. code:: RobotFramework

${Dhcpv6}	Create Dhcpv6 Client	Port=${Port}
Create Dhcpv6 Client Custom Options	Sessions=${Dhcpv6}	Wildcards=True
Create Dhcpv6 Server
Arguments
Port
** kwargs
Documentation
创建DHCPv6服务端会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): DHCPv6服务端会话名称, 类型为：string

Enable (bool): 使能DHCPv6服务端会话, 类型为：bool, 取值范围：True或False, 默认值：True

EmulationMode (str): 默认值：DHCPV6, 取值范围：

DHCPV6

DHCPV6PD

RenewalTimer (int): T1租约更新时间（%）, 取值范围：1-200, 默认值：50

RebindingTimer (int): T2租约更新时间（%）, 取值范围：1-200, 默认值：80

DnsList (str): DNS地址列表, 取值范围：IPv6地址, 默认值："::"

EnableDelayedAuth (bool): 使能延时认证, 取值范围：True或False, 默认值：False

DhcpRealm (str): DHCP认证域名, 默认值："xinertel.com"

AuthenticationKeyId (int): 认证秘钥ID, 取值范围：0-4294967295, 默认值：0

AuthenticationKey (str): 认证秘钥, 默认值：""

AuthenticationKeyType (str): 认证秘钥类型, 默认值：ASCII, 取值范围：

ASCII

HEX

EnabledReconfigureKey (bool): 使能重新配置认证, 取值范围：True或False, 默认值：False

ReconfigureKey (str): 重新配置秘钥类型, 默认值：""

ReconfigureKeyType (str): 重新配置秘钥类型, 默认值：ASCII, 取值范围：

ASCII

HEX

EnabledDhcpv6Only (bool): 使能单独DHCPv6, 取值范围：True或False, 默认值：False

EnabledTcp (bool): 使能TCP, 取值范围：True或False, 默认值：False

TcpPort (int): TCP端口号, 取值范围：1-65535, 默认值：547

LeaseQueryStatusCode (str): 租借查询应答码, 默认值：SUCCESS, 取值范围：

SUCCESS

UNKNOWN_QUERY_TYPE

MALFORMED_QUERY

NOT_CONFIGURED

NOT_ALLOWED

BulkLeaseQueryStatusCode (str): 批量租借查询应答码, 默认值：SUCCESS, 取值范围：

SUCCESS

UNKNOWN_QUERY_TYPE

MALFORMED_QUERY

NOT_CONFIGURED

NOT_ALLOWED

QUERY_TERMINATED

ActiveLeaseQueryStatusCode (str): 活动租借查询应答码, 默认值：SUCCESS, 取值范围：

SUCCESS

UNKNOWN_QUERY_TYPE

MALFORMED_QUERY

NOT_CONFIGURED

NOT_ALLOWED

QUERY_TERMINATED

DATA_MISSING

CATCH_UP_COMPLETE

NOT_SUPPORTED

StartTlsStatusCode (str): 启动TLS应答码, 默认值：SUCCESS, 取值范围：

SUCCESS

TLS_CONNECTION_REFUSED

Returns:

(:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Dhcpv6 Server	Port=${Port}	DadTransmits=10
Create Dhcpv6 Server Address Pool
Arguments
Sessions
** kwargs
Documentation
创建DHCPv6 Server Address Pool对象

Args：

Session (:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型为：object / list

Keyword Args:

PrefixLength (int): 地址池前缀长度, 取值范围：0-128, 默认值：64

AssignMode (str): 默认值：SUCCESS, 取值范围：

CUSTOM

EUI64

StartAddress (str): 地址池起始地址, 取值范围：IPv6地址, 默认值："2001::1"

HostStep (str): 地址池地址跳变, 取值范围：IPv6地址, 默认值："::1"

AddressCount (int): 地址池地址总数, 取值范围：1-4294967295, 默认值：65535

PreferredLifetime (int): 首选生命周期（秒）, 取值范围：0-4294967295, 默认值：604800

ValidLifetime (int): 有效生命周期（秒）, 取值范围：0-4294967295, 默认值：2592000

MinIaidValue (int): 最小IAID值, 取值范围：0-4294967295, 默认值：0

MaxIaidValue (int): 最大IAID值, 取值范围：0-4294967295, 默认值：4294967295

Returns:

(:obj:Dhcpv6AddressPoolsConfig): DHCPv6 Server Address Pool对象, 类型：object / list

Examples: .. code:: RobotFramework

${Dhcpv6}	Create Dhcpv6 Server	Port=${Port}
Create Dhcpv6 Server Address Pool	Sessions=${Dhcpv6}	MinIaidValue=10
Create Dhcpv6 Server Custom Options
Arguments
Sessions
** kwargs
Documentation
创建DHCPv6 Server Custom Options对象

Args：

Session (:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型为：object / list

Keyword Args:

OptionVal (int): 选项标识, 取值范围：0-255, 默认值：0

IncludeMsg (list): 包含选项的消息类型, 默认值：['ADVERTISE', 'REPLY'], 取值范围：

ADVERTISE

REPLY

RECONFIGURE

RELAYREPLY

Wildcards (bool): 使能通配符, 取值范围：True或False, 默认值：False

StringIsHexadecimal (bool): 使能十六进制字符串, 取值范围：True或False, 默认值：False

OptionPayload (str): 选项负载, 默认值：""

OptionHexPayload (str): 选项负载, 默认值：""

Returns:

(:obj:Dhcpv6ServerCustomOptionsConfig): DHCPv6 Server Custom Options对象, 类型：object / list

Examples: .. code:: RobotFramework

${Dhcpv6}	Create Dhcpv6 Server	Port=${Port}
Create Dhcpv6 Server Custom Options	Sessions=${Dhcpv6}	Wildcards=True
Create Dhcpv6 Server Prefix Pool
Arguments
Sessions
** kwargs
Documentation
创建DHCPv6 Server Prefix Pool对象

Args：

Session (:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型为：object / list

Keyword Args:

PrefixLength (int): 前缀池前缀长度, 取值范围：0-128, 默认值：64

PrefixPoolStart (str): 前缀池起始地址, 取值范围：IPv6地址, 默认值："2001::1"

PrefixPoolStep (str): 前缀池地址跳变, 取值范围：IPv6地址, 默认值："0:0:0:1::"

PrefixAddressCount (int): 前缀池地址总数, 取值范围：1-65535, 默认值：16

PreferredLifetime (int): 最优租期（秒）, 取值范围：0-4294967295, 默认值：604800

ValidLifetime (int): 有效租期（秒）, 取值范围：0-4294967295, 默认值：2592000

MinIaidValue (int): 最小IAID值, 取值范围：0-4294967295, 默认值：0

MaxIaidValue (int): 最大IAID值, 取值范围：0-4294967295, 默认值：4294967295

Returns:

(:obj:Dhcpv6PrefixPoolsConfig): DHCPv6 Server Prefix Pool对象, 类型：object / list

Examples: .. code:: RobotFramework

${Dhcpv6}	Create Dhcpv6 Server	Port=${Port}
Create Dhcpv6 Server Prefix Pool	Sessions=${Dhcpv6}	MinIaidValue=10
Create Dot1x
Arguments
Port
** kwargs
Documentation
创建802.1x会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): 802.1x会话名称, 类型为：string

Enable (bool): 使能801.1x会话, 类型为：bool, 取值范围：True或False, 默认值：True

AuthMode (str): 默认值：MD5, 取值范围：

MD5

TLS

TTLS

Identity (str): 默认值：xinertel, 取值范围：string length in [1,255]

Password (str): 默认值：xinertel, 取值范围：string length in [1,255]

UseAuthenticatorMac (bool): 使能801.1x会话, 类型为：bool, 取值范围：True或False, 默认值：False

AuthenticatorMac(str): 默认值：01:80:c2:00:00:03, 取值范围：有效的mac地址

RetryCount (int): 默认值：5, 取值范围：uint32

RetryTimeout (int): 默认值：5, 取值范围：1-4294967295

RetransmitCount (int): 默认值：5, 取值范围：uint32

RetransmitTimeout (int): 默认值：5, 取值范围：1-4294967295

SupplicantCertificateName (str): 默认值：‘’, 取值范围：string length in [1,255]

CertificatePassword (str): 默认值：‘’, 取值范围：string length in [1,255]

DuplicateUserInfoToInner (bool): 使能801.1x会话, 类型为：bool, 取值范围：True或False, 默认值：True

InnerIdentity (str): 默认值：xinertel, 取值范围：string length in [1,255]

InnerPassword (str): 默认值：xinertel, 取值范围：string length in [1,255]

InnerTunnelAuthMode (str): 默认值：AUTO, 取值范围：

AUTO

GTC

MS_CHAPV2

MD5

EnableClientCertificate (bool): 使能801.1x会话, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:Dot1x): 802.1x会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Dot1x	Port=${Port}	DadTransmits=10
Create Igmp
Arguments
Port
** kwargs
Documentation
创建IGMP协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): IGMP协会话名称, 类型为：string

Enable (bool): 使能ICMP协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

Version (str): 版本, 类型为：string, 默认值：IGMPV2, 支持版本：

IGMPV1

IGMPV2

IGMPV3

PackReports (bool): 合并报告报文, 类型为：bool, 取值范围：True或False, 默认值：False

InitialJoin (bool): 单个初始报文加入组, 类型为：bool, 取值范围：True或False, 默认值：False

RobustJoin (bool): 多个初始报文加入组, 类型为：bool, 取值范围：True或False, 默认值：False

RobustnessVariable (int): Robust值, 类型为：number, 取值范围：2-255, 默认值：2

UnsolicitedReportInterval (int): 发送初始报文的时间间隔 (秒), 类型为：number, 取值范围：0-65535, 默认值：10

ForceLeave (bool): 强制发送Leave报文, 类型为：bool, 取值范围：True或False, 默认值：True

RouterPresentTimeout (int): IGMPv1路由器存在的超时时间 (秒), 类型为：number, 取值范围：0-65535, 默认值：400

NotFragment (bool): 设置IP头报文分片标志位, 类型为：bool, 取值范围：True或False, 默认值：False

TosValue (bool): 设置IP头TOS值 (Hex), 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:Igmp): IGMP协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Igmp	Port=${Port}	Version=IGMPV3
Create Igmp Querier
Arguments
Port
** kwargs
Documentation
创建IGMP Querier协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): IGMP Querier协会话名称, 类型为：string

Enable (bool): 使能IGMP Querier协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

Version (str): 版本, 类型为：string, 默认值：IGMPV2, 支持版本：

IGMPV1

IGMPV2

IGMPV3

RobustnessVariable (int): 健壮系数, 取值范围：2-255, 默认值: 2

Interval (int): 查询时间间隔（秒）, 取值范围：0-4294967295, 默认值: 125

QueryResponseInterval (int): 查询响应时间间隔（毫秒）, 取值范围：0-4294967295, 默认值: 10000

StartupQueryCount (int): 初始查询报文个数, 取值范围：1-255, 默认值：2

LastMemberQueryInterval (int): 最后成员查询时间间隔（毫秒）, 取值范围：0-4294967295, 默认值: 1000

LastMemberQueryCount (bool): 最后成员查询次数, 取值范围：0-255, 默认值: 2

IPv4DoNotFragment (bool): 设置IP头报文分片标志位, 取值范围：True或False, 默认值: False

IPv4TosValue (str): 设置IP头TOS值, 类型为：bool, 取值范围：0x0-0xff, 默认值: 0xc0

Returns:

(:obj:IgmpQuerier): IGMP协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Igmp Querier| Port=${Port}	Version=IGMPV3
Create Imix
Arguments
Name
Seed
=
None
Documentation
创建流量Imix模板

Args:

Name (str): 创建的Imix模板名称

Seed (int): Imix模板随机种子

Returns:

(:obj:Imix): Imix模板对象

Examples: .. code:: RobotFramework

Create Imix	Name=Imix_1	Seed=10121112
Create Interface
Arguments
Port
Layers
=
None
Documentation
在指定端口上創建接口

Args:

Port (:obj:Port): 测试仪仪表端口Port对象

Layers (list): 接口封装类型, 支持的有：

eth

ipv4

ipv6

Returns:

(:obj:Interface): 接口interface对象

Examples: robotframework:

.. code:: robotframework

${Locations}	Create List	//192.168.0.1/1/1	
${Layers}	Create List	eth	ipv4
${Port}	Reserve Ports	${Ports}	${Location}
${Interface}	Create Interface	${Port}	${Layers}
Create Isis
Arguments
Port
** kwargs
Documentation
创建ISIS协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): ISIS协会话名称, 类型为：string

Enable (bool): 使能ISIS协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

IpVersion (str): IP版本, 类型为：string, 默认值：IPV4, 支持版本：

IPV4

IPV6

IPV4IPV6

Level (str): 区域类型, 类型为：string, 默认值：L2, 支持版本：

L1

L2

L1L2

NetworkType (str): 网络类型, 类型为：string, 默认值：BROADCAST, 支持参数：

BROADCAST

P2P

SystemId (str): 系统ID, 类型为：string, 取值范围：MAC地址, 默认值：00:00:00:00:00:01

Priority (int): 路由器优先级, 类型为：number, 取值范围：0-127, 默认值：0

AuthMethod (str): 认证方式, 类型为：string, 默认值：NONE, 支持参数：

NONE

SIMPLE

MD5

Password (str): 4字节自治域跳变, 类型为：string, 默认值：Xinertel

CircuitId (int): 电路ID, 类型为：number, 取值范围：0-255, 默认值：1

Area1 (str): 区域ID 1, 类型为：hex number, 取值范围：0x0-0xff, 默认值：0x10

Area2 (str): 区域ID 2, 类型为：hex number, 取值范围：0x0-0xff, 默认值：空

Area3 (str): 区域ID 3, 类型为：hex number, 取值范围：0x0-0xff, 默认值：空

MetricMode (str): 度量模式, 类型为：string, 默认值：NARROWWIDE, 支持参数：

NARROW

WIDE

NARROWWIDE

TeRouterId (str): TE路由器ID, 类型为：string, 取值范围：IPv4地址, 默认值：192.168.1.1

TeRouterIdIpv6 (str): IPv6 TE路由器ID, 类型为：string, 取值范围：IPv6地址, 默认值：3000::1

HelloInterval (int): Hello PDU发送间隔(秒), 类型为：number, 取值范围：1-300, 默认值：10

HelloMultiplier (int): Hello时间间隔倍数, 类型为：number, 取值范围：1-100, 默认值：3

PsnInterval (int): PSNP发送间隔(秒), 类型为：number, 取值范围：1-20, 默认值：2

LspRefreshTime (int): LSP刷新时间(秒), 类型为：number, 取值范围：1-65535, 默认值：900

RetransInterval (int): LSP重传间隔(秒), 类型为：number, 取值范围：1-100, 默认值：5

HelloPadding (bool): 类型为：bool, 取值范围：True或False, 默认值：True

LspSize (int): LSP大小, 类型为：number, 取值范围：100-1492, 默认值：1492

ValidateIpAddr (bool): 使能接口校验, 类型为：bool, 取值范围：True或False, 默认值：False

EnableGracefulRestart (bool): 使能平滑重启, 类型为：bool, 取值范围：True或False, 默认值：False

EnableViewRoutes (bool): 使能查看路由, 类型为：bool, 取值范围：True或False, 默认值：False

EnableBFD (bool): 使能BFD, 类型为：bool, 取值范围：True或False, 默认值：False

MtParams (int): 多拓扑参数数量, 类型为：number, 取值范围：0-2, 默认值：0

PerPduAuthentication (int): Per PDU认证数量, 类型为：number, 取值范围：0-4, 默认值：0

ReportLabel (bool): 使能ReportLabel, 类型为：bool, 默认值：True

LearnRoute (bool): 使能LearnRoute, 类型为：bool, 默认值：True

RecordLspNextSequenceNum (bool): 使能Record Lsp Next Sequence Number, 类型为：bool, 默认值：True

L1NarrowMetric (int): L1 Narrow Metric, 类型为：number, 取值范围：0-63, 默认值：1

L1WideMetric (int): L1 Wild Metric, 类型为：number, 取值范围：0-16777214, 默认值：1

L2NarrowMetric (int): L2 Narrow Metric, 类型为：number, 取值范围：0-63, 默认值：1

L2WideMetric (int): L2 Wide Metric, 类型为：number, 取值范围：0-16777214, 默认值：1

Returns:

(:obj:IsisRouter): ISIS协议会话对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${MtId}	Create List	IPV4	IPV6
${{MtFlags}	Create List	ABIT	OBIT
Edit Isis	Session=${Session}	EnableViewRoutes=True	MtParams=1
Create Isis Binding Sr Sid Sub Tlv
Arguments
Binding
** kwargs
Documentation
创建ISIS Capability Srms Preference Sub Tlv对象

Args:

Binding (:obj:IsisSrBindingTlv): ISIS Tlv对象, 类型为：object

Keyword Args:

ValueType (str): 选择标识符（SID或标签）, 默认值：BIT32, 取值范围：

BIT20

BIT32

Sid (int): 值类型为20bit时，指定起始标签; 值类型为32bit时，指定起始SID, 默认值：12000

Returns:

(:obj:IsisSrSRMSPrefSubTlv): ISIS Capability Srms Preference Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Binding}	Create Isis Binding Tlv	Lsp=${LSP}	Ipv4Version=False
Create Isis Binding Sr sid Sub Tlv | Binding=${Binding}
Create Isis Capability Sr Algorithm Sub Tlv
Arguments
Capability
** kwargs
Documentation
创建ISIS Capability Sr Algorithm Sub Tlv对象

Args:

Capability (:obj:IsisCapabilityTlv): ISIS Tlv对象, 类型为：object

Keyword Args:

Algorithm (list): 算法值, 默认值：0, 取值范围：int

Returns:

(:obj:IsisSrAlgorithmSubTlv): ISIS Capability Sr Algorithm Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Capability}	Create Isis Capability Tlv	Lsp=${LSP}	SystemId=1.1.1.1
Create Isis Capability Sr Algorithm Sub Tlv	Capability=${Capability}		
Create Isis Capability Sr Capability Sub Tlv
Arguments
Session
Capability
** kwargs
Documentation
创建ISIS Capability Sr Capability Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Capability (:obj:IsisCapabilityTlv): ISIS Tlv对象, 类型为：object

Keyword Args:

Flags (list): 选择一个或多个包含在TLV中的标志位, 默认值：['NOSHOW', 'IPv4_CAPABLE'], 取值范围：

NOSHOW

IPv4_CAPABLE

IPv6_CAPABLE

ValueType (str): 选择标识符（SID或标签）, 默认值：BIT32, 取值范围：

BIT20

BIT32

Returns:

(:obj:IsisSrCapabilitySubTlv): ISIS Capability Sr Capability Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Capability}	Create Isis Capability Tlv	Lsp=${LSP}	SystemId=1.1.1.1
Create Isis Capability Sr Capability Sub Tlv	Session={Session}	Capability=${Capability}	
Create Isis Capability Sr Fad Sub Tlv
Arguments
Session
Capability
** kwargs
Documentation
创建ISIS Capability Sr Fad Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Capability (:obj:IsisCapabilityTlv): ISIS Tlv对象, 类型为：object

Keyword Args:

FlexAlgo (int): 灵活算法ID, 默认值：128, 取值范围：128-255

MetricType (str): 指定算路使用的度量类型, 默认值：IGP_METRIC, 取值范围：

IGP_METRIC

MIN_LINK_DELAY

TE_METRIC

CalType (int): 指定特定IGP算法的计算类型, 默认值：0, 取值范围：0-255

Priority (int): 指定该Sub TLV的优先级, 默认值：0

FlexAlgoSubTlv (list): 选择灵活算法路径计算要遵循的约束条件, 默认值：['UNKNOWN'], 取值范围：

UNKNOWN

EXCLUDE_ADMIN

INCLUDE__ANY_ADMIN

INCLUDE_ALL_ADMIN

DEFINITION_FLAGS

EXCLUDE_SRLG

ExcludeAdmin (int): 类型为：number, 默认值：0, 取值范围：0-4294967295

IncludeAnyAdmin (int): 类型为：number, 默认值：0, 取值范围：0-4294967295

IncludeAllAdmin (int): 类型为：number, 默认值：0, 取值范围：0-4294967295

DefinitionFlags (list): 类型为：hex int, 默认值：0x80, 取值范围：0-FF

ExcludeSRLG (list): 类型为：hex int, 默认值：0x10020000, 取值范围：0-4294967295

Returns:

(:obj:IsisFelxAlgoDefinitionSubTlv): ISIS Capability Sr Fad Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Capability}	Create Isis Capability Tlv	Lsp=${LSP}	SystemId=1.1.1.1
Create Isis Capability Sr Fad Sub Tlv	Session={Session}	Capability=${Capability}	
Create Isis Capability Sr Node Msd Sub Tlv
Arguments
Session
Capability
** kwargs
Documentation
创建ISIS Capability Sr Node Msd Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Capability (:obj:IsisCapabilityTlv): ISIS Tlv对象, 类型为：object

Keyword Args:

Flags (list): 选择一个或多个包含在TLV中的标志位, 默认值：UNKNOWN, 取值范围：

UNKNOWN

MAX_SEG_LELT

MAX_END_POP

MAX_T_INSERT

MAX_T_ENCAPS

MAX_END_D

MaxSegmentLeft (int): 在应用与SID关联的SRv6 Endpoint Function指令之前，指定接收报文的SRH中SL（Segment Left）字段的最大值, 默认值：8, 取值范围：0-255

MaxEndPop (int): 指定SRH栈的顶端SRH中SID的最大数量, 默认值：8, 取值范围：0-255

MaxInsert (int): 指定执行T.Insert行为时可包含SID的最大数量, 默认值：8, 取值范围：0-255

MaxEncap (int): 指定执行T.Encap行为时可包含SID的最大数量, 默认值：8, 取值范围：0-255

MaxEndD (int): 指定执行End.DX6和End.DT6功能时，SRH中SID的最大数量, 默认值：8, 取值范围：0-255

Returns:

(:obj:IsisSrMsdSubTlv): ISIS Capability Sr Node Msd Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Capability}	Create Isis Capability Tlv	Lsp=${LSP}	SystemId=1.1.1.1
Create Isis Capability Sr Node Msd Sub Tlv	Capability=${Capability}		
Create Isis Capability Srms Preference Sub Tlv
Arguments
Capability
** kwargs
Documentation
创建ISIS Capability Srms Preference Sub Tlv对象

Args:

Capability (:obj:IsisCapabilityTlv): ISIS Tlv对象, 类型为：object

Keyword Args:

Preference (int): 指定本节点作为SR Mapping Server的优先级, 取值范围：0-255, 默认值：0

Returns:

(:obj:IsisSrSRMSPrefSubTlv): ISIS Capability Srms Preference Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Capability}	Create Isis Capability Tlv	Lsp=${LSP}	SystemId=1.1.1.1
Create Isis Capability Srms Preference Sub Tlv	Capability=${Capability}		
Create Isis Capability Srv6 Capability Sub Tlv
Arguments
Session
Capability
** kwargs
Documentation
创建ISIS Capability Srv6 Capability Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Capability (:obj:IsisCapabilityTlv): ISIS Tlv对象, 类型为：object

Keyword Args:

Flags (list): 选择一个或多个包含在TLV中的标志位, 默认值：UNKNOWN, 取值范围：

UNKNOWN

UNUSED0

O_BIT

UNUSED2

UNUSED3

UNUSED4

UNUSED5

UNUSED6

UNUSED7

UNUSED8

UNUSED9

UNUSED10

UNUSED11

UNUSED12

UNUSED13

UNUSED14

UNUSED15

Returns:

(:obj:IsisSrv6CapabilitySubTlv): ISIS Capability Srv6 Capability Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Capability}	Create Isis Capability Tlv	Lsp=${LSP}	SystemId=1.1.1.1
Create Isis Capability Srv6 Capability Sub Tlv	Session=Session	Capability=${Capability}	
Create Isis Capability Tlv
Arguments
Session
Lsp
** kwargs
Documentation
创建ISIS Capability TLV对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Lsp (:obj:IsisLspConfig): ISIS LSP对象, 类型为：object

Keyword Args:

Option (list): 选项, 默认值：['NOSHOW', 'SBIT'], 取值范围：

NOSHOW

SBIT

DBIT

RouterId (str): 路由器ID, 默认值："192.0.0.1", 取值范围：有效IPv4地址

Returns:

(:obj:IsisCapabilityTlv): ISIS Neighbor TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
Create Isis Capability Tlv	Session=${Session}	Lsp=${LSP}	RouterId=1.1.1.1
Create Isis Ipv4 Tlv
Arguments
Lsp
** kwargs
Documentation
创建ISIS IPv4 TLV对象

Args:

Lsp (:obj:IsisLspConfig): ISIS LSP对象, 类型为：object

Keyword Args:

Name (str): ISIS IPv4 TLV对象名称, 类型为：string

Enable (bool): 使能ISIS IPv4 TLV, 类型为：bool, 取值范围：True或False, 默认值：True

RouteType (str): 路由类型, 类型为：string, 默认值：INTERNAL, 支持参数：

INTERNAL

EXTERNAL

RouteCount (int): 路由数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

Increment (int): 步长, 类型为：number, 取值范围：1-4294967295, 默认值：1

MetricType (str): 度量类型, 类型为：string, 默认值：INTERNAL, 支持参数：

INTERNAL

EXTERNAL

WideMetric (int): 扩展度量, 类型为：number, 取值范围：0-16777214, 默认值：10

UpDownBit (bool): Up/Down位, 类型为：bool, 取值范围：True或False, 默认值：False

StartIpv4Prefix (str): 起始IPv4路由前缀, 类型为：string, 取值范围：IPv4地址, 默认值：192.168.1.1

PrefixLength (int): 前缀长度, 类型为：number, 取值范围：1-32, 默认值：24

NarrowMetric (int): 默认度量, 类型为：number, 取值范围：0-63, 默认值：10

Returns:

(:obj:IsisIpv4TlvConfig): ISIS IPv4 TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
Create Isis Ipv4 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02	
Create Isis Ipv6 Tlv
Arguments
Lsp
** kwargs
Documentation
创建ISIS IPv6 TLV对象

Args:

Lsp (:obj:IsisLspConfig): ISIS LSP对象, 类型为：object

Keyword Args:

Name (str): ISIS IPv6 TLV对象名称, 类型为：string

Enable (bool): 使能ISIS IPv6 TLV, 类型为：bool, 取值范围：True或False, 默认值：True

RouteType (str): 路由类型, 类型为：string, 默认值：INTERNAL, 支持参数：

INTERNAL

EXTERNAL

RouteCount (int): 路由数量, 类型为：number, 取值范围：1-4294967295, 默认值：1

Increment (int): 步长, 类型为：number, 取值范围：1-4294967295, 默认值：1

MetricType (str): 度量类型, 类型为：string, 默认值：INTERNAL, 支持参数：

INTERNAL

EXTERNAL

WideMetric (int): 扩展度量, 类型为：number, 取值范围：0-16777214, 默认值：10

UpDownBit (bool): Up/Down位, 类型为：bool, 取值范围：True或False, 默认值：False

StartIpv6Prefix (str): 起始IPv4路由前缀, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

PrefixLength (int): 前缀长度, 类型为：number, 取值范围：1-32, 默认值：24

Returns:

(:obj:IsisIpv6TlvConfig): ISIS IPv6 TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
Create Isis Ipv6 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02	
Create Isis Lsp
Arguments
Session
** kwargs
Documentation
创建ISIS LSP对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Keyword Args:

Name (str): ISIS LSP对象名称, 类型为：string

Enable (bool): 使能ISIS LSP, 类型为：bool, 取值范围：True或False, 默认值：True

SystemId (str): 系统ID, 类型为：string, 取值范围：MAC地址, 默认值：00:00:00:00:00:01

Level (str): 区域类型, 类型为：string, 默认值：L2, 支持版本：

L1

L2

PseudonodeId (int): 伪节点ID, 类型为：number, 取值范围：1-100, 默认值：0

TeRouterId (str): TE路由器ID, 类型为：string, 取值范围：IPv4地址, 默认值：192.168.1.1

TeRouterIdIpv6 (str): IPv6 TE路由器ID, 类型为：string, 取值范围：IPv6地址, 默认值：3000::1

SequenceNumber (int): 序列号, 类型为：number, 取值范围：1-300, 默认值：10

RemainingLifeTime (int): 剩余生存时间, 类型为：number, 取值范围：1-100, 默认值：3

Checksum (int): 使能正确校验和, 类型为：number, 取值范围：1-20, 默认值：2

AttachedBit (int): 区域关联位, 类型为：number, 取值范围：1-65535, 默认值：900

OverloadBit (int): 过载位, 类型为：number, 取值范围：1-100, 默认值：5

Returns:

(:obj:IsisLspConfig): ISIS LSP对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}
Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
Create Isis Neighbor Custom Sub Tlv
Arguments
SubTlv
** kwargs
Documentation
创建Isis Neighbor Custom Sub Tlv对象

Args:

SubTlv (:obj:IsisSrLinkMsdSubTlv): ISIS Neighbor Sr Link Msd Sid Sub TLV对象, 类型为：object

Keyword Args:

SubType (int): 该Sub-TLV的Type字段值, 默认值：0, 取值范围：0-255

SubValue (int): 该Sub-TLV的Value字段值, 取值范围：十六进制值。默认值：08

Returns:

(:obj:IsisSrLinkMsdSubTlv): Isis Neighbor Sr Link Msd Sid Sub Tlv对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Neighbor}	Create Isis Neighbor Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
${Msd}	Create Isis Neighbor Sr Link Msd Sid Sub Tlv	Neighbor=${Neighbor}	
Isis Neighbor Custom Sub Tlv	SubTlv=${Msd}		
Create Isis Neighbor Sr Adj Sid Sub Tlv
Arguments
Session
Neighbor
** kwargs
Documentation
创建Isis Neighbor Sr Adj Sid Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Neighbor (:obj:IsisNeighborConfig): ISIS Neighbor TLV对象, 类型为：object

Keyword Args:

Flags (list) : 选择一个或多个包含在TLV中的标志位, 默认值：['NOSHOW', 'VALUE', 'LOCAL'], 取值范围：

NOSHOW

ADDRESS

BACKUP

VALUE

LOCAL

SET

PERSISTENT

Sid (int): Flags中包含L.Local和V.Value时，指定标签值; Flags中不包含Value/Index时，指定SID/Label范围内的标签偏移值, 默认值：0, 取值范围：0-4294967295

Weight (int): 指定Adj-SID权重，用于负载分担, 默认值：0, 取值范围：0-255

Returns:

(:obj:IsisSrAdjSidSubTlv): Isis Neighbor Sr Adj Sid Sub Tlv对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Neighbor}	Create Isis Neighbor Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Neighbor Sr Adj Sid Sub Tlv	Neighbor=${Neighbor}		
Create Isis Neighbor Sr Lan Adj Sid Sub Tlv
Arguments
Session
Neighbor
** kwargs
Documentation
创建Isis Neighbor Sr Lan Sid Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Neighbor (:obj:IsisNeighborConfig): ISIS Neighbor TLV对象, 类型为：object

Keyword Args:

Flags (list) : 选择一个或多个包含在TLV中的标志位, 默认值：['NOSHOW', 'VALUE', 'LOCAL'], 取值范围：

NOSHOW

ADDRESS

BACKUP

VALUE

LOCAL

SET

PERSISTENT

Sid (int): Flags中包含L.Local和V.Value时，指定标签值; Flags中不包含Value/Index时，指定SID/Label范围内的标签偏移值, 默认值：0, 取值范围：0-4294967295

Weight (int): 指定Adj-SID权重，用于负载分担, 默认值：0, 取值范围：0-255

SystemId (str): 指定LAN上邻居的系统ID, 默认值："00:00:00:00:00:01"

Returns:

(:obj:IsisSrAdjSidSubTlv): Isis Neighbor Sr Adj Sid Sub Tlv对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Neighbor}	Create Isis Neighbor Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Neighbor Sr Lan Adj Sid Sub Tlv	Neighbor=${Neighbor}		
Create Isis Neighbor Sr Link Msd Sub Tlv
Arguments
Session
Neighbor
** kwargs
Documentation
创建Isis Neighbor Sr Link Msd Sid Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Neighbor (:obj:IsisNeighborConfig): ISIS Neighbor TLV对象, 类型为：object

Keyword Args:

Flags (list): 选择一个或多个包含在TLV中的标志位, 默认值：UNKNOWN, 取值范围：

UNKNOWN

MAX_SEG_LELT

MAX_END_POP

MAX_T_INSERT

MAX_T_ENCAPS

MAX_END_D

MaxSegmentLeft (int): 在应用与SID关联的SRv6 Endpoint Function指令之前，指定接收报文的SRH中SL（Segment Left）字段的最大值, 默认值：8, 取值范围：0-255

MaxEndPop (int): 指定SRH栈的顶端SRH中SID的最大数量, 默认值：8, 取值范围：0-255

MaxInsert (int): 指定执行T.Insert行为时可包含SID的最大数量, 默认值：8, 取值范围：0-255

MaxEncap (int): 指定执行T.Encap行为时可包含SID的最大数量, 默认值：8, 取值范围：0-255

MaxEndD (int): 指定执行End.DX6和End.DT6功能时，SRH中SID的最大数量, 默认值：8, 取值范围：0-255

Returns:

(:obj:IsisSrLinkMsdSubTlv): Isis Neighbor Sr Link Msd Sid Sub Tlv对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Neighbor}	Create Isis Neighbor Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Neighbor Sr Link Msd Sid Sub Tlv	Neighbor=${Neighbor}		
Create Isis Neighbor Srv6 Endx Sid Sub Tlv
Arguments
Session
Neighbor
** kwargs
Documentation
创建Isis Neighbor Srv6 EndX Sid Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Neighbor (:obj:IsisNeighborConfig): ISIS Neighbor TLV对象, 类型为：object

Keyword Args:

Flags (list): 选择一个或多个包含在TLV中的标志位, 默认值：UNKNOWN, 取值范围：

UNKNOWN

BACKUP

SET

PERSISTENT

UNUSED3

UNUSED4

UNUSED5

UNUSED6

UNUSED7

Algorithm (int): 指定SID关联的算法, 默认值：0, 取值范围：0-255

Weight (int): 指定End.X SID的权重，用于负载分担, 默认值：100, 取值范围：0-255

EndpointFunc (str): 端点行为, 默认值：END_NO, 取值范围：

END_NO

END_PSP

END_USP

END_PSP_USP

END_X_NO

END_X_PSP

END_X_USP

END_X_PSP_USP

END_T_NO

END_T_PSP

END_T_USP

END_T_PSPS_USP

END_B6

END_B6_ENCAPS

END_BM

END_DX6

END_DX4

EDN_DT6

END_DT4

END_DT46

END_DX2

END_DX2V

END_DX2U

END_DX2M

END_S

END_B6_RED

END_B6_ENCAPS_RED

END_WITH_USD

END_PSP_USD

END_USP_USD

END_PSP_USP_USD

END_X_USD

END_X_PSP_USD

END_X_USP_USD

END_X_PSP_USP_USD

END_T_USD

END_T_PSP_USD

END_T_USP_USD

END_T_PSP_USP_USD

EnableCustom (bool): 使能自定义端点行为, 默认值：False

CustomFunc (int): 自定义端点行为, 默认值：0, 取值范围：0-65535

SID (str): 指定通告的SRv6 SID, 默认值："::1", 取值范围：有效IPv6地址

Returns:

(:obj:IsisSrv6EndXSidSubTlv): Isis Neighbor Srv6 EndX Sid Sub Tlv对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Neighbor}	Create Isis Neighbor Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Neighbor Srv6 EndX Sid Sub Tlv	Neighbor=${Neighbor}		
Create Isis Neighbor Srv6 Lan Endx Sid Sub Tlv
Arguments
Session
Neighbor
** kwargs
Documentation
创建Isis Neighbor Srv6 Lan EndX Sid Sub Tlv对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Neighbor (:obj:IsisNeighborConfig): ISIS Neighbor TLV对象, 类型为：object

Keyword Args:

SystemIdLan (str): LAN系统标识, 默认值："00:10:96:00:00:01"

Flags (list): 选择一个或多个包含在TLV中的标志位, 默认值：UNKNOWN, 取值范围：

UNKNOWN

BACKUP

SET

PERSISTENT

UNUSED3

UNUSED4

UNUSED5

UNUSED6

UNUSED7

Algorithm (int): 指定SID关联的算法, 默认值：0, 取值范围：0-255

Weight (int): 指定End.X SID的权重，用于负载分担, 默认值：100, 取值范围：0-255

EndpointFunc (list): 端点行为, 默认值：END_NO, 取值范围：

END_NO

END_PSP

END_USP

END_PSP_USP

END_X_NO

END_X_PSP

END_X_USP

END_X_PSP_USP

END_T_N

END_T_PSP

END_T_USP

END_T_PSPS_USP

END_B6

END_B6_ENCAPS

END_BM

END_DX6

END_DX4

EDN_DT6

END_DT4

END_DT46

END_DX2

END_DX2V

END_DX2U

END_DX2M

END_S

END_B6_RED

END_B6_ENCAPS_RED

END_WITH_USD

END_PSP_USD

END_USP_USD

END_PSP_USP_USD

END_X_USD

END_X_PSP_USD

END_X_USP_USD

END_X_PSP_USP_USD

END_T_USD

END_T_PSP_USD

END_T_USP_USD

END_T_PSP_USP_USD

EnableCustom (bool): 使能自定义端点行为, 默认值：False

CustomFunc (int): 自定义端点行为, 默认值：0

SID (str): 指定通告的SRv6 SID, 默认值："::1", 取值范围：有效IPv6地址

Returns:

(:obj:IsisSrv6LanEndXSidSubTlv): Isis Neighbor Srv6 Lan EndX Sid Sub Tlv对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Neighbor}	Create Isis Neighbor Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Neighbor Srv6 Lan EndX Sid Sub Tlv	Neighbor=${Neighbor}		
Create Isis Neighbor Te Config
Arguments
Neighbor
** kwargs
Documentation
创建ISIS邻居TLV的Te Config对象

Args:

Neighbor (:obj:IsisNeighborConfig): ISIS Neighbor TLV对象, 类型为：object

Keyword Args:

EnableInterfaceIp (bool): 是否包含本地IPv4地址, 默认值：False

InterfaceIp (str): 本地IPv4地址, 取值范围：有效的ip地址, 默认值：'0.0.0.0'

EnableNeighborIp (bool): 是否包含邻居IPv4地址, 默认值：False

NeighborIp (int): 邻居IPv4地址, 取值范围：有效的ip地址, 默认值：10

EnableInterfaceIpv6 (bool): 是否包含本地IPv6地址, 默认值：False

InterfaceIpv6 (str): 本地IPv6地址, 取值范围：有效的ipv6地址, 默认值：'2000::1'

EnableNeighborIpv6 (bool): 是否包含邻居IPv6地址, 默认值：False

NeighborIpv6 (str): 邻居IPv6地址, 取值范围：有效的ipv6地址, 默认值：'2000::1'

EnableTeGroup (bool): 是否包含TE组, 默认值：False

TeGroup (int): TE组, 取值范围：0-4294967295, 默认值：1

EnableMaxBandwidth (bool): 是否包含最大带宽值, 默认值：False

MaximunLink (int): 最大带宽值(字节/秒), 取值范围：0-4294967295, 默认值：1000

EnableResBandwidth (bool): 是否包含预留带宽值, 默认值：False

MaximumReservableLink (int): 最大预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：1000

EnableUnresBandwidth (bool): 是否包含未预留带宽优先级, 默认值：False

UnreservedBandwidth0 (int): 优先级0的未预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：0

UnreservedBandwidth1 (int): 优先级1的未预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：0

UnreservedBandwidth2 (int): 优先级2的未预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：0

UnreservedBandwidth3 (int): 优先级3的未预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：0

UnreservedBandwidth4 (int): 优先级4的未预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：0

UnreservedBandwidth5 (int): 优先级5的未预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：0

UnreservedBandwidth6 (int): 优先级6的未预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：0

UnreservedBandwidth7 (int): 优先级7的未预留带宽值(字节/秒), 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:IsisTEConfig): ISIS Neighbor TLV Te Config对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Neighbor}	Create Isis Neighbor Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Neighbor Te Config	Neighbor=${Neighbor}		
Create Isis Neighbor Tlv
Arguments
Lsp
** kwargs
Documentation
创建ISIS邻居TLV对象

Args:

Lsp (:obj:IsisLspConfig): ISIS LSP对象, 类型为：object

Keyword Args:

SystemId (str): 邻居系统ID, 取值范围：有效的MAC地址, 默认值："00:00:00:00:00:01"

PseudonodeSystemId (int): 伪节点ID, 取值范围：0-255, 默认值：0

NarrowMetric (int): 默认度量, 取值范围：0-63, 默认值：1

WideMetric (int): 扩展度量, 取值范围：0-16777214, 默认值：10

Returns:

(:obj:IsisNeighborConfig): ISIS Neighbor TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
Create Isis Neighbor Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02	
Create Isis Sr Binding Tlv
Arguments
Session
Lsp
** kwargs
Documentation
创建ISIS Binding TLV对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Lsp (:obj:IsisLspConfig): ISIS LSP对象, 类型为：object

Keyword Args:

EnableMt (bool): 使能多拓扑, 默认值：False

MtId (str): 多拓扑ID, 默认值：STANDARD, 取值范围：

STANDARD

IPV6_ROUTING

Flags (list): 标签, 默认值：['NOSHOW'], 取值范围：

NOSHOW

FBIT

MBIT

SBIT

DBIT

ABIT

Weight (int): 权重, 默认值：0, 取值范围：0-255

Range (int): 范围, 默认值：1, 取值范围：0-65535

Ipv4Version (bool): 默认值：True

Ipv4Prefix (str): IPv4前缀, 默认值："192.0.0.1"

Ipv4PrefixLength (int): IPv4前缀长度, 默认值：1, 取值范围：1-32

Ipv6Prefix (str): IPv6前缀, 默认值："2000::1

Ipv6PrefixLength (int): IPv6前缀长度, 默认值：64, 取值范围：1-128

Returns:

(:obj:IsisSrBindingTlv): ISIS Neighbor TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
Create Isis Binding Tlv	Session={Session}	Lsp=${LSP}	Ipv4Version=False
Create Isis Srv6 End Sid Sub Tlv
Arguments
Session
Location
** kwargs
Documentation
创建ISIS Capability Srms Preference Sub Tlv对象

Args:

Location (:obj:IsisSrv6LocatorTlv): ISIS Tlv对象, 类型为：object

Keyword Args:

Flags (list): 选择一个或多个包含在TLV中的标志位, 默认值：['UNKNOWN'], 取值范围：

UNKNOWN

UNUSED0

UNUSED1

UNUSED2

UNUSED3

UNUSED4

UNUSED5

UNUSED6

UNUSED7

EndpointFunc (str): 端点行为, 默认值：END_NO, 取值范围：

END_NO

END_PSP

END_USP

END_PSP_USP

END_X_NO

END_X_PSP

END_X_USP

END_X_PSP_USP

END_T_NO

END_T_PSP

END_T_USP

END_T_PSPS_USP

END_B6

END_B6_ENCAPS

END_BM

END_DX6

END_DX4

EDN_DT6

END_DT4

END_DT46

END_DX2

END_DX2V

END_DX2U

END_DX2M

END_S

END_B6_RED

END_B6_ENCAPS_RED

END_WITH_USD

END_PSP_USD

END_USP_USD

END_PSP_USP_USD

END_X_USD

END_X_PSP_USD

END_X_USP_USD

END_X_PSP_USP_USD

END_T_USD

END_T_PSP_USD

END_T_USP_USD

END_T_PSP_USP_USD

EnableCustom (bool): 使能自定义端点行为, 默认值：False

CustomFunc (int): 自定义端点行为, 默认值：0, 取值范围：0-65535

SID (str): 指定通告的SRv6 SID, 默认值："::1", 取值范围：IPv6地址

Returns:

(:obj:IsisSrv6EndSidSubTlv): ISIS Capability Srms Preference Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Location}	Create Isis Srv6 Location Tlv	Lsp=${LSP}	Algorithm=1
Create Isis Srv6 End Sid Sub Tlv	Session={Session}	Location=${Location}	
Create Isis Srv6 Location Tlv
Arguments
Session
Lsp
** kwargs
Documentation
创建ISIS Binding TLV对象

Args:

Session (:obj:IsisRouter): ISIS协议会话对象列表, 类型为：object

Lsp (:obj:IsisLspConfig): ISIS LSP对象, 类型为：object

Keyword Args:

MtId (str): 多拓扑ID, 默认值：STANDARD, 取值范围：

Metric (int): 指定度量值, 默认值：0, 取值范围：0-4294967295

Flags (list): 标签, 默认值：['UNKNOWN'], 取值范围：

UNKNOWN

D_BIT

A_BIT

UNUSED2

UNUSED3

UNUSED4

UNUSED5

UNUSED6

UNUSED7

Algorithm (int): Locator关联算法, 类型为：number, 取值范围：0-255, 默认值：0

NumLocator (int): Locator数量, 取值范围：0-4294967295, 默认值：1

LocatorSize (int): 定位器大小, 取值范围：1-128, 默认值：64

Locator (str): 定位器, 默认值："aaaa:1:1:1::", 取值范围：IPv6地址

LocatorStep (int): 定位器步长, 默认值：1, 取值范围：0-65535

Returns:

(:obj:IsisSrv6LocatorTlv): ISIS Srv6 Location TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
Create Isis Srv6 Location Tlv	Session={Session}	Lsp=${LSP}	Algorithm=1
Create Isis Tlv Bier Mpls Sub Sub Tlv
Arguments
Bier
** kwargs
Documentation
创建ISIS Tlv Bier Mpls Sub Sub Tlv对象

Args:

Bier (:obj:IsisBierSubTlv): ISIS Bierv6 Sub Tlv对象, 类型为：object

Keyword Args:

MaxSI (int): 指定最大Set ID, 默认值：1, 取值范围：0-255

LabelorBiftId (int): 指定标签范围中的起始标签值, 默认值：100, 取值范围：0-4294967295

BSLength (int): 指定本地比特串的长度, 默认值：1, 取值范围：0-15

Returns:

(:obj:IsisBierMplsSubTlv): ISIS Prefix Sid Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Ipv6}	Create Isis Ipv6 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Tlv Bier Sub Tlv	Tlv=${Ipv6}		
Create Isis Tlv Bier Mpls Sub Sub Tlv	Bier=${Ipv6}		
Create Isis Tlv Bier Sub Tlv
Arguments
Tlv
** kwargs
Documentation
创建ISIS Tlv Bier Sub Tlv对象

Args:

Tlv (:obj:IsisIpv4TlvConfig): ISIS Tlv对象, 类型为：object

Keyword Args:

BFRId (int): 指定BFR（Bit Forwarding Router，比特转发路由器）ID, 取值范围：1-65535, 默认值：1

SubDomainId (int): 指定BIER子域ID, 取值范围：0-255, 默认值：1

IgpAlgorithm (int): IGP算法, 取值范围：0-255, 默认值：0

BierAlgorithm (int): BIER算法, 取值范围：0-255, 默认值：0

Returns:

(:obj:IsisBierSubTlv): ISIS Prefix Sid Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Ipv4}	Create Isis Ipv4 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Tlv Bier Sub Tlv	Tlv=${Ipv4}		
Create Isis Tlv Bierv6 Bift Id Sub Tlv
Arguments
Bier
** kwargs
Documentation
创建ISIS Tlv Bierv6 Bift Id Sub Tlv对象

Args:

Bier (:obj:IsisIpv6TlvConfig): ISIS Tlv对象, 类型为：object

Keyword Args:

Type(int): 指定Type字段值, 默认值：7, 取值范围：0-255

MPRA (str): 指定MPRA地址, 默认值：'::1', 取值范围：有效IPv6地址

Returns:

(:obj:IsisBierBiftIdSubTlv): ISIS Prefix Sid Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Ipv6}	Create Isis Ipv6 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Tlv Bierv6 Bift Id Sub Tlv	Tlv=${Ipv6}		
Create Isis Tlv Bierv6 Sub Sub Tlv
Arguments
Bier
** kwargs
Documentation
创建ISIS Tlv Bierv6 Sub Sub Tlv对象

Args:

Bier (:obj:IsisBierSubTlv): ISIS Bierv6 Sub Tlv对象, 类型为：object

Keyword Args:

MaxSI (int): 指定最大Set ID, 默认值：1, 取值范围：0-255

LabelorBiftId (int): 指定标签范围中的起始标签值, 默认值：100, 取值范围：0-4294967295

BSLength (int): 指定本地比特串的长度, 默认值：1, 取值范围：0-15

Returns:

(:obj:IsisBierMplsSubTlv): ISIS Prefix Sid Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Ipv6}	Create Isis Ipv6 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Tlv Bier Sub Tlv	Tlv=${Ipv6}		
Create Isis Tlv Bierv6 Sub Sub Tlv	Bier=${Ipv6}		
Create Isis Tlv End Bier Sub Tlv
Arguments
Bier
** kwargs
Documentation
创建ISIS Tlv End Bier Sub Tlv对象

Args:

Bier (:obj:IsisIpv6TlvConfig): ISIS Tlv对象, 类型为：object

Keyword Args:

Type (int): 指定Type字段值。取值范围：0-255, 默认值：3

EndBierAddr (str): 指定End.BIER SID, 默认值："::1", 取值范围：有效IPv6地址

Returns:

(:obj:IsisEndBierSubTlv): ISIS Prefix Sid Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Ipv6}	Create Isis Ipv6 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Tlv End Bier Sub Tlv	Tlv=${Ipv6}		
Create Isis Tlv Flex Algorithm Prefix Metric Sub Tlv
Arguments
Tlv
** kwargs
Documentation
创建ISIS Tlv Flex Algorithm Prefix Metric Sid Sub Tlv对象

Args:

Tlv (:obj:IsisIpv4TlvConfig): ISIS Tlv对象, 类型为：object

Keyword Args:

Algorithm (int): Locator关联算法, 类型为：number, 取值范围：128-255, 默认值：128

Metric (int): 度量值, 类型为：number, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:IsisFlexAlgoPrefixMetricSubTlv): ISIS Prefix Sid Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Ipv4}	Create Isis Ipv4 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Tlv Flex Algorithm Prefix Metric Sub Tlv	Tlv=${Ipv4}		
Create Isis Tlv Prefix Sid Sub Tlv
Arguments
Session
Tlv
** kwargs
Documentation
创建ISIS Tlv Prefix Sid Sub Tlv对象

Args:

Tlv (:obj:IsisIpv4TlvConfig): ISIS Tlv对象, 类型为：object

Keyword Args:

Flags (list): 选择一个或多个包含在TLV中的标志位, 默认值：['NOSHOW', 'NOPHP'], 取值范围：

NOSHOW

ADVERTISEMENT

NODESID

NOPHP

EXPLICIT

VALUE

LOCAL

Sid (int): SID/Label, 默认值：0, 取值范围：0-4294967295

Algorithm (int): 指定计算到其他节点/前缀的可达信息的算法, 指定SID关联的算法, 默认值：0, 取值范围：0-255

PrefixSidStep (int): 默认值：1

Returns:

(:obj:IsisSrPrefixSidSubTlv): ISIS Prefix Sid Sub TLV对象

Examples: .. code:: RobotFramework

${Session}	Create Isis	Port=${Port}	
${LSP}	Create Isis Lsp	Session=${Session}	SystemId=00:00:00:00:00:02
${Ipv4}	Create Isis Ipv4 Tlv	Lsp=${LSP}	SystemId=00:00:00:00:00:02
Create Isis Tlv Prefix Sid Sub Tlv	Tlv=${Ipv4}		
Create L2tp
Arguments
Port
** kwargs
Documentation
创建L2tp协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): L2tp协会话名称, 类型为：string

Enable (bool): 使能L2tp协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

EmulationMode (str): L2TP角色, 默认值：LAC, 取值范围：

LAC

LNS

TunnelCountPerNode (int): 每LAC/LNS隧道数, 取值范围：1-32768, 默认值：1

SessionCountPerTunnel (int): 每隧道会话数, 取值范围：0-65535, 默认值：0

TunnelStartingId (int): 隧道起始ID, 取值范围：1-65535, 默认值：1

SessionStartingId (int): 会话起始ID, 取值范围：1-65535, 默认值：1

UdpSourcePort (int): UDP源端口, 取值范围：1-65535, 默认值：1701

UdpChecksumEnabled (bool): 使能UDP校验和, 默认值：True

RetryTunnelCreationEnabled (bool): 使能隧道重试, 默认值：False

TunnelCreationTimeout (int): 隧道建立超时(secs), 取值范围：1-65535, 默认值：5

MaxTunnelCreationTimes (int): 隧道建立最大尝试次数, 取值范围：1-65535, 默认值：5

HostName (str): 主机名, 取值范围：string length in [1,255], 默认值：xinertel

EnableAuthentication (bool): 使能认证, 默认值：True

IncomingTunnelPassword (str): Incoming隧道密码, 取值范围：string length in [1,255], 默认值：xinertel

OutgoingTunnelPassword (str): Outgoing隧道密码, 取值范围：string length in [1,255], 默认值：xinertel

HelloEnabled (bool): 使能Hello, 默认值：False

HelloInterval (int): Hello间隔(secs), 取值范围：1-255, 默认值：60

TxBitRate (int): 发送bps速率(bits/sec), 取值范围：1-65535, 默认值：56000

BearerCapabilities (str): 负载能力, 默认值：ANALOG, 取值范围：

DIGITAL

ANALOG

BOTH

BearerType (str): 负载类型, 默认值：ANALOG, 取值范围：

DIGITAL

ANALOG

FrameCapabilities (str): 帧能力, 默认值：SYNC, 取值范围：

SYNC

ASYNC

BOTH

FrameType (str): 帧类型, 默认值：SYNC, 取值范围：

SYNC

ASYNC

CallingNumberEnabled (bool): 使能Calling Number, 默认值：False

CallingNumber (str): 隧道的Calling Number, 默认值：xinertel

RxWindowSize (int): 接收窗口大小, 取值范围：1-65535, 默认值：4

UseGatewayAsRemoteIp (bool): 使用网关作为远端地址, 默认值：True

RemoteIpv4Address (str): 远端IPv4地址, 取值范围：IPv4地址, 默认值：2.1.1.1

RemoteIpv4AddressStep (str): 远端IPv4地址跳变, 取值范围：IPv4地址, 默认值：0.0.0.1

RemoteIpv6Address (str): 远端IPv6地址, 取值范围：IPv6地址, 默认值：2000::1

RemoteIpv6AddressStep (str): 远端IPv6地址跳变, 取值范围：IPv6地址, 默认值：::1

LcpProxyMode (str): LCP代理模式, 默认值：NONE, 取值范围：

NONE

LCP

LCP_AUTH

ForceLcpRenegotiation (bool): 强制LCP重协商, 默认值：False

Ipv4TosValue (hex int): IPv4 TOS值, 取值范围：1-65535, 默认值：0xc0

Ipv6TrafficClassValue (hex int): IPv6 Traffic Class Value, 取值范围：1-65535, 默认值：0x0

HideFramingCapabilities (bool): 默认值：False

HideBearerCapabilities (bool): 默认值：False

HideAssignedTunnelId (bool): 默认值：False

HideChallenge (bool): 默认值：False

HideChallengeResponse (bool): 默认值：False

HideAssignedSessionId (bool): 默认值：False

HideCallSerialNumber (bool): 默认值：False

HideFramingType (bool): 默认值：False

HideCallingNumber (bool): 默认值：False

HideTxConnectSpeed (bool): 默认值：False

HideLastSentLcpConfReq (bool): 默认值：False

HideLastReceivedLcpConfReq (bool): 默认值：False

HideProxyAuthenType (bool): 默认值：False

HideProxyAuthenName (bool): 默认值：False

HideProxyAuthenChallenge (bool): 默认值：False

HideProxyAuthenId (bool): 默认值：False

HideProxyAuthenResponse (bool): 默认值：False

Returns:

(:obj:L2tp): L2tp协议会话对, 类型：object

Examples: .. code:: RobotFramework

Create L2tp	Port=${Port}
Create Ldp
Arguments
Port
** kwargs
Documentation
创建LDP协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): LDP协会话名称, 类型为：string

Enable (bool): 使能LDP协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

HelloType (str): Hello类型, 类型为：string, 默认值：DIRECT, 取值范围:

DIRECT

TARGETED

DIRECT_TARGETED

LabelAdvertType (str): 标签分配方式, 类型为：string, 默认值：DIRECT, 取值范围:

DU

DOD

TransportMode (str): Transport Address TLV模式, 类型为：string, 默认值：TESTER_IP, 取值范围:

TESTER_IP

ROUTER_ID

NONE

DutIpv4Address (int): DUT IPv4地址, 类型为：number, 型为：string, 默认值：2.1.1.1, 取值范围: IPv4地址

DirectHelloInterval (int): 直连Hello发送间隔(sec), 类型为：number, 默认值：5, 取值范围：1-21845

TargetedHelloInterval (int): 远端Hello发送间隔(sec), 类型为：number, 默认值：15, 取值范围：1-21845

KeepAliveInterval (int): 保活间隔(sec), 类型为：number, 默认值：60, 取值范围：1-21845

LabelReqRetryCount (int): 标签请求间隔(sec), 类型为：number, 默认值：10, 取值范围：1-65535

LabelReqRetryInterval (int): 标签请求重试次数, 类型为：number, 默认值：60, 取值范围：1-65535

Authentication (str): 鉴权类型, 类型为：string, 默认值：DIRECT, 取值范围:

NONE

MD5

Password (str): 密码, 类型为：string, 默认值：xinertel

EgressLabel (str): 出标签方式, 类型为：string, 默认值：DIRECT, 取值范围:

NEXT_AVAILABLE

IMPLICIT

EXPLICIT

MinLabel (int): 最小标签值, 类型为：number, 默认值：16, 取值范围：0-1048575

EnableLspResult (bool): LSP统计使能, 类型为：bool, 取值范围：True或False, 默认值： False

EnablePseudowireLspResult (bool): 伪线LSP统计使能, 类型为：bool, 取值范围：True或False, 默认值： False

LspBindMode (str): LSP绑定模式, 类型为：string, 默认值：TX_RX, 取值范围:

TX_RX

TX

RX

NONE

VcLspBindMode (str): 虚拟电路LSP绑定模式, 类型为：string, 默认值：TX_RX, 取值范围:

TX_RX

TX

RX

NONE

GeneralizedLspBindMode (str): 通用伪线LSP绑定模式, 类型为：string, 默认值：TX_RX, 取值范围:

TX_RX

TX

RX

NONE

Returns:

(:obj:Ldp): LDP协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Ldp	Port=${Port}
Create Ldp Fec 128
Arguments
Session
** kwargs
Documentation
创建LDP FEC 128对象

Args:

Session (:obj:Ldp): LDP协议会话对象, 类型为：object

Keyword Args:

Name (str): LDP FEC 128对象名称, 类型为：string

Enable (bool): 使能LDP FEC 128, 类型为：bool, 取值范围：True或False, 默认值：True

ControlWordEnable (bool): 控制字使能, 类型为：bool, 取值范围：True或False, 默认值：False

Encapsulation (str): 封装类型(hex), 类型为：string, 默认值：PREFIX_FEC, 取值范围:

ETHERNET_TAGGED_MODE

ETHERNET

CEM

GroupId (int): 组ID, 类型为：number, 默认值：1, 取值范围：1-65535

InterfaceMtu (int): 接口MTU,类型为：number, 默认值：1500, 取值范围: 1-65535

IncludePwStatusTlv (bool): 伪线状态码使能, 类型为：bool, 取值范围：True或False, 默认值：False

PwStatusCode (list): 伪线状态码, 类型为：list, 默认值：PW_NOT_FORWARDING, 取值范围:

PW_NOT_FORWARDING

LOCAL_AC_RX_FAULT

LOCAL_AC_TX_FAULT

LOCAL_PSN_PW_RX_FAULT

LOCAL_PSN_PW_TX_FAULT

UseCustomPwStatusTlv (bool): 自定义伪线状态码使能, 类型为：bool, 取值范围：True或False, 默认值：False

CustomPwStatusCode (int): 自定义伪线状态码, 类型为：number, 默认值：0, 取值范围: 0-4294967295

VcCount (int): VC数量, 类型为：number, 默认值：1, 取值范围: 0-4294967295

StartVcId (int): 起始VC, 类型为：number, 默认值：1, 取值范围: 0-4294967295

VcIdStep (int): VC跳变步长, 类型为：number, 默认值：1, 取值范围: 0-4294967295

Returns:

(:obj:LdpFec128LspConfig): LDP FEC 128对象列表, 类型: list

Examples: .. code:: RobotFramework

${Session}	Create Ldp	Port=${Port}
Edit Ldp	Session=${Session}	HelloType=DIRECT_TARGETED
${Ingress}	Create Ldp Fec 128	Session=${Session}
Create Ldp Fec 129
Arguments
Session
** kwargs
Documentation
创建LDP FEC 129对象

Args:

Session (:obj:Ldp): LDP协议会话对象, 类型为：object

Keyword Args:

Name (str): LDP FEC 129对象名称, 类型为：string

Enable (bool): 使能LDP FEC 129, 类型为：bool, 取值范围：True或False, 默认值：True

ControlWordEnable (bool): 控制字使能, 类型为：bool, 取值范围：True或False, 默认值：False

Encapsulation (str): 封装类型(hex), 类型为：string, 默认值：PREFIX_FEC, 取值范围:

ETHERNET_TAGGED_MODE

ETHERNET

CEM

GroupId (int): 组ID, 类型为：number, 默认值：1, 取值范围：1-65535

InterfaceMtu (int): 接口MTU,类型为：number, 默认值：1500, 取值范围: 1-65535

IncludePwStatusTlv (bool): 伪线状态码使能, 类型为：bool, 取值范围：True或False, 默认值：False

PwStatusCode (list): 伪线状态码, 类型为：list, 默认值：PW_NOT_FORWARDING, 取值范围:

PW_NOT_FORWARDING

LOCAL_AC_RX_FAULT

LOCAL_AC_TX_FAULT

LOCAL_PSN_PW_RX_FAULT

LOCAL_PSN_PW_TX_FAULT

UseCustomPwStatusTlv (bool): 自定义伪线状态码使能, 类型为：bool, 取值范围：True或False, 默认值：False

CustomPwStatusCode (int): 自定义伪线状态码, 类型为：number, 默认值：0, 取值范围: 0-4294967295

PwCount (int): PW数量, 类型为：number, 默认值：1, 取值范围: 0-65535

Agi (str): 起始Agi, 型为：string, 默认值：100:1, 取值范围: IPv6地址

AgiStep (str): Agi跳变步长, 型为：string, 默认值：0:1, 取值范围: IPv6地址

Saii (str): 起始Saii, 型为：string, 默认值：10.0.0.1, 取值范围: IPv4地址

SaiiStep (str): Saii跳变步长, 型为：string, 默认值：0.0.0.1, 取值范围: IPv4地址

Taii (str): 起始Taii, 型为：string, 默认值：192.0.0.1, 取值范围: IPv4地址

TaiiStep (str): Taii跳变步长, 型为：string, 默认值：0.0.0.1, 取值范围: IPv4地址

Returns:

(:obj:LdpFec129LspConfig): LDP FEC 129对象列表, 类型: list

Examples: .. code:: RobotFramework

${Session}	Create Ldp	Port=${Port}
Edit Ldp	Session=${Session}	HelloType=DIRECT_TARGETED
${Ingress}	Create Ldp Fec 129	Session=${Session}
Create Ldp Ipv4 Egress
Arguments
Session
** kwargs
Documentation
创建LDP IPv4 Egress对象

Args:

Session (:obj:Ldp): LDP协议会话对象, 类型为：object

Keyword Args:

Name (str): LDP IPv4 Egress对象名称, 类型为：string

Enable (bool): 使能LDP IPv4 Egress, 类型为：bool, 取值范围：True或False, 默认值：True

FecType (str): Fec类型, 类型为：string, 默认值：PREFIX_FEC, 取值范围:

PREFIX_FEC

HOST_FEC

LspCount (int): Lsp数量, 类型为：number, 默认值：1, 取值范围：1-65535

StartIpv4Prefix: Lsp IPv4前缀地址, 型为：string, 默认值：192.0.1.0, 取值范围: IPv4地址

PrefixLength (int): Lsp IPv4前缀长度, 类型为：number, 默认值：24, 取值范围: 1-32

PrefixStep (int): Lsp IPv4前缀跳变步长, 类型为：number, 默认值：1, 取值范围: 1-65535

Ipv4PrefixStep: Lsp IPv4前缀地址跳变步长, 型为：string, 默认值：0.0.1.0, 取值范围: IPv4地址

Returns:

(:obj:LdpIpv4EgressLspConfig): LDP IPv4 Egress对象列表, 类型: list

Examples: .. code:: RobotFramework

${Session}	Create Ldp	Port=${Port}
Edit Ldp	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Ldp Ipv4 Egress	Session=${Session}
Create Ldp Ipv4 Ingress
Arguments
Session
** kwargs
Documentation
创建LDP IPv4 Ingress对象

Args:

Session (:obj:Ldp): LDP协议会话对象, 类型为：object

Keyword Args:

Name (str): LDP IPv4 Ingress对象名称, 类型为：string

Enable (bool): 使能LDP IPv4 Ingress, 类型为：bool, 取值范围：True或False, 默认值：True

FecType (str): Fec类型, 类型为：string, 默认值：PREFIX_FEC, 取值范围:

PREFIX_FEC

HOST_FEC

LspCount (int): Lsp数量, 类型为：number, 默认值：1, 取值范围：1-65535

StartIpv4Prefix: Lsp IPv4前缀地址, 型为：string, 默认值：192.0.1.0, 取值范围: IPv4地址

PrefixLength (int): Lsp IPv4前缀长度, 类型为：number, 默认值：24, 取值范围: 1-32

PrefixStep (int): Lsp IPv4前缀跳变步长, 类型为：number, 默认值：1, 取值范围: 1-65535

Ipv4PrefixStep: Lsp IPv4前缀地址跳变步长, 型为：string, 默认值：0.0.1.0, 取值范围: IPv4地址

Returns:

(:obj:LdpIpv4IngressLspConfig): LDP IPv4 Ingress对象列表, 类型: list

Examples: .. code:: RobotFramework

${Session}	Create Ldp	Port=${Port}
Edit Ldp	Session=${Session}	HelloType=DIRECT_TARGETED
${Ingress}	Create Ldp Ipv4 Ingress	Session=${Session}
Create Lsp Ping
Arguments
Port
** kwargs
Documentation
创建Lsp Ping会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): Lsp Ping会话名称, 类型为：string

Enable (bool): 使能Lsp Ping会话, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:LspPing): Lsp Ping会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Lsp Ping	Port=${Port}
Create Lsp Ping Echo Request
Arguments
Sessions
** kwargs
Documentation
创建Lsp Ping Echo Request对象

Args：

Session (:obj:LspPing): Lsp Ping会话对象, 类型为：object / list

Keyword Args:

OperationMode (list): Operation模式, 默认值：['PING'], 取值范围：

PING

TRACE

ReplyMode (str): Echo Reply模式, 默认值：REPLYVIAUDP, 取值范围：

NOTREPLY

REPLYVIAUDP

PingInterval (int): Ping发送测试包的时间间隔（秒）, 默认值：4, 取值范围：1-65535

PingTimeOut (int): Ping探测超时时间（秒）, 默认值：2, 取值范围：1-60

TraceInterval (int): Trace发送测试包的时间间隔（秒）, 默认值：120, 取值范围：1-65535

TraceTimeOut (int): Trace探测超时时间（秒）, 默认值：2, 取值范围：1-60

InnerLabel (str): 标签, 默认值：NONE, 取值范围：

NONE

LDPIPv4

VPNIPv4

SEGMENT_ROUTING

OuterLabel (str): 标签, 默认值：NONE, 取值范围：

NONE

LDPIPv4

VPNIPv4

SEGMENT_ROUTING

TimeToLive (int): 生存时间, 默认值：255, 取值范围：1-255

ExpBits (int): 实验比特位的值, 默认值：0, 取值范围：0-7

PadMode (str): 填充模式, 默认值：WITHOUT_PAD, 取值范围：

WITHOUT_PAD

DROP_PAD

COPY_PAD

Data (int): 填充数据, 默认值：'', 取值范围：0-255

DesIpv4Addr (str): 目的地址, 默认值："127.0.0.1"，取值范围：有效的ipv4地址

ValidateFecStack (bool): 校验FEC Stack, 默认值：False, 取值范围：True或False

DownstreamMappingTlvType (str): Downstream Mapping TLV类型, 默认值：DOWNSTREAM_DETAILED_MAPPING_TLV, 取值范围：

DOWNSTREAM_MAPPING_TLV

DOWNSTREAM_DETAILED_MAPPING_TLV

Returns:

(:obj:LspPingEchoRequestConfig): Lsp Ping Echo Request对象, 类型：object / list

Examples: .. code:: RobotFramework

${LspPing}	Create Lsp Ping	Port=${Port}
Create Lsp Ping Echo Request	Sessions=${LspPing}	
Create Lsp Ping Fec Ldp Ipv4
Arguments
EchoRequests
** kwargs
Documentation
创建Lsp Ping Fec Ldp Ipv4对象

Args：

EchoRequests (:obj:LspPingEchoRequestConfig): Lsp Ping Echo Request对象, 类型为：object / list

Keyword Args:

Count (int): 数量, 默认值：1, 取值范围：1-65535

StartAddr (str): IPv4地址, 默认值："172.0.0.1"，取值范围：有效的ipv4地址

PrefixLength (int): 前缀长度, 默认值：24, 取值范围：1-32

Step (int): 步长, 默认值：1, 取值范围：1-255

Returns:

(:obj:LspPingFecLdpIpv4PrefixConfig): Lsp Ping Fec Ldp Ipv4对象, 类型：object / list

Examples: .. code:: RobotFramework

${LspPing}	Create Lsp Ping	Port=${Port}
${EchoRequest}	Create Lsp Ping Echo Request	Sessions=${LspPing}
Create Lsp Ping Fec Ldp Ipv4	EchoRequests=${EchoRequest}	
Create Lsp Ping Fec Segment Routing
Arguments
EchoRequests
** kwargs
Documentation
创建Lsp Ping Fec Segment Routing对象

Args：

EchoRequests (:obj:LspPingEchoRequestConfig): Lsp Ping Echo Request对象, 类型为：object / list

Keyword Args:

IgpProtocol (str): FEC校验使用的IGP协议, 默认值：ISIS, 取值范围：

OSPF

ISIS

PrefixCount (int): 前缀数量, 默认值：1, 取值范围：1-4294967295

PrefixAddrIncrement (int): 地址步长, 默认值：1, 取值范围：1-4294967295

Returns:

(:obj:LspPingFecSrConfig): Lsp Ping Fec Segment Routing对象, 类型：object / list

Examples: .. code:: RobotFramework

${LspPing}	Create Lsp Ping	Port=${Port}
${EchoRequest}	Create Lsp Ping Echo Request	Sessions=${LspPing}
Create Lsp Ping Fec Segment Routing	EchoRequests=${EchoRequest}	
Create Lsp Ping Fec Sr Adjacency
Arguments
Srs
** kwargs
Documentation
创建Lsp Ping Fec Sr Adjacency对象

Args：

Srs (:obj:LspPingFecSrConfig): Lsp Ping Fec Segment Routing对象, 类型为：object / list

Keyword Args:

IsisSystemId (str): ISIS系统ID, 默认值："00:00:94:00:00:01"，取值范围：有效的mac地址

IsisLanSystemId (str): ISIS LAN系统ID, 默认值："00:00:00:00:00:00"，取值范围：有效的mac地址

IsisNeighborId (str): ISIS邻居ID, 默认值："00:00:94:00:00:01"，取值范围：有效的mac地址

IsisNodeId (int): ISIS节点ID, 默认值：0, 取值范围：uint8

OspfLinkType (str): OSPF链路类型, 默认值：P2P, 取值范围：

P2P

TRANSITNETWORK

STUBNETWORK

VIRTUALLINK

OspfLinkId (str): OSPF链路ID, 默认值："0.0.0.0"，取值范围：有效的ipv4地址

OspfLinkData (str): OSPF链路数据, 默认值："0.0.0.0"，取值范围：有效的ipv4地址

LocalRouterId (str): 本地路由器ID, 默认值："192.168.1.1"，取值范围：有效的ipv4地址

RemoteRouterId (str): 远端路由器ID, 默认值："192.168.1.1"，取值范围：有效的ipv4地址

LocalInterfaceId (str): 本地接口ID, 默认值："0.0.0.0"，取值范围：有效的ipv4地址

RemoteInterfaceId (str): 远端接口ID, 默认值："0.0.0.0"，取值范围：有效的ipv4地址

Returns:

(:obj:LspPingFecSrDetailConfig): Lsp Ping Fec Sr Detail对象, 类型：object / list

Examples: .. code:: RobotFramework

${LspPing}	Create Lsp Ping	Port=${Port}
${EchoRequest}	Create Lsp Ping Echo Request	Sessions=${LspPing}
${Sr}	Create Lsp Ping Fec Segment Routing	EchoRequests=${EchoRequest}
Create Lsp Ping Fec Sr Ajacency	Srs=${Sr}	
Create Lsp Ping Fec Sr Prefix
Arguments
Srs
** kwargs
Documentation
创建Lsp Ping Fec Sr Prefix对象

Args：

Srs (:obj:LspPingFecSrConfig): Lsp Ping Fec Segment Routing对象, 类型为：object / list

Keyword Args:

Prefix (str): 前缀地址, 默认值："192.0.0.1"，取值范围：有效的ipv4地址

Length (int): 前缀地址长度, 默认值：24, 取值范围：1-32

Algorithm (int): 算法, 默认值：0, 取值范围：uint8

Returns:

(:obj:LspPingFecSrDetailConfig): Lsp Ping Fec Sr Detail对象, 类型：object / list

Examples: .. code:: RobotFramework

${LspPing}	Create Lsp Ping	Port=${Port}
${EchoRequest}	Create Lsp Ping Echo Request	Sessions=${LspPing}
${Sr}	Create Lsp Ping Fec Segment Routing	EchoRequests=${EchoRequest}
Create Lsp Ping Fec Sr Prefix	Srs=${Sr}	
Create Lsp Ping Fec Vpn Ipv4
Arguments
EchoRequests
** kwargs
Documentation
创建Lsp Ping Fec Vpn Ipv4对象

Args：

EchoRequests (:obj:LspPingEchoRequestConfig): Lsp Ping Echo Request对象, 类型为：object / list

Keyword Args:

Count (int): 数量, 默认值：1, 取值范围：1-65535

StartAddr (str): IPv4地址, 默认值："172.0.0.1"，取值范围：有效的ipv4地址

PrefixLength (int): 前缀长度, 默认值：24, 取值范围：1-32

Step (int): 步长, 默认值：1, 取值范围：1-255

RouteDistinguisher (str): 路由标识, 默认值："100:1", 取值范围：匹配格式"uint16:uint32 | ipv4:uint16 | uint32:uint16 | uint16.uint16:uint16"

Returns:

(:obj:LspPingFecVPNIpv4PrefixConfig): Lsp Ping Fec Vpn Ipv4对象, 类型：object / list

Examples: .. code:: RobotFramework

${LspPing}	Create Lsp Ping	Port=${Port}
${EchoRequest}	Create Lsp Ping Echo Request	Sessions=${LspPing}
Create Lsp Ping Fec Vpn Ipv4	EchoRequests=${EchoRequest}	
Create Memberships
Arguments
Session
** kwargs
Documentation
创建组播协议和组播组绑定关系对象

Args:

Session (:obj:Mld, Igmp): IGMP/MLD协会话对象, 类型为：object

Keyword Args:

DeviceGroupMapping (str): 主机和组播组映射关系, 类型为：str, 默认值：MANYTOMANY, 取值范围：

MANYTOMANY

ONETOONE

ROUNDROBIN

SourceFilterMode (str): 源地址过滤模式, 类型为：str, 默认值：EXCLUDE, 取值范围：

INCLUDE

EXCLUDE

UserDefinedSources (bool): 自定义源地址, 类型为：bool, 取值范围：True或False, 默认值：False

SpecifySourcesAsList (bool): 配置离散源地址, 类型为：bool, 取值范围：True或False, 默认值：False

SourceAddressList (list): 离散源地址列表, 类型为：list, 取值范围：ipv4 or ipv6 string list

NumberOfSources (int): 组播组地址掩码, 类型为：number, 取值范围：0-16777215 默认值：1

StartingSourceIp (str): 组播组起始源地址, 类型为：string, 取值范围：ipv4 or ipv6 string list，, 默认值ipv4: 192.0.1.0 , ipv6: 2000::1

PrefixLength (int): 组跳变位, 类型为：number, 取值范围：ipv4: 1-32 默认值：32, ipv6: 1-128 默认值：128

Increment (int): 跳变步长, 类型为：number, 取值范围：0-16777215 默认值：1

Returns:

(:obj:MldMembershipsConfig): 组播协议和组播组绑定关系对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Mld	Port=${Port}	
Create Memberships	Session=${Session}	Start=225.0.1.1	DeviceGroupMapping=ONETOONE
Create Mld
Arguments
Port
** kwargs
Documentation
创建MLD协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): MLD协会话名称, 类型为：string

Enable (bool): 使能MLD协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

Version (str): 版本, 类型为：string, 默认值：MLDV1, 支持版本：

MLDV1

MLDV2

PackReports (bool): 合并报告报文, 类型为：bool, 取值范围：True或False, 默认值：False

InitialJoin (bool): 单个初始报文加入组, 类型为：bool, 取值范围：True或False, 默认值：False

RobustJoin (bool): 多个初始报文加入组, 类型为：bool, 取值范围：True或False, 默认值：False

RobustnessVariable (int): Robust值, 类型为：number, 取值范围：2-255, 默认值：2

UnsolicitedReportInterval (int): 发送初始报文的时间间隔 (秒), 类型为：number, 取值范围：0-65535, 默认值：10

ForceLeave (bool): 强制发送Leave报文, 类型为：bool, 取值范围：True或False, 默认值：True

TrafficClass (hex int): IP头的Traffic Class值, 型为：string, 取值范围：0x0-0xff, 默认值：0xc0

Returns:

(:obj:Mld): MLD协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Mld	Port=${Port}	Version=MLDV2
Create Mld Querier
Arguments
Port
** kwargs
Documentation
创建MLD Querier协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): MLD Querier协会话名称, 类型为：string

Enable (bool): 使能MLD Querier协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

Version (str): 版本, 类型为：string, 默认值：MLDV1, 支持版本：

MLDV1

MLDV2

RobustnessVariable (int): 健壮系数, 取值范围：2-255, 默认值: 2

Interval (int): 查询时间间隔（秒）, 取值范围：0-4294967295, 默认值: 125

QueryResponseInterval (int): 查询响应时间间隔（毫秒）, 取值范围：0-4294967295, 默认值: 10000

StartupQueryCount (int): 初始查询报文个数, 取值范围：1-255, 默认值：2

LastMemberQueryInterval (int): 最后成员查询时间间隔（毫秒）, 取值范围：0-4294967295, 默认值: 1000

LastMemberQueryCount (bool): 最后成员查询次数, 取值范围：0-255, 默认值: 2

IPv6TrafficClassValue (str): 设置IPv6头TrafficClass值, 取值范围：0x0-0xff, 默认值: 0x0

Returns:

(:obj:MldQuerier): MLD协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Mld Querier| Port=${Port}	Version=MLDV3
Create Mpls Wizard
Arguments
Type
Documentation
测试仪表创建MPLS向导

Args:

Type (str): mpls向导类型, 支持: mpls_ip_vpn mpls_6vpe ldp_vpls

Returns:

bool：布尔值 (范围：True / False)

Examples: ::

Create Mpls Wizard	Type=mpls_ip_vpn
Create Multicast Group
Arguments
Version
=
IPv4
** kwargs
Documentation
创建全局组播组对象

Args:

Version (str): 组播组IP版本，类型string, 支持ipv4和ipv6

Keyword Args:

Count (int): 组播组数量, 类型为：number, 取值范围：0-65535, 默认值：1

Mode (str): 组播组地址模式, 类型为：string, 默认值：RANGE, 取值范围：

RANGE

LIST

RFC_4814

Start (str): 组播组地址起始值, 类型为：ipv4/ipv6 string, 默认值：225.0.0.1或ff1e::1

Number (int): 组播组地址数量, 类型为：number, 取值范围：1-268435456, 默认值：1

Increment (int): 组播组地址步长, 类型为：number, 取值范围：1-268435456, 默认值：1

Prefix (int): 组播组地址掩码, 类型为：number, 取值范围：ipv4: 1-32 默认值：32, ipv6: 1-128 默认值：128

Returns:

(:obj:MldSelectMulticastGroupCommand): 全局组播组对象, 类型：object

Examples: .. code:: RobotFramework

Create Multicast Group	Version=IPV4	Start=225.0.1.1	Number=20
Create Ospf
Arguments
Port
** kwargs
Documentation
创建OSPFv2协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): OSPFv2协会话名称, 类型为：string

Enable (bool): 使能OSPFv2协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

AreaId (str): 区域ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

EnableBfd (bool): 使能BFD, 类型为：bool, 取值范围：True或False, 默认值：False

NetworkType (str): 网络类型, 类型为：string, 取值范围：Broadcast或P2P, 默认值：Broadcast

Priority (int): 路由器优先级, 类型为：number, 取值范围：0-255, 默认值：0

Cost (int): 接口开销, 类型为：number, 取值范围：1-65535, 默认值：10

AuthenticationType (str): 类型为：string, 取值范围：None Simple或MD5, 默认值：None

Password (str): 密码, 类型为：string, 默认值：Xinertel

Md5KeyId (int): MD5密钥, 类型为：number, 取值范围：0-255, 默认值：1

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

EnableOspfv2Mtu (bool): 使能OSPF MTU, 类型为：bool, 取值范围：True或False, 默认值：True

EnableGracefulRestart (bool): 使能平滑重启, 类型为：bool, 取值范围：True或False, 默认值：False

GracefulRestartReason (str): 平滑重启原因, 类型为：string, 默认值：UNKNOWN,支持的原因：

UNKNOWN

SOFTWARE

RELOADORUPGRADE

SWITCH

EnableViewRoutes (bool): 使能查看路由, 类型为：bool, 取值范围：True或False, 默认值：False

HelloInterval (int): Hello包间隔(秒), 类型为：number, 取值范围：0-65535, 默认值：10

RouterDeadInterval (int): 路由器失效间隔(秒), 类型为：number, 取值范围：0-4294967295, 默认值：40

LsaRetransInterval (int): LSA重传间隔(秒), 类型为：number, 取值范围：0-4294967295, 默认值：5

LsaRefreshTime (int): LSA刷新间隔(秒), 类型为：number, 取值范围：1-1800, 默认值：1800

EnableSrManagement (bool): 启用SR, 类型为：bool, 取值范围：True或False, 默认值： False

Returns:

(:obj:OspfRouter): OSPFv2协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Ospf	Port=${Port}
Create Ospf Adj Sid Sub Tlv
Arguments
Session
ExtendedLinkTlv
** kwargs
Documentation
创建OSPFv2 Adj Sid Sub Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

ExtendedLinkTlv (:obj:Ospfv2ExtendedLinkTlvConfig): OSPFv2 Extended Link Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Adj Sid Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Flags (list): 选项, 类型为：list, 默认值： ['ValueIndexFlag', 'LocalGlobalFlag', 'NONE'], 支持选项有：

BackupFlag

ValueIndexFlag

LocalGlobalFlag

GroupFlag

PersistentFlag

NONE

MultiTopologyId (int): 最大Set ID, 类型为：number, 取值范围：0-255, 默认值：0

Weight (int): 最大Set ID, 类型为：number, 取值范围：0-255, 默认值：0

SidLabel (int): 最大Set ID, 类型为：number, 取值范围：1-255, 默认值：1

Returns:

(:obj:Ospfv2AdjSidSubTlvConfig): OSPFv2 Adj Sid Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Extended Link Lsa	Session=${Session}	Age=20
${Tlv}		Create Ospf Extended link Tlv	OpaqueExtendedLinkLsa=${Lsa}
Create Ospf Adj Sid Sub Tlv	Session=${Session}	ExtendedLinkTlv=${Tlv}	
Create Ospf Asbr Summary Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 Asbr Summary LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Summary LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

AsbrRouterId (int): 路由个数, 类型为：number, 取值范围：1-1000000, 默认值：1

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：10

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2AsbrSummaryLsaConfig): OSPFv2 Asbr Summary LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf Asbr Summary Lsa	Session=${Session}	Age=20
Create Ospf Bier Mpls Encap Sub Tlv
Arguments
Tlv
** kwargs
Documentation
创建OSPFv2 Bier Mpls Encap Sub Tlv对象

Args:

Tlv (:obj:Port): OSPFv2 Bier Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Bier Mpls Encap Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

TlvType (int): Type字段值, 类型为：number, 取值范围：0-255, 默认值：10

MaxSi (int): 最大Set ID, 类型为：number, 取值范围：1-255, 默认值：1

Label (int): 标签范围中的起始标签值, 类型为：number, 取值范围：0-1048575, 默认值：100

Returns:

(:obj:Ospfv2BierMplsEncapSubTlvConfig): OSPFv2 Bier Mpls Encap Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
${Tlv}	Create Ospf Ext Prefix Range Tlv	OpaqueRouterInfoLsa=${Lsa}	
${SubTlv}| Create Ospf Bier Sub Tlv	Tlv=${Tlv}		
Create Ospf Bier Mpls Encap Sub Tlv	Tlv=${SubTlv}		
Create Ospf Bier Sub Tlv
Arguments
Tlv
** kwargs
Documentation
创建OSPFv2 Bier Sub Tlv对象

Args:

Tlv (:obj:Port): OSPFv2 Ext Prefix Range Tlv / Ospfv2 Ext Prefix Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Bier Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

TlvType (int): Type字段值, 类型为：number, 取值范围：0-255, 默认值：9

SubDomainId (int): BIER子域ID, 类型为：number, 取值范围：1-255, 默认值：1

MtId (int): 多拓扑ID, 类型为：number, 取值范围：1-255, 默认值：1

BfrId (int): BFR（Bit Forwarding Router，比特转发路由器）ID, 类型为：number, 取值范围：1-65535, 默认值：1

Bar (int): BIER算法, 类型为：number, 取值范围：0-255, 默认值：0

Ipa (int): IGP算法, 类型为：number, 取值范围：0-255, 默认值：0

Returns:

(:obj:Ospfv2BierSubTlvConfig): OSPFv2 Bier Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
${Tlv}	Create Ospf Ext Prefix Range Tlv	OpaqueRouterInfoLsa=${Lsa}	
Create Ospf Bier Sub Tlv	Tlv=${Tlv}		
Create Ospf Custom Sub Tlv
Arguments
SrLinkMsdSubTlv
** kwargs
Documentation
创建OSPFv2 Custom Sub Tlv对象

Args:

SrLinkMsdSubTlv (:obj:Ospfv2SrLinkMsdSubTlvConfig): OSPFv2 Sr Link Msd Sub Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Custom Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

SubType (int): 类型为：number, 取值范围：0-255, 默认值：0

SubValue (int): 类型为：number, 取值范围：0-255, 默认值：8

Returns:

(:obj:Ospfv2CustomMsdSubTlvConfig): OSPFv2 Custom Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Extended Link Lsa	Session=${Session}	Age=20
${Tlv}		Create Ospf Extended link Tlv	OpaqueExtendedLinkLsa=${Lsa}
${SubTlv}	Create Ospf Sr Link Msd Sub Tlv	SrLinkMsdSubTlv=${Tlv}	
Create Ospf Custom Sub Tlv	SrLinkMsdSubTlv = ${SubTlv}		
Create Ospf Ext Prefix Range Tlv
Arguments
Session
OpaqueExtendedPrefixLsa
** kwargs
Documentation
创建OSPFv2 Ext Prefix Range Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

OpaqueExtendedPrefixLsa (:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Extended Prefix LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Ext Prefix Range Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

PrefixLength (int): 前缀长度, 类型为：number, 取值范围：0-32, 默认值：24

AF (str): 前缀的地址族, 类型为：string, 默认值：IPv4Unicast, 取值范围：

IPv4Unicast

ExtendedPrefixRange (int): 要生成的前缀的数量, 类型为：number, 取值范围：1-65535, 默认值：1

ExtendedPrefixFlags (list): 包含在TLV中的标志位, 类型为：list, 默认值： NoneFlag, 支持选项有：

NoneFlag

IAInterArea

AddressPrefix (str): 起始地址前缀, 类型为：string, 默认值：192.0.1.0, 取值范围：有效的ipv4地址

Returns:

(:obj:Ospfv2ExtPrefixRangeTlvConfig): OSPFv2 Ext Prefix Range Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Extended Prefix Lsa	Session=${Session}	Age=20
Create Ospf Ext Prefix Range Tlv	Session=${Session}	OpaqueExtendedPrefixLsa=${Lsa}	
Create Ospf Ext Prefix Tlv
Arguments
Session
OpaqueExtendedPrefixLsa
** kwargs
Documentation
创建OSPFv2 Ext Prefix Range Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

OpaqueExtendedPrefixLsa (:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Extended Prefix LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Ext Prefix Range Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

RouteType (str): 起始地址前缀, 类型为：string, 默认值：Unspecified, 取值范围：

Unspecified

IntraArea

InterArea

AsExternal

NssaExternal

AddressPrefix (str): 起始地址前缀, 类型为：string, 默认值：192.0.1.0, 取值范围：有效的ipv4地址

PrefixLength (int): 要生成的前缀的数量, 类型为：number, 取值范围：0-32, 默认值：24

PrefixTlvBlockCount (int): 要生成的前缀的数量, 类型为：number, 取值范围：0-32, 默认值：1

AF (str): 起始地址前缀, 类型为：string, 默认值：IPv4Unicast, 取值范围：

IPv4Unicast

ExtendedPrefixFlags (list): 包含在TLV中的标志位, 类型为：list, 默认值： NoneFlag, 支持选项有：

NoneFlag

AttachFlag

NodeFlag

Returns:

(:obj:Ospfv2ExtPrefixTlvConfig): OSPFv2 Ext Prefix Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Extended Prefix Lsa	Session=${Session}	Age=20
Create Ospf Ext Prefix Range Tlv	Session=${Session}	OpaqueExtendedPrefixLsa=${Lsa}	
Create Ospf Extended Link Tlv
Arguments
OpaqueExtendedLinkLsa
** kwargs
Documentation
创建OSPFv2 Extended link Tlv对象

Args:

OpaqueExtendedLinkLsa (:obj:Ospfv2OpaqueSrExtLinkLsaConfig): OSPFv2 Opaque Router Info LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Extended link Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

LinkType (str): 前缀的地址族, 类型为：string, 默认值：P2P, 取值范围：

P2P

TRANSITNETWORK

STUBNETWORK

VIRTUALLINK

LinkId (str): 起始地址前缀, 类型为：string, 默认值：0.0.0.0, 取值范围：有效的ipv4地址

LinkData (str): 起始地址前缀, 类型为：string, 默认值：0.0.0.0, 取值范围：有效的ipv4地址

Returns:

(:obj:Ospfv2ExtendedLinkTlvConfig): OSPFv2 Extended link Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Extended Link Lsa	Session=${Session}	Age=20
Create Ospf Extended link Tlv	OpaqueExtendedLinkLsa=${Lsa}		
Create Ospf External Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 External LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 External LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

LsType (str): LSA类型, 类型为：string, 默认值： ExtLsaLsType1, 支持选项有：

ExtLsaLsType1: AS-External(5)

ExtLsaLsType2: NSSA(7)

RouteCount (int): 路由个数, 类型为：number, 取值范围：1-1000000, 默认值：1

StartNetworkPrefix (str): 起始网络前缀, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：192.0.1.0

PrefixLength (int): 路由器优先级, 类型为：number, 取值范围：1-32, 默认值：24

Increment (int): 步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

MetricType (str): 选项, 类型为：string, 默认值： ExtLsaLsMetricType1, 支持选项有：

ExtLsaLsMetricType1

ExtLsaLsMetricType2

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：10

ForwardingAddress (str): 转发地址,即：LSA中携带的转发地址, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：192.0.1.0

RouterTag (int): 路由标签, 类型为：number, 取值范围：0-2147483647, 默认值：0

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

LsaAutomaticConversion (bool): LSA自动转换, 即：当配置的会话为NSSA会话时,Renix会自动将此处配置的外部LSA转换为NSSA-LSA进行发送;当配置的会话为非NSSA会话时,Renix会自动将此处配置的NSSA-LSA转换为外部LSA进行发送, 类型为：bool, 取值范围：True或False, 默认值：True

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2ExternalLsaConfig): OSPFv2 External LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf External Lsa	Session=${Session}	Age=20
Create Ospf Lan Adj Sid Sub Tlv
Arguments
Session
ExtendedLinkTlv
** kwargs
Documentation
创建OSPFv2 Lan Adj Sid Sub Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

ExtendedLinkTlv (:obj:Ospfv2ExtendedLinkTlvConfig): OSPFv2 Extended Link Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Lan Adj Sid Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Flags (list): 选项, 类型为：list, 默认值： ['ValueIndexFlag', 'LocalGlobalFlag', 'NONE'], 支持选项有：

BackupFlag

ValueIndexFlag

LocalGlobalFlag

GroupFlag

PersistentFlag

NONE

MultiTopologyId (int): 最大Set ID, 类型为：number, 取值范围：0-255, 默认值：0

Weight (int): 最大Set ID, 类型为：number, 取值范围：0-255, 默认值：0

NeighborId (str): 起始地址前缀, 类型为：string, 默认值：0.0.0.0, 取值范围：有效的ipv4地址

SidLabel (int): 最大Set ID, 类型为：number, 取值范围：1-255, 默认值：1

Returns:

(:obj:Ospfv2LanSidSubTlvConfig): OSPFv2 Lan Adj Sid Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Extended Link Lsa	Session=${Session}	Age=20
${Tlv}		Create Ospf Extended link Tlv	OpaqueExtendedLinkLsa=${Lsa}
Create Ospf Lan Adj Sid Sub Tlv	Session=${Session}	Tlv=${Tlv}	
Create Ospf Network Atch Router
Arguments
NetworkLsa
** kwargs
Documentation
创建OSPFv2 Network LSA Atch Router对象

Args:

NetworkLsa (:obj:Ospfv2NetworkLsaConfig): 测试仪表OSPFv2 Network LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Network LSA Atch Router的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AttachedRouter (str): 附加路由器的IP地址, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

Returns:

(:obj:Ospfv2NetworkAtchRouterConfig): OSPFv2 Network LSA Atch Router对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${NetworkLsa}	Create Ospf Network Lsa	Session=${Session}	Age=20
Create Ospf Network Lsa Atch Router	NetworkLsa=${NetworkLsa}	Metric=65535	
Create Ospf Network Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 Network LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Network LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

DrIpAddress (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

PrefixLength (int): 路由器优先级, 类型为：number, 取值范围：1-32, 默认值：24

Options (list): 选项, 类型为：list, 默认值： NONTBIT | EBIT, 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2NetworkLsaConfig): OSPFv2 Network LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf Network Lsa	Session=${Session}	Age=20
Create Ospf Opaque Extended Link Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 Opaque Extended Link LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的Opaque Extended Link LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Scope (str): Tlv类型, 类型为：string, 默认值： AreaLocal, 支持选项有：

LinkLocal

AreaLocal

AreaSystemWide

AdvertisingRouterId (str): 通告路由器ID, 类型为：string, 取值范围：有效的ipv4地址, 默认值：192.0.0.1

Instance (int): 实例, 类型为：number, 取值范围：0-16777215, 默认值：1

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2OpaqueSrExtLinkLsaConfig): OSPFv2 Opaque Extended Link LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf Opaque Extended Link LSA	Session=${Session}	Age=20
Create Ospf Opaque Extended Prefix Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 Opaque Extended Prefix LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Opaque Extended Prefix LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Scope (str): LSA的泛洪区域, 类型为：string, 默认值：AreaLocal, 取值范围：

LinkLocal

AreaLocal

AreaSystemWide

AdvertisingRouterId (str): 通告路由器ID, 类型为：string, 默认值：192.0.0.1, 取值范围：有效的ipv4地址

Instance (int): 指定LSA中Instance字段的值, 类型为：number, 默认值：1, 取值范围：0-16777215

Options (list): 类型为：list, 默认值：['NONTBIT', 'EBIT'], 取值范围：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): LSA的老化时间。单位为秒, 类型为：number, 默认值：1, 取值范围：0-3600

SequenceNumber (int): LSA的序列号, 类型为：number, 默认值：0x80000001, 取值范围：0-4294967295

Checksum (bool): LSA的校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2OpaqueSrExtPrefixLsaConfig): OSPFv2 Opaque Extended Prefix LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf Opaque Extended Prefix Lsa	Session=${Session}	Age=20
Create Ospf Opaque Router Info Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 Opaque Router Info LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Opaque Router Info LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Router Info LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
Create Ospf Prefix Sid Sub Tlv
Arguments
Session
Tlv
** kwargs
Documentation
创建OSPFv2 Prefix Sid Sub Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Tlv (:obj:Ospfv2ExtPrefixTlvConfig): OSPFv2 Ext Prefix Range Tlv / Ospfv2 Ext Prefix Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Prefix Sid Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

PrefixSidTlvFlags (list): 包含在TLV中的标志位, 类型为：list, 默认值： NoPhp, 取值范围：

NoPhp

MappingServer

ExplicitNull

ValueIndex

LacalGlobal

MultiTopologyId (int): 指定MT-ID的值, 类型为：number, 取值范围：0-255, 默认值：0

Algorithm (int): 计算到其他节点/前缀的可达信息的算法, 类型为：number, 默认值：0

SidIndexLabel (int): Flags中包含Value/Index时，指定标签值; Flags中不包含Value/Index时，指定SID/Label范围内的标签偏移值, 类型为：number, 取值范围：0-4294967295, 默认值：0

SidIndexLabelStep (int): SidIndexLabel跳变, 类型为：number, 取值范围：0-4294967295, 默认值：1

Returns:

(:obj:Ospfv2PrefixSidSubTlvConfig): OSPFv2 Prefix Sid Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
${Tlv}	Create Ospf Ext Prefix Range Tlv	OpaqueRouterInfoLsa=${Lsa}	
Create Ospf Prefix Sid Sub Tlv	Session=${Session}	Tlv=${Tlv}	
Create Ospf Router Info Capability Tlv
Arguments
OpaqueRouterInfoLsa
** kwargs
Documentation
创建OSPFv2 Router Info Capability Tlv对象

Args:

OpaqueRouterInfoLsa (:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Router Info LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Router Info Capability Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

InfoCapability (int): 指定TLV值, 类型为：number, 默认值：1, 取值范围：0-255

Returns:

(:obj:Ospfv2RouterInfoCapabilityTlvConfig): OSPFv2 Router Info Capability Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
Create Ospf Router Info Capability Tlv	OpaqueRouterInfoLsa=${Lsa}		
Create Ospf Router Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 Router LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Router LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：192.0.0.1

RouterType (list): 路由器类型, 类型为：list, 默认值：NONTBIT, 支持选项有：

NONTBIT

ABR

ASBR

VLE

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2RouterLsaConfig): OSPFv2 Router LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf Router Lsa	Session=${Session}	Age=20
Create Ospf Router Lsa Link
Arguments
RouterLsa
** kwargs
Documentation
创建OSPFv2 Router LSA Link对象

Args:

RouterLsa (:obj:Ospfv2RouterLsaConfig): 测试仪表OSPFv2 Router LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Router LSA Link的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

LinkType (str): 链路类型, 类型为：string, 默认值：P2P, 支持选项有：

P2P

TRANSITNETWORK

STUBNETWORK

VIRTUALLINK

LinkId (str): 链路状态ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

LinkData (str): 链路数据, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

Metric (int): 度量值, 类型为：number, 取值范围：0-65535, 默认值：1

Returns:

(:obj:Ospfv2RouterLsaLinksConfig): OSPFv2 Router LSA Link对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${RouterLsa}	Create Ospf Router Lsa	Session=${Session}	Age=20
Create Ospf Router Lsa Link	RouterLsa=${RouterLsa}	Metric=65535	
Create Ospf Sid Label Binding Sub Tlv
Arguments
Session
Tlv
** kwargs
Documentation
创建OSPFv2 Sid Label Binding Sub Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Tlv (:obj:Ospfv2ExtPrefixTlvConfig): OSPFv2 Ext Prefix Range Tlv / Ospfv2 Ext Prefix Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Sid Label Binding Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

SidLabelBindingTlvFlags (list): 包含在TLV中的标志位, 类型为：list, 默认值： NoneFlag, 取值范围：

NoneFlag

MirroringContext

Weight (int): 进行负载均衡时的权重, 类型为：number, 取值范围：0-255, 默认值：0

MultiTopologyId (int): 指定MT-ID的值, 类型为：number, 取值范围：0-255, 默认值：0

SidLabelType (str): 标识符（SID或者标签）, 类型为：string, 默认值：Bit20, 取值范围：

Bit20

Bit32

SidLabel (int): SID/Label Type为20-Bit Label时，指定标签值; SID/Label Type为32-Bit SID时，指定SID, 类型为：number, 取值范围：0-255, 默认值：16

Returns:

(:obj:Ospfv2SidLabelBindingSubTlvConfig): OSPFv2 Sid Label Binding Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
${Tlv}	Create Ospf Ext Prefix Range Tlv	OpaqueRouterInfoLsa=${Lsa}	
Create Ospf Sid Label Binding Sub Tlv	Session=${Session}	Tlv=${Tlv}	
Create Ospf Sr Algorithm Tlv
Arguments
OpaqueRouterInfoLsa
** kwargs
Documentation
创建OSPFv2 Sr Algorithm Tlv对象

Args:

OpaqueRouterInfoLsa (:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Router Info LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Sr Algorithm Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Algorithms (int): 类型为：number, 默认值：0

Returns:

(:obj:Ospfv2SrAlgorithmTlvConfig): OSPFv2 Sr Algorithm Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
Create Ospf Sr Algorithm Tlv	OpaqueRouterInfoLsa=${Lsa}		
Create Ospf Sr Fad Tlv
Arguments
Session
OpaqueRouterInfoLsa
** kwargs
Documentation
创建OSPFv2 Sr Fad Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

OpaqueRouterInfoLsa (:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Router Info LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Sr Fad Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

FlexAlgo (int): 灵活算法ID, 类型为：number, 默认值：128, 取值范围：128-255

MetricType (str): 指定算路使用的度量类型, 类型为：str, 默认值：IGP_METRIC, 取值范围：

IGP_METRIC

MIN_LINK_DELAY

TE_METRIC

CalcType (int): 指定特定IGP算法的计算类型, 类型为：number, 默认值：0, 取值范围：0-127

Priority (int): 指定该Sub-TLV的优先级, 类型为：number, 默认值：0, 取值范围：0-255

FlexAlgoSubTlv (list): 选择灵活算法路径计算要遵循的约束条件, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

EXCLUDE_ADMIN

INCLUDE_ANY_ADMIN

INCLUDE_ALL_ADMIN

DEFINITION_FLAGS

EXCLUDE_SRLG

ExcludeAdmin (int): 类型为：number, 默认值：0, 取值范围：0-4294967295

IncludeAnyAdmin (int): 类型为：number, 默认值：0, 取值范围：0-4294967295

IncludeAllAdmin (int): 类型为：number, 默认值：0, 取值范围：0-4294967295

DefinitionFlags (list): 类型为：hex int, 默认值：0x80, 取值范围：0-FF

ExcludeSRLG (list): 类型为：hex int, 默认值：0x10020000, 取值范围：0-4294967295

Returns:

(:obj:Ospfv2FlexAlgoDefinitionTlvConfig): OSPFv2 Sr Fad Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
Create Ospf Sr Fad Tlv	Session=${Session}	OpaqueRouterInfoLsa=${Lsa}	
Create Ospf Sr Fapm Sub Tlv
Arguments
Tlv
** kwargs
Documentation
创建OSPFv2 Sr Fapm Sub Tlv对象

Args:

Tlv (:obj:Port): OSPFv2 Ext Prefix Range Tlv / Ospfv2 Ext Prefix Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Sr Fapm Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Algorithm (int): 灵活算法ID, 类型为：number, 取值范围：128-255, 默认值：128

Flags (int): 单字节值, 类型为：number, 取值范围：0-255, 默认值：0

Metric (int): 度量值, 类型为：number, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:Ospfv2SrFapmSubTlvConfig): OSPFv2 Sr Fapm Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
${Tlv}	Create Ospf Ext Prefix Range Tlv	OpaqueRouterInfoLsa=${Lsa}	
Create Ospf Sr Fapm Sub Tlv	Tlv=${Tlv}		
Create Ospf Sr Link Msd Sub Tlv
Arguments
Session
ExtendedLinkTlv
** kwargs
Documentation
创建OSPFv2 Sr Link Msd Sub Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

ExtendedLinkTlv (:obj:Ospfv2ExtendedLinkTlvConfig): OSPFv2 Extended Link Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Sr Link Msd Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Flags (list): 包含在TLV中的标志位, 类型为：list, 默认值： UNKNOWN, 支持选项有：

UNKNOWN

MAX_SEG_LEFT

MAX_END_POP

MAX_T_INSERT

MAX_T_ENCAPS

MAX_END_D

MaxSegmentLeft (int): 指定接收报文的SRH中SL（Segment Left）字段的最大值, 类型为：number, 取值范围：0-255, 默认值：8

MaxEndPop (int): 指定SRH栈的顶端SRH中SID的最大数量, 类型为：number, 取值范围：0-255, 默认值：8

MaxInsert (int): 指定执行T.Insert行为时可包含SID的最大数量, 类型为：number, 取值范围：0-255, 默认值：8

MaxEncap (int): 指定执行T.Encap行为时可包含SID的最大数量, 类型为：number, 取值范围：0-255, 默认值：8

MaxEndD (int): 指定执行End.DX6和End.DT6功能时，SRH中SID的最大数量, 类型为：number, 取值范围：0-255, 默认值：8

Returns:

(:obj:Ospfv2SrLinkMsdSubTlvConfig): OSPFv2 Sr Link Msd Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Extended Link Lsa	Session=${Session}	Age=20
${Tlv}		Create Ospf Extended link Tlv	OpaqueExtendedLinkLsa=${Lsa}
Create Ospf Sr Link Msd Sub Tlv	Session=${Session}	Tlv=${Tlv}	
Create Ospf Sr Node Msd Tlv
Arguments
Session
OpaqueRouterInfoLsa
** kwargs
Documentation
创建OSPFv2 Sr Node Msd Tlv对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

OpaqueRouterInfoLsa (:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Router Info LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Sr Node Msd Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Flags (list): TLV中的标志位, 类型为：list, 默认值：UNKNOWN, 取值范围：

UNKNOWN

MAX_SEG_LEFT

MAX_END_POP

MAX_T_INSERT

MAX_T_ENCAPS

MAX_END_D

MaxSegmentLeft (int): 在应用与SID关联的SRv6 Endpoint Function指令之前，指定接收报文的SRH中SL（Segment Left）字段的最大值, 类型为：number, 默认值：0, 取值范围：0-255

MaxEndPop (int): 指定SRH栈的顶端SRH中SID的最大数量, 类型为：number, 默认值：8, 取值范围：0-255

MaxInsert (int): 指定执行T.Insert行为时可包含SID的最大数量, 类型为：number, 默认值：8, 取值范围：0-255

MaxEncap (int): 指定执行T.Encap行为时可包含SID的最大数量, 类型为：number, 默认值：8, 取值范围：0-255

MaxEndD (int): 指定执行End.DX6和End.DT6功能时，SRH中SID的最大数量, 类型为：number, 默认值：8, 取值范围：0-255

Returns:

(:obj:Ospfv2SrNodeMsdTlvConfig): OSPFv2 Sr Node Msd Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
Create Ospf Sr Node Msd Tlv	Session=${Session}	OpaqueRouterInfoLsa=${Lsa}	
Create Ospf Sr Sid Label Range Tlv
Arguments
OpaqueRouterInfoLsa
** kwargs
Documentation
创建OSPFv2 Sr Sid Label Range Tlv对象

Args:

OpaqueRouterInfoLsa (:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Router Info LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Sr Sid Label Range Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

SidLabelType (str): 类型为：str, 默认值：Bit20, 取值范围：

Bit20

Bit32

SidLabelBase (int): SID/Label Type为20-Bit Label时，指定起始标签; SID/Label Type为32-Bit SID时，指定起始SID, 类型为：number, 默认值：0, 取值范围：1-4294967295

SidLabelRange (int): 指定要创建的SID/标签的数量, 类型为：number, 默认值：0, 取值范围：1-16777215

Returns:

(:obj:Ospfv2SidLabelRangeTlvConfig): OSPFv2 Sr Sid Label Range Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
Create Ospf Sr Sid Label Range Tlv	OpaqueRouterInfoLsa=${Lsa}		
Create Ospf Sr Srms Preference Tlv
Arguments
OpaqueRouterInfoLsa
** kwargs
Documentation
创建OSPFv2 Sr Srms Preference Tlv对象

Args:

OpaqueRouterInfoLsa (:obj:Ospfv2OpaqueRouterInfoLsaConfig): OSPFv2 Opaque Router Info LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Sr Srms Preference Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Preference (int): 指定路由器作为SR Mapping Server的优先级, 类型为：number, 默认值：1, 取值范围：0-255

Returns:

(:obj:Ospfv2SrmsPreferenceTlvConfig): OSPFv2 Sr Srms Preference Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}	
${Lsa}	Create Ospf Opaque Router Info Lsa	Session=${Session}	Age=20
Create Ospf Sr Srms Preference Tlv	OpaqueRouterInfoLsa=${Lsa}		
Create Ospf Summary Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 Summary LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Summary LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

RouteCount (int): 路由个数, 类型为：number, 取值范围：1-1000000, 默认值：1

StartNetworkPrefix (str): 起始网络前缀, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：192.0.1.0

PrefixLength (int): 路由器优先级, 类型为：number, 取值范围：1-32, 默认值：24

Increment (int): 步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：10

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2SummaryLsaConfig): OSPFv2 Summary LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf Summary Lsa	Session=${Session}	Age=20
Create Ospf Te Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv2 Te LSA对象

Args:

Session (:obj:OspfRouter): OSPFv2协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv2 Te LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

TlvType (str): Tlv类型, 类型为：string, 默认值： LsaLink, 支持选项有：

LsaRouter

LsaLink

RouterId (str): 路由器ID, 类类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

LinkId (str): Link ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

LinkType (str): Link类型, 类型为：string, 默认值： LsaLink, 支持选项有：

LinkP2P

LinkMultiaccess

Instance (int): 实例, 类型为：number, 取值范围：0-16777215, 默认值：1

Metric (int): 度量值, 类型为：number, 取值范围：0-16777215, 默认值：10

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

TOSBIT

EBIT

MCBIT

NPBIT

EABIT

DCBIT

OBIT

DNBIT

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv2TeLsaConfig): OSPFv2 Te LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospf	Port=${Port}
Create Ospf Te Lsa	Session=${Session}	Age=20
Create Ospfv3
Arguments
Port
** kwargs
Documentation
创建OSPFv3协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): OSPFv3协会话名称, 类型为：string

Enable (bool): 使能OSPFv3协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

InstanceId (int): 实例ID, 类型为：number, 取值范围：0-255, 默认值：0

AreaId (str): 区域ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

EnableExtendedLsa (bool): 使能扩展LSA, 类型为：bool, 取值范围：True或False, 默认值：False

ExtendedLsaMode (str): 扩展LSA模式, 类型为：string, 默认值：Full, 取值范围：

NONE

MixedModeOriginateOnly

MixedModeOriginateSPF

Full

AreaExtendedLsaMode (str): 扩展区域LSA模式, 类型为：string, 默认值：InheritGlobal, 取值范围：

InheritGlobal

NONE

MixedModeOriginateOnly

MixedModeOriginateSPF

Full

EnableBfd (bool): 使能BFD, 类型为：bool, 取值范围：True或False, 默认值：False

NetworkType (str): 网络类型, 类型为：string, 取值范围：Broadcast或P2P, 默认值：Broadcast

Priority (int): 路由器优先级, 类型为：number, 取值范围：0-255, 默认值：0

InterfaceId (int): 接口ID, 类型为：number, 取值范围：0-4294967295, 默认值：10

Cost (int): 接口开销, 类型为：number, 取值范围：1-65535, 默认值：10

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'V6BIT', 'EBIT', 'RBIT'], 支持选项有：

NONTBIT

V6BIT

EBIT

MCBIT

NBIT

RBIT

DCBIT

Unused17

Unused16

Unused15

Unused14

Unused13

Unused12

Unused11

Unused10

Unused9

Unused8

Unused7

Unused6

Unused5

Unused4

Unused3

Unused2

Unused1

Unused0

EnableOspfv3Mtu (bool): 使能OSPFv3 MTU, 类型为：bool, 取值范围：True或False, 默认值：True

EnableGracefulRestart (bool): 使能平滑重启, 类型为：bool, 取值范围：True或False, 默认值：False

GracefulRestartReason (str): 平滑重启原因, 类型为：string, 默认值：UNKNOWN, 取值范围：

UNKNOWN

SOFTWARE

RELOADORUPGRADE

SWITCH

EnableViewRoutes (bool): 使能查看路由, 类型为：bool, 取值范围：True或False, 默认值：False

HelloInterval (int): Hello包间隔(秒), 类型为：number, 取值范围：0-65535, 默认值：10

RouterDeadInterval (int): 路由器失效间隔(秒), 类型为：number, 取值范围：0-65535, 默认值：40

LsaRetransInterval (int): LSA重传间隔(秒), 类型为：number, 取值范围：0-4294967295, 默认值：5

LsaRefreshTime (int): LSA刷新间隔(秒), 类型为：number, 取值范围：1-1800, 默认值：1800

Returns:

(:obj:Ospfv3Router): OSPFv3协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Ospfv3	Port=${Port}
Create Ospfv3 As External Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 As External LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 As External LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

LinkStateId (int): 链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

PrefixCount (int): 前缀个数, 类型为：number, 取值范围：1-4294967295, 默认值：1

StartPrefixAddress (str): 起始网络前缀, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

PrefixLength (int): 路由器优先级, 类型为：number, 取值范围：1-128, 默认值：64

Increment (int): 步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

PrefixOptions (list): 前缀选项, 类型为：list, 默认值： NONTBIT, 支持选项有：

NONTBIT

NUBIT

LABIT

MCBIT

PBIT

DNBit

NBit

Unused1

Unused0

IsExternalMetric (bool): 是否外部度量值, 类型为：bool, 取值范围：True或False, 默认值：False

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：1

EnableForwardingAddress (bool): 使能转发地址, 类型为：bool, 取值范围：True或False, 默认值：False

ForwardingAddress (str): 转发地址,即：LSA中携带的转发地址, 类型为：string, 取值范围：IPv6地址, 默认值：'::'

AdminTag (int): 管理标签, 类型为：number, 取值范围：0-4294967295, 默认值：0

ReferencedLsType (int): 参考链路状态类型, 类型为：hex number, 取值范围：0x0-0xFFFF, 默认值：0x0

ReferencedLinkStateId (int): 参考链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

LsaAutomaticConversion (bool): LSA自动转换, 即：当配置的会话为NSSA会话时,Renix会自动将此处配置的外部LSA转换为NSSA-LSA进行发送;当配置的会话为非NSSA会话时,Renix会自动将此处配置的NSSA-LSA转换为外部LSA进行发送, 类型为：bool, 取值范围：True或False, 默认值：True

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3AsExternalLsaConfig): OSPFv3 As External LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 As External Lsa	Session=${Session}	Age=20
Create Ospfv3 Bier Mpls Encap Sub Tlv
Arguments
SubTlv
** kwargs
Documentation
创建OSPFv3 Bier Mpls Encap Sub Tlv对象

Args:

SubTlv (:obj:Ospfv3BierSubTlvConfig): Ospfv3 Bier Sub Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Bier Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

TlvType (int): Type字段值, 类型为：number, 取值范围：0-255, 默认值：10

MaxSi (int): 最大Set ID, 类型为：number, 取值范围：1-255, 默认值：1

Label (int): 标签范围中的起始标签值, 类型为：number, 取值范围：0-1048575, 默认值：100

BsLen (int): 本地比特串的长度, 类型为：number, 取值范围：0-15, 默认值：4

Returns:

(:obj:Ospfv3BierMplsEncapSubTlvConfig): Ospfv3 Bier Mpls Encap Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${Lsa}	Create Ospfv3 Inter Area Prefix Lsa	Session=${Session}	Age=20
${SubTlv}	Create Ospfv3 Bier Sub Tlv	Lsa=${Lsa}	
Create Ospfv3 Bier Mpls Encap Sub Tlv	SubTlv=${SubTlv}		
Create Ospfv3 Bier Sub Tlv
Arguments
Lsa
** kwargs
Documentation
创建OSPFv3 Bier Sub Tlv对象

Args:

Lsa (:obj:Ospfv3InterAreaRouterLsaConfig): Ospfv3 Inter Area Router LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Bier Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

TlvType (int): Type字段值, 类型为：number, 取值范围：0-255, 默认值：9

SubDomainId (int): BIER子域ID, 类型为：number, 取值范围：1-255, 默认值：1

MtId (int): 多拓扑ID, 类型为：number, 取值范围：1-255, 默认值：1

BfrId (int): BFR（Bit Forwarding Router，比特转发路由器）ID, 类型为：number, 取值范围：1-65535, 默认值：1

Bar (int): BIER算法, 类型为：number, 取值范围：0-255, 默认值：0

Ipa (int): IGP算法, 类型为：number, 取值范围：0-255, 默认值：0

Returns:

(:obj:Ospfv3BierSubTlvConfig): Ospfv3 Bier Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${Lsa}	Create Ospfv3 Inter Area Prefix Lsa	Session=${Session}	Age=20
Create Ospfv3 Bier Sub Tlv	Lsa=${Lsa}		
Create Ospfv3 Endx Sid Structure Sub Tlv
Arguments
SubTlv
** kwargs
Documentation
创建OSPFv3 Endx Sid Structure Sub Tlv对象

Args:

SubTlv (:obj:Ospfv3Srv6EndXSidSubTlvConfig): OSPFv3 Srv6 EndX Sid Sub Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Srv6 Link Msd Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

LbLength (int): SRv6 SID Locator Block长度, 类型为：number, 取值范围：0-128, 默认值：32

LnLength (int): SRv6 SID Locator Node长度, 类型为：number, 取值范围：0-128, 默认值：32

FunctionLength (int): SRv6 SID Function长度, 类型为：number, 取值范围：0-128, 默认值：32

ArgumentLength (int): SRv6 SID Argument长度, 类型为：number, 取值范围：0-128, 默认值：32

Returns:

(:obj:Ospfv3Srv6SidStructureSubTlvConfig): Ospfv3 Endx Sid Structure Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${RouterLsa}	Create Ospfv3 Router Lsa	Session=${Session}	Age=20
${LsaLink}	Create Ospfv3 Router Lsa Link	RouterLsa=${RouterLsa}	Metric=65535
${SubTlv}	Create Ospfv3 Srv6 Msd Sid Sub Tlv	RouterLsaLink=${LsaLink}	
Create Ospfv3 Endx Sid Structure Sub Tlv	SubTlv=${SubTlv}		
Create Ospfv3 Inter Area Prefix Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Inter Area Prefix LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Inter Prefix LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

LinkStateId (int): 链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

ExtendedLsaTlvs (list): 扩展LSA TLVs, 类型为：list, 默认值： Ipv6InterAreaPrefix, 支持选项有：

NONE

Ipv6InterAreaPrefix

PrefixCount (int): 前缀个数, 类型为：number, 取值范围：1-4294967295, 默认值：1

StartPrefixAddress (str): 起始网络前缀, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

PrefixLength (int): 路由器优先级, 类型为：number, 取值范围：1-128, 默认值：64

Increment (int): 步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

PrefixOptions (list): 前缀选项, 类型为：list, 默认值： NONTBIT, 支持选项有：

NONTBIT

NUBIT

LABIT

MCBIT

PBIT

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：1

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3InterAreaPrefixLsaConfig): Ospfv3 Inter Area Prefix LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Inter Area Prefix Lsa	Session=${Session}	Age=20
Create Ospfv3 Inter Area Router Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Inter Area Router LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Router LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

LinkStateId (int): 链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

AsbrId (str): ASBR ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：1

Options (list): 选项, 类型为：list, 默认值： NONTBIT | V6BIT | EBIT, 支持选项有：

NONTBIT

V6BIT

EBIT

MCBIT

NBIT

RBIT

DCBIT

Unused17

Unused16

Unused15

Unused14

Unused13

Unused12

Unused11

Unused10

Unused9

Unused8

Unused7

Unused6

Unused5

Unused4

Unused3

Unused2

Unused1

Unused0

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3InterAreaRouterLsaConfig): Ospfv3 Inter Area Router LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Inter Area Router Lsa	Session=${Session}	Age=20
Create Ospfv3 Intra Area Prefix Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Intra Area Prefix LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Intra Prefix LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

LinkStateId (int): 链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

ReferencedLsType (str): 参考LS类型, 类型为：hex number, 取值范围：0x0-0xFFFF, 默认值：0x0

ReferencedAdvertisingRouterId (str): 参考通告路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

ReferencedLinkStateId (int): 参考链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

ExtendedLsaTlvs (list): 扩展LSA TLVs, 类型为：list, 默认值： Ipv6IntraAreaPrefix, 支持选项有：

NONE

Ipv6IntraAreaPrefix

PrefixCount (int): 前缀个数, 类型为：number, 取值范围：1-4294967295, 默认值：1

StartPrefixAddress (str): 起始网络前缀, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

PrefixLength (int): 路由器优先级, 类型为：number, 取值范围：1-128, 默认值：64

Increment (int): 步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

PrefixOptions (list): 前缀选项, 类型为：list, 默认值： NONTBIT, 支持选项有：

NONTBIT

NUBIT

LABIT

MCBIT

PBIT

DNBit

NBit

Unused1

Unused0

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：1

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3IntraAreaPrefixLsaConfig): Ospfv3 Intra Area Prefix LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Intra Area Prefix Lsa	Session=${Session}	Age=20
Create Ospfv3 Lan Endx Sid Structure Sub Tlv
Arguments
SubTlv
** kwargs
Documentation
创建OSPFv3 Lan Endx Sid Structure Sub Tlv对象

Args:

SubTlv (:obj:Ospfv3Srv6LanEndXSidSubTlvConfig): OSPFv3 Srv6 Lan EndX Sid Sub Tlv对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Srv6 Link Msd Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

LbLength (int): SRv6 SID Locator Block长度, 类型为：number, 取值范围：0-128, 默认值：32

LnLength (int): SRv6 SID Locator Node长度, 类型为：number, 取值范围：0-128, 默认值：32

FunctionLength (int): SRv6 SID Function长度, 类型为：number, 取值范围：0-128, 默认值：32

ArgumentLength (int): SRv6 SID Argument长度, 类型为：number, 取值范围：0-128, 默认值：32

Returns:

(:obj:Ospfv3Srv6LanEndXSidSubTlvConfig): Ospfv3 Lan Endx Sid Structure Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${RouterLsa}	Create Ospfv3 Router Lsa	Session=${Session}	Age=20
${LsaLink}	Create Ospfv3 Router Lsa Link	RouterLsa=${RouterLsa}	Metric=65535
${SubTlv}	Create Ospfv3 Srv6 Msd Sid Sub Tlv	RouterLsaLink=${LsaLink}	
Create Ospfv3 Lan Endx Sid Structure Sub Tlv	SubTlv=${SubTlv}		
Create Ospfv3 Link Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Link LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Link LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

LinkStateId (int): 链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

ExtendedLsaTlvs (list): 扩展LSA TLVs, 类型为：list, 默认值： Ipv6IntraAreaPrefix, 支持选项有：

NONE

Ipv6IntraAreaPrefix

Ipv6LinkLocalAddr

Ipv4LinkLocalAddr

PrefixCount (int): 前缀个数, 类型为：number, 取值范围：1-4294967295, 默认值：1

StartPrefixAddress (str): 起始网络前缀, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

PrefixLength (int): 路由器优先级, 类型为：number, 取值范围：1-128, 默认值：64

Increment (int): 步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

PrefixOptions (list): 前缀选项, 类型为：list, 默认值： NONTBIT, 支持选项有：

NONTBIT

NUBIT

LABIT

MCBIT

PBIT

DNBit

NBit

Unused1

Unused0

LinkLocalInterfaceAddress (str): 本地链路接口地址, 类型为：string, 取值范围：IPv6地址, 默认值：fe80::1

Ipv4LinkLocalInterfaceAddress (str): 本地链路接口地址, 类型为：string, 取值范围：IPv4地址, 默认值：0.0.0.0

RouterPriority (int): 路由优先级, 类型为：number, 取值范围：1-255, 默认值：1

Options (list): 选项, 类型为：list, 默认值： NONTBIT | V6BIT | EBIT, 支持选项有：

NONTBIT

V6BIT

EBIT

MCBIT

NBIT

RBIT

DCBIT

Unused17

Unused16

Unused15

Unused14

Unused13

Unused12

Unused11

Unused10

Unused9

Unused8

Unused7

Unused6

Unused5

Unused4

Unused3

Unused2

Unused1

Unused0

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3LinkLsaConfig): OSPFv3 Link LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Link Lsa	Session=${Session}	Age=20
Create Ospfv3 Network Atch Router
Arguments
Lsa
** kwargs
Documentation
创建OSPFv3 Network LSA Atch Router对象

Args:

Lsa (:obj:Ospfv3NetworkLsaConfig): 测试仪表OSPFv3 Network LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Network LSA Atch Router的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AttachedRouter (str): 附加路由器的IP地址, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：0.0.0.0

Returns:

(:obj:Ospfv3NetworkAtchRouterConfig): OSPFv3 Network LSA Atch Router对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${RouterLsa}	Create Ospfv3 Network Lsa	Session=${Session}	Age=20
Create Ospfv3 Network Lsa Atch Router	Lsa=${RouterLsa}	Metric=65535	
Create Ospfv3 Network Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Network LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Network LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

LinkStateId (int): 链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

V6BIT

EBIT

MCBIT

NBIT

RBIT

DCBIT

Unused17

Unused16

Unused15

Unused14

Unused13

Unused12

Unused11

Unused10

Unused9

Unused8

Unused7

Unused6

Unused5

Unused4

Unused3

Unused2

Unused1

Unused0

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3NetworkLsaConfig): OSPFv3 Network LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Network Lsa	Session=${Session}	Age=20
Create Ospfv3 Nssa External Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Nssa External LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Nssa External LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.1.1.1

LinkStateId (int): 链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

ExtendedLsaTlvs (list): 扩展LSA TLVs, 类型为：list, 默认值： Ipv6ExternalPrefix, 支持选项有：

NONE

Ipv6ExternalPrefix

ExtendedLsaSubTlvs (list): 扩展LSA Sub-TLV, 类型为：list, 默认值： NONTBIT, 支持选项有：

NONE

Ipv6ForwardingAddr

Ipv4ForwardingAddr

RouteTag

PrefixCount (int): 前缀个数, 类型为：number, 取值范围：1-4294967295, 默认值：1

StartPrefixAddress (str): 起始网络前缀, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

PrefixLength (int): 路由器优先级, 类型为：number, 取值范围：1-128, 默认值：64

Increment (int): 步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

PrefixOptions (list): 前缀选项, 类型为：list, 默认值： NONTBIT, 支持选项有：

NONTBIT

NUBIT

LABIT

MCBIT

PBIT

DNBit

NBit

Unused1

Unused0

IsExternalMetric (bool): 是否外部度量值, 类型为：bool, 取值范围：True或False, 默认值：False

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：1

EnableForwardingAddress (bool): 使能转发地址, 类型为：bool, 取值范围：True或False, 默认值：False

ForwardingAddress (str): Ipv6转发地址,即：LSA中携带的转发地址, 类型为：string, 取值范围：IPv6地址, 默认值：'::'

Ipv4ForwardingAddress (str): IPv4转发地址, 取值范围：IPv4地址, 默认值：0.0.0.0

AdminTag (int): 管理标签, 类型为：number, 取值范围：0-4294967295, 默认值：0

ReferencedLsType (int): 参考链路状态类型, 类型为：hex number, 取值范围：0x0-0xFFFF, 默认值：0x0

ReferencedLinkStateId (int): 参考链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

LsaAutomaticConversion (bool): LSA自动转换, 即：当配置的会话为NSSA会话时,Renix会自动将此处配置的外部LSA转换为NSSA-LSA进行发送;当配置的会话为非NSSA会话时,Renix会自动将此处配置的NSSA-LSA转换为外部LSA进行发送, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3NssaExternalLsaConfig): OSPFv3 Nssa External LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Nssa External Lsa	Session=${Session}	Age=20
Create Ospfv3 Opaque Router Info Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Opaque Router Info LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Opaque Router Info LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Scope (str): 起始网络前缀, 类型为：string, 默认值：AreaLocal, 取值范围：

LinkLocal

AreaLocal

AreaSystemWide

AdvertisingRouterId (str): 起始网络前缀, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.0.1

LinkStateId (int): 路由优先级, 类型为：number, 取值范围：1-255, 默认值：0

TlvsFlag (list): 前缀选项, 类型为：list, 默认值： ['NONTBIT', 'InfoCapabilities'], 支持选项有：

NONEBIT

InfoCapabilities

FuncCapabilities

InformationalCapabilities (list): 前缀选项, 类型为：list, 默认值： NONEBIT, 支持选项有：

NONEBIT

RcBit

RhBit

SrsBit

TesBit

PolBit

Etbit

MiBit

SrhBit

Unused8

Unused9

Unused10

Unused11

Unused12

Unused13

Unused14

Unused15

Unused16

Unused17

Unused18

Unused19

Unused20

Unused22

Unused21

Unused23

Unused24

Unused25

Unused26

Unused27

Unused28

Unused29

Unused30

FunctionalCapabilities (list): 前缀选项, 类型为：list, 默认值： NONEBIT, 支持选项有：

NONEBIT

Unused0

Unused1

Unused2

Unused3

Unused4

Unused5

Unused6

Unused7

Unused8

Unused9

Unused10

Unused11

Unused12

Unused13

Unused14

Unused15

Unused16

Unused17

Unused18

Unused19

Unused20

Unused22

Unused21

Unused23

Unused24

Unused25

Unused26

Unused27

Unused28

Unused29

Unused30

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3OpaqueRouterInfoLsaConfig): OSPFv3 Opaque Router Info LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Opaque Router Info LSA	Session=${Session}	Age=20
Create Ospfv3 Router Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Router LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Router LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

AdvertisingRouterId (str): 通告路由器ID即：指定最初发布LSA的路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.0.0.1

LinkStateId (int): 链路状态ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

RouterType (str): 路由器类型, 类型为：string, 默认值：NONTBIT, 支持选项有：

NONEBIT

RouterTypeABR

RouterTypeASBR

RouterTypeVirtype

Options (list): 选项, 类型为：list, 默认值： ['NONTBIT', 'EBIT'], 支持选项有：

NONTBIT

V6BIT

EBIT

MCBIT

NBIT

RBIT

DCBIT

Unused17

Unused16

Unused15

Unused14

Unused13

Unused12

Unused11

Unused10

Unused9

Unused8

Unused7

Unused6

Unused5

Unused4

Unused3

Unused2

Unused1

Unused0

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3RouterLsaConfig): OSPFv3 Router LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Router Lsa	Session=${Session}	Age=20
Create Ospfv3 Router Lsa Link
Arguments
RouterLsa
** kwargs
Documentation
创建OSPFv3 Router LSA Link对象

Args:

RouterLsa (:obj:Ospfv3RouterLsaConfig): 测试仪表OSPFv3 Router LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Router LSA Link的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

LinkType (str): 链路类型, 类型为：string, 默认值：P2P, 支持选项有：

P2P

TRANSITNETWORK

VIRTUALLINK

InterfaceId (int): 接口ID,即该ID用于唯一标识simulated router的接口, 类型为：number, 取值范围：0-4294967295, 默认值：1

NeighborInterfaceId (int): 邻居接口ID,即该ID用于唯一标识邻居路由器的接口, 类型为：number, 取值范围：0-4294967295, 默认值：1

NeighborRouterId (str): 邻居路由器ID, 类型为：string, 取值范围：0.0.0.0-255.255.255.255, 默认值：1.0.0.1

Metric (int): 度量值, 类型为：number, 取值范围：1-65535, 默认值：1

Returns:

(:obj:Ospfv3RouterLsaLinksConfig): OSPFvv3 Router LSA Link对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${RouterLsa}	Create Ospfv3 Router Lsa	Session=${Session}	Age=20
Create Ospfv3 Router Lsa Link	RouterLsa=${RouterLsa}	Metric=65535	
Create Ospfv3 Sr Algorithm Tlv
Arguments
Lsa
** kwargs
Documentation
创建OSPFv3 Sr Algorithm Tlv对象

Args:

Lsa (:obj:Ospfv3OpaqueRouterInfoLsaConfig): Ospfv3 Opaque Router Info LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Sr Algorithm Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Algorithms (int): 算法, 类型为：number, 默认值：0

Returns:

(:obj:Ospfv3SrAlgorithmTlvConfig): Ospfv3 Sr Algorithm Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${Lsa}	Create Ospfv3 Opaque Router Info LSA	Session=${Session}	Age=20
Create Ospfv3 Sr Algorithm Tlv	Lsa=${Lsa}		
Create Ospfv3 Sr Fad Tlv
Arguments
Session
Lsa
** kwargs
Documentation
创建OSPFv3 Sr Fad Tlv对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Lsa (:obj:Ospfv3OpaqueRouterInfoLsaConfig): Ospfv3 Opaque Router Info LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Sr Fad Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

FlexAlgorithm (int): 灵活算法ID, 类型为：number, 取值范围：128-255, 默认值：128

MetricType (str): 度量类型, 类型为：string, 默认值：IGPMetric, 取值范围：

IGPMetric

MinUnidirectionalLinkDelay

TEDefaultMetric

CalculationType (int): 特定IGP算法的计算类型, 类型为：number, 取值范围：0-127, 默认值：0

Priority (int): 该TLV的优先级, 类型为：number, 取值范围：0-255, 默认值：0

FlexAlgorithmSubTlvs (list): 灵活算法路径计算要遵循的约束条件, 类型为：list, 默认值： NONEBIT, 支持选项有：

NONEBIT

ExcludeAdminGroups

IncludeAnyAdminGroups

IncludeAllAdminGroups

DefinitionFlags

ExcludeSRLG

ExcludeAdminGroups (int): 算法, 类型为：number, 取值范围：0-4294967295, 默认值：0

IncludeAnyAdminGroups (int): 算法, 类型为：number, 取值范围：0-4294967295, 默认值：0

IncludeAllAdminGroups (int): 算法, 类型为：number, 取值范围：0-4294967295, 默认值：0

DefinitionFlags (int): 算法, 类型为：number, 取值范围：0-FF, 默认值：0x80

ExcludeSRLG (int): 算法, 类型为：number, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:Ospfv3SrFadTlvConfig): Ospfv3 Sr Fad Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${Lsa}	Create Ospfv3 Opaque Router Info LSA	Session=${Session}	Age=20
Create Ospfv3 Sr Fad Tlv	Lsa=${Lsa}		
Create Ospfv3 Sr Fapm Sub Tlv
Arguments
Lsa
** kwargs
Documentation
创建OSPFv3 Sr Fapm Sub Tlv对象

Args:

Lsa (:obj:Ospfv3InterAreaRouterLsaConfig): Ospfv3 Inter Area Router LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Sr Fapm Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Algorithm (int): 灵活算法ID, 类型为：number, 取值范围：128-255, 默认值：128

Metric (int): 度量值, 类型为：number, 取值范围：128-255, 默认值：0

Returns:

(:obj:Ospfv3SrFapmSubTlvConfig): Ospfv3 Sr Fapm Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${Lsa}	Create Ospfv3 Inter Area Prefix Lsa	Session=${Session}	Age=20
Create Ospfv3 Sr Fapm Sub Tlv	Lsa=${Lsa}		
Create Ospfv3 Srv6 Capabilities Tlv
Arguments
Session
Lsa
** kwargs
Documentation
创建OSPFv3 Srv6 Capabilities Tlv对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Lsa (:obj:Ospfv3OpaqueRouterInfoLsaConfig): Ospfv3 Opaque Router Info LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Srv6 Capabilities Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Flags (list): 类型为：list, 默认值： NONEBIT, 支持选项有：

NONEBIT

Unused0

OFlag

Unused2

Unused3

Unused4

Unused5

Unused6

Unused7

Unused8

Unused9

Unused10

Unused11

Unused12

Unused13

Unused14

Unused15

Returns:

(:obj:Ospfv3Srv6CapabilitiesTlvConfig): Ospfv3 Srv6 Capabilities Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${Lsa}	Create Ospfv3 Opaque Router Info LSA	Session=${Session}	Age=20
Create Ospfv3 Srv6 Capabilities Tlv	Lsa=${Lsa}		
Create Ospfv3 Srv6 Endx Sid Sub Tlv
Arguments
Session
RouterLsaLink
** kwargs
Documentation
创建OSPFv3 Srv6 EndX Sid Sub Tlv对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

RouterLsaLink (:obj:Ospfv3RouterLsaLinksConfig): OSPFv3 Router Lsa LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Srv6 EndX Sid Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

EndpointBehaviorId (int): SRv6 SID的端点行为ID, 类型为：number, 默认值：0

Flags (list): 包含在TLV中的标志位, 类型为：list, 默认值：NONEBIT, 取值范围：

NONEBIT

Unused0

Unused1

Unused2

Unused3

Unused4

PersistentFlag

SetFlag

BackupFlag

Algorithm (int): SID关联的算法, 类型为：number, 取值范围：0-255, 默认值：0

Weight (int): END.X SID / LAN END.X SID的权重，用于负载分担, 类型为：number, 取值范围：0-255, 默认值：1

Sid (str): 通告的SRv6 SID, 邻居路由器ID, 类型为：string, 取值范围：有效的ipv6地址, 默认值：'aaaa:1:1:1::'

Returns:

(:obj:Ospfv3Srv6EndXSidSubTlvConfig): OSPFv3 Srv6 EndX Sid Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${RouterLsa}	Create Ospfv3 Router Lsa	Session=${Session}	Age=20
${LsaLink}	Create Ospfv3 Router Lsa Link	RouterLsa=${RouterLsa}	Metric=65535
Create Ospfv3 Srv6 Endx Sid Sub Tlv	RouterLsaLink=${LsaLink}		
Create Ospfv3 Srv6 Lan Endx Sid Sub Tlv
Arguments
Session
RouterLsaLink
** kwargs
Documentation
创建OSPFv3 Srv6 Lan EndX Sid Sub Tlv对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

RouterLsaLink (:obj:Ospfv3RouterLsaLinksConfig): OSPFv3 Router Lsa LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Srv6 Lan EndX Sid Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

EndpointBehaviorId (int): SRv6 SID的端点行为ID, 类型为：number, 默认值：0

Flags (list): 包含在TLV中的标志位, 类型为：list, 默认值：NONEBIT, 取值范围：

NONEBIT

Unused0

Unused1

Unused2

Unused3

Unused4

PersistentFlag

SetFlag

BackupFlag

Algorithm (int): SID关联的算法, 类型为：number, 取值范围：0-255, 默认值：0

Weight (int): END.X SID / LAN END.X SID的权重，用于负载分担, 类型为：number, 取值范围：0-255, 默认值：1

Sid (str): 通告的SRv6 SID, 邻居路由器ID, 类型为：string, 取值范围：有效的ipv6地址, 默认值：'aaaa:1:1:1::'

Returns:

(:obj:Ospfv3Srv6LanEndXSidSubTlvConfig): OSPFv3 Srv6 Lan EndX Sid Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${RouterLsa}	Create Ospfv3 Router Lsa	Session=${Session}	Age=20
${LsaLink}	Create Ospfv3 Router Lsa Link	RouterLsa=${RouterLsa}	Metric=65535
Create Ospfv3 Srv6 Lan Endx Sid Sub Tlv	RouterLsaLink=${LsaLink}		
Create Ospfv3 Srv6 Link Msd Sub Tlv
Arguments
Session
RouterLsaLink
** kwargs
Documentation
创建OSPFv3 Srv6 Link Msd Sub Tlv对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

RouterLsaLink (:obj:Ospfv3RouterLsaLinksConfig): OSPFv3 Router Lsa LSA列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Srv6 Link Msd Sub Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Msds (list): 包含在TLV中的标志位, 类型为：list, 默认值：NONEBIT, 取值范围：

NONTBIT

MaxiSegmentLeft

MaxiEndPop

MaxiTInsert

MaxiTEncaps

MaxiEndD

MaximumEndDSrh (int): 接收报文的SRH中SL（Segment Left）字段的最大值, 类型为：number, 取值范围：0-255, 默认值：8

MaximumEndPop (int): SRH栈的顶端SRH中SID的最大数量, 类型为：number, 取值范围：0-255, 默认值：8

MaximumSegmentsLeft (int): 执行T.Insert行为时可包含SID的最大数量, 类型为：number, 取值范围：0-255, 默认值：8

MaximumTEncapSrh (int): 执行T.Encap行为时可包含SID的最大数量, 类型为：number, 取值范围：0-255, 默认值：8

MaximumTInsertSrh (int): 执行End.DX6和End.DT6功能时，SRH中SID的最大数量, 类型为：number, 取值范围：0-255, 默认值：8

Returns:

(:obj:Ospfv3Srv6MsdSubTlvConfig): OSPFv3 Srv6 Link Msd Sub Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${RouterLsa}	Create Ospfv3 Router Lsa	Session=${Session}	Age=20
${LsaLink}	Create Ospfv3 Router Lsa Link	RouterLsa=${RouterLsa}	Metric=65535
Create Ospfv3 Srv6 Msd Sid Sub Tlv	RouterLsaLink=${LsaLink}		
Create Ospfv3 Srv6 Location Lsa
Arguments
Session
** kwargs
Documentation
创建OSPFv3 Srv6 Location LSA对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Srv6 Location LSA的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

Scope (str): 起始网络前缀, 类型为：string, 默认值：AreaLocal, 取值范围：

LinkLocal

AreaLocal

AreaSystemWide

AdvertisingRouterId (str): 起始网络前缀, 类型为：string, 取值范围：IPv4地址, 默认值：192.0.0.1

LinkStateId (int): 路由优先级, 类型为：number, 取值范围：1-255, 默认值：0

Age (int): 路由器优先级, 类型为：number, 取值范围：0-3600, 默认值：0

SequenceNumber (int): 序列号, 类型为：hex number, 取值范围：0x1-0xFFFFFFFF, 默认值：0x80000001

Checksum (bool): 校验和, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:Ospfv3Srv6LocatorLsaConfig): OSPFv3 Srv6 Location LSA对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}
Create Ospfv3 Srv6 Location LSA	Session=${Session}	Age=20
Create Ospfv3 Srv6 Location Tlv
Arguments
Session
Lsa
** kwargs
Documentation
创建OSPFv3 Srv6 Location Tlv对象

Args:

Session (:obj:Ospfv3Router): OSPFv3协议会话对象列表, 类型为：object

Lsa (:obj:Ospfv3Srv6LocatorLsaConfig): Ospfv3 Srv6 Location LSA对象, 类型为：object

Keyword Args:

Name (str): 创建的OSPFv3 Srv6 Location Tlv的名称, 类型为：string

Enable (bool): 使能, 类型为：bool, 取值范围：True或False, 默认值：True

RouterType (str): 路由器类型, 类型为：string, 默认值：IntraArea, 支持选项有：

IntraArea

InterArea

ASExternal

NSSAExternal

Algorithm (int): Locator关联算法, 类型为：number, 取值范围：0-255, 默认值：0

LocatorLength (int): Locator前缀长度, 类型为：number, 取值范围：0-128, 默认值：64

Flags (list): 类型为：list, 默认值： NONEBIT, 支持选项有：

NONEBIT

Unused0

Unused1

Unused2

Unused3

Unused4

Unused5

ABit

NFlag

Metric (int): 度量值, 类型为：number, 取值范围：1-16777215, 默认值：1

Locator (str): 通告的Locator, 类型为：string, 取值范围：有效的ipv6地址, 默认值：'aaaa:1:1:1::'

Returns:

(:obj:Ospfv3Srv6LocatorTlvConfig): Ospfv3 Srv6 Location Tlv对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Ospfv3	Port=${Port}	
${Lsa}	Create Ospfv3 Opaque Router Info LSA	Session=${Session}	Age=20
Create Ospfv3 Srv6 Location Tlv	Lsa=${Lsa}		
Create Pcep
Arguments
Port
** kwargs
Documentation
创建PCEP协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): PCEP协会话名称, 类型为：string

Enable (bool): 使能PCEP协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

Role (str): PCEP角色, 类型为：string, 默认值：PCE, 取值范围:

PCE

PCC

IpVersion (str): IP版本, 类型为：string, 默认值：IPv4, 取值范围:

IPv4

IPv6

UseGatewayAsDutIp (bool): 使用网关地址作为DUT地址, 选中则使用接口上配置的网关IP地址作为DUT地址；未选中则自定义DUT IP地址, 类型为：bool, 取值范围：True或False, 默认值：True

SessionIpAddress (str): 会话IP地址, 用于PCEP连接的IP类型, 类型为：string, 默认值：Interface_IP, 取值范围:

Interface_IP

Router_ID

PeerIpv4Address (str): DUT IPv4地址, 使用网关地址作为DUT地址未选中且IP版本为IPv4时可见, 指定DUT的IPv4地址, 类型为：string, 默认值：192.85.1.1, 取值范围：有效的Ipv4地址

PeerIpv4AddressStep (str): DUT IPv4地址跳变, 使用网关地址作为DUT地址未选中且IP版本为IPv4时可见, 指定DUT IPv4地址的增量步长, 类型为：string, 默认值：0.0.0.1, 取值范围：有效的Ipv4地址

PeerIpv6Address (str): DUT IPv6地址, 使用网关地址作为DUT地址未选中且IP版本为IPv6时可见, 指定DUT的IPv6地址, 类型为：string, 默认值：2000::1, 取值范围：有效的Ipv6地址

PeerIpv6AddressStep (str): DUT IPv6地址跳变, 使用网关地址作为DUT地址未选中且IP版本为IPv6时可见, 指定DUT的IPv6地址的增量步长, 类型为：string, 默认值：::1, 取值范围：有效的Ipv6地址

SessionInitiator (bool): 会话发起者, 选中则主动发起会话建立请求；未选中则监听对端的发起会话建立请求。双方均主动发起会话建立请求时，IP地址大的一方优先级更高, 类型为：bool, 取值范围：True或False, 默认值：True

Negotiation (bool): 使能Negotiation, 选中则对Keepalive Timer和Dead Timer的值进行协商, 类型为：bool, 取值范围：True或False, 默认值：True

KeepAlive (str): Keep Alive间隔 (sec), KEEPALIVE消息的发送间隔，以秒为单位, 类型为：string, 默认值：30, 0-65535

MinKeepAlive (int): KEEPALIVE消息发送间隔的最小值。以秒为单位, 类型为：number, 取值范围：0-255, 默认值： 0

MaxKeepAlive (int): KEEPALIVE消息发送间隔的最大值，以秒为单位, 类型为：number, 取值范围：0-255, 默认值： 255

Dead (str): Dead间隔 (sec), 从未收到对端消息到PCEP会话断开连接之间的时间间隔。类型为：string, 取值范围：0-65535, 默认值： 120

MinDeadAlive (int): 最小可接受Dead间隔(sec), 类型为：number, 取值范围：0-255, 默认值： 0

MaxDeadAlive (int): 最大可接受Dead间隔(sec), 类型为：number, 取值范围：0-255, 默认值： 255

EnableStatefulCapability (bool): 选中则OPEN消息中包含Stateful PCE Capability TLV, 类型为：bool, 取值范围：True或False, 默认值： True

StatefulCapability (list): 使能PCE Stateful Capability选中时可见, 单击单元格并从下拉菜单中选择一个或多个能力, 类型为：list, 默认值：['LSP_UPDATE','LSP_INSTANTIATION'], 取值范围:

LSP_UPDATE

INCLUDE_DB_VERSION

LSP_INSTANTIATION

TRIGGERED_RESYNC

DELTA_LSP_SYN

TRIGGERED_INITIAL_SYNC

EnableSegmentRoutingCapability (list): 选择段路由扩展，OPEN消息中将包括该Capability TLV, 类型为：list, 默认值：['SR'], 取值范围：

SR

SRv6

PathSetupTypeList (list): 添加路径建立类型, 类型为：list, 默认值：[0,1]

SrCapabilityFlags (list): 选择一个或多个SR能力标志, PCEP角色为PCC，且使能Segment Routing Capability中选中SR时可见, 类型为：list, 默认值：['NONTBIT','NFlag','XFlag'],

NONTBIT

NFlag

XFlag

Srv6CapabilityFlags (list): 选择一个或多个SRv6能力标志, PCEP角色为PCC，且使能Segment Routing Capability中选中SRv6时可见, 类型为：list, 默认值：['NONTBIT','NFlag','XFlag'],

NONTBIT

NFlag

XFlag

MSDs (list): 选择一个或多个MSD类型, PCEP角色为PCC，且使能Segment Routing Capability中选中SRv6时可见, 类型为：list, 默认值：['NONTBIT']

NONTBIT

MaxiSegmentLeft

MaxiEndPop

MaxiHEncaps

MaxiEndD

MaximumSidDepth (int): 指定SID的最大数量, PCEP角色为PCC，且使能Segment Routing Capability中选中SR时可见, 类型为：number, 默认值：0, 取值范围：0-255

MaxSegmentsLeft (int): 指定MSD取值, PCEP角色为PCC，使能Segment Routing Capability中选中SRv6，且MSDs中选中Maximum Segments Left时可见, 类型为：number, 默认值：8, 取值范围：0-255

MaxEndPop (int): 指定MSD取值, PCEP角色为PCC，使能Segment Routing Capability中选中SRv6，且MSDs中选中Maximum End Pop时可见, 类型为：number, 默认值：8, 取值范围：0-255

MaxHencaps (int): 指定MSD取值, PCEP角色为PCC，使能Segment Routing Capability中选中SRv6，且MSDs中选中Maximum H.Encaps时可见, 类型为：number, 默认值：8, 取值范围：0-255

MaxEndD (int): 指定MSD取值, PCEP角色为PCC，使能Segment Routing Capability中选中SRv6，且MSDs中选中Maximum End D时可见, 类型为：number, 默认值：8, 取值范围：0-255

EnableDbVersionTlv (bool): 选中则配置DB version TLV, 类型为：bool, 取值范围：True或False, 默认值： False

LspStateDbVersion (int): 指定LSP状态数据库的初始版本号, 选中使能DB Version TLV时可见, 类型为：number, 默认值： 1, 取值范围：1-18446744073709551614

Returns:

(:obj:Pcep): PCEP协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Pcep	Port=${Port}
Create Pcep Bw Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Bw Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Bw Object对象名称, 类型为：string

Enable (bool): PCEP Bw Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Bandwidth (str): 类型为：string, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:PcepBwObjectConfig): Pcep Bw Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Bw Object	PcepLsp=${Egress}
Create Pcep Endpoint Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Endpoint Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Endpoint Object对象名称, 类型为：string

Enable (bool): PCEP Endpoint Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PcepEndPointObjectConfig): Pcep Endpoint Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Endpoint Object	PcepLsp=${Egress}
Create Pcep Lsp Auto Tx Parameters
Arguments
PcepAutoParameters
** kwargs
Documentation
创建PCEP PCE Lsp Auto Tx Parameters对象

Args:

PcepAutoParameters(:obj:BgpRouter): : PCEP LSP Auto Parameters对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Auto Tx Parameters对象名称, 类型为：string

Enable (bool): PCEP Auto Tx Parameters对象, 类型为：bool, 取值范围：True或False, 默认值：True

ObjectCategory (str): 选择对象类别, 类型为：string, 默认值：LSP, 取值范围：

BANDWIDTH

RP

NO_PATH

ENDPOINT

METRIC

ERO

RRO

LSPA

SRP

LSP

XRO

SelectObjectHandle (str): 选择对象, 类型为：string, 默认值：""

Returns:

(:obj:PcepAutoTxParametersConfig): Pcep Lsp Auto Tx Parameters对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Parameter}	Create Pcep Pce Auto Update Parameters	PcepLsp=${Egress}
${LspAutoTx}	Create Pcep Lsp Auto Tx Parameters	PcepAutoParameters=${Parameter}
Create Pcep Lspa Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Lspa Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Lspa Object对象名称, 类型为：string

Enable (bool): PCEP Lspa Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

SetupPriority (int): 指定TE LSA抢占资源的优先级。类型为：number, 取值范围：0-7, 默认值：0

HoldingPriority (int): 指定TE LSA持有资源的优先级。类型为：number, 取值范围：0-7, 默认值：0

LFlag (bool): LSPA L Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Affinities (bool): 选中则对32位掩码和链接属性进行比较，设置包含链接条件和排除链接条件, 类型为：bool, 取值范围：True或False, 默认值：False

ExcludeAny (int): Affinities选中时启用, 排除与32位掩码中任何属性匹配的链接, 类型为：number, 取值范围：0-4294967295, 默认值：0

IncludeAny (int): Affinities选中时启用, 包含与32位掩码中任何属性匹配的链接, 类型为：number, 取值范围：0-4294967295, 默认值：0

IncludeAll (int): Affinities选中时启用, 包含与32位掩码中全部属性匹配的链接, 类型为：number, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:PcepLspaObjectConfig): Pcep Lspa Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Lspa Object	PcepLsp=${Egress}
Create Pcep Metric List
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Metric List对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Metric List对象名称, 类型为：string

Enable (bool): PCEP Metric List对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PcepMetricListConfig): Pcep Metric List对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Metric List	PcepLsp=${Egress}
Create Pcep Metric Object
Arguments
PcepMetricLists
** kwargs
Documentation
创建PCEP Metric Object对象

Args:

PcepMetricLists(:obj:BgpRouter): : PCEP Metric List对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Metric Object对象, 类型为：string

Enable (bool): PCEP Metric Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

BoundFlag (bool): PCReq消息中METRIC Object的B(Bound)位是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

ComputedFlag (bool): PCReq消息中METRIC Object的C(Computed Metric)位是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

MetricType (str): 指定度量值类型, 类型为：string, 默认值：MAX_SID_DEPTH, 取值范围:

IGP_METRIC

TE_METRIC

HOP_COUNTS

MAX_SID_DEPTH

MetricValue (int): 指定最大度量值, 类型为：number, 取值范围：0-4294967295, 默认值：10

Returns:

(:obj:PcepMetricObjectConfig): Pcep Metric Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Metric List	PcepLsp=${Egress}
${Subobject}	Create Pcep Metric Object	PcepMetricLists=${Object}
Create Pcep No Path Reason
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP No Path Reason对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCE LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP No Path Object对象名称, 类型为：string

Enable (bool): PCEP No Path Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

NoPathType (str): No-Path类型, 类型为：string, 默认值：NOT_SATISFYING_CONSTRAINTS, 取值范围:

NOT_SATISFYING_CONSTRAINTS

PCE_CHAIN_BROKEN

CFlag (bool): C Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

NoPathReason (str): No-Path原因, 类型为：string, 默认值：NONTBIT, 取值范围:

NONTBIT

PCE_UNAVAILABLE

UNKNOWN_DESTINATION

UNKNOWN_SOURCE

Returns:

(:obj:PcepNoPathObjectConfig): Pcep No Path Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep No Path Object	PcepLsp=${Egress}
Create Pcep Pcc Auto Delegation Parameters
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Auto Delegation Parameters对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCC LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Auto Delegation Parameters对象名称, 类型为：string

Enable (bool): PCEP Auto Delegation Parameters对象, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:PcepAutoDelegationParametersConfig): Pcep Pcc Lsp Auto Delegation Parameters对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Parameter}	Create Pcep Pcc Auto Delegation Parameters	PcepLsp=${Egress}
Create Pcep Pcc Auto Request Parameters
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP PCC Lsp Auto Request Parameters对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCC LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Auto Request Parameters对象名称, 类型为：string

Enable (bool): PCEP Auto Request Parameters对象, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:PcepAutoRequestParametersConfig): Pcep Pce Lsp Auto Request Parameters对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
${Parameter}	Create Pcep Pcc Auto Request Parameters	PcepLsp=${Egress}
Create Pcep Pcc Auto Sync Parameters
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP PCC Lsp Auto Sync Parameters对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCC LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Auto Sync Parameters对象名称, 类型为：string

Enable (bool): PCEP Auto Sync Parameters对象, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:PcepAutoSyncParametersConfig): Pcep Pce Lsp Auto Sync Parameters对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
${Parameter}	Create Pcep Pcc Auto Sync Parameters	PcepLsp=${Egress}
Create Pcep Pcc Lsp
Arguments
Sessions
** kwargs
Documentation
创建PCEP PCC LSP对象

Args:

Sessions(:obj:Pcep): : PCEP协议会话对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP PCC LSP对象名称, 类型为：string

Enable (bool): 使能PCEP PCC LSP, 类型为：bool, 取值范围：True或False, 默认值：True

LspCount (int): Lsp数量, 类型为：number, 默认值：1, 取值范围：1-65535

AutoGenSymbolicName (bool): 系统自动生成Symbolic Name, 类型为：bool, 取值范围：True或False, 默认值：False

SymbolicName (str): 设置Symbolic Name, 类型为：string, 默认值：PLSP_@s

PathSetupType (str): 建立LSP的方法, 类型为：string, 默认值：SEGMENT_ROUTING, 取值范围：

SEGMENT_ROUTING

SRv6

SourceIpv4Address (str): 起始源IP地址, 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

SourceIpv4AddressStep (str): 源IP地址的跳变步长, 类型为：string, 默认值：0.0.0.1, 取值范围: IPv4地址

SourceIpv4AddressSessionOffset: 源IPv4地址接口跳变, 指定PCEP会话块中源IP地址在会话之间的跳变步长, 类型为：string, 默认值：0.0.1.0, 取值范围: IPv4地址

DestinationIpv4Address (str): 起始目的IP地址, 类型为：string, 默认值：193.85.1.1, 取值范围: IPv4地址

DestinationIpv4AddressStep (str): 目的IP地址的跳变步长, 类型为：string, 默认值：0.0.0.1, 取值范围: IPv4地址

DestinationIpv4AddressSessionOffset (str): 目的IPv4地址跳变, 指定PCEP会话块中源IP地址在会话之间的跳变步长, 类型为：string, 默认值：0.0.1.0, 取值范围: IPv4地址

SourceIpv6Address (str): 源IPv6地址的跳变步长, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

SourceIpv6AddressStep (str): 源IPv6地址的跳变步长, 类型为：string, 默认值：::1, 取值范围: IPv6地址

SourceIpv6AddressSessionOffset (str): 源IPv6地址接口跳变, 指定PCEP会话块中源IP地址在会话之间的跳变步长, 类型为：string, 默认值：::1:0, 取值范围: IPv6地址

DestinationIpv6Address (str): 起始目的IPv6地址, 类型为：string, 默认值：2001::1, 取值范围: IPv6地址

DestinationIpv6AddressStep (str): 目的IPv6地址的跳变步长, 类型为：string, 默认值：::1, 取值范围: IPv6地址

DestinationIpv6AddressSessionOffset (str): 目的IPv6地址跳变, 指定PCEP会话块中源IP地址在会话之间的跳变步长, 类型为：string, 默认值：::1:0, 取值范围: IPv6地址

LspInitiateMethod (str): LSP初始方式, 类型为：string, 默认值：REPORT, 取值范围:

REPORT

PCE_INITIATE

SYNCHRONIZATION

REQUEST

ImmediateDelegation (bool): 直接托管, 会话建立后自动将LSP托管给PCE, LSP初始方式为Report Method、Synchronization Method或Request Method时可见, 类型为：bool, 取值范围：True或False, 默认值：True

DelegationInSynchronization (bool): 同步中托管, LSP初始方式为Synchronization Method时可见, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PccLspConfig): Pcep Pcc Lsp对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
Create Pcep Pcc Lsp Info
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP PCC LSP INFO对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCC LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP PCC LSP INFO对象名称, 类型为：string

Enable (bool): PCEP PCC LSP INFO对象, 类型为：bool, 取值范围：True或False, 默认值：True

Administrator (bool): 使能Administrative, 类型为：bool, 取值范围：True或False, 默认值：True

State (str): 设置Initial LSP State, 类型为：string, 默认值：GOING_UP, 取值范围：

DOWN

UP

ACTIVE

GOING_DOWN

GOING_UP

RESERVED_5

RESERVED_6

RESERVED_7

AutoGeneratedPlspId (bool): 自动生成PLSP-ID, 类型为：bool, 取值范围：True或False, 默认值：True

PlspId (int): 指定起始PLSP-ID, 类型为：number, 默认值：1, 取值范围：1-1048575

Step (int): 指定PLSP-ID的跳变步长, 类型为：number, 默认值：1, 取值范围：1-1048575

LspId (int): 指定起始LSP ID, 类型为：number, 默认值：1, 取值范围：1-65535

LspIdStep (int): 指定同一个会话中LSP-ID的跳变步长, 类型为：number, 默认值：1, 取值范围：1-65535

LspIdSessionOffset (int): 指定PCEP会话块中LSP-ID在会话之间的跳变步长, 类型为：number, 默认值：1, 取值范围：1-65535

TunnelId (int): 指定起始隧道ID, 类型为：number, 默认值：1, 取值范围：1-65535

TunnelStep (int): 指定同一个会话中隧道ID的跳变步长, 类型为：number, 默认值：1, 取值范围：1-65535

TunnelSessionOffset (int): 指定PCEP会话块中隧道ID在会话之间的跳变步长, 类型为：number, 默认值：1, 取值范围：1-65535

ExtendedTunnelIPv4Id (str): 指定扩展隧道ID, 类型为：string, 默认值：10.0.0.1, 取值范围: IPv4地址

ExtendedTunnelIPv4IdStep (str): 指定同一个会话中扩展隧道ID的跳变步长, 类型为：string, 默认值：0.0.0.1, 取值范围: IPv4地址

ExtendedTunnelIPv4IdSessionOffset (str): 指定PCEP会话块中扩展隧道ID在会话之间的跳变步长, 类型为：string, 默认值：0.0.1.0, 取值范围: IPv4地址

ExtendedTunnelIPv6Id (str): 指定扩展隧道ID, 类型为：string, 默认值：2000:1::1, 取值范围: IPv6地址

ExtendedTunnelIPv6IdStep (str): 指定同一个会话中扩展隧道ID的跳变步长, 类型为：string, 默认值：::1, 取值范围: IPv6地址

ExtendedTunnelIPv6IdSessionOffset: 指定PCEP会话块中扩展隧道ID在会话之间的跳变步长, 类型为：string, 默认值：::1:0, 取值范围: IPv6地址

Returns:

(:obj:PccLspInfoObjectConfig): Pcep Pcc Lsp Info对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
${LspInfo}	Create Pcep Pcc Lsp Info	PcepLsp=${Egress}
Create Pcep Pce Auto Initiate Parameters
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP PCE Lsp Auto Initiate Parameters对象

Args:

PcepLsps(:obj:PceLspConfig): : PCEP PCE LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Auto Initiate Parameters对象名称, 类型为：string

Enable (bool): PCEP Auto Initiate Parameters对象, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:PcepAutoInitiateParametersConfig): Pcep Pce Lsp Auto Initiate Parameters对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Parameter}	Create Pcep Pce Auto Initiate Parameters	PcepLsp=${Egress}
Create Pcep Pce Auto Reply Parameters
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP PCE Lsp Auto Reply Parameters对象

Args:

PcepLsps(:obj:PceLspConfig): : PCEP PCE LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Auto Reply Parameters对象名称, 类型为：string

Enable (bool): PCEP Auto Reply Parameters对象, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:PcepAutoReplyParametersConfig): Pcep Pce Lsp Auto Reply Parameters对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Parameter}	Create Pcep Pce Auto Reply Parameters	PcepLsp=${Egress}
Create Pcep Pce Auto Update Parameters
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP PCE Lsp Auto Update Parameters对象

Args:

PcepLsps(:obj:PceLspConfig): : PCEP PCE LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Auto Update Parameters对象名称, 类型为：string

Enable (bool): PCEP Auto Update Parameters对象, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:PcepAutoUpdateParametersConfig): Pcep Pce Lsp Auto Update Parameters对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Parameter}	Create Pcep Pce Auto Update Parameters	PcepLsp=${Egress}
Create Pcep Pce Lsp
Arguments
Sessions
** kwargs
Documentation
创建PCEP PCE LSP对象

Args:

Sessions(:obj:Pcep): : PCEP协议会话对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP PCE LSP对象名称, 类型为：string

Enable (bool): 使能PCEP PCE LSP, 类型为：bool, 取值范围：True或False, 默认值：True

LspCount (int): Lsp数量, 类型为：number, 默认值：1, 取值范围：1-65535

AutoGenSymbolicName (bool): 系统自动生成Symbolic Name, 类型为：bool, 取值范围：True或False, 默认值：False

SymbolicName (str): 设置Symbolic Name, 类型为：string, 默认值：PLSP_@s

PathSetupType (str): 建立LSP的方法, 类型为：string, 默认值：SEGMENT_ROUTING, 取值范围：

SEGMENT_ROUTING

SRv6

SourceIpv4Address (str): 起始源IP地址, 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

SourceIpv4AddressStep (str): 源IP地址的跳变步长, 类型为：string, 默认值：0.0.0.1, 取值范围: IPv4地址

SourceIpv4AddressSessionOffset: 源IPv4地址接口跳变, 指定PCEP会话块中源IP地址在会话之间的跳变步长, 类型为：string, 默认值：0.0.1.0, 取值范围: IPv4地址

DestinationIpv4Address (str): 起始目的IP地址, 类型为：string, 默认值：193.85.1.1, 取值范围: IPv4地址

DestinationIpv4AddressStep (str): 目的IP地址的跳变步长, 类型为：string, 默认值：0.0.0.1, 取值范围: IPv4地址

DestinationIpv4AddressSessionOffset: 目的IPv4地址跳变, 指定PCEP会话块中源IP地址在会话之间的跳变步长, 类型为：string, 默认值：0.0.1.0, 取值范围: IPv4地址

SourceIpv6Address (str): 源IPv6地址的跳变步长, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

SourceIpv6AddressStep (str): 源IPv6地址的跳变步长, 类型为：string, 默认值：::1, 取值范围: IPv6地址

SourceIpv6AddressSessionOffset: 源IPv6地址接口跳变, 指定PCEP会话块中源IP地址在会话之间的跳变步长, 类型为：string, 默认值：::1:0, 取值范围: IPv6地址

DestinationIpv6Address (str): 起始目的IPv6地址, 类型为：string, 默认值：2001::1, 取值范围: IPv6地址

DestinationIpv6AddressStep (str): 目的IPv6地址的跳变步长, 类型为：string, 默认值：::1, 取值范围: IPv6地址

DestinationIpv6AddressSessionOffset: 目的IPv6地址跳变, 指定PCEP会话块中源IP地址在会话之间的跳变步长, 类型为：string, 默认值：::1:0, 取值范围: IPv6地址

LspInitiateMethod (str): LSP初始方式, 类型为：string, 默认值：UPDATE, 取值范围:

UPDATE

PCE_INITIATE

REPLY

ImmediateUpdate (bool): 直接更新, 类型为：bool, 取值范围：True或False, 默认值：True

Returns:

(:obj:PceLspConfig): Pcep Pce Lsp对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
Create Pcep Pce Lsp Info
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP PCE LSP INFO对象

Args:

PcepLsps(:obj:PceLspConfig): : PCEP PCE LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP PCE LSP INFO对象名称, 类型为：string

Enable (bool): PCEP PCE LSP INFO对象, 类型为：bool, 取值范围：True或False, 默认值：True

Administrator (bool): 使能Administrative, 类型为：bool, 取值范围：True或False, 默认值：True

State (str): 设置Initial LSP State, 类型为：string, 默认值：GOING_UP, 取值范围：

DOWN

UP

ACTIVE

GOING_DOWN

GOING_UP

RESERVED_5

RESERVED_6

RESERVED_7

Returns:

(:obj:PceLspInfoObjectConfig): Pcep Pce Lsp Info对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Info}	Create Pcep Pce Lsp Info	PcepLsp=${Egress}
Create Pcep Rp Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP PCC Rp Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCC LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP PCC Rp Object对象名称, 类型为：string

Enable (bool): PCEP PCC Rp Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

AutoGeneratedId (bool): 自动生成RP-ID 类型为：bool, 取值范围：True或False, 默认值：True

RpId (int): 指定起始RP-ID, Auto-Generated RP-ID未选中时启用, 类型为：number, 取值范围：0-4294967295, 默认值：1

RpIdStep (int): 指定PLSP-ID的跳变步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

Priority (int): 指定请求的优先级。数字越大，优先级越高, 类型为：number, 取值范围：0-7, 默认值：0

PFlag (bool): PCReq消息中P Flag置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCRep消息中I Flag置位, 类型为：bool, 取值范围：True或False, 默认值：False

BFlag (bool): RP Object的B(Bi-directional)位置位, 类型为：bool, 取值范围：True或False, 默认值：False

OFlag (bool): RP Object的O(strict/loose)位置位, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PcepRpObjectConfig): Pcep Pcc Rp Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
${Parameter}	Create Pcep Rp Object	PcepLsp=${Egress}
Create Pcep Sr Ero Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Sr Ero Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Sr Ero Object对象名称, 类型为：string

Enable (bool): PCEP Sr Ero Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PcepSrEroObjectConfig): Pcep Metric List对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Sr Ero Object	PcepLsp=${Egress}
Create Pcep Sr Ero Sub Object
Arguments
PcepSrEroObjects
** kwargs
Documentation
创建PCEP Sr Ero Sub Object对象

Args:

PcepSrEroObjects(:obj:PcepSrEroObjectConfig): : PCEP PCE LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Sr Ero Sub Object对象名称, 类型为：string

Enable (bool): PCEP Sr Ero Sub Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

RouteType (str): PCReq消息中P Flag是否置位, 类型为：string, 默认值：STRICT, 取值范围:

STRICT

LOOSE

NaiType (str): PCReq消息中I Flag是否置位, 类型为：string, 默认值：IPV4_NODE_ID, 取值范围:

ABSENT

IPV4_NODE_ID

IPV6_NODE_ID

IPV4_ADJACENCY

IPV6_ADJACENCY_GLOBAL

UNNUMBERED_ADJACENCY

IPV6_ADJACENCY_LINK_LOCAL

MFlag (bool): M Flag, 类型为：bool, 取值范围：True或False, 默认值：True

CFlag (bool): C Flag, 类型为：bool, 取值范围：True或False, 默认值：False

SFlag (bool): 类型为：bool, 取值范围：True或False, 默认值：False

FFlag (bool): F Flag, 类型为：bool, 取值范围：True或False, 默认值：False

SidLabel (int): SID Label, 类型为：number, 取值范围：0-1048575, 默认值：16

SidLabelStep (int): SID Label跳变, 类型为：number, 取值范围：0-1048575, 默认值：0

SidLabelSessionOffset (int): SID Label接口间跳变, 类型为：number, 取值范围：0-1048575, 默认值：0

SidIndex (int): SID Index（32 Bits）, 类型为：number, 取值范围：0-4294967295, 默认值：1

SidIndexStep (int): SID Index跳变（32 Bits）, 类型为：number, 取值范围：0-4294967295, 默认值：0

SidIndexSessionOffset (int): SID Index接口间跳变（32 Bits）, 类型为：number, 取值范围：0-1048575, 默认值：0

SidTrafficClass (int): SID Traffic Class（3 bits）, 类型为：number, 取值范围：0-7, 默认值：0

SidTimeToLive (int): SID Time To Liv, 类型为：number, 取值范围：0-255, 默认值：255

SidBottomOfStack (bool): SID Bottom Of Stack Flag（1 Bit）, 类型为：bool, 取值范围：True或False, 默认值：False

NaiIpv4NodeId (str): NAI IPv4 Node ID, 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

NaiIpv6NodeId (str): NAI IPv6 Node ID, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiLocalIpv4Address (str): NAI Local IPv4 Address, 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

NaiLocalIpv6Address (str): NAI Local IPv6 Address, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiRemoteIpv4Address (str): NAI Remote IPv4 Address, 类型为：string, 默认值：193.85.1.1, 取值范围: IPv4地址

NaiRemoteIpv6Address (str): NAI Remote IPv6 Address, 类型为：string, 默认值：2001::1, 取值范围: IPv6地址

NaiLocalNodeId (str): NAI Local Node-ID, 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

NaiLocalInterfaceId (int): NAI Local Interface ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

NaiRemoteNodeId (str): NAI Remote Node-ID, 类型为：string, 默认值：193.85.1.1, 取值范围: IPv4地址

NaiRemoteInterfaceId (int): NAI Remote Interface ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:PcepSrEroSubObjectConfig): Pcep Sr Ero Sub Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Sr Ero Object	PcepLsp=${Egress}
${Subobject}	Create Pcep Sr Ero Sub Object	PcepSrEroObjects=${Object}
Create Pcep Sr Rro Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Sr Rro Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCC LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Sr Ero Object对象名称, 类型为：string

Enable (bool): PCEP Sr Ero Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PcepSrRroObjectConfig): Pcep Metric List对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
${Object}	Create Pcep Sr Rro Object	PcepLsp=${Egress}
Create Pcep Sr Rro Sub Object
Arguments
PcepSrRroObjects
** kwargs
Documentation
创建PCEP Sr Rro Sub Object对象

Args:

PcepLsps(:obj:PcepSrRroObjectConfig): : PCEP PCE Sr Rro对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Sr Rro Sub Object对象名称, 类型为：string

Enable (bool): PCEP Sr Rro Sub Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

NaiType (str): 子对象中NT字段的值, 类型为：string, 默认值：IPV4_NODE_ID, 取值范围:

ABSENT

IPV4_NODE_ID

IPV6_NODE_ID

IPV4_ADJACENCY

IPV6_ADJACENCY_GLOBAL

UNNUMBERED_ADJACENCY

IPV6_ADJACENCY_LINK_LOCAL

MFlag (bool): 子对象中的M Flag置位, 类型为：bool, 取值范围：True或False, 默认值：True

CFlag (bool): 子对象中的C Flag置位, 类型为：bool, 取值范围：True或False, 默认值：False

SFlag (bool): 子对象中的S Flag置位, 类型为：bool, 取值范围：True或False, 默认值：False

FFlag (bool): 子对象中的F Flag置位, 类型为：bool, 取值范围：True或False, 默认值：False

SidIndex (int): 指定起始SID Index, 类型为：number, 取值范围：0-1048575, 默认值：1

SidLabel (int): 指定起始SID Label, 类型为：number, 取值范围：0-1048575, 默认值：16

SidTrafficClass (int): 指定流量类型字段的值, 类型为：number, 取值范围：0-7, 默认值：0

SidTimeToLive (int): 指定TTL字段值, 类型为：number, 取值范围：0-255, 默认值：255

SidBottomOfStack (bool): 是否指定的SID Label为标签栈的栈底标签, 类型为：bool, 取值范围：True或False, 默认值：False

NaiIpv4NodeId (str): 指定NAI IPv4节点ID, 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

NaiIpv6NodeId (str): 指定NAI IPv6节点ID, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiLocalIpv4Address (str): 指定NAI本地IPv4地址, 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

NaiLocalIpv6Address (str): 指定NAI本地IPv6地址, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiRemoteIpv4Address (str): 指定NAI远端IPv4地址, 类型为：string, 默认值：193.85.1.1, 取值范围: IPv4地址

NaiRemoteIpv6Address (str): 指定NAI远端IPv6地址, 类型为：string, 默认值：2001::1, 取值范围: IPv6地址

NaiLocalNodeId (str): 指定NAI远端节点ID, 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

NaiLocalInterfaceId (int): 指定NAI本地接口ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

NaiRemoteNodeId (str): 指定NAI远端节点ID, 类型为：string, 默认值：193.85.1.1, 取值范围: IPv4地址

NaiRemoteInterfaceId (int): 指定NAI远端接口ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:PcepSrRroSubObjectConfig): Pcep Sr Ero Sub Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
${Object}	Create Pcep Sr Rro Object	PcepLsp=${Egress}
${Subobject}	Create Pcep Sr Rro Sub Object	PcepSrRroObjects=${Object}
Create Pcep Srp Info
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Srp Info对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCE LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Srp Info对象名称, 类型为：string

Enable (bool): PCEP Srp Info对象, 类型为：bool, 取值范围：True或False, 默认值：True

AutoGeneratedId (bool): 自动生成SRP-ID, 类型为：bool, 取值范围：True或False, 默认值：True

SrpId (int): 指定起始SRP-ID, 类型为：number, 取值范围：0-4294967295, 默认值：1

SrpIdStep (int): 指定SRP-ID的跳变步长, 类型为：number, 取值范围：0-4294967295, 默认值：1

Returns:

(:obj:PcepSrpObjectConfig): Pcep Srp Info对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Srp Info	PcepLsp=${Egress}
Create Pcep Srv6 Ero Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Srv6 Ero Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Srv6 Ero Object对象名称, 类型为：string

Enable (bool): PCEP Srv6 Ero Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PcepSrv6EroObjectConfig): Pcep Srv6 Ero Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Srv6 Ero Object	PcepLsp=${Egress}
Create Pcep Srv6 Ero Sub Object
Arguments
PcepSrv6EroObjects
** kwargs
Documentation
创建PCEP Srv6 Ero Sub Object对象

Args:

PcepSrv6EroObjects(:obj:PcepSrv6EroObjectConfig): : PCEP Srv6 Ero对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Srv6 Ero Sub Object对象名称, 类型为：string

Enable (bool): PCEP Srv6 Ero Sub Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

RouteType (str): 建立LSP使用的路由类型, 类型为：string, 默认值：STRICT, 取值范围:

STRICT

LOOSE

NaiType (str): 指定端点行为, 类型为：string, 默认值：IPV6_NODE_ID, 取值范围:

ABSENT

IPV4_NODE_ID

IPV6_NODE_ID

IPV4_ADJACENCY

IPV6_ADJACENCY_GLOBAL

UNNUMBERED_ADJACENCY

IPV6_ADJACENCY_LINK_LOCAL

SFlag (bool): 子对象中的S Flag置位, 类型为：bool, 取值范围：True或False, 默认值：False

FFlag (bool): 子对象中的F Flag置位, 类型为：bool, 取值范围：True或False, 默认值：False

EndpointBehavior (str): 指定端点行为, 类型为：string, 默认值：Invalid, 取值范围:

Invalid

EndNoPspUsp

EndPsp

EndUsp

EndPspUsp

EndXNoPspUsp

EndXPsp

EndXUsp

EndXPspUsp

EndTNoPspUsp

EndTPsp

EndTUsp

EndTPspUsp

EndB6Encaps

EndBM

EndDX6

EndDX4

EndDT6

EndDT4

EndDT46

EndDX2

EndDX2V

EndDT2U

EndDT2M

ENDB6EncapsRed

EndUSD

EndPSPUSD

EndUSPUSD

EndPSPUSPUSD

EndXUSD

EndXPSPUSD

EndXUSPUSD

EndXPSPUSPUSD

EndTUSD

EndTPSPUSD

EndTUSPUSD

EndTPSPUSPUSD

SRv6Sid (str): 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiIpv6NodeId (str): 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiLocalIpv6Address (str): 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiRemoteIpv6Address (str): 类型为：string, 默认值：2001::1, 取值范围: IPv6地址

NaiLocalInterfaceId (int): 类型为：number, 取值范围：0-4294967295, 默认值：0

NaiRemoteInterfaceId (int): 类型为：number, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:PcepSrv6EroSubObjectConfig): Pcep Srv6 Ero Sub Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Srv6 Ero Object	PcepLsp=${Egress}
${Subobject}	Create Pcep Srv6 Ero Sub Object	PcepSrEroObjects=${Object}
Create Pcep Srv6 Rro Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP Srv6 Rro Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP PCC LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Srv6 Rro Object对象名称, 类型为：string

Enable (bool): PCEP Srv6 Rro Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PcepSrv6RroObjectConfig): Pcep Srv6 Rro Onject对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
${Object}	Create Pcep Srv6 Rro Object	PcepLsp=${Egress}
Create Pcep Srv6 Rro Sub Object
Arguments
PcepSrv6RroObjects
** kwargs
Documentation
创建PCEP Srv6 Rro Sub Object对象

Args:

PcepSrv6RroObjects(:obj:PcepSrv6RroObjectConfig): : PCEP Srv6 Rro对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Srv6 Rro Sub Object对象名称, 类型为：string

Enable (bool): PCEP Srv6 Rro Sub Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

NaiType (str): 子对象中NT字段的值, 类型为：string, 默认值：IPV6_NODE_ID, 取值范围:

ABSENT

IPV4_NODE_ID

IPV6_NODE_ID

IPV4_ADJACENCY

IPV6_ADJACENCY_GLOBAL

UNNUMBERED_ADJACENCY

IPV6_ADJACENCY_LINK_LOCAL

SFlag (bool): 子对象中的S Flag置位, 类型为：bool, 取值范围：True或False, 默认值：False

FFlag (bool): 子对象中的F Flag置位, 类型为：bool, 取值范围：True或False, 默认值：False

EndpointBehavior (str): 指定端点行为, 类型为：string, 默认值：Invalid, 取值范围:

Invalid

EndNoPspUsp

EndPsp

EndUsp

EndPspUsp

EndXNoPspUsp

EndXPsp

EndXUsp

EndXPspUsp

EndTNoPspUsp

EndTPsp

EndTUsp

EndTPspUsp

EndB6Encaps

EndBM

EndDX6

EndDX4

EndDT6

EndDT4

EndDT46

EndDX2

EndDX2V

EndDT2U

EndDT2M

ENDB6EncapsRed

EndUSD

EndPSPUSD

EndUSPUSD

EndPSPUSPUSD

EndXUSD

EndXPSPUSD

EndXUSPUSD

EndXPSPUSPUSD

EndTUSD

EndTPSPUSD

EndTUSPUSD

EndTPSPUSPUSD

SRv6Sid (str): 指定SRv6 SID, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiIpv6NodeId (str): 指定NAI IPv6节点ID, 指定NAI IPv6节点ID, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiLocalIpv6Address (str): 指定NAI本地IPv6地址, 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

NaiRemoteIpv6Address (str): 指定NAI远端IPv6地址, 类型为：string, 默认值：2001::1, 取值范围: IPv6地址

NaiLocalInterfaceId (int): 指定NAI本地接口ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

NaiRemoteInterfaceId (int): 指定NAI远端接口ID, 类型为：number, 取值范围：0-4294967295, 默认值：0

Returns:

(:obj:PcepSrv6RroSubObjectConfig): Pcep Srv6 Rro Sub Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pcc Lsp	Sessions=${Session}
${Object}	Create Pcep Srv6 Rro Object	PcepLsp=${Egress}
${Subobject}	Create Pcep Srv6 Rro Sub Object	PcepSrv6RroObjects=${Object}
Create Pcep Xro Object
Arguments
PcepLsps
** kwargs
Documentation
创建PCEP XRO Object对象

Args:

PcepLsps(:obj:PccLspConfig): : PCEP LSP对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP XRO Object对象名称, 类型为：string

Enable (bool): PCEP XRO Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

PFlag (bool): PCReq消息中P Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：True

IFlag (bool): PCReq消息中I Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

FFlag (bool): PCReq消息中F Flag是否置位, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:PcepXroObjectConfig): Pcep XRO Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep XRO Object	PcepLsp=${Egress}
Create Pcep Xro Sub Object
Arguments
PcepXroObjects
** kwargs
Documentation
创建PCEP XRO Object对象

Args:

PcepXroObjects(:obj:PcepXroObjectConfig): : PCEP XRO Object对象列表, 类型为：object / list

Keyword Args:

Name (str): PCEP Xro Sub Object对象名称, 类型为：string

Enable (bool): PCEP Xro Sub Object对象, 类型为：bool, 取值范围：True或False, 默认值：True

XFlag (bool): 类型为：bool, 取值范围：True或False, 默认值：False

Type (str): 类型为：string, 默认值：IPv4_PREFIX, 取值范围:

IPv4_PREFIX

IPv6_PREFIX

UNNUMBERED_INTERFACE_ID

AUTONOMOUS_SYS_NUM

SRLG

PrefixLength (int): 类型为：number, 取值范围：0-32, 默认值：24

Attribute (str): 类型为：string, 默认值：INTERFACE, 取值范围:

INTERFACE

NODE

SRLG

Ipv4Address (str): 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

Ipv6Address (str): 类型为：string, 默认值：2000::1, 取值范围: IPv6地址

TeRouterId (str): 类型为：string, 默认值：192.85.1.1, 取值范围: IPv4地址

InterfaceId (int): 类型为：number, 默认值：0

AsNumber (int): 类型为：number, 默认值：0

SrlgId (int): 类型为：number, 默认值：0

Returns:

(:obj:PcepXroSubObjectConfig): Pcep Xro Sub Object对象列表, 类型: object / list

Examples: .. code:: RobotFramework

${Session}	Create Pcep	Port=${Port}
Edit Pcep	Session=${Session}	HelloType=DIRECT_TARGETED
${Egress}	Create Pcep Pce Lsp	Sessions=${Session}
${Object}	Create Pcep Xro Object	PcepLsp=${Egress}
${Subobject}	Create Pcep Xro Sub Object	PcepXroObjects=${Object}
Create Peclsp For Srte
Arguments
Excel
Session
TunnelCount
=
16000
PcelspCount
=
4000
SymbolicNameIdentification
=
Tunnel
Documentation
从Excel表格创建SRTE性能测试PCE LSP

Args:

Excel: Excel文件完整路径

Session: PceLspConfig对象

TunnelCount: 隧道数量

PcelspCount: pcelsp数量

Returns:

bool: 布尔值Bool (范围：True / False)

Examples:

Create Pim
Arguments
Port
** kwargs
Documentation
创建PIM协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): PIM协会话名称, 类型为：string

Enable (bool): 使能PIM协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

SessionMode (str): 协议模式, 类型为：string, 默认值：SM, 支持版本：

SM

SSM

IpVersion (str): IP版本, 类型为：string, 默认值：IPV4, 支持版本：

IPV4

IPV6

DrPriority (int): DR优先级, 类型为：number, 取值范围：1-65535, 默认值：1

DrAddr (str): DR地址, 类型为：string, 取值范围：IPv4地址, 默认值：0.0.0.0

DrIpv6Addr (str): DR IPv6地址, 类型为：string, 取值范围：IPv6地址, 默认值：'::'

GenIdMode (str): GenID模式, 类型为：string, 默认值：FIXED, 支持参数：

FIXED

INCR

RAND

RegisterEnable (bool): Register使能, 类型为：bool, 取值范围：True或False, 默认值：False

BsrEnable (bool): BSR使能, 类型为：bool, 取值范围：True或False, 默认值：False

BsrPriority (int): BSR优先级, 类型为：number, 取值范围：0-255, 默认值：1

BsrInterval (int): BSR消息发送时间间隔（秒）, 类型为：number, 取值范围：1-3600, 默认值：60

HelloInterval (int): Hello消息发送时间间隔（秒）, 类型为：number, 取值范围：1-3600, 默认值：30

HelloHoldTime (int): Hello消息超时时间（秒）, 类型为：number, 取值范围：1-65535, 默认值：105

JoinPruneInterval (int): Join/Prune消息发送时间间隔（秒）, 类型为：number, 取值范围：1-65535, 默认值：60

JoinPruneHoldTime (int): Join/Prune消息超时时间（秒）, 类型为：number, 取值范围：1-65535, 默认值：210

Returns:

(:obj:PimRouter): PIM协议会话对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Pim	Port=${Port}
${DrAddr}	Set Variable	${Session.DrAddr}
Create Pim Group
Arguments
Session
** kwargs
Documentation
创建PIM Group对象

Args:

Session (:obj:PimRouter): PIM协议会话对象列表, 类型为：object

Keyword Args:

Name (str): PIM Group对象名称, 类型为：string

Enable (bool): 使能PIM Group对象, 类型为：bool, 取值范围：True或False, 默认值：True

GroupCheck (bool): 协议模式, 类型为：bool, 取值范围：True或False, 默认值：False

GroupType (str): 组类别, 类型为：string, 默认值：ANY_G, 支持版本：

ANY_G

S_G

S_G_RPT

ANY_RP

GroupAddr (str): 组地址, 类型为：string, 取值范围：IPv4地址, 默认值：225.0.0.1

GroupCount (int): 组数目, 类型为：number, 取值范围：1-65535（BigTao） 1-500000（DarYu）, 默认值：1

GroupModifierStep (int): 组地址增量步进, 类型为：number, 取值范围：0-65535, 默认值：1

GroupModifierBit (int): 组地址增量位, 类型为：number, 取值范围：1-32, 默认值：32

RpAddr (str): RP地址, 类型为：string, 取值范围：IPv4地址, 默认值：10.10.10.10

JoinSrc (str): Join源地址, 类型为：string, 取值范围：IPv4地址, 默认值：1.1.1.1

JoinMaskLen (int): Join掩码长度, 类型为：number, 取值范围：1-32, 默认值：32

PruneSrcAddr: Prune源地址, 类型为：string, 取值范围：IPv4地址, 默认值：1.1.1.1

PruneMaskLen (int): Prune掩码长度, 类型为：number, 取值范围：1-32, 默认值：32

Returns:

(:obj:PimGroupConfig): PIM Group对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Pim	Port=${Port}
Create Pim Group	Session=${Session}	GroupAddr=255.0.0.2
Create Pim Ipv6 Group
Arguments
Session
** kwargs
Documentation
创建PIM IPv6 Group对象

Args:

Session (:obj:PimRouter): PIM协议会话对象列表, 类型为：object

Keyword Args:

Name (str): PIM IPv6 Group对象名称, 类型为：string

Enable (bool): 使能PIM IPv6 Group对象, 类型为：bool, 取值范围：True或False, 默认值：True

GroupCheck (bool): 协议模式, 类型为：bool, 取值范围：True或False, 默认值：False

GroupType (str): 组类别, 类型为：string, 默认值：ANY_G, 支持版本：

ANY_G

S_G

S_G_RPT

ANY_RP

GroupAddr (str): 组地址, 类型为：string, 取值范围：IPv6地址, 默认值：ff1e::1

GroupCount (int): 组数目, 类型为：number, 取值范围：1-65535（BigTao） 1-500000（DarYu）, 默认值：1

GroupModifierStep (int): 组地址增量步进, 类型为：number, 取值范围：0-65535, 默认值：1

GroupModifierBit (int): 组地址增量位, 类型为：number, 取值范围：1-128, 默认值：128

RpAddr (str): RP地址, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

JoinSrc (str): Join源地址, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

JoinMaskLen (int): Join掩码长度, 类型为：number, 取值范围：1-128, 默认值：64

PruneSrcAddr (str): Prune源地址, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

PruneMaskLen (int): Prune掩码长度, 类型为：number, 取值范围：1-128, 默认值：64

Returns:

(:obj:PimIpv6GroupConfig): PIM IPv6 Group对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Pim	Port=${Port}
Create Pim IPv6 Group	Session=${Session}	GroupAddr=ff1e::2
Create Pim Ipv6 Register Group
Arguments
Session
** kwargs
Documentation
创建PIM IPv6 Register Group对象

Args:

Session (:obj:PimRouter): PIM协议会话对象列表, 类型为：object

Keyword Args:

Name (str): PIM IPv6 Register Group对象名称, 类型为：string

Enable (bool): 使能PIM IPv6 Register Group对象, 类型为：bool, 取值范围：True或False, 默认值：True

MulticastGroupToSourceDistribution (str): 组播地址和源地址映射方式, 类型为：string, 默认值：PAIR, 支持参数：

PAIR

BACKBONE

RegisterTransmitMode (str): 注册发送模式, 类型为：string, 默认值：CONTINUOUS, 支持参数：

FIXED

CONTINUOUS

FixedModeCount (int): 固定模式数量, 类型为：number, 取值范围：1-1000, 默认值：5

MulticastGroupCount (int): 多播组数量, 类型为：number, 取值范围：1-65535, 默认值：1

StartMulticastGroupAddr (str): 多播组起始地址, 类型为：string, 取值范围：IPv6地址, 默认值：ff1e::2

MulticastGroupStep (int): 多播组步长, 类型为：number, 取值范围：1-255, 默认值：1

MulticastGroupPrefixLength (int): 多播组前缀长度, 类型为：number, 取值范围：1-128, 默认值：64

MulticastSourceCount (int): 组播源数量, 类型为：number, 取值范围：1-65535, 默认值：1

StartMulticastSourceAddr (str): 多播组起始地址, 类型为：string, 取值范围：IPv6地址, 默认值：2001::1

MulticastSourceStep (int): 多播组步长, 类型为：number, 取值范围：1-255, 默认值：1

MulticastSourcePrefixLength (int): 多播组前缀长度, 类型为：number, 取值范围：1-128, 默认值：64

RpAddr (str): RP地址, 类型为：string, 取值范围：IPv6地址, 默认值：2000::2

RegisterTransmitInterval (int): Register发送时间间隔（秒）, 类型为：number, 取值范围：10-180, 默认值：60

Returns:

(:obj:PimIpv6RegisterGroupConfig): Create Pim Ipv6 Register Group对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Pim	Port=${Port}
Create Pim Ipv6 Register Group	Session=${Session}	RpAddr=3000::2
Create Pim Ipv6 Rp Map
Arguments
Session
** kwargs
Documentation
创建PIM IPv6 Rp Map对象

Args:

Session (:obj:PimRouter): PIM协议会话对象列表, 类型为：object

Keyword Args:

Name (str): PIM IPv6 Rp Map对象名称, 类型为：string

Enable (bool): 使能PIM IPv6 Rp Map对象, 类型为：bool, 取值范围：True或False, 默认值：True

MulticastGroupAddr (str): 组播地址和源地址映射方式, 类型为：string, 取值范围：IPv6地址, 默认值：ff1e::1

RpAddr (str): RP地址, 类型为：string, 取值范围：IPv6地址, 默认值：2000::1

PrefixLength (int): Register发送时间间隔（秒）, 类型为：number, 取值范围：0-128, 默认值：128

RpPriority (int): Register发送时间间隔（秒）, 类型为：number, 取值范围：0-255, 默认值：0

RpHoldTime (int): Register发送时间间隔（秒）, 类型为：number, 取值范围：1-65535, 默认值：150

Returns:

(:obj:PimIpv6RpMapConfig): PIM IPv6 Rp Map对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Pim	Port=${Port}
Create Pim Ipv6 Rp Map	Session=${Session}	RpAddr=3000::1
Create Pim Register Group
Arguments
Session
** kwargs
Documentation
创建PIM IPv4 Register Group对象

Args:

Session (:obj:PimRouter): PIM协议会话对象列表, 类型为：object

Keyword Args:

Name (str): PIM IPv4 Register Group对象名称, 类型为：string

Enable (bool): 使能PIM IPv4 Register Group对象, 类型为：bool, 取值范围：True或False, 默认值：True

MulticastGroupToSourceDistribution (str): 组播地址和源地址映射方式, 类型为：string, 默认值：PAIR, 支持参数：

PAIR

BACKBONE

RegisterTransmitMode (str): 注册发送模式, 类型为：string, 默认值：CONTINUOUS, 支持参数：

FIXED

CONTINUOUS

FixedModeCount (int): 固定模式数量, 类型为：number, 取值范围：1-1000, 默认值：5

MulticastGroupCount (int): 多播组数量, 类型为：number, 取值范围：1-65535, 默认值：1

StartMulticastGroupAddr (str): 多播组起始地址, 类型为：string, 取值范围：IPv4地址, 默认值：225.0.1.1

MulticastGroupStep (int): 多播组步长, 类型为：number, 取值范围：1-255, 默认值：1

MulticastGroupPrefixLength (int): 多播组前缀长度, 类型为：number, 取值范围：1-32, 默认值：24

MulticastSourceCount (int): 组播源数量, 类型为：number, 取值范围：1-65535, 默认值：1

StartMulticastSourceAddr (str): 多播组起始地址, 类型为：string, 取值范围：IPv4地址, 默认值：192.168.1.1

MulticastSourceStep (int): 多播组步长, 类型为：number, 取值范围：1-255, 默认值：1

MulticastSourcePrefixLength (int): 多播组前缀长度, 类型为：number, 取值范围：1-32, 默认值：24

RpAddr (str): RP地址, 类型为：string, 取值范围：IPv4地址, 默认值：10.10.10.20

RegisterTransmitInterval (int): Register发送时间间隔（秒）, 类型为：number, 取值范围：10-180, 默认值：60

Returns:

(:obj:PimRegisterGroupConfig): PIM IPv4 Register Group对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Pim	Port=${Port}
Create Pim Register Group	Session=${Session}	RpAddr=20.10.10.20
Create Pim Rp Map
Arguments
Session
** kwargs
Documentation
创建PIM IPv4 Rp Map对象

Args:

Session (:obj:PimRouter): PIM协议会话对象列表, 类型为：object

Keyword Args:

Name (str): PIM IPv4 Rp Map对象名称, 类型为：string

Enable (bool): 使能PIM IPv4 Rp Map对象, 类型为：bool, 取值范围：True或False, 默认值：True

MulticastGroupAddr (str): 组播地址和源地址映射方式, 类型为：string, 取值范围：IPv4地址, 默认值：255.0.0.1

RpAddr (str): RP地址, 类型为：string, 取值范围：IPv4地址, 默认值：10.10.10.10

PrefixLength (int): Register发送时间间隔（秒）, 类型为：number, 取值范围：0-32, 默认值：32

RpPriority (int): Register发送时间间隔（秒）, 类型为：number, 取值范围：0-255, 默认值：0

RpHoldTime (int): Register发送时间间隔（秒）, 类型为：number, 取值范围：1-65535, 默认值：150

Returns:

(:obj:PimIpv6RpMapConfig): PIM IPv6 Rp Map对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Pim	Port=${Port}
Create Pim IPv4 Rp Map	Session=${Session}	RpAddr=20.10.10.10
Create Pppoe
Arguments
Port
EmulationMode
=
CLIENT
** kwargs
Documentation
创建PPPoE协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

EmulationMode (str): PPPoE角色, 默认值：CLIENT, 取值范围：

CLIENT SERVER

Keyword Args:

Name (str): PPPoE协会话名称

Enable (bool): 使能PPPoE协议会话, 默认值：True

AuthenticationType (str): 认证方式, 默认值：NO_AUTHENTICATION, 取值范围：

NO_AUTHENTICATION NEGOTIATION CHAP_MD5 PAP

Username (str): 用户名, 默认值：xinertel, 取值范围：string length in [1,126]

Password (str): 密码, 默认值：xinertel, 取值范围：string length in [1,126]

ServiceName (str): 服务名, 默认值："", 取值范围：string length in [0,255]

EnableMaxPayloadTag (bool): 使能最大净荷标签, 默认值：False

MaxPayloadBytes (int): 最大净荷(字节), 取值范围：1-65535, 默认值：1500

LcpConfigReqTimeout (int): LCP Configure-Request超时时间 (sec), 取值范围：1-65535, 默认值：3

LcpConfigReqMaxAttempts (int): LCP Configure-Request最大尝试次数, 取值范围：1-65535, 默认值：10

LcpTermReqTimeout (int): LCP Terminate-Request超时时间 (sec), 取值范围：1-65535, 默认值：3

LcpTermReqMaxAttempts (int): LCP Terminate-Request最大尝试次数, 取值范围：1-65535, 默认值：10

NcpConfigReqTimeout (int): NCP Configure-Request超时时间 (sec), 取值范围：1-65535, 默认值：3

NcpConfigReqMaxAttempts (int): NCP Configure-Request最大尝试次数, 取值范围：1-65535, 默认值：10

LcpNcpMaxNak (int): LCP/NCP最大Nak数量, 取值范围：1-65535, 默认值：5

EnableMruNegotiation (bool): 使能MRU协商, 默认值：True

MruSize (int): MRU(字节), 取值范围：128-65535, 默认值：1492

EnableEchoRequest (bool): 使能Echo-Request报文, 默认值：False

EchoRequestInterval (int): Echo-Request间隔 (sec), 取值范围：1-65535, 默认值：10

EchoRequestMaxAttempts (int): Echo-Request最大尝试次数, 取值范围：1-65535, 默认值：3

EnableMagicNumber (bool): 使能Magic Number, 默认值：True

PadiTimeout (int): Client参数, PADI超时时间 (sec), 取值范围：1-65535, 默认值：3

PadiMaxAttempts (int): Client参数, PADI最大尝试次数, 取值范围：1-65535, 默认值：10

PadrTimeout (int): Client参数, PADR超时时间 (sec), 取值范围：1-65535, 默认值：3

PadrMaxAttempts (int): Client参数, PADR最大尝试次数, 取值范围：1-65535, 默认值：10

EnableRelayAgent (bool): Client参数, 启用中继代理, 默认值：False

RelayAgentDestMac (str): Client参数, 中继代理MAC地址, 取值范围：有效的mac地址, 默认值：00:00:00:00:00:00

RelayAgentDestMacStep (str): Client参数, 中继代理MAC地址跳变, 取值范围：有效的mac地址, 默认值：00:00:00:00:00:01

UseRelayAgentPadi (bool): Client参数, PADI中包含中继代理信息, 默认值：True

UseRelayAgentPadr (bool): Client参数, PADR中包含中继代理信息, 默认值：True

RelayAgentType (str): Client参数, 中继代理类型, 默认值：RFC2516, 取值范围：

RFC2516 DSL_FORUM

RelaySessionId (str): Client参数, 中继会话ID, 取值范围：string length in [0,12], 默认值：""

CircuitId (str): Client参数, 环路ID, 取值范围：string length in [0,63], 默认值：@s

RemoteId (str): Client参数, 远程ID, 取值范围：string length in [0,63], 默认值：@m-@p

ChapChalReqTimeout (int): Client参数, CHAP Challenge Request超时时间 (sec), 取值范围：1-65535, 默认值：3

ChapAckTimeout (int): Client参数, CHAP Ack超时时间 (sec), 取值范围：1-65535, 默认值：3

ChapMaxReplyAttempts (int): Client参数, CHAP Reply最大尝试次数, 取值范围：1-65535, 默认值：10

PapReqTimeout (int): Client参数, PAP Request超时时间 (sec), 取值范围：1-65535, 默认值：3

PapReqMaxAttempts (int): Client参数, PAP Request最大尝试次数, 取值范围：1-65535, 默认值：10

EnableAutoRetry (bool): Client参数, 使能PPPoE协议会话, 默认值：False

AutoRetryCount (int): Client参数, 重连次数, 取值范围：1-65535, 默认值：65535

LcpDelay (int): Client参数, LCP 推迟时间(ms), 取值范围：1-65535, 默认值：0

EnableAutoFillIpv6 (bool): Client参数, 启用获取Global IPv6地址, 默认值：True

AcName (str): Server参数, 访问集中器名称, 默认值：Xinertel

ChapReplyTimeout (int): Server参数, CHAP Reply超时时间(sec), 取值范围：1-65535, 默认值：3

ChapMaxChalAttempts (int): Server参数, CHAP Challenge最大尝试次数, 取值范围：1-65535, 默认值：10

PapPeerReqTimeout (int): Server参数, 等待PAP Request超时时间(sec), 取值范围：1-65535, 默认值：3

Ipv4Start (str): Server参数, IPv4起始地址, 默认值：192.0.1.0

Ipv4Step (str): Server参数, IPv4地址步长, 默认值：0.0.0。1

Ipv4Count (int): Server参数, IPv4地址数量, 取值范围：1-65535, 默认值：3

Ipv6InterfaceId (str): Server参数, 起始Interface ID, 默认值："::2"

Ipv6InterfaceIdStep (str): Server参数, Interface ID跳变步长, 默认值："::1"

Ipv6PrefixStart (str): Server参数, IPv6起始前缀, 默认值："2002::"

Ipv6PrefixStep (str): Server参数, IPv6前缀跳变步长, 默认值："0:0:0:1::"

Ipv6Count (int): Server参数, IPv6前缀数量, 取值范围：1-65535, 默认值：1

EnableForceConnectMode (bool): 强制重连模式, 默认值：False

UnconnectedSessionThreshold (int): 未连接会话门限值, 取值范围：1-65535, 默认值：1

MAndOFlag (str): Server参数, M 与 O 标志位, 默认值：M0_O0, 支持

M0_O0 M0_O1 M1

Returns:

(:obj:PppoeClent): PPPoE协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Pppoe	Port=${Port}	
Create Pppoe	Port=${Port}	EmulationMode=Server
Create Pppoe Custom Option
Arguments
Session
** kwargs
Documentation
编辑PPPoE自定义选项

Args:

Session (:obj:PppoeClent) or (:obj:PppoeServer): PPPoE协议会话对象

Keyword Args:

OptionValue (int): 选项标识符, 默认值: 0, 取值范围: 0-65535

SubPortocolType (str): 包含选项的消息类型, 默认值：1 sec, 支持类型:

LinkControlProtocol

IPControlProtocol

IPv6ControlProtocol

PPPoEPADIandPADR

UseWildcards (bool): 使用通配符, 默认值：False

StringIsHexadecimal (int): 使能十六进制字符, 默认值：False

OptionData (str): 十进制选项载荷

OptionHexData (int): 十六进制选项载荷

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Create Pppoe Custom Option	Sessions=${Sessions}	OptionValue=1	SubPortocolType=LinkControlProtocol	OptionData=55
Create Rip
Arguments
Port
** kwargs
Documentation
创建RIP协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): RIP协议会话名称, 类型为：string

Enable (bool): 使能RIP协议会话, 类型为：bool, 取值范围：True或False, 默认值：True

Version (str): RIP版本, 类型为：string, 默认值：RIPV2, 支持版本：

RIPV1

RIPV2

RIPNG

UpdateType (str): 仿真路由器指定发送RIP消息的通信方式, 类型为：string, 默认值：MULTICAST, 支持方式：

BROADCAST

MULTICAST

UNICAST

DutIpv4Address (str): 指定接收RIP消息的路由器的IP地址, 当RIP版本为RIPv1或者RIPv2时，该选项可配。 类型为：string, 默认值：224.0.0.9

DutIpv6Address (str): 指定接收RIP消息的路由器的IP地址, 当RIP版本为RIPng并且更新类型指定为Unicast时，该选项可配。 类型为：string, 默认值：ff02::9

AuthMethod (str): 认证方式, 当RIP版本为RIPv2时配置该选项。 类型为：string, 默认值：NONE, 支持方式：

NONE

SIMPLE

MD5

Password (str): 当认证方式为Simple/MD5时，输入的认证密码, 类型为：string, 默认值：Xinetel

Md5KeyId (int): 当认证方式为MD5时，输入的MD5密钥, 类型为：number, 取值范围：0-255, 默认值：1

UpdateInterval (int): 发送RIP更新消息的时间间隔，单位为秒, 类型为：number, 取值范围：1-65535, 默认值：30

UpdateJitter (int): 发送RIP更新消息的时间抖动, 类型为：number, 取值范围：0-5, 默认值：0

MaxRoutePerUpdate (int): 更新消息中可携带的最大路由数, 类型为：number, 取值范围：1-70, 默认值：25

SplitHorizon (bool): 是否开启水平分割功能, 类型为：bool, 取值范围：True或False, 默认值：False

EnableViewRoutes (bool): 是否需要查看学到的路由信息, 类型为：bool, 取值范围：True或False, 默认值：False

EnableIpAddrValidation (bool): 验证收到的IP地址是否和本地地址在同一网段, 类型为：bool, 取值范围：True或False, 默认值：False

Returns:

(:obj:RipRouter): RIP协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Rip	Port=${Port}	EnableIpAddrValidation=True
Create Rip Ipv4 Route
Arguments
Session
** kwargs
Documentation
创建RIP IPv4路由对象

Args:

Session(:obj:RipRouter): Rip协议会话对象列表, 类型为：object

Keyword Args:

Name (str): RIP IPv4路由名称, 类型为：string

Enable (bool): 使能RIP IPv4路由, 类型为：bool, 取值范围：True或False, 默认值：True

RouteCount (str): 路由池中包含的路由的个数, 类型为：string, 取值范围：1-16777215, 默认值：1

StartIpv4Prefix (str): 指定起始IPv4地址, 类型为：string, 取值范围：有效的ipv4地址, 默认值：192.168.1.0

PrefixLength (int): 地址前缀长度, 类型为：number, 取值范围：1-32, 默认值：24

Increment (str): 增量步长, 类型为：string, 取值范围：1-255, 默认值：1

NextHop (str): 指定路由下一跳, 类型为：string, 取值范围：有效的ipv4地址, 默认值：0.0.0.0

Metric (int): 路由度量, 16表示不可达。 类型为：number, 取值范围：1-16, 默认值：1

RouteTag (int): 路由标签域的值, 0表示没有tag. 类型为：number, 取值范围：0-65535, 默认值：0

Returns:

(:obj:RipIpv4RouteConfig): RIP IPv4路由对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Rip	Port=${Port}
Create Rip Ipv4 Route	Session=${Session}	Metric=10
Create Rip Ipv6 Route
Arguments
Session
** kwargs
Documentation
创建RIP IPv6路由对象

Args:

Session(:obj:RipRouter): Rip协议会话对象列表, 类型为：object

Keyword Args:

Name (str): RIP IPv6路由名称, 类型为：string

Enable (bool): 使能RIP IPv6路由, 类型为：bool, 取值范围：True或False, 默认值：True

RouteCount (int): 路由池中包含的路由的个数, 类型为：number, 取值范围：1-2147483647, 默认值：1

StartIpv6Prefix (str): 起始IPv6地址, 类型为：string, 取值范围：有效的IPv6地址, 默认值：'2000::'

RouteStep (str): IP地址的增加步长, 类型为：string, 取值范围：有效的IPv6地址, 默认值：'0:0:0:1::'

PrefixLength (int): 地址的前缀长度, 类型为：number, 取值范围：1-128, 默认值：64

NextHop (str): 路由下一跳, 类型为：string, 取值范围：有效的IPv6地址, 默认值：'::'

Metric (int): 路由度量, 类型为：number, 取值范围：1-16, 默认值：1

RouteTag (int): 路由标签域的值, 0表示没有tag, 类型为：number, 取值范围：0-65535, 默认值：0

Returns:

(:obj:RipIpv6RouteConfig): RIP IPv6路由对象, 类型：object

Examples: .. code:: RobotFramework

${Session}	Create Rip	Port=${Port}
Create Rip Ipv6 Route	Session=${Session}	
Create Stream Header
Arguments
Stream
HeaderTypes
Index
=
None
Documentation
创建流量报文头部

Args:

Stream (:obj:StreamTemplate):: 测试仪表流量对象object, 类型为：object

Index (int): 报文头部创建在当前流量头部的序号, 类型为：number, 取值范围None或0-16383,当Index为None表示重新创建流量报文类型

HeaderTypes (list): 报文头部类型列表,类型为：list,支持的报文头部(不区分大小写):

ethernetii

vlan

vxlan

arp

ipv4

ipv6

tcp

udp

l2tpv2data

ppp

pppoe

icmpv4echorequest

destunreach

icmpv4echoreply

informationreply

informationrequest

icmpv4parameterproblem

icmpv4redirect

sourcequench

timeexceeded

timestampreply

timestamprequest

icmpmaskrequest

icmpmaskreply

destinationunreachable

icmpv6echoreply

icmpv6echorequest

packettoobig

icmpv6parameterproblem

timeexceed

routersolicit

routeradvertise

icmpv6redirect

neighborsolicit

neighboradvertise

mldv1query

mldv1report

mldv1done

mldv2query

mldv2report

igmpv1

igmpv1query

igmpv2

igmpv2query

igmpv3report

igmpv3query

custom

ospfv2linkstateupdate

ospfv2linkstaterequest

ospfv2databasedescription

ospfv2linkstateacknowledge

ospfv2unknown

ospfv2hello

mpls

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

${HeaderTypes}	Create List	EthernetII	IPv4	TCP
Create Stream Header	Stream=${Stream}	HeaderTypes=${HeaderTypes}		
Create Vxlan
Arguments
Port
** kwargs
Documentation
创建Vxlan协议会话对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): Vxlan协会话名称, 类型为：string

Enable (bool): 使能Vxlan协议会话, 默认值：True

AutoUdpSourcePort (bool): 自动计算UDP源端口, 默认值：True

UdpSourcePort (int): 配置UDP源端口, 取值范围：3-4095, 默认值：1025

EnableUdpChecksum (bool): 使能计算UDP校验和, 默认值：False

EvpnLearning (bool): 使能EVPN学习, 默认值：False

OvsdbLearning (bool): 使能OVSDB学习, 默认值：False

MulticastType (str): 组播类型, 默认值：IGMP, 取值范围：

IGMP

PIM

MLD

VtepTunnelIp (str): VTEP 隧道IP地址, 默认值：INTERFACEIP, 取值范围：

INTERFACEIP

ROUTERID

EnableIrb (bool): 默认值：False

RPAddress (str): 选择PIM的RP地址, 取值范围：IPv4地址, 默认值：192.0.0.1

RPIpv6Address (str): 选择PIM的RP地址, 取值范围：IPv6地址, 默认值：2000::1

IrbMode (str): 默认值：Symmetric, 取值范围：

Symmetric

Returns:

(:obj:Vxlan): Vxlan协议会话对象, 类型：object

Examples: .. code:: RobotFramework

Create Vxlan	Port=${Port}
Create Vxlan Segment
Arguments
** kwargs
Documentation
创建Vxlan Segment对象

Args:

Port (:obj:Port): 测试仪表端口对象, 类型为：object

Keyword Args:

Name (str): Vxlan协会话名称, 类型为：string

Enable (bool): 使能Vxlan协议会话, 默认值：True

StartVni (int): 起始 VNI, 取值范围：0-16777215, 默认值：0

VniCount (int): VNI个数, 取值范围：1-65535, 默认值：1

VniStep (int): VNI 跳变步长, 取值范围：1-65535, 默认值：1

CommunicationType (str): 学习方式, 默认值：UNICAST, 取值范围：

UNICAST

MULTICAST

VxlanEVPN

VniDistributionType (str): VNI在VPN之间的分配方式, 默认值：ROUNDROBIN, 取值范围：

ROUNDROBIN

LINEAR

EnableL3Vni (bool): 使能L3VNI, 默认值：False

StartL3Vni (int): 起始L3VNI, 取值范围：1-16777215, 默认值：1

L3VniStep (int): L3VNI跳变步长, 取值范围：1-16777215, 默认值：1

L3VniCount (int): L3 VNI数量, 取值范围：1-65535, 默认值：1

VniTrafficType (str): 流端点模式, 默认值：ROUNDROBIN, 取值范围：

L2VNI

L3VNI

L2AndL3VNI

EnableVmArp (bool): 使能VM ARP, 默认值：False

Returns:

(:obj:VxlanSegmentConfig): Vxlan Segment对象, 类型：object

Examples: .. code:: RobotFramework

Create Vxlan Segment	Port=${Port}
Del Benchmark
Del Imix Distribution Frame
Arguments
IMix
Index
=
None
Documentation
在Imix模板删除指定自定义帧长

Args:

IMix (:obj:Imix): 测试仪表Imix模板对象

Index (int): 测试仪表Imix模板自定义帧长序号

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

${Imix}	Create Imix	Name=Imix_1	Seed=10121112		
Add IMix Distribution Frame	IMix=${Imix}	Type=random	Min=64	Max=128	Weight=50
Add IMix Distribution Frame	IMix=${Imix}	Type=random	Min=128	Max=256	Weight=50
Bind Stream Imix	Stream=${Stream}	Imix=${Imix}			
Del IMix Distribution Frame | IMix=${Imix} | Index=1
Del Objects
Arguments
Objects
Documentation
删除测试仪表相关对象

Args:

:param Objects: 测试仪表相关对象 :type Objects: 类型为：list，测试仪表相关对象object列表

Returns: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

${Port}	Get Ports
Del Objects	Port=${Port}
Del Port
Arguments
Ports
=
None
Documentation
删除测试仪端口

Args:

Ports: 测试仪表端口对象列表, 类型为：list

Returns:

Returns：布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Del Port	Ports=${Port_1}
Del Port	
Del Stream
Arguments
Ports
=
None
Streams
=
None
Documentation
删除测试仪流量

Args:

Ports (list (:obj:Port)): 测试仪表端口对象列表

Streams (list (:obj:StreamTemplate)): 测试仪表流量对象列表

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

${Stream_1} | Add Stream | Ports=${Port_1}
${Stream_2} | Add Stream | Ports=${Port_2}
${Stream_2} | Add Stream | Ports=${Port_3}
Del Stream | Streams=${Stream_1} |
Del Stream | Ports=${Port_2} |
Del Stream |
Dhcp Abort
Arguments
Sessions
Documentation
终止测试仪表DHCP协议会话

Args:

Sessions (:obj:DhcpClient): DHCPv4 Client协议对象

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcp Abort	Sessions=${Sessions}
Dhcp Bind
Arguments
Sessions
Documentation
Bind测试仪表DHCP协议会话

Args:

Sessions (:obj:DhcpClient): DHCPv4 Client协议对象

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcp Bind	Sessions=${Sessions}
Dhcp Rebind
Arguments
Sessions
Documentation
重新Bind测试仪表DHCP协议会话

Args:

Sessions (:obj:DhcpClient): DHCPv4 Client协议对象

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcp Rebind	Sessions=${Sessions}
Dhcp Reboot
Arguments
Sessions
Documentation
重新启动测试仪表DHCP协议会话

Args:

Sessions (:obj:DhcpClient): DHCPv4 Client协议对象

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcp Reboot	Sessions=${Sessions}
Dhcp Release
Arguments
Sessions
Documentation
释放测试仪表DHCP协议会话

Args:

Sessions (:obj:DhcpClient): DHCPv4 Client协议对象

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcp Release	Sessions=${Sessions}
Dhcp Renew
Arguments
Sessions
Documentation
Renew测试仪表DHCP协议会话

Args:

Sessions (:obj:DhcpClient): DHCPv4 Client协议对象

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcp Renew	Sessions=${Sessions}
Dhcpv6 Client Abort
Arguments
Sessions
Documentation
中断DHCPv6/PD客户端

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Abort	Sessions=${Sessions}
Dhcpv6 Client Active Lease Query
Arguments
Sessions
Documentation
DHCPv6客户端活动租借查询

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Active Lease Query	Sessions=${Sessions}
Dhcpv6 Client Bind
Arguments
Sessions
Documentation
DHCPv6客户端绑定地址

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Bind	Sessions=${Sessions}
Dhcpv6 Client Bulk Lease Query
Arguments
Sessions
** kwargs
Documentation
DHCPv6客户端批量租借查询

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Keyword Args：

QueryType (str): Bulk Leasequery消息中query-type类型, 默认值：QUERY_BY_ADDRESS, 取值范围：

QUERY_BY_ADDRESS

QUERY_BY_CLIENTID

QUERY_BY_RELAY_ID

QUERY_BY_LINK_ADDRESS

QUERY_BY_REMOTE_ID

ClientAddress (str): 指定客户端IPv6地址, 默认值：'2000::1', 取值范围：有效的ipv6地址

ClientId (str): 客户端ID, 默认值：'', 取值范围：匹配正则表达式"^([0-9a-fA-F]{0,512})$"

RelayIdentifier (str): 中继器ID, 默认值：'', 取值范围：匹配正则表达式"^([0-9a-fA-F]{0,512})$"

LinkAddress (str): 链路地址, 默认值：'2000::1', 取值范围：有效的ipv6地址

RemoteId (str): 中继代理Remote-ID值, 默认值：''

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Bulk Lease Query	Sessions=${Sessions}
Dhcpv6 Client Confirm
Arguments
Sessions
Documentation
DHCPv6客户端确认参数

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Confirm	Sessions=${Sessions}
Dhcpv6 Client Info Request
Arguments
Sessions
Documentation
DHCPv6客户端请求信息

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Info Request	Sessions=${Sessions}
Dhcpv6 Client Lease Query
Arguments
Sessions
** kwargs
Documentation
DHCPv6客户端租借查询

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Keyword Args:

QueryType (str): Leasequery消息中query-type类型, 默认值：QUERY_BY_ADDRESS, 取值范围：

QUERY_BY_ADDRESS

QUERY_BY_CLIENTID

ClientAddress (str): 客户端IPv6地址, 默认值：'2000::1', 取值范围：有效的ipv6地址

ClientId (str): 客户端ID, 默认值：'', 取值范围：匹配正则表达式"^([0-9a-fA-F]{0,512})$"

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Lease Query	Sessions=${Sessions}
Dhcpv6 Client Rebind
Arguments
Sessions
Documentation
DHCPv6客户端广播续租地址

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Rebind	Sessions=${Sessions}
Dhcpv6 Client Release
Arguments
Sessions
Documentation
DHCPv6客户端释放地址

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Release	Sessions=${Sessions}
Dhcpv6 Client Renew
Arguments
Sessions
Documentation
DHCPv6客户端单播续租地址

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Renew	Sessions=${Sessions}
Dhcpv6 Client Start Tls
Arguments
Sessions
Documentation
DHCPv6客户端启动TLS

Args:

Sessions (:obj:Dhcpv6Client): DHCPv6客户端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Client Start Tls	Sessions=${Sessions}
Dhcpv6 Server Abort
Arguments
Sessions
Documentation
中断DHCPv6/PD服务器

Args:

Session (:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Server Abort	Sessions=${Sessions}
Dhcpv6 Server Reconfigure Rebind
Arguments
Sessions
Documentation
DHCPv6服务端重新配置Rebind

Args:

Session (:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Server Reconfigure Rebind	Sessions=${Sessions}
Dhcpv6 Server Reconfigure Renew
Arguments
Sessions
Documentation
DHCPv6服务端重新配置Renew

Args:

Session (:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Server Reconfigure Renew	Sessions=${Sessions}
Dhcpv6 Server Start
Arguments
Sessions
Documentation
启动DHCPv6服务端

Args:

Session (:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Server Start	Sessions=${Sessions}
Dhcpv6 Server Stop
Arguments
Sessions
Documentation
停止DHCPv6服务端

Args:

Session (:obj:Dhcpv6Server): DHCPv6服务端会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dhcpv6 Server Stop	Sessions=${Sessions}
Disconnect Bgp
Arguments
Sessions
Documentation
断开BGP协议会话连接

Args:

Sessions (:obj:BgpRouter): BGP协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Disconnect Bgp	Sessions=${Sessions}
Disconnect L2tp
Arguments
Sessions
Documentation
断开L2tp协议会话

Args:

Sessions (:obj:L2tp): L2tp协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Disconnect L2tp	Sessions=${Sessions}
Disconnect Pppoe
Arguments
Sessions
Documentation
断开PPPoE协议会话

Args:

Sessions (list (:obj:PppoeClent)): PPPoE协议会话对象列表, 类型为：list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Disconnect Pppoe	Sessions=${Sessions}
Dot1x Delete Certificate
Arguments
Sessions
Documentation
删除802.1x证书

Args:

Sessions (:obj:Dot1x): 802.1x会话对象, 类型为：object / list

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dot1x Upload Certificate	Sessions=${Sessions}
Dot1x Upload Certificate
Arguments
Sessions
Folder
Documentation
上传802.1x证书

Args:

Sessions (:obj:Dot1x): 802.1x会话对象, 类型为：object / list

Folder (str): 证书所在路径，e.g.'c:/CertificateFolder'

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: .. code:: RobotFramework

Dot1x Upload Certificate	Sessions=${Sessions}	Folder=${Folder}
Download Packages
Arguments
Port
FileDir
FileName
MaxCount
=
0
TimeOut
=
30
Documentation
下载指定端口捕获到的数据包

Args:

Port (:obj:Port): 测试仪表端口对象object

FileDir (str): 报文保存的路径, ("D:/test")

FileName (str): 报文保存的文件的名称

MaxCount (int): 下载报文最大数量，默认值0, 表示下载端口上捕获到的所有报文

TimeOut (int): 下载报文的超时时间单位秒，超时时间内为下载完成则下载失败, 默认值30

Returns:

(str): 下载数据包文件的绝对路径(例如："D:\test\10.0.5.10_1_1\dowload.pcap")

Examples: robotframework:

.. code:: robotframework

${Port}	Get Ports			
&{File}	Download Packages	Port=${Port}	FileDir=D:/test	FileName=download
Edit Benchmark Address Learning Capacity
Arguments
Config
MinAddressCount
=
1
MaxAddressCount
=
65536
InitAddressCount
=
20480
Resolution
=
2
AgingTime
=
15
LearningRate
=
10000
Documentation
编辑RFC2889测试套件地址容量测试项参数

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

MinAddressCount (int): 学习地址最小值, 默认值: 1, 范围: 1-16777216

MaxAddressCount (int): 习地址最小值 默认值: 65536, 范围: 1-16777216

InitAddressCount (int) 习地址最小值, 默认值: 20480, 范围: 1-16777216

Resolution (int): 精度(%), 默认值: 2, 范围: 1-100

AgingTime (int): 老化时间(秒), 默认值: 50, 范围: 1-3600

LearningRate (int): 地址学习速率(帧/秒), 默认值: 10000, 范围: 1-148809523

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Address Learning Rate
Arguments
Config
MinRateCount
=
1488
MaxRateCount
=
1488
InitRateCount
=
1488
Resolution
=
2
AgingTime
=
15
AddressCount
=
1000
Documentation
编辑RFC2889测试套件地址容量测试项参数

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

MinRateCount (int): 学习地址最小值, 默认值: 1488, 范围: 1-148809523

MaxRateCount (int): 习地址最小值 默认值: 1488, 范围: 1-148809523

InitRateCount (int) 习地址最小值, 默认值: 1488, 范围: 1-148809523

Resolution (int): 精度(%), 默认值: 2, 范围: 1-100

AgingTime (int): 老化时间(秒), 默认值: 50, 范围: 1-3600

AddressCount (int): 地址数量, 默认值: 1000, 范围: 1-4294967295

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Burst Count Loop
Arguments
Config
Mode
=
step
Start
=
1
End
=
1
Step
=
1
Custom
=
[1, 2]
Documentation
编辑RFC2889测试套件突发帧数，设置测试项: 广播帧转发测试、拥塞控制测试、错误帧过滤测试、转发测试

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

Mode (str): 负载单位, 默认值: step, 支持类型:

step

custom

Start (int): 开始帧数, 默认值: 1, 范围: 1-65535

End (int): 结束帧数, 默认值: 1, 范围: 1-65535

Step (int) 帧数步长, 默认值: 1, 范围: 1-65535

Custom (list[int]): 自定义帧数, 默认值: [1, 2]

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Duration
Arguments
Config
Trial
=
1
Mode
=
second
Count
=
100
Documentation
编辑测试套件测试时长设置

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

Trial (int): 测试验次数, 默认值: 1

Mode (str): 模式, 默认值: second, 支持second和burst

Count (int): 突发包个数(帧)或时长(秒), 默认值: 100, 范围: 1-80000000

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Errored Frame Filtering
Arguments
Config
CrcTested
=
True
CrcFrameLength
=
64
UndersizedTested
=
True
UndersizedFrameLength
=
60
OversizedTested
=
True
OversizedFrameLength
=
1519
MaxLegalFrameLength
=
1518
BurstSize
=
1
Documentation
编辑RFC2889测试套件错误帧过滤测试项参数

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

CrcTested (bool): 使能错误类型CRC, 默认值: True

CrcFrameLength (int): CRC帧长度, 默认值: 64, 范围: 64-10000

UndersizedTested (bool): 使能超短帧长度, 默认值: True

UndersizedFrameLength (int) 超短帧长度, 默认值: 60, 范围: 58-63

OversizedTested (int): 使能超长帧长度, 默认值: True

OversizedFrameLength (int): 超长帧长度, 默认值: 1519, 范围: 1519-16383

MaxLegalFrameLength (int): 最大合法帧长, 默认值: 1518, 范围: 1-4294967295

BurstSize (int): 地址数量, 默认值: 1000, 范围: 1-4294967295

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Frame
Arguments
Config
Type
=
custom
Length
=
128
Min
=
128
Max
=
256
Start
=
128
End
=
256
Step
=
128
Custom
=
None
ImixTemplates
=
None
Documentation
编辑测试套件帧长度设置

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

Type (str): 帧长度类型, 默认值: custom, 支持类型:

fixed

random

step

custom

fixed

imix

Length (int): 固定帧长值, 默认值: 128, 范围: 58-16383

Min (int): 最小帧长值, 默认值: 128, 范围: 58-16383

Max (int): 最大帧长值, 默认值: 128, 范围: 58-16383

Start (int): 开始帧长值, 默认值: 128, 范围: 58-16383

End (int): 结束帧长值, 默认值: 128, 范围: 58-16383

Step (int): 跳变帧步长值, 默认值: 128, 范围: 58-16383

Custom (int): 自定义帧长列表, 默认值: [64, 128, 256, 512, 1024, 1280, 1518], 范围: 58-16383

ImixTemplates (list): IMix模板列表, 默认值: None

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

@{Items}	Create List	throughput	frameloss				
@{FrameSize}	Create List	256	1024	16383			
${Wizard}	${Config}	Create Benchmark	Type=rfc2544	Items=${Items}			
Edit Benchmark Path	Configs=${Config}	Path=C:/test					
Relate Benchmark Ports	Config=${Wizard}	Ports=${Ports}					
Create Benchmark Streams	Config=${Wizard}	Items=@{RFC2544Items}	Type=eth	SrcPoints=@{SrcPoints}	DstPoints=@{SrcPoints}	Mode=meshed	Mapping=roundrobin
Edit Benchmark Learning	Configs=${Config}	Frequency=once					
Edit Benchmark Duration	Config=${Config}	Count=1000					
Edit Benchmark Frame	Config=${Config}	Type=custom	Custom=@{FrameSize}				
Edit Benchmark Search	Config=${Config}	Init=100					
Expand Benchmark	Config=${Wizard}						
Edit Benchmark Latency
Arguments
Configs
🏷 Type
=
FIFO
🏷 DelayBefore
=
2
🏷 DelayAfter
=
10
Documentation
编辑测试套件时间参数

Args:

Configs (list (:obj:config)): 仪表测试测试套件测试项对象object列表

Type (str): 时延类型, 支持以下类型:

LIFO: (Store and forward)

FIFO: (Bit forwarding);

LILO

FILO

DelayBefore (int): 启动流前延迟时间，单位: 秒, ，默认值: 2, 范围: 1-3600

DelayAfter (int): 停止流后延迟时间，单位: 秒, ，默认值: 10, 范围: 1-3600

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Learning
Arguments
Configs
Frequency
🏷 EnableLearning
=
True
🏷 LearningRate
=
1000
🏷 LearningRepeat
=
5
🏷 DelayBefore
=
2
🏷 EnableArp
=
False
🏷 ArpRate
=
1000
🏷 ArpRepeat
=
5
Documentation
编辑测试套件地址学习设置

Args:

Configs (list (:obj:config)): 仪表测试测试套件测试项对象object列表

Frequency (str): 学习频率, 支持以下类型:

once

trial

frame

iter

EnableLearning (bool): 使能地址学习, 默认值: True

LearningRate (int): 地址学习速率，单位: 帧/秒, 默认值: 1000, 范围: 1-14880952

LearningRepeat (int): 学习重复次数, 默认值: 5, 范围: 1-65536

DelayBefore (int): 学习延迟时间，单位: 秒, 默认值: 2, 范围: 1-65536

EnableArp (bool): 使能三层ARP学习, 默认值: True

ArpRate (int): ARP学习速率，单位: 秒, 默认值: 1000, 范围: 1-14880952

ArpRepeat (int): ARP学习重复次数, 默认值: 5, 范围: 1-65536

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Multicast Base Parameters
Arguments
Configs
Version
=
igmpv2
Ipv4GroupAddressStart
=
225.0.0.1
Ipv4GroupAddressStep
=
0.1.0.0
Ipv4PrefixLength
=
32
Ipv6GroupAddressStart
=
ff1e::1
Ipv6GroupAddressStep
=
0:0:0:1::
Ipv6PrefixLength
=
128
GroupIncrement
=
1
JoinGroupDelay
=
15
LeaveGroupDelay
=
15
JoinLeaveSendRate
=
1000
GroupDistributeMode
=
even
Documentation
编辑RFC3918测试套件-组播参数

Args:

Configs (list (:obj:config)): 仪表测试测试套件测试项对象object列表

Version (str): 负载单位, 默认值: percent, 支持类型:

igmpv1

igmpv2

igmpv3

mldv1

mldv2

Ipv4GroupAddressStart (str): 起始IP地址, 默认值: 225.0.0.1

Ipv4GroupAddressStep (str): 起始IP步长, 默认值: 0.1.0.0

Ipv4PrefixLength (int): IP前缀长度, 默认值: 32, 范围: 1-32

Ipv6GroupAddressStart (str): 起始IPv6地址, 默认值: ffle::

Ipv6GroupAddressStep (str): 起始IPv6步长, 默认值: 0:0:0:1::

Ipv6PrefixLength (int): IPv6前缀长度, 默认值: 128, 范围: 1-128

GroupIncrement (int): 组跳变步长, 默认值: 1, 范围: 1-4294967295

JoinGroupDelay (int): 加入组延迟(秒), 默认值: 15, 范围: 0-4294967295

LeaveGroupDelay (int): 离开组延迟(秒), 默认值: 15, 范围: 0-4294967295

JoinLeaveSendRate (int): 组播发消息速率(包/秒), 默认值: 1000, 范围: 0-1000000000

GroupDistributeMode (str): 组播组分布模式, 默认值: even, 范围:

even: 平均

weigh: 权重

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Multicast Group Count Loop
Arguments
Config
LoopMode
=
step
FixedGroup
=
10
MinGroup
=
10
MaxGroup
=
50
StartGroup
=
10
EndGroup
=
50
StepGroup
=
10
CustomGroup
=
(10, 20, 100)
Documentation
RFC3918测试套件-组播组

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

LoopMode (str): 模式, 默认值: step, 支持:

fixed random step custom

FixedGroup (str): 固定, 默认值: 10

MinGroup (str): 最小, 默认值: 10

MaxGroup (int): 最大, 默认值: 50

StartGroup (int): 开始, 默认值: 10

EndGroup (int): 结束, 默认值: 50

StepGroup (int): 步长, 默认值: 10

CustomGroup (list[int]): 自定义比例, 默认值: (10, 20, 100)

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Multicast Join Leave Delay
Arguments
Config
DelayBetweenJoinAndStartStream
=
10
DelayBetweenJoinAndLeave
=
10
Documentation
RFC3918测试套件-配置加入离开组时延

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

DelayBetweenJoinAndStartStream (int): 从启动流量开始到发送加入组报文之间的时间间隔。单位是秒, 默认值: 10, 范围: 0-3600

DelayBetweenJoinAndLeave (int): 发送加入组报文和发送离开组报文之间的时间间隔。单位是秒, 默认值: 10, 范围: 0-3600

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Multicast Mixed Throughput Unicast Streams
Arguments
Config
Streams
Documentation
RFC3918测试套件组播混合吞吐量-配置单播流量

Args:

Config (:obj:config): 仪表测试测试套件测试项对象object

Streams (list[(:obj:StreamTemplate)]): 仪表测试流模板对象object列表

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Multicast Other
Arguments
Configs
StopTestWhenFailed
=
True
VerifyFreq
=
topo_changed
DurationMode
=
second
TimeDurationCount
=
1
BurstDurationCount
=
100
TxFrameRate
=
1000
Documentation
编辑RFC3918测试套件-组播参数-其他

Args:

Configs (list (:obj:config)): 仪表测试测试套件测试项对象object列表

StopTestWhenFailed (bool): 如果流验证失败停止测试, 默认值: True

VerifyFreq (str): 验证频率, 默认值: topo_changed, 支持: none topo_changed frame iteration

DurationMode (str): 时长模式, 默认值: second, 支持: second burst

TimeDurationCount (int): 发送秒速, 默认值: 1000

BurstDurationCount (int): 帧发送数量, 默认值: 100

TxFrameRate (int): 帧发送速率(帧/秒), 默认值: 1000

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Multicast Stream Tos
Arguments
Configs
Tos
=
0
FlowLabel
=
0
TTL
=
7
Priority
=
0
Documentation
编辑RFC3918测试套件-组播参数-流配置

Args:

Configs (list (:obj:config)): 仪表测试测试套件测试项对象object列表

Tos (int): IPv4 TOS值, 默认值: 0

FlowLabel (int): IPv6 Flow Label值, 默认值: 0

TTL (int): IPv4 TTL值, 默认值: 10

Priority (int): VLAN优先级, 默认值: 0

Returns:

bool: 布尔值Bool (范围：True / False)

Examples: robotframework:

.. code:: robotframework

Edit Benchmark Multicast Traffic Ratio Loop