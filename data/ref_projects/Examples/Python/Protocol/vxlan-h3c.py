# =================================================================================

from TesterLibrary.base import *

locations = ['//10.0.11.191/1/9', '//10.0.11.191/1/10', '//10.0.11.191/1/11', '//10.0.11.191/1/12',
             '//10.0.11.191/1/13', '//10.0.11.191/1/14', '//10.0.11.191/1/15', '//10.0.11.191/1/16',
             '//10.0.11.191/1/5', '//10.0.11.191/1/6', '//10.0.11.191/1/7', '//10.0.11.191/1/8'] if len(
    sys.argv) < 2 else sys.argv[
    1].split(' ')
Product = 'DarYu' if len(sys.argv) < 3 else sys.argv[2].split(' ')

verdict = 'pass'
errInfo = ''
try:

    # 初始化仪表，执行仪表平台为DarYu
    init_tester(Product=Product)

    # 创建端口，并预约端口

    Port1, Port2, Port3, Port4, Port5, Port6, Port7, Port8, Port9, Port10, Port11, Port12 = reserve_port(
        Locations=locations, Force=True)

    # 创建接口
    vxlans_1 = []
    vxlans_2 = []
    vxlans_3 = []
    vxlans_4 = []
    vxlans_5 = []
    vxlans_6 = []
    vxlans_7 = []
    vxlans_8 = []
    stream_names = ['L3 dut3-stc_T11-30']
    stream_names_TC4_V6 = ['L3 dut3-dut4-v6_T11-30']
    Interface_TC4_T_All = []
    Interface_TC4_V6_1 = []
    Interface_TC4_V6_2 = []
    Interface_TC4_V6_All = []
    Interface_TC5_T_All = []
    Interface_TC5_All = []
    Interface_TC5_V6_1 = []
    Interface_TC5_V6_2 = []
    Interface_TC5_V6_All = []
    udplayer = ['udp']
    headerlayers = ['eth', 'vlan']
    headerlayers_ipv4 = ['ipv4']
    headerlayers_ipv6 = ['ipv6']

    for num in range(1, 21):
        h = hex(num)[2:]
        i = num + 1
        interfaces_vtep1 = create_interface(Port=Port1, Layers='ipv4', Name="VTEP Device 1-" + str(num))
        edit_interface(Interface=interfaces_vtep1,
                       Layer='EthIILayer',
                       Address='10:00:00:50:00:' + h)
        edit_interface(Interface=interfaces_vtep1,
                       Layer='IPv4Layer',
                       Address='13.6.1.' + str(i),
                       Gateway='13.6.1.1')
        Session_vxlan = create_vxlan(Port=Port1, Name="VTEP Device 1-" + str(num))
        vxlans_1.append(Session_vxlan)
        select_interface(Session=Session_vxlan, Interface=interfaces_vtep1)

        T1 = 20 + num
        interfaces_vtep2 = create_interface(Port=Port4, Layers='ipv4', Name="VTEP Device 1-" + str(T1))
        edit_interface(Interface=interfaces_vtep2,
                       Layer='EthIILayer',
                       Address='10:00:00:51:00:' + h)
        edit_interface(Interface=interfaces_vtep2,
                       Layer='IPv4Layer',
                       Address='13.6.2.' + str(i),
                       Gateway='13.6.2.1')
        Session_vxlan = create_vxlan(Port=Port4, Name="VTEP Device 1-" + str(T1))
        vxlans_3.append(Session_vxlan)
        select_interface(Session=Session_vxlan, Interface=interfaces_vtep2)

        T2 = 40 + num
        interfaces_vtep3 = create_interface(Port=Port7, Layers='ipv4', Name="VTEP Device 1-" + str(T2))
        edit_interface(Interface=interfaces_vtep3,
                       Layer='EthIILayer',
                       Address='10:00:00:52:00:' + h)
        edit_interface(Interface=interfaces_vtep3,
                       Layer='IPv4Layer',
                       Address='13.6.3.' + str(i),
                       Gateway='13.6.3.1')
        Session_vxlan = create_vxlan(Port=Port7, Name="VTEP Device 1-" + str(T2))
        vxlans_5.append(Session_vxlan)
        select_interface(Session=Session_vxlan, Interface=interfaces_vtep3)

        T3 = 60 + num
        interfaces_vtep4 = create_interface(Port=Port10, Layers='ipv4', Name="VTEP Device 1-" + str(T3))
        edit_interface(Interface=interfaces_vtep4,
                       Layer='EthIILayer',
                       Address='10:00:00:53:00:' + h)
        edit_interface(Interface=interfaces_vtep4,
                       Layer='IPv4Layer',
                       Address='13.6.4.' + str(i),
                       Gateway='13.6.4.1')
        Session_vxlan = create_vxlan(Port=Port10, Name="VTEP Device 1-" + str(T3))
        vxlans_7.append(Session_vxlan)
        select_interface(Session=Session_vxlan, Interface=interfaces_vtep4)

    for num in range(1, 21):
        h = hex(num)[2:]
        i = num + 1
        interfaces_vtep1 = create_interface(Port=Port1, Layers='ipv4', Name="VTEP Device 2-" + str(num))
        edit_interface(Interface=interfaces_vtep1,
                       Layer='EthIILayer',
                       Address='10:00:00:50:00:' + h)
        edit_interface(Interface=interfaces_vtep1,
                       Layer='IPv4Layer',
                       Address='13.6.1.' + str(i),
                       Gateway='13.6.1.1')
        Session_vxlan = create_vxlan(Port=Port1, Name="VTEP Device 2-" + str(num))
        vxlans_2.append(Session_vxlan)
        select_interface(Session=Session_vxlan, Interface=interfaces_vtep1)

        T1 = 20 + num
        interfaces_vtep2 = create_interface(Port=Port4, Layers='ipv4', Name="VTEP Device 2-" + str(T1))
        edit_interface(Interface=interfaces_vtep2,
                       Layer='EthIILayer',
                       Address='10:00:00:51:00:' + h)
        edit_interface(Interface=interfaces_vtep2,
                       Layer='IPv4Layer',
                       Address='13.6.2.' + str(i),
                       Gateway='13.6.2.1')
        Session_vxlan = create_vxlan(Port=Port4, Name="VTEP Device 2-" + str(T1))
        vxlans_4.append(Session_vxlan)
        select_interface(Session=Session_vxlan, Interface=interfaces_vtep2)

        T2 = 40 + num
        interfaces_vtep3 = create_interface(Port=Port7, Layers='ipv4', Name="VTEP Device 2-" + str(T2))
        edit_interface(Interface=interfaces_vtep3,
                       Layer='EthIILayer',
                       Address='10:00:00:52:00:' + h)
        edit_interface(Interface=interfaces_vtep3,
                       Layer='IPv4Layer',
                       Address='13.6.3.' + str(i),
                       Gateway='13.6.3.1')
        Session_vxlan = create_vxlan(Port=Port7, Name="VTEP Device 2-" + str(T2))
        vxlans_6.append(Session_vxlan)
        select_interface(Session=Session_vxlan, Interface=interfaces_vtep3)

        T3 = 60 + num
        interfaces_vtep4 = create_interface(Port=Port10, Layers='ipv4', Name="VTEP Device 2-" + str(T3))
        edit_interface(Interface=interfaces_vtep4,
                       Layer='EthIILayer',
                       Address='10:00:00:53:00:' + h)
        edit_interface(Interface=interfaces_vtep4,
                       Layer='IPv4Layer',
                       Address='13.6.4.' + str(i),
                       Gateway='13.6.4.1')
        Session_vxlan = create_vxlan(Port=Port10, Name="VTEP Device 2-" + str(T3))
        vxlans_8.append(Session_vxlan)
        select_interface(Session=Session_vxlan, Interface=interfaces_vtep4)

    count = 1
    xin = 0
    number = 0
    l3vni = 10011
    e = 200
    f = 11
    for num in range(1, 41):
        a = hex(num - 1)[2:]
        b = hex(count)[2:]
        c = 1
        d = 2
        h = hex(count)[2:]
        i = count + 1
        g = hex(num)[2:]
        if number % 2 == 0:
            number = number + 1
            e = e + 1
            Segment = create_vxlan_segment(Name='Seg ' + str(e),
                                           StartVni=str(e),
                                           CommunicationType=2,
                                           EnableL3Vni=True,
                                           StartL3Vni=str(l3vni),
                                           VniTrafficType=1)
            interfaces_vm_1 = create_interface(Port=Port1, Layers='ipv4', Count=30, Name='VM Device ' + str(num))
            edit_interface(Interface=interfaces_vm_1,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_1,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(c) + '.2',
                           Gateway='4.' + str(count) + '.' + str(c) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_1)
            interfaces_vm_2 = create_interface(Port=Port1, Layers='ipv4', Count=30, Name='VM Device 2-' + str(num))
            edit_interface(Interface=interfaces_vm_2,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_2,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(c) + '.2',
                           Gateway='4.' + str(count) + '.' + str(c) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_2)
            interfaces_vm_3 = create_interface(Port=Port1, Layers='ipv6', Count=6, Name='VM Device v6 ' + str(num))
            edit_interface(Interface=interfaces_vm_3,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_3,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(c) + '::2')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_3)
            interfaces_vm_4 = create_interface(Port=Port1, Layers='ipv6', Count=6, Name='VM Device v6 2-' + str(num))
            edit_interface(Interface=interfaces_vm_4,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_4,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(c) + '::2')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_4)
            interfaces_rt5_1 = create_interface(Port=Port1, Layers='ipv4', Count=10, Name="RT5 Device " + str(count))
            edit_interface(Interface=interfaces_rt5_1,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:8F')
            edit_interface(Interface=interfaces_rt5_1,
                           Layer='IPv4Layer',
                           Address='5.' + str(count) + '.1.2',
                           Gateway='5.' + str(count) + '.1.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_1)
            interfaces_rt5_2 = create_interface(Port=Port1, Layers='ipv4', Count=10, Name="RT5 Device 2-" + str(count))
            edit_interface(Interface=interfaces_rt5_2,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:8F')
            edit_interface(Interface=interfaces_rt5_2,
                           Layer='IPv4Layer',
                           Address='5.' + str(count) + '.1.2',
                           Gateway='5.' + str(count) + '.1.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_2)
            interfaces_rt5_3 = create_interface(Port=Port1, Layers='ipv6', Count=10, Name="RT5 Device V6 " + str(count))
            edit_interface(Interface=interfaces_rt5_3,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:91')
            edit_interface(Interface=interfaces_rt5_3,
                           Layer='IPv6Layer',
                           Address='5:' + hex(count)[2:] + ':1::2',
                           Gateway='5:' + hex(count)[2:] + ':1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_3)
            interfaces_rt5_4 = create_interface(Port=Port1, Layers='ipv6', Count=10,
                                                Name="RT5 Device V6 2-" + str(count))
            edit_interface(Interface=interfaces_rt5_4,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:91')
            edit_interface(Interface=interfaces_rt5_4,
                           Layer='IPv6Layer',
                           Address='5:' + hex(count)[2:] + ':1::2',
                           Gateway='5:' + hex(count)[2:] + ':1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_4)
            interfaces_host_1 = create_interface(Port=Port2, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC4-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_1,
                           Layer='EthIILayer',
                           Address='00:10:80:00:' + g + ':01')
            edit_interface(Interface=interfaces_host_1,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_1,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(num) + '.2',
                           Gateway='2.1.' + str(num) + '.1')
            Interface_TC4_T_All.append(interfaces_host_1)
            interfaces_host_2 = create_interface(Port=Port2, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC4-V6-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_2,
                           Layer='EthIILayer',
                           Address='00:10:80:00:' + g + ':01')
            edit_interface(Interface=interfaces_host_2,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_2,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(num)[2:] + ':1::2',
                           Gateway='2:1:' + hex(num)[2:] + ':1::1')
            Interface_TC4_V6_1.append(interfaces_host_2)
            interfaces_host_3 = create_interface(Port=Port3, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC5-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_3,
                           Layer='EthIILayer',
                           Address='00:10:81:00:' + g + ':01')
            edit_interface(Interface=interfaces_host_3,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_3,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(num) + '.102',
                           Gateway='2.1.' + str(num) + '.1')
            Interface_TC5_T_All.append(interfaces_host_3)
            interfaces_host_4 = create_interface(Port=Port3, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC5-V6-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_4,
                           Layer='EthIILayer',
                           Address='00:10:81:00:' + g + ':01')
            edit_interface(Interface=interfaces_host_4,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_4,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(num)[2:] + ':1::102',
                           Gateway='2:1:' + hex(num)[2:] + ':1::1')
            Interface_TC5_V6_1.append(interfaces_host_4)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_1)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_2)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_3)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_4)
            binding_vxlan_vtep(Vteps=vxlans_1[xin], Interfaces=interfaces_vm_1)
            binding_vxlan_vtep(Vteps=vxlans_1[xin], Interfaces=interfaces_vm_3)
            binding_vxlan_vtep(Vteps=vxlans_2[xin], Interfaces=interfaces_vm_2)
            binding_vxlan_vtep(Vteps=vxlans_2[xin], Interfaces=interfaces_vm_4)
            binding_vxlan_vtep(Vteps=vxlans_1[xin], Interfaces=interfaces_rt5_1)
            binding_vxlan_vtep(Vteps=vxlans_1[xin], Interfaces=interfaces_rt5_3)
            binding_vxlan_vtep(Vteps=vxlans_2[xin], Interfaces=interfaces_rt5_2)
            binding_vxlan_vtep(Vteps=vxlans_2[xin], Interfaces=interfaces_rt5_4)


        else:
            number = number + 1
            e = e + 1
            Segment = create_vxlan_segment(Name='Seg ' + str(e),
                                           StartVni=str(e),
                                           CommunicationType=2,
                                           EnableL3Vni=True,
                                           StartL3Vni=str(l3vni),
                                           VniTrafficType=1)

            interfaces_vm_1 = create_interface(Port=Port1, Layers='ipv4', Count=30, Name='VM Device ' + str(num))
            edit_interface(Interface=interfaces_vm_1,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_1,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(d) + '.2',
                           Gateway='4.' + str(count) + '.' + str(d) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_1)
            interfaces_vm_2 = create_interface(Port=Port1, Layers='ipv4', Count=30, Name='VM Device 2-' + str(num))
            edit_interface(Interface=interfaces_vm_2,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_2,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(d) + '.2',
                           Gateway='4.' + str(count) + '.' + str(d) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_2)
            interfaces_vm_3 = create_interface(Port=Port1, Layers='ipv6', Count=6, Name='VM Device v6 ' + str(num))
            edit_interface(Interface=interfaces_vm_3,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_3,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(d) + '::2')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_3)
            interfaces_vm_4 = create_interface(Port=Port1, Layers='ipv6', Count=6, Name='VM Device v6 2-' + str(num))
            edit_interface(Interface=interfaces_vm_4,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_4,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(d) + '::2')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_4)
            interfaces_host_1 = create_interface(Port=Port2, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC4-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_1,
                           Layer='EthIILayer',
                           Address='00:10:80:00:' + g + ':01')
            edit_interface(Interface=interfaces_host_1,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_1,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(num) + '.2',
                           Gateway='2.1.' + str(num) + '.1')
            Interface_TC4_T_All.append(interfaces_host_1)
            interfaces_host_2 = create_interface(Port=Port2, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC4-V6-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_2,
                           Layer='EthIILayer',
                           Address='00:10:80:00:' + g + ':01')
            edit_interface(Interface=interfaces_host_2,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_2,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(num)[2:] + ':1::2',
                           Gateway='2:1:' + hex(num)[2:] + ':1::1')
            Interface_TC4_V6_2.append(interfaces_host_2)
            interfaces_host_3 = create_interface(Port=Port3, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC5-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_3,
                           Layer='EthIILayer',
                           Address='00:10:81:00:' + g + ':01')
            edit_interface(Interface=interfaces_host_3,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_3,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(num) + '.102',
                           Gateway='2.1.' + str(num) + '.1')
            Interface_TC5_T_All.append(interfaces_host_3)
            interfaces_host_4 = create_interface(Port=Port3, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC5-V6-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_4,
                           Layer='EthIILayer',
                           Address='00:10:81:00:' + g + ':01')
            edit_interface(Interface=interfaces_host_4,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_4,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(num)[2:] + ':1::102',
                           Gateway='2:1:' + hex(num)[2:] + ':1::1')
            Interface_TC5_V6_2.append(interfaces_host_4)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_1)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_2)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_3)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_4)
            binding_vxlan_vtep(Vteps=vxlans_1[xin], Interfaces=interfaces_vm_1)
            binding_vxlan_vtep(Vteps=vxlans_1[xin], Interfaces=interfaces_vm_3)
            binding_vxlan_vtep(Vteps=vxlans_2[xin], Interfaces=interfaces_vm_2)
            binding_vxlan_vtep(Vteps=vxlans_2[xin], Interfaces=interfaces_vm_4)
            l3vni = l3vni + 1
            count = count + 1
            xin = xin + 1
            f = f + 1

    count = 21
    xin = 0
    number = 0
    l3vni = 10031
    e = 240
    f = 31
    for num in range(1, 41):
        a = hex(num + 39)[2:]
        b = hex(count)[2:]
        c = 1
        d = 2
        h = hex(count)[2:]
        i = count + 1
        g = hex(num)[2:]
        if number % 2 == 0:
            number = number + 1
            e = e + 1
            T = 40 + num
            Segment = create_vxlan_segment(Name='Seg ' + str(e),
                                           StartVni=str(e),
                                           CommunicationType=2,
                                           EnableL3Vni=True,
                                           StartL3Vni=str(l3vni),
                                           VniTrafficType=1)
            interfaces_vm_1 = create_interface(Port=Port4, Layers='ipv4', Count=30, Name='VM Device ' + str(T))
            edit_interface(Interface=interfaces_vm_1,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_1,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(c) + '.2',
                           Gateway='4.' + str(count) + '.' + str(c) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_1)
            interfaces_vm_2 = create_interface(Port=Port4, Layers='ipv4', Count=30, Name='VM Device 2-' + str(T))
            edit_interface(Interface=interfaces_vm_2,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_2,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(c) + '.2',
                           Gateway='4.' + str(count) + '.' + str(c) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_2)
            interfaces_vm_3 = create_interface(Port=Port4, Layers='ipv6', Count=6, Name='VM Device v6 ' + str(T))
            edit_interface(Interface=interfaces_vm_3,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_3,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(c) + '::2')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_3)
            interfaces_vm_4 = create_interface(Port=Port4, Layers='ipv6', Count=6, Name='VM Device v6 2-' + str(T))
            edit_interface(Interface=interfaces_vm_4,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_4,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(c) + '::2')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_4)
            interfaces_rt5_1 = create_interface(Port=Port4, Layers='ipv4', Count=10, Name="RT5 Device " + str(count))
            edit_interface(Interface=interfaces_rt5_1,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:8F')
            edit_interface(Interface=interfaces_rt5_1,
                           Layer='IPv4Layer',
                           Address='5.' + str(count) + '.1.2',
                           Gateway='5.1.1.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_1)
            interfaces_rt5_2 = create_interface(Port=Port4, Layers='ipv4', Count=10, Name="RT5 Device 2-" + str(count))
            edit_interface(Interface=interfaces_rt5_2,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:8F')
            edit_interface(Interface=interfaces_rt5_2,
                           Layer='IPv4Layer',
                           Address='5.' + str(count) + '.1.2',
                           Gateway='5.1.1.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_2)
            interfaces_rt5_3 = create_interface(Port=Port4, Layers='ipv6', Count=10, Name="RT5 Device V6 " + str(count))
            edit_interface(Interface=interfaces_rt5_3,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:91')
            edit_interface(Interface=interfaces_rt5_3,
                           Layer='IPv6Layer',
                           Address='5:' + hex(count)[2:] + ':1::2',
                           Gateway='5:1:1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_3)
            interfaces_rt5_4 = create_interface(Port=Port4, Layers='ipv6', Count=10,
                                                Name="RT5 Device V6 2-" + str(count))
            edit_interface(Interface=interfaces_rt5_4,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:91')
            edit_interface(Interface=interfaces_rt5_4,
                           Layer='IPv6Layer',
                           Address='5:' + hex(count)[2:] + ':1::2',
                           Gateway='5:1:1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_4)
            interfaces_host_1 = create_interface(Port=Port5, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC4-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_1,
                           Layer='EthIILayer',
                           Address='00:10:80:01:' + g + ':01')
            edit_interface(Interface=interfaces_host_1,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_1,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.2',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_2 = create_interface(Port=Port5, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC4-V6-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_2,
                           Layer='EthIILayer',
                           Address='00:10:80:01:' + g + ':01')
            edit_interface(Interface=interfaces_host_2,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_2,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::2',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            interfaces_host_3 = create_interface(Port=Port6, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC5-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_3,
                           Layer='EthIILayer',
                           Address='00:10:81:01:' + g + ':01')
            edit_interface(Interface=interfaces_host_3,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_3,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.102',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_4 = create_interface(Port=Port6, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC5-V6-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_4,
                           Layer='EthIILayer',
                           Address='00:10:81:01:' + g + ':01')
            edit_interface(Interface=interfaces_host_4,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_4,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::102',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_1)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_2)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_3)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_4)
            binding_vxlan_vtep(Vteps=vxlans_3[xin], Interfaces=interfaces_vm_1)
            binding_vxlan_vtep(Vteps=vxlans_3[xin], Interfaces=interfaces_vm_3)
            binding_vxlan_vtep(Vteps=vxlans_4[xin], Interfaces=interfaces_vm_2)
            binding_vxlan_vtep(Vteps=vxlans_4[xin], Interfaces=interfaces_vm_4)
            binding_vxlan_vtep(Vteps=vxlans_3[xin], Interfaces=interfaces_rt5_1)
            binding_vxlan_vtep(Vteps=vxlans_3[xin], Interfaces=interfaces_rt5_3)
            binding_vxlan_vtep(Vteps=vxlans_4[xin], Interfaces=interfaces_rt5_2)
            binding_vxlan_vtep(Vteps=vxlans_4[xin], Interfaces=interfaces_rt5_4)

        else:
            number = number + 1
            e = e + 1
            T = 40 + num
            Segment = create_vxlan_segment(Name='Seg ' + str(e),
                                           StartVni=str(e),
                                           CommunicationType=2,
                                           EnableL3Vni=True,
                                           StartL3Vni=str(l3vni),
                                           VniTrafficType=1)

            interfaces_vm_1 = create_interface(Port=Port4, Layers='ipv4', Count=30, Name='VM Device ' + str(T))
            edit_interface(Interface=interfaces_vm_1,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_1,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(d) + '.2',
                           Gateway='4.' + str(count) + '.' + str(d) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_1)
            interfaces_vm_2 = create_interface(Port=Port4, Layers='ipv4', Count=30, Name='VM Device 2-' + str(T))
            edit_interface(Interface=interfaces_vm_2,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_2,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(d) + '.2',
                           Gateway='4.' + str(count) + '.' + str(d) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_2)
            interfaces_vm_3 = create_interface(Port=Port4, Layers='ipv6', Count=6, Name='VM Device v6 ' + str(T))
            edit_interface(Interface=interfaces_vm_3,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_3,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(d) + '::2')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_3)
            interfaces_vm_4 = create_interface(Port=Port4, Layers='ipv6', Count=6, Name='VM Device v6 2-' + str(T))
            edit_interface(Interface=interfaces_vm_4,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_4,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(d) + '::2')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_4)
            interfaces_host_1 = create_interface(Port=Port5, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC4-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_1,
                           Layer='EthIILayer',
                           Address='00:10:80:01:' + g + ':01')
            edit_interface(Interface=interfaces_host_1,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_1,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.2',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_2 = create_interface(Port=Port5, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC4-V6-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_2,
                           Layer='EthIILayer',
                           Address='00:10:80:01:' + g + ':01')
            edit_interface(Interface=interfaces_host_2,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_2,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::2',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            interfaces_host_3 = create_interface(Port=Port6, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC5-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_3,
                           Layer='EthIILayer',
                           Address='00:10:81:01:' + g + ':01')
            edit_interface(Interface=interfaces_host_3,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_3,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.102',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_4 = create_interface(Port=Port6, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC5-V6-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_4,
                           Layer='EthIILayer',
                           Address='00:10:81:01:' + g + ':01')
            edit_interface(Interface=interfaces_host_4,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_4,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::102',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_1)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_2)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_3)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_4)
            binding_vxlan_vtep(Vteps=vxlans_3[xin], Interfaces=interfaces_vm_1)
            binding_vxlan_vtep(Vteps=vxlans_3[xin], Interfaces=interfaces_vm_3)
            binding_vxlan_vtep(Vteps=vxlans_4[xin], Interfaces=interfaces_vm_2)
            binding_vxlan_vtep(Vteps=vxlans_4[xin], Interfaces=interfaces_vm_4)
            l3vni = l3vni + 1
            count = count + 1
            xin = xin + 1
            f = f + 1

    count = 41
    xin = 0
    number = 0
    l3vni = 10051
    e = 280
    f = 51
    for num in range(1, 41):
        a = hex(num + 79)[2:]
        b = hex(count)[2:]
        c = 1
        d = 2
        h = hex(count)[2:]
        i = count + 1
        g = hex(num)[2:]
        if number % 2 == 0:
            number = number + 1
            e = e + 1
            T = 80 + num
            Segment = create_vxlan_segment(Name='Seg ' + str(e),
                                           StartVni=str(e),
                                           CommunicationType=2,
                                           EnableL3Vni=True,
                                           StartL3Vni=str(l3vni),
                                           VniTrafficType=1)
            interfaces_vm_1 = create_interface(Port=Port7, Layers='ipv4', Count=30, Name='VM Device ' + str(T))
            edit_interface(Interface=interfaces_vm_1,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_1,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(c) + '.2',
                           Gateway='4.' + str(count) + '.' + str(c) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_1)
            interfaces_vm_2 = create_interface(Port=Port7, Layers='ipv4', Count=30, Name='VM Device 2-' + str(T))
            edit_interface(Interface=interfaces_vm_2,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_2,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(c) + '.2',
                           Gateway='4.' + str(count) + '.' + str(c) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_2)
            interfaces_vm_3 = create_interface(Port=Port7, Layers='ipv6', Count=6, Name='VM Device v6 ' + str(T))
            edit_interface(Interface=interfaces_vm_3,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_3,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(c) + '::2',
                           Gateway='4:' + b + ':' + str(c) + '::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_3)
            interfaces_vm_4 = create_interface(Port=Port7, Layers='ipv6', Count=6, Name='VM Device v6 2-' + str(T))
            edit_interface(Interface=interfaces_vm_4,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_4,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(c) + '::2',
                           Gateway='4:' + b + ':' + str(c) + '::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_4)
            interfaces_rt5_1 = create_interface(Port=Port7, Layers='ipv4', Count=10, Name="RT5 Device " + str(count))
            edit_interface(Interface=interfaces_rt5_1,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:8F')
            edit_interface(Interface=interfaces_rt5_1,
                           Layer='IPv4Layer',
                           Address='5.' + str(count) + '.1.2',
                           Gateway='5.1.1.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_1)
            interfaces_rt5_2 = create_interface(Port=Port7, Layers='ipv4', Count=10, Name="RT5 Device 2-" + str(count))
            edit_interface(Interface=interfaces_rt5_2,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:8F')
            edit_interface(Interface=interfaces_rt5_2,
                           Layer='IPv4Layer',
                           Address='5.' + str(count) + '.1.2',
                           Gateway='5.1.1.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_2)
            interfaces_rt5_3 = create_interface(Port=Port7, Layers='ipv6', Count=10, Name="RT5 Device V6 " + str(count))
            edit_interface(Interface=interfaces_rt5_3,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:91')
            edit_interface(Interface=interfaces_rt5_3,
                           Layer='IPv6Layer',
                           Address='5:' + hex(count)[2:] + ':1::2',
                           Gateway='5:1:1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_3)
            interfaces_rt5_4 = create_interface(Port=Port7, Layers='ipv6', Count=10,
                                                Name="RT5 Device V6 2-" + str(count))
            edit_interface(Interface=interfaces_rt5_4,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:91')
            edit_interface(Interface=interfaces_rt5_4,
                           Layer='IPv6Layer',
                           Address='5:' + hex(count)[2:] + ':1::2',
                           Gateway='5:1:1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_4)
            interfaces_host_1 = create_interface(Port=Port8, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC4-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_1,
                           Layer='EthIILayer',
                           Address='00:10:80:02:' + g + ':01')
            edit_interface(Interface=interfaces_host_1,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_1,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.2',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_2 = create_interface(Port=Port8, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC4-V6-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_2,
                           Layer='EthIILayer',
                           Address='00:10:80:02:' + g + ':01')
            edit_interface(Interface=interfaces_host_2,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_2,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::2',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            interfaces_host_3 = create_interface(Port=Port9, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC5-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_3,
                           Layer='EthIILayer',
                           Address='00:10:81:02:' + g + ':01')
            edit_interface(Interface=interfaces_host_3,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_3,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.102',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_4 = create_interface(Port=Port9, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC5-V6-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_4,
                           Layer='EthIILayer',
                           Address='00:10:81:02:' + g + ':01')
            edit_interface(Interface=interfaces_host_4,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_4,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::102',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_1)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_2)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_3)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_4)
            binding_vxlan_vtep(Vteps=vxlans_5[xin], Interfaces=interfaces_vm_1)
            binding_vxlan_vtep(Vteps=vxlans_5[xin], Interfaces=interfaces_vm_3)
            binding_vxlan_vtep(Vteps=vxlans_6[xin], Interfaces=interfaces_vm_2)
            binding_vxlan_vtep(Vteps=vxlans_6[xin], Interfaces=interfaces_vm_4)
            binding_vxlan_vtep(Vteps=vxlans_5[xin], Interfaces=interfaces_rt5_1)
            binding_vxlan_vtep(Vteps=vxlans_5[xin], Interfaces=interfaces_rt5_3)
            binding_vxlan_vtep(Vteps=vxlans_6[xin], Interfaces=interfaces_rt5_2)
            binding_vxlan_vtep(Vteps=vxlans_6[xin], Interfaces=interfaces_rt5_4)

        else:
            number = number + 1
            e = e + 1
            T = 80 + num
            Segment = create_vxlan_segment(Name='Seg ' + str(e),
                                           StartVni=str(e),
                                           CommunicationType=2,
                                           EnableL3Vni=True,
                                           StartL3Vni=str(l3vni),
                                           VniTrafficType=1)

            interfaces_vm_1 = create_interface(Port=Port7, Layers='ipv4', Count=30, Name='VM Device ' + str(T))
            edit_interface(Interface=interfaces_vm_1,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_1,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(d) + '.2',
                           Gateway='4.' + str(count) + '.' + str(d) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_1)
            interfaces_vm_2 = create_interface(Port=Port7, Layers='ipv4', Count=30, Name='VM Device 2-' + str(T))
            edit_interface(Interface=interfaces_vm_2,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_2,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(d) + '.2',
                           Gateway='4.' + str(count) + '.' + str(d) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_2)
            interfaces_vm_3 = create_interface(Port=Port7, Layers='ipv6', Count=6, Name='VM Device v6 ' + str(T))
            edit_interface(Interface=interfaces_vm_3,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_3,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(d) + '::2',
                           Gateway='4:' + b + ':' + str(d) + '::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_3)
            interfaces_vm_4 = create_interface(Port=Port7, Layers='ipv6', Count=6, Name='VM Device v6 2-' + str(T))
            edit_interface(Interface=interfaces_vm_4,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_4,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(d) + '::2',
                           Gateway='4:' + b + ':' + str(d) + '::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_4)
            interfaces_host_1 = create_interface(Port=Port8, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC4-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_1,
                           Layer='EthIILayer',
                           Address='00:10:80:02:' + g + ':01')
            edit_interface(Interface=interfaces_host_1,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_1,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.2',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_2 = create_interface(Port=Port8, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC4-V6-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_2,
                           Layer='EthIILayer',
                           Address='00:10:80:02:' + g + ':01')
            edit_interface(Interface=interfaces_host_2,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_2,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::2',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            interfaces_host_3 = create_interface(Port=Port9, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC5-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_3,
                           Layer='EthIILayer',
                           Address='00:10:81:02:' + g + ':01')
            edit_interface(Interface=interfaces_host_3,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_3,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.102',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_4 = create_interface(Port=Port9, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC5-V6-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_4,
                           Layer='EthIILayer',
                           Address='00:10:81:02:' + g + ':01')
            edit_interface(Interface=interfaces_host_4,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_4,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::102',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_1)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_2)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_3)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_4)
            binding_vxlan_vtep(Vteps=vxlans_5[xin], Interfaces=interfaces_vm_1)
            binding_vxlan_vtep(Vteps=vxlans_5[xin], Interfaces=interfaces_vm_3)
            binding_vxlan_vtep(Vteps=vxlans_6[xin], Interfaces=interfaces_vm_2)
            binding_vxlan_vtep(Vteps=vxlans_6[xin], Interfaces=interfaces_vm_4)
            l3vni = l3vni + 1
            count = count + 1
            xin = xin + 1
            f = f + 1

    count = 61
    xin = 0
    number = 0
    l3vni = 10071
    e = 320
    f = 71
    for num in range(1, 41):
        a = hex(num + 119)[2:]
        b = hex(count)[2:]
        c = 1
        d = 2
        h = hex(count)[2:]
        i = count + 1
        g = hex(num)[2:]
        if number % 2 == 0:
            number = number + 1
            e = e + 1
            T = 120 + num
            Segment = create_vxlan_segment(Name='Seg ' + str(e),
                                           StartVni=str(e),
                                           CommunicationType=2,
                                           EnableL3Vni=True,
                                           StartL3Vni=str(l3vni),
                                           VniTrafficType=1)
            interfaces_vm_1 = create_interface(Port=Port10, Layers='ipv4', Count=30, Name='VM Device ' + str(T))
            edit_interface(Interface=interfaces_vm_1,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_1,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(c) + '.2',
                           Gateway='4.' + str(count) + '.' + str(c) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_1)
            interfaces_vm_2 = create_interface(Port=Port10, Layers='ipv4', Count=30, Name='VM Device 2-' + str(T))
            edit_interface(Interface=interfaces_vm_2,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_2,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(c) + '.2',
                           Gateway='4.' + str(count) + '.' + str(c) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_2)
            interfaces_vm_3 = create_interface(Port=Port10, Layers='ipv6', Count=6, Name='VM Device v6 ' + str(T))
            edit_interface(Interface=interfaces_vm_3,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_3,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(c) + '::2',
                           Gateway='4:' + b + ':' + str(c) + '::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_3)
            interfaces_vm_4 = create_interface(Port=Port10, Layers='ipv6', Count=6, Name='VM Device v6 2-' + str(T))
            edit_interface(Interface=interfaces_vm_4,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_4,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(c) + '::2',
                           Gateway='4:' + b + ':' + str(c) + '::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_4)
            interfaces_rt5_1 = create_interface(Port=Port10, Layers='ipv4', Count=10, Name="RT5 Device " + str(count))
            edit_interface(Interface=interfaces_rt5_1,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:8F')
            edit_interface(Interface=interfaces_rt5_1,
                           Layer='IPv4Layer',
                           Address='5.' + str(count) + '.1.2',
                           Gateway='5.1.1.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_1)
            interfaces_rt5_2 = create_interface(Port=Port10, Layers='ipv4', Count=10, Name="RT5 Device 2-" + str(count))
            edit_interface(Interface=interfaces_rt5_2,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:8F')
            edit_interface(Interface=interfaces_rt5_2,
                           Layer='IPv4Layer',
                           Address='5.' + str(count) + '.1.2',
                           Gateway='5.1.1.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_2)
            interfaces_rt5_3 = create_interface(Port=Port10, Layers='ipv6', Count=10,
                                                Name="RT5 Device V6 " + str(count))
            edit_interface(Interface=interfaces_rt5_3,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:91')
            edit_interface(Interface=interfaces_rt5_3,
                           Layer='IPv6Layer',
                           Address='5:' + hex(count)[2:] + ':1::2',
                           Gateway='5:1:1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_3)
            interfaces_rt5_4 = create_interface(Port=Port10, Layers='ipv6', Count=10,
                                                Name="RT5 Device V6 2-" + str(count))
            edit_interface(Interface=interfaces_rt5_4,
                           Layer='EthIILayer',
                           Address='00:10:94:00:30:91')
            edit_interface(Interface=interfaces_rt5_4,
                           Layer='IPv6Layer',
                           Address='5:' + hex(count)[2:] + ':1::2',
                           Gateway='5:1:1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_rt5_4)
            interfaces_host_1 = create_interface(Port=Port11, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC4-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_1,
                           Layer='EthIILayer',
                           Address='00:10:80:03:' + g + ':01')
            edit_interface(Interface=interfaces_host_1,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_1,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.2',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_2 = create_interface(Port=Port11, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC4-V6-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_2,
                           Layer='EthIILayer',
                           Address='00:10:80:03:' + g + ':01')
            edit_interface(Interface=interfaces_host_2,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_2,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::2',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            interfaces_host_3 = create_interface(Port=Port12, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC5-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_3,
                           Layer='EthIILayer',
                           Address='00:10:81:03:' + g + ':01')
            edit_interface(Interface=interfaces_host_3,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_3,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.102',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_4 = create_interface(Port=Port12, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC5-V6-T' + str(f) + '-' + str(c))
            edit_interface(Interface=interfaces_host_4,
                           Layer='EthIILayer',
                           Address='00:10:81:03:' + g + ':01')
            edit_interface(Interface=interfaces_host_4,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_4,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::102',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_1)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_2)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_3)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_4)
            binding_vxlan_vtep(Vteps=vxlans_7[xin], Interfaces=interfaces_vm_1)
            binding_vxlan_vtep(Vteps=vxlans_7[xin], Interfaces=interfaces_vm_3)
            binding_vxlan_vtep(Vteps=vxlans_8[xin], Interfaces=interfaces_vm_2)
            binding_vxlan_vtep(Vteps=vxlans_8[xin], Interfaces=interfaces_vm_4)
            binding_vxlan_vtep(Vteps=vxlans_7[xin], Interfaces=interfaces_rt5_1)
            binding_vxlan_vtep(Vteps=vxlans_7[xin], Interfaces=interfaces_rt5_3)
            binding_vxlan_vtep(Vteps=vxlans_8[xin], Interfaces=interfaces_rt5_2)
            binding_vxlan_vtep(Vteps=vxlans_8[xin], Interfaces=interfaces_rt5_4)

        else:
            number = number + 1
            e = e + 1
            T = 120 + num
            Segment = create_vxlan_segment(Name='Seg ' + str(e),
                                           StartVni=str(e),
                                           CommunicationType=2,
                                           EnableL3Vni=True,
                                           StartL3Vni=str(l3vni),
                                           VniTrafficType=1)

            interfaces_vm_1 = create_interface(Port=Port10, Layers='ipv4', Count=30, Name='VM Device ' + str(T))
            edit_interface(Interface=interfaces_vm_1,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_1,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(d) + '.2',
                           Gateway='4.' + str(count) + '.' + str(d) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_1)
            interfaces_vm_2 = create_interface(Port=Port10, Layers='ipv4', Count=30, Name='VM Device 2-' + str(T))
            edit_interface(Interface=interfaces_vm_2,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_2,
                           Layer='IPv4Layer',
                           Address='4.' + str(count) + '.' + str(d) + '.2',
                           Gateway='4.' + str(count) + '.' + str(d) + '.1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_2)
            interfaces_vm_3 = create_interface(Port=Port10, Layers='ipv6', Count=6, Name='VM Device v6 ' + str(T))
            edit_interface(Interface=interfaces_vm_3,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_3,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(d) + '::2',
                           Gateway='4:' + b + ':' + str(d) + '::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_3)
            interfaces_vm_4 = create_interface(Port=Port10, Layers='ipv6', Count=6, Name='VM Device v6 2-' + str(T))
            edit_interface(Interface=interfaces_vm_4,
                           Layer='EthIILayer',
                           Address='00:00:10:' + b + ':' + a + ':00')
            edit_interface(Interface=interfaces_vm_4,
                           Layer='IPv6Layer',
                           Address='4:' + b + ':' + str(d) + '::2',
                           Gateway='4:' + b + ':' + str(d) + '::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_vm_4)
            interfaces_host_1 = create_interface(Port=Port11, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC4-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_1,
                           Layer='EthIILayer',
                           Address='00:10:80:03:' + g + ':01')
            edit_interface(Interface=interfaces_host_1,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_1,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.2',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_2 = create_interface(Port=Port11, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC4-V6-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_2,
                           Layer='EthIILayer',
                           Address='00:10:80:03:' + g + ':01')
            edit_interface(Interface=interfaces_host_2,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_2,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::2',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            interfaces_host_3 = create_interface(Port=Port12, Layers=headerlayers, Tops=headerlayers_ipv4, Count=20,
                                                 Name='TC5-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_3,
                           Layer='EthIILayer',
                           Address='00:10:81:03:' + g + ':01')
            edit_interface(Interface=interfaces_host_3,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_3,
                           Layer='IPv4Layer',
                           Address='2.1.' + str(T) + '.102',
                           Gateway='2.1.' + str(T) + '.1')
            interfaces_host_4 = create_interface(Port=Port12, Layers=headerlayers, Tops=headerlayers_ipv6, Count=20,
                                                 Name='TC5-V6-T' + str(f) + '-' + str(d))
            edit_interface(Interface=interfaces_host_4,
                           Layer='EthIILayer',
                           Address='00:10:81:03:' + g + ':01')
            edit_interface(Interface=interfaces_host_4,
                           Layer='VLANLayer',
                           VlanId=e,
                           Step=0,
                           Priority=7)
            edit_interface(Interface=interfaces_host_4,
                           Layer='IPv6Layer',
                           Address='2:1:' + hex(T)[2:] + ':1::102',
                           Gateway='2:1:' + hex(T)[2:] + ':1::1')
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_1)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_2)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_3)
            binding_vxlan_vm(Segments=Segment, Interfaces=interfaces_host_4)
            binding_vxlan_vtep(Vteps=vxlans_7[xin], Interfaces=interfaces_vm_1)
            binding_vxlan_vtep(Vteps=vxlans_7[xin], Interfaces=interfaces_vm_3)
            binding_vxlan_vtep(Vteps=vxlans_8[xin], Interfaces=interfaces_vm_2)
            binding_vxlan_vtep(Vteps=vxlans_8[xin], Interfaces=interfaces_vm_4)
            l3vni = l3vni + 1
            count = count + 1
            xin = xin + 1
            f = f + 1

    Points_TC4_T_All = get_layer_from_interfaces(Interfaces=Interface_TC4_T_All, Layer='ipv4')
    Points_TC5_T_All = get_layer_from_interfaces(Interfaces=Interface_TC5_T_All, Layer='ipv4')
    stream_TC4_T_TC5_T = add_stream(Type='binding', Names=stream_names, SrcPoints=Points_TC4_T_All,
                                    DstPoints=Points_TC5_T_All,
                                    TrafficMeshMode='ONE_TO_ONE', Layer='IPV4')
    create_stream_header(Stream=stream_TC4_T_TC5_T, Index=0, HeaderTypes=udplayer)
    edit_header_udp(Stream=stream_TC4_T_TC5_T, Level=0, SourcePort=20000, DestPort=10000)
    edit_modifier(Stream=stream_TC4_T_TC5_T, Attribute='SourcePort', Level=0, Type='Increment', Count=1000,
                  HeaderType='udp')
    edit_modifier(Stream=stream_TC4_T_TC5_T, Attribute='DestPort', Level=0, Type='Increment', Count=100,
                  HeaderType='udp')

    Interface_TC4_V6_All = Interface_TC4_V6_1 + Interface_TC4_V6_2
    Interface_TC5_V6_All = Interface_TC5_V6_2 + Interface_TC5_V6_1
    Points_TC4_V6_All = get_layer_from_interfaces(Interfaces=Interface_TC4_V6_All, Layer='ipv6')
    Points_TC5_V6_All = get_layer_from_interfaces(Interfaces=Interface_TC5_V6_All, Layer='ipv6')
    stream_TC4_V6_TC5_V6 = add_stream(Type='binding', Names=stream_names_TC4_V6, SrcPoints=Points_TC4_V6_All,
                                      DstPoints=Points_TC5_V6_All,
                                      TrafficMeshMode='ONE_TO_ONE', Layer='IPV6')
    create_stream_header(Stream=stream_TC4_V6_TC5_V6, Index=0, HeaderTypes=udplayer)
    edit_header_udp(Stream=stream_TC4_V6_TC5_V6, Level=0, SourcePort=20000, DestPort=10000)
    edit_modifier(Stream=stream_TC4_V6_TC5_V6, Attribute='SourcePort', Level=0, Type='Increment', Count=1000,
                  HeaderType='udp')
    edit_modifier(Stream=stream_TC4_V6_TC5_V6, Attribute='DestPort', Level=0, Type='Increment', Count=100,
                  HeaderType='udp')

    dirname, tempfilename = os.path.split(os.path.abspath(__file__))
    filename, extension = os.path.splitext(tempfilename)
    save_case(Path=f'{dirname}/xcfg/{filename}.xcfg')

except Exception as e:
    verdict = 'fail'
    errInfo = repr(e)
finally:
    print(f'errInfo:\n{errInfo}')
    print(f'verdict:{verdict}')
