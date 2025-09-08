
# Introduction

A company's network defense starts with fortifying the Internet edge with firewalls, but it is equally important to use hardware for regulating network traffic that reveals no more information than is necessary. Those who want to break into network systems employ reconnaissance techniques, which might reveal information that they can exploit to penetrate the edge defense. Ultimately, the tools that network engineers use to troubleshoot network problems are the same tools you will use to identify and learn vulnerable points in your perimeter infrastructure.

In this lab, we will use 7 different tools:
- ARP (Address Resolution Protocol) - This is a network protocol used to determine hardware addresses (MAC) of a device based on the IP address. It can be used when a device wants to communicate with another device on a network or it can be used to set up network interfaces on devices.

-  Ipconfig/Ifconfig - This command displays all of the TCP/IP network configuration values within a computer, including default gateways and netmasks. It can be used to refresh the Dynamic Host Configuration Protocols (DHCP) and the Domain Name System (DNS) settings. This command can be used to enable and disable ethernet or other network adapters. This command is a Windows-only command. Ifconfig is the linux based command that functions nearly identical to ipconfig. It can be used to display TCP/IP information as well as default gateways and netmasks.

- Hping3 - This is an updated version of a legacy tool called hping, a well-known, well-used tool for network scanning and firewall testing. Hping3 can send ICMP-based ping probes and other customized TCP/IP packets.

- Ping - This command sends a request over the network to a specific device. The communication will either succeed (return packets to the host machine) or fail (no packets returned). The command can be used with an IP address or a URL.

-  Tcpdump - This tool, which has been around since 1987, was written by Van Jacobson, who also wrote traceroute. Tcpdump is a network analyzer that intercepts and displays TCP/IP packets and uses the libpcap library to capture packets.

- Nmap - Nmap is similar to hping3 but extends its functionality by an order of magnitude with respect to the packets and speed with which they’re sent. Nmap also has a GUI version called Zenmap. Developed by Gordon Lyon (also known by his pseudonym, Fyodor Vaskovich), it was first published in 1997. Nmap crafts packets that it injects into a network and then analyzes the responses to map machines, ports, and services.

- Wireshark - Wireshark is similar to tcpdump but provides a more granular GUI interface. This allows for capture filters and display filters of the packet flows that it captures. It can also open saved capture files in a number of formats.

<u>Lab Overview</u>

Section 1:
1. In the first part of the lab, you will use the ipconfig, ARP, and ping commands to explore the Local Area Network.  

2. In the second part of the lab, you will use Nmap/Zenmap and Wireshark to capture and analyze network traffic.

Section 2:
Apply what was learned in section 1 with less guidance and different deliverables, as well as expanded tasks and alternative methods. Explore the WAN and use different tools for analyzing network traffic.

Section 3:
Explore the virtual environment to answer a set of questions and challenges that allow you to use the skills you learned in the lab to conduct independent, unguided work - similar to what might be encountered in a real-world situation.

SS 1

<u>Learning Objectives</u>

1. Identify IP addresses, MAC addresses, and subnet masks using network utilities.  
2. Generate customized TCP/IP packets, with varying speed and purpose.  
3. Capture network traffic for the purpose of analysis and investigation.  
4. Apply appropriate filters to view only the traffic subset of interest.  
5. Analyze network traffic to determine the configuration of running applications on the IP hosts from which traffic is captured.

<u>Topology</u>

The following virtual machines will be used:
- vWorkstation (Windows Server 2019)
- TargetWindows01 (Windows Server 2019)
- TargetLinux01 (Ubuntu Linux)
- pfSense
- AttackLinux01 (Kali Linux)
- RemoteWindows01 (Windows Server 2019)

SS 2

# Section 1,

<u>Part 1 - Explore the Local Area Network</u>

On the vWorkstation taskbar, **click** the **Command Prompt icon** to open a new Command Prompt window.

At the command prompt, **type ipconfig** and **press Enter** to display basic information about the vWorkstation’s network adapters.

SS3

  
At the command prompt, **type ipconfig /all** and **press Enter** to display detailed information about the vWorkstation’s network adapters.

SS4

vWorkstation
```cmd
Ethernet adapter Student:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : vmxnet3 Ethernet Adapter #3
   Physical Address. . . . . . . . . : 00-50-56-BD-31-02
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 172.30.0.2(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 172.30.0.1
   DNS Servers . . . . . . . . . . . : 172.30.0.10
   NetBIOS over Tcpip. . . . . . . . : Enabled
```


On the Lab View toolbar, **select TargetWindows01** from the Virtual Machine drop-down menu to connect to the TargetWindows01 machine.

**Repeat steps 1-3** on TargetWindows01.

SS5

TargetWindows01
```cmd
C:\Users\Administrator>ipconfig

Windows IP Configuration


Ethernet adapter TrueLab:

   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 192.168.205.2
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.205.254

Ethernet adapter Student:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::9d00:c31c:993f:228b%5
   IPv4 Address. . . . . . . . . . . : 172.30.0.10
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 172.30.0.1

C:\Users\Administrator>ipconfig /all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : TargetWindows01
   Primary Dns Suffix  . . . . . . . : securelabsondemand.com
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : securelabsondemand.com

Ethernet adapter TrueLab:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : vmxnet3 Ethernet Adapter
   Physical Address. . . . . . . . . : 00-50-56-BD-26-EF
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.205.2(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.205.254
   NetBIOS over Tcpip. . . . . . . . : Disabled

Ethernet adapter Student:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : vmxnet3 Ethernet Adapter #3
   Physical Address. . . . . . . . . : 00-50-56-BD-86-ED
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::9d00:c31c:993f:228b%5(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.30.0.10(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 172.30.0.1
   DHCPv6 IAID . . . . . . . . . . . : 167792726
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-30-4F-B8-24-00-50-56-BD-26-EF
   DNS Servers . . . . . . . . . . . : 127.0.0.1
   NetBIOS over Tcpip. . . . . . . . : Enabled
```

On the Lab View toolbar, **select vWorkstation** from the Virtual Machine drop-down menu to connect to the vWorkstation machine.

At the command prompt, **type arp** and **press Enter** to display the help guide for the ARP utility.

SS6

At the command prompt, **type arp -a** and press Enter to display the current ARP cache for the vWorkstation.

```cmd
C:\Users\Administrator>arp -a

Interface: 192.168.205.4 --- 0xd
  Internet Address      Physical Address      Type
  192.168.205.254       00-50-56-ab-66-1c     dynamic
  192.168.253.254       00-50-56-ab-66-1c     dynamic
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static

Interface: 172.30.0.2 --- 0x11
  Internet Address      Physical Address      Type
  172.30.0.1            00-50-56-bd-14-0f     dynamic
  172.30.0.10           00-50-56-bd-86-ed     dynamic
  172.30.0.255          ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
```

At the command prompt, **type arp -d** and **press Enter** to clear the ARP cache.

```cmd
arp -d
```

At the command compt, **type arp -a** and **press Enter** to display the updated ARP cache.

```cmd
C:\Users\Administrator>arp -a

Interface: 192.168.205.4 --- 0xd
  Internet Address      Physical Address      Type
  192.168.205.254       00-50-56-ab-66-1c     dynamic
  224.0.0.22            01-00-5e-00-00-16     static

Interface: 172.30.0.2 --- 0x11
  Internet Address      Physical Address      Type
  224.0.0.22            01-00-5e-00-00-16     static
```

At the command prompt, **type ping 172.30.0.10** and **press Enter** to ping the TargetWindows01 machine.

```cmd
C:\Users\Administrator>ping 172.30.0.10

Pinging 172.30.0.10 with 32 bytes of data:
Reply from 172.30.0.10: bytes=32 time<1ms TTL=128
Reply from 172.30.0.10: bytes=32 time<1ms TTL=128
Reply from 172.30.0.10: bytes=32 time<1ms TTL=128
Reply from 172.30.0.10: bytes=32 time<1ms TTL=128

Ping statistics for 172.30.0.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

At the command prompt, **type arp -a** and **press Enter** to display the updated ARP cache.
The ARP cache should now once again contain an entry for TargetWindows01.

```cmd
C:\Users\Administrator>arp -a

Interface: 192.168.205.4 --- 0xd
  Internet Address      Physical Address      Type
  192.168.205.254       00-50-56-ab-66-1c     dynamic
  224.0.0.22            01-00-5e-00-00-16     static

Interface: 172.30.0.2 --- 0x11
  Internet Address      Physical Address      Type
  172.30.0.1            00-50-56-bd-14-0f     dynamic
  172.30.0.10           00-50-56-bd-86-ed     dynamic
  172.30.0.255          ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
```

At the command prompt, **type exit** and **press Ente**r to close the command prompt window.

On the vWorkstation desktop, **double-click** the **NetworkAssessment file** to open it in OpenOffice Calc.

SS7

**Complete** the **LAN tab** using the information obtained from the ipconfig and ARP utilities.

(We can do this using ipconfig /all and arp -a)

SS8

<u>Part 2 - Analyze Network Traffic</u>

On the vWorkstation desktop, **double-click** the **Wireshark icon** to open the Wireshark application.

SS9

In the Wireshark window, **click** the **Student interface** to select the network interface that Wireshark will use to capture traffic.

From the Wireshark toolbar, **click** the **Start Capture button (the blue shark fin)** to begin the capture session.

SS10

**Minimize** the **Wireshark window**.

On the vWorkstation desktop, **double-click** the **Nmap - Zenmap GUI icon** to open the Zenmap application.

On the vWorkstation desktop, **double-click** the **Nmap - Zenmap GUI icon** to open the Zenmap application.

SS11

In the Zenmap window, **type 172.30.0.1** (the internal firewall interface) in the _Target_ box and **select Ping scan** from the Profile drop-down menu, then **click Scan** to start the scan.

SS12

**Restore** the **Wireshark window**.

In the Wireshark window, **type icmp** in the Filter box and **press Enter** to filter the results to show only the ping traffic.

SS13

On the Wireshark toolbar, **click** the **Clear button** (the x) to remove the ICMP filter, then **type arp** in the Filter box and **press Enter** to filter the results to show only ARP-related traffic.

SS14

**Review** the ARP packet results and **locate** a packet that lists the vWorkstation as the source and the firewall’s internal interface as the destination.

We can do so by identifying the vWorkstation using its MAC address.

00-50-56-BD-31-02

SS15

On the Wireshark toolbar, **click** the **Clear button** to remove the ARP filter.

**Restore** the **Zenmap window**.

In the Zenmap window, **select Regular scan** from the Profile drop-down list and **click Scan** to start a new scan.  
  
If you did not minimize the Wireshark window, you should see the traffic generated by nmap captured in real-time.

SS16

**Repeat steps 8 and 10** to observe whether the Regular scan generated additional ICMP and ARP traffic.

SS17

In the Zenmap window, **select Intense scan** from the Profile drop-down list and **click Scan** to start a new scan.

*This scan will take several minutes to complete. If you did not minimize the Wireshark window, you should see the traffic generated by nmap captured in real-time. While the scan is running, compare the command for this scan with that of the Ping scan. In this case, Nmap is directed to scan the IP address (**172.30.0.1**) as quickly as possible (**-T4**), to attempt to detect the operating system (**-A**), and to return as much information (verbose results) as it can (**-v**). You should notice that Wireshark has already captured substantially more traffic than the prior two scans.*

SS18

When the scan is complete, **restore** the **Wireshark window**.

**Repeat steps 8 and 10** to observe whether the Intense scan generated additional ICMP and ARP traffic.

SS19

SS20

From the Wireshark tool bar, **click** the **Stop icon** to end the capture session

**Restore** the **Zenmap window**.

In the Zenmap window, **click** the **Ports/Hosts tab** to see which ports are open and listening.

SS21

End Section 1

# Section 2

<u>Part 1 - Explore the WAN</u>

Use the Virtual Machine menu to **connect** to the **AttackLinux01 machine**.

SS22

At the AttackLinux01 login page, use the following credentials to **log in**:  
  
Username: **root**  
Password: **toor**

From the AttackLinux01 menu bar, **click** the **Activities menu**, then **click** the **Terminal icon** on the Applications bar to open a new Terminal window.

SS23

At the command prompt, **execute ifconfig** to display information about AttackLinux01’s default network adapter.

SS24

At the command prompt, **execute ifconfig -a** to display information about all of AttackLinux01’s network adapters.

*While AttackLinux01 has no additional network adapters to display, the **-a** switch is the ifconfig equivalent of the **/all** switch on Windows.*

SS25

**Close** the **Terminal window**.

Use the Virtual Machine menu to **connect** to the **RemoteWindows01 machine**

From the RemoteWindows01 taskbar, **open** a new **command prompt window**

At the command prompt, **execute the command** to display information about RemoteWindows01’s default network adapter.

```cmd
C:\Users\Administrator>ipconfig

Windows IP Configuration


Ethernet adapter Student:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::5969:38ab:fcdc:5977%11
   IPv4 Address. . . . . . . . . . . : 10.0.1.2
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 10.0.1.1

Ethernet adapter TrueLab:

   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 192.168.205.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.205.254
```

At the command prompt, **execute the command** to display the ARP cache for RemoteWindows01.  
  
```cmd
C:\Users\Administrator>arp -a

Interface: 10.0.1.2 --- 0xb
  Internet Address      Physical Address      Type
  10.0.1.1              00-50-56-bd-db-47     dynamic
  10.0.1.255            ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static

Interface: 192.168.205.1 --- 0xe
  Internet Address      Physical Address      Type
  192.168.205.254       00-50-56-ab-66-1c     dynamic
  192.168.253.254       00-50-56-ab-66-1c     dynamic
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
```

At the command prompt, **execute the command** to clear the ARP cache.

```cmd
C:\Users\Administrator>arp -d

C:\Users\Administrator>arp -a

Interface: 10.0.1.2 --- 0xb
  Internet Address      Physical Address      Type
  224.0.0.22            01-00-5e-00-00-16     static

Interface: 192.168.205.1 --- 0xe
  Internet Address      Physical Address      Type
  192.168.205.254       00-50-56-ab-66-1c     dynamic
  224.0.0.22            01-00-5e-00-00-16     static
```

At the command prompt, **execute the command** to ping the protected network's external firewall IP address at 202.20.1.1.

```cmd
C:\Users\Administrator>ping 202.20.1.1

Pinging 202.20.1.1 with 32 bytes of data:
Reply from 202.20.1.1: bytes=32 time=3ms TTL=63
Reply from 202.20.1.1: bytes=32 time=2ms TTL=63
Reply from 202.20.1.1: bytes=32 time=3ms TTL=63
Reply from 202.20.1.1: bytes=32 time=3ms TTL=63

Ping statistics for 202.20.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 2ms, Maximum = 3ms, Average = 2ms
```

At the command prompt, **execute the command** to display the updated ARP cache.  
  
The ARP cache for the Student network interface should now contain an entry for the RemoteWindows01 machine's default gateway (10.0.1.1).

```cmd
Interface: 10.0.1.2 --- 0xb
  Internet Address      Physical Address      Type
  10.0.1.1              00-50-56-bd-db-47     dynamic
  10.0.1.255            ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static

Interface: 192.168.205.1 --- 0xe
  Internet Address      Physical Address      Type
  192.168.205.254       00-50-56-ab-66-1c     dynamic
  224.0.0.22            01-00-5e-00-00-16     static
```

Use the Virtual Machine menu to **connect** to the **vWorkstation machine**.

**Restore** or **re-open** the **NetworkAssessment file**.

**Complete** the **WAN tab** using the information obtained from the if/ipconfig and arp utilities.

```cmd
C:\Users\Administrator>ipconfig /all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : RemoteWindows01
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No

Ethernet adapter Student:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : vmxnet3 Ethernet Adapter #3
   Physical Address. . . . . . . . . : 00-50-56-BD-E9-E9
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::5969:38ab:fcdc:5977%11(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.0.1.2(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 10.0.1.1
   DHCPv6 IAID . . . . . . . . . . . : 469782614
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-30-4F-B8-50-00-50-56-BD-E9-E9
   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter TrueLab:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : vmxnet3 Ethernet Adapter #2
   Physical Address. . . . . . . . . : 00-50-56-BD-5E-E7
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.205.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.205.254
   NetBIOS over Tcpip. . . . . . . . : Disabled
```

SS26

<u>Part 2 - Analyze Network Traffic</u>

Using the Virtual Machine menu, **connect** to the **AttackLinux01 machine**.

From the AttackLinux01 menu bar, **open** a new **Terminal window**.

At the command prompt, **execute hping3 -h** to open the help screen for hping3.

SS27

At the command prompt, **execute hping3 -1 -c 1 202.20.1.1**.

*This command uses ICMP mode (**-1**) to send a single packet (**-c 1**) to the external interface of the pfSense firewall/router (**202.20.1.1**).*

SS28

From the menu bar, **open** a second **Terminal window**.

At the command prompt in the second terminal window, **execute tcpdump -h**.
*As with hping3, adding the **-h** switch provides guidance on the available switches and parameters.*

SS29

In the tcpdump window, **execute tcpdump -i eth0 -n host 202.20.1.1** to collect packets as they are transmitted to the IP address 202.20.1.1.

SS30

In the hping3 window, **execute hping3 -1 -c 1 202.20.1.1** to send another ICMP packet to the external firewall interface

*In the tcpdump window, you will see tcpdump echo back the captured packets. There are two pairs of packets. The first two packets are the ICMP echo request and the ICMP echo reply. The second pair of packets consists of an Address Resolution Protocol (ARP) request and an ARP reply providing the MAC address of the firewall.*

SS31

SS32

In the hping3 terminal window, **execute hping3 -S -c 1 -s 5151 202.20.1.1** to send a single (**-c 1**) SYN packet (**-S**), directed to the firewall (**202.20.1.1**) on source port (**-s**) 5151.

*Notice that the tcpdump output shows the SYN packet sent (Flags [S]) from the Kali machine to the firewall, but with no response. The destination port was not listening. Because hping3 is sending the packet without a specified destination port, you should not expect any response.*

SS33

SS34

In the hping3 window, **type hping3 -S -c 1 -s 5151 -p 80 202.20.1.1** and **press Enter** to send the same packet to a specific destination port (**-p 80**) that should be listening.

*In the tcpdump window, the output shows the attempted three-way handshake. The firewall’s port 80 was listening and responded with a SYN/ACK. In a normal connection request, the third ACK packet would be sent. However, because hping3 did not intend to establish a connection, it instead sent the firewall a reset (R) packet, closing the connection request. Now you know that port 80 is active and listening. You could use this same technique to assess every individual port on a system, but doing so manually would be very tedious and time-consuming, and would be better accomplished by using a tool like Nmap. Nonetheless, it is valuable to observe and understand the transaction and handshake process at the packet level.*

SS35
SS36

In the hping3 window, **execute exit** to close the window.

In the tcpdump window, **press Ctrl+C** to cancel listening mode and return to the command prompt.

At the command prompt, **execute telnet 202.20.1.1 80** to request a telnet connection to the pfSense firewall-router on port 80.  
  
*The system will return a message indicating that a Telnet connection was made (connected to 202.20.1.1).*

SS37

**Execute get** to return a response from the web service.

*You should be able to see the type and version of the Web server running. This technique for enumerating information about the service running is called banner grabbing.*

SS38

End Section 2

# Section 3

<u>Part 1 - Explore the DMZ</u>

As a first step, you will need to expand your network assessment to one more area of the network that you have not previously explored - the DMZ, or De-militarized Zone. The term "DMZ" is used to describe a network segment that is separate from the tightly-guarded Private Network or LAN. The DMZ is typically used to house servers that must be exposed to the public Internet - for example, web servers - and therefore require a less restrictive firewall policy than other parts of a network. In this case, the DMZ contains one server - TargetLinux01. Connect to TargetLinux01, then gather the information required to complete the DMZ tab of the NetworkAssessment spreadsheet on the vWorkstation.

So we need to retrieve the IP, Subnet Mask, MAC, and Default Gateway of the TargetLinux01 Machine...

we can do so by running:

```shell
ifconfig -a
```

SS39

SS40

<u>Part 2 - Perform Reconnaissance on the Firewall</u>

Next, you will need to conduct some additional reconnaissance on the firewall itself. From the AttackLinux01 machine, start a tcpdump or Wireshark capture, then run a Regular scan of the pfSense firewall’s external interface. Analyze the capture and consider the following questions.

- Were any ICMP packets sent to the firewall?
- Were any ARP packets sent to the firewall?
- Were any DNS packets sent to the firewall?
- What ports are open on the pfSense firewall?

SS41
SS42
SS43
SS44
SS45

