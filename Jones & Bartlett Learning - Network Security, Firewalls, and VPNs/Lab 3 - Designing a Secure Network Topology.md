
# Introduction

Designing a secure network is a fundamental practice of computer networking. Individuals spend many hours perfecting and enhancing the controls that secure different areas of their network. In this lab, you will have the opportunity to practice some of these best practices in a virtual environment. Implementing network security can run the gamut from simple to complex, but regardless of how many controls are applied, it always important to abide by the defense-in-depth principle. Defense-in-depth refers to the concept of using multiple layers of security to ensure there are back-up controls in place should one or more layers be breached. 

Designing a secure network takes practice and knowledge of the basic components of IP-based networking, including routers, switches, firewalls, and normal desktop computers. Before building or altering a production network, it is important to thoroughly plan the network topology. One solution for planning and testing a network topology is the Graphical Network Simulator, or GNS3. As the name implies, GNS3 allows users to create a graphical model of a network topology for testing purposes. The network elements within GNS3 are called appliances. Each appliance consists of two components: a graphical representation of a network device and a virtual machine (VM) that can be loaded to the device. It is important to note that GNS3 is licensed under the GNU public license and is therefore free to download. However, not all of the VMs that are used with the appliances are free, as they may be subject to different license agreements. If you would like to learn more about GNS3, you can visit the GNS3 website (https://www.gns3.com/software).

In this lab, you will use GNS3 to design a simple network topology, capture traffic between devices, and perform packet analysis to validate network connectivity.

1. Identify common network devices and components.  
2. Design a network topology in the GNS3 environment.  
3. Configure routers, firewalls, switches, and workstations according to specification.  
4. Validate network connectivity by performing packet capture and analysis.  
5. Design and configure a network topology using VLANs.

# Section 1

<u>Part 1 - Design a Simple Network Topology</u>

*In this part of the lab, you will be introduced to GNS3, an application used to build, design, and test a simulated network environment. The appliances within the GNS3 environment mimic real-life devices on a network with full virtual machines and containers, and in some cases, bridges connections to machines outside of the GNS3 program. For example, the vWorkstation appliance that you will encounter in GNS3 is a link to the vWorkstation desktop from which you will be accessing GNS3. In the next steps, you will design a network based on the information in the tables below.*

|                   |                |                 |              |
| ----------------- | -------------- | --------------- | ------------ |
| **IP Addressing** |                |                 |              |
| **Device**        | **IP Address** | **Subnet mask** | **Gateway**  |
| vWorkstation      | 172.30.0.2     | 255.255.255.0   | 172.30.0.254 |
| PC2               | 172.30.0.4     | 255.255.255.0   | 172.30.0.254 |
| PC3               | 172.30.1.2     | 255.255.255.0   | 172.30.1.254 |
| PC4               | 172.30.1.4     | 255.255.255.0   | 172.30.1.254 |
|                   | em1 interface  | em2 interface   |              |
| **pfSense**       | 172.30.0.254   | 172.30.1.254    |              |

|   |   |   |
|---|---|---|
|**Network Connectivity**|   |   |
|**Device**|**Port**|**Device connected to port**|
|Switch1|Ethernet0|pfSense Router|
||Ethernet1|vWorkstation|
||Ethernet2|PC2|
|Switch2|Ethernet0|pfSense Router|
||Ethernet1|PC3|
||Ethernet2|PC4|
|**pfSense**|Em0||
||Em1|Switch1|
||Em2|Switch2|
|vWorkstation|Ethernet0|Switch1|
|PC2|Ethernet0|Switch1|
|PC3|Ethernet0|Switch2|
|PC4|Ethernet0|Switch2|

On the vWorkstation desktop, **double-click** the **GNS3 icon** to launch the GNS3 application.  
  
GNS3 will automatically open to the Project dialog box.

SS1

SS2

At the Project dialog box, **type** _**yourname**_**_section1** in the Name field, where _yourname_ is your own last name, then **click OK** to proceed.

From the Devices toolbar on the left, **click** the **Browse End Devices icon**, then **select** the **vWorkstation icon** and **drag** it to the topology canvas.

SS3

SS4

*The vWorkstation appliance represents a bridged link to the virtual machine you are accessing GNS3 from. By including the host VM as a participant in the topology, you are able to directly interact with the items in the topology from your virtual desktop.*

From the End devices pane, **select** the **VPCS icon** and **drag** it to the topology canvas.

SS5

**Repeat step 4 twice** to add two more VPCS icons to the topology canvas.

SS6

In the topology canvas, **right-click** the **PC1 icon** and **select Change hostname** from the context menu to open the Change hostname dialog box.

SS7

In the Change hostname dialog box, **type PC4** in the Hostname field and **click OK** to change the hostname of PC1 to PC4.  
  
Because the vWorkstation is already technically PC1, this device is being renamed to avoid confusion.

In the topology canvas, **re-arrange** the **PC icons** so that they appear in numerical order

SS8

From the Devices toolbar, **click** the **Browse Switches icon**, then **select** the **Ethernet Switch icon** and **drag** it to the topology canvas.

SS9

*This is an unmanaged, built-in switch that is available in a default GNS3 deployment. While it does not support advanced Layer 2 operations or configuration through a command-line interface (CLI), it still allows you to specify the number and types of ports for basic switching and virtual networking operations. For more advanced switching operations, the GNS3 Marketplace provides a wealth of devices for download, both open-source and proprietary. For the purposes of this lab, the Ethernet Switch provides sufficient functionality.*

**Repeat step 9** to add a second switch icon to the topology canvas.

In the topology canvas, **double-click** the **Switch1 icon** to open the Switch1 configuration dialog box.

In the Switch1 configuration dialog box, **select port 7** from the port list, then **click** the **Delete button** to remove this port

SS10

**Repeat step 12 four more times** to remove ports 6 through 3, then **click OK** to save your changes and close the Switch1 configuration dialog box.

SS11

**Repeat steps 11-13** for Switch2.

SS12

From the left pane, **click** the **Browse Security Devices icon**, then **select** the **pfSense Router icon** and **drag** it to the topology canvas.

SS13

*You can display the hardware configuration of each device by hovering the cursor over the device. The ports and addresses should appear for the device in question.*

From the Actions toolbar at the top, **click** the **Play icon** to start all devices in the topology.

When prompted, **click Yes** to confirm that you want to start all devices.

SS14

From the Devices toolbar, **click** the **Add a link icon** to enter linking mode.

In linking mode, your cursor will change to a cross icon. In linking mode, you can create a connection between two appliances by clicking the first appliance and selecting an interface, then clicking the second appliance and selecting an interface.

In the topology canvas, **click** the **pfSense router** and **select em1** from the context menu.

SS15

In the topology canvas, **click Switch1** and **select Ethernet0** from the context menu to create a link between the two appliances.

SS16

**Repeat steps 19-20** to create the following links:  
  
pfSense-Router1 (em2) to Switch2 (Ethernet0)  
Switch1 (Ethernet1) to vWorkstation (eth0)  
Switch1 (Ethernet2) to PC2 (Ethernet0)  
Switch2 (Ethernet1) to PC3 (Ethernet0)  
Switch2 (Ethernet2) to PC4 (Ethernet0)

SS17

*Network design is important. So is having manageable and readable diagrams. A best practice when drawing network diagrams is to think of the topology as a tree. If there is a device that all other devices are connect to, then that device becomes the root of your tree. From there, all devices that are one connection away from the root become the next level in your topology. By repeating this process, you will eventually have an upside-down tree, where the root is at the top of your diagram and the PCs (the leaves) are at the bottom of the diagram.*

**Minimize** the **GNS3 window**.

From the vWorkstation taskbar (the actual vWorkstation, not the GNS3 appliance), **click** the **Command Prompt icon** to open a Command Prompt window.

At the command prompt, **type ipconfig** and **press Enter** to display the IP configuration for the vWorkstation.

SS18

You should see an IP address of 172.30.0.2 with a subnet mask of 255.255.255.0, or otherwise represented as a /24 network mask because the 24 bits are all set to 1’s. The default gateway should be 172.30.0.254.

At the command prompt, **type exit** and **press Enter** to close the Command Prompt window.

In the next steps, you will set up the appropriate IP addresses on the three VPCs. The vWorkstation and PC2 will reside on the same network via a connection to Switch1, and PC3 and PC4 will reside on a different network, accessed through Switch2.

**Restore** the **GNS3 window**.

In the topology canvas, **right-click** the **PC2 icon** and **select Console** from the context menu to open the console for the PC2 appliance.

SS19

At the command prompt, **type ip 172.30.0.4/24 172.30.0.254** and **press Enter** to assign an IP address and default gateway to PC2.

SS20

*The format of the IP command is **ip IP address/subnet mask gateway**. You could have also typed **ip 172.30.0.4 255.255.255.0 172.30.0.254**.*

At the command prompt, **type save** and **press Enter** to save your changes, then **close** the **console window**.

SS21

**Repeat steps 27-29** on **PC3**, using the following IP configuration:

IP Address: **172.30.1.2**  
Subnet mask: **/24** or **255.255.255.0**  
Default gateway: **172.30.1.254**

SS22

**Repeat steps 27-29** on **PC4**, using the following IP configuration:    

IP Address: **172.30.1.4**  
Subnet mask: **/24** or **255.255.255.0**  
Default gateway: **172.30.1.254**

SS23

Now that you have configured the switches and the host devices, you will validate the connections with some basic connectivity tests. While you have yet to configure the router, which means that only same-network communications will be permitted at this time, it is good practice to test each additional connection introduced in a network. This allows you to rule out these basic links as problem sources once you begin to add more complexity to the topology. By incrementally verifying each component of your build, you are able to more quickly localize problems in future troubleshooting efforts, as you can safely assume they are caused by your most recent additions.

In the topology canvas, **right-click** the **PC4 icon** and **select Console** from the context menu to re-open the console for the PC4 appliance.

In the console window, **type ping 172.30.1.2** and **press Enter** to test connectivity between PC4 and PC3.

SS24

**Close** the **PC4 console window**.

**Repeat steps 32-33** using PC2 and attempt to ping the vWorkstation (172.30.0.2).

SS25

**Close** the **PC2 console window**.

In the topology canvas, **right-click** the **pfSense router icon** and **select Console** from the context menu to open the console for the pfSense router appliance.

At the Enter an option prompt, **type 2** and **press Enter** to open the Set interface(s) IP address menu.

SS26

When prompted to select an interface, **type 2** and **press Enter** to select the LAN (em1) interface).

SS27

When prompted to enter an IP address, **type 172.30.0.254** and **press Enter** to assign an IP address to the pfSense LAN interface.

SS28

Recall that this was the IP address you assigned as the Default Gateway for the two PCs connected to Switch1.

When prompted for a subnet mask, **type 24** and **press Enter**.

SS29

When prompted to assign an upstream gateway, **press Enter** to continue with none.

When prompted to assign an IPv6 address, **press Enter** to continue with none.

SS30

When prompted to enable DHCP, **type n** and **press Enter** to continue.

pfSense will take a few seconds to save the changes to the LAN interface.

SS31

When prompted to continue, **press Enter**.

**Repeat steps 40-47** for the OPT1 interface, assigning 172.30.1.254 as the IP address, and 24 as the subnet mask.

SS32

SS33

SS34

**Close** the **pfSense console window**.

*Although all IP addresses are now configured, communication is still not possible between the computer attached to Switch1 and the computers attached to Switch2. This is because the pfSense router needs to be further configured to allow traffic between the two interfaces. The default gateways will allow traffic to flow to the router on an interface, but it will not pass traffic to the other interface. To resolve this, you will use the pfSense web GUI.*

**Minimize** the **GNS3 window**.

From the vWorkstation taskbar, **click** the **Chrome icon** to open a new browser window.

In the browser navigation bar, **type 172.30.0.254** and **press Enter** to navigate to the pfSense web configurator.

SS35

At the pfSense log-in screen, **type** the following credentials and **click Sign In** to open the pfSense web configurator.  
  
Username: **admin**  
Password: **pfsense**

From the pfSense menu bar, **click** the **Interfaces menu** and **select LAN** to open the Interfaces / LAN (em1) page.

SS36

In the Description field, **delete** the **default value** and **type LAN1**

SS37

On a network with only a LAN and WAN interface, this description would be perfectly adequate, but because your network has two LAN interfaces, you will rename them to LAN1 and LAN2.

At the bottom of the page, **click** the **Save button** to save your changes.

SS38

At the top of the page, **click** the **Apply Changes button** to apply your changes to the active firewall configuration.

**Repeat steps 55-58** for the OPT interface, changing the Description to LAN2.

SS39

From the pfSense menu bar, **click** the **Firewall menu** and **select Rules** to open the WAN Rules table

SS40

At the WAN Rules table, **click** the **LAN1 tab** to open the LAN1 Rules table.
*Notice that the LAN1 Rules table contains three default rules, including one that allows IPv4 traffic from LAN1 to any destination.*

SS41

At the LAN1 Rules table, **click** the **LAN2 tab** to open the LAN2 Rules table
*Notice that the LAN2 Rules table is currently empty.*

SS42

At the bottom of the LAN2 Rules table, **click** either of the two green **Add buttons** to add a new rule.

In the Edit Firewall Rule section, **verify** that the Action menu is set to **Pass**, then **select Any** from the Protocol menu to pass any protocol.

SS43

In the Source section, **select LAN2 net** from the Source menu to assign LAN2 net as the Source for this firewall rule

SS44

At the bottom of the page, **click** the **Save button** to return to the LAN2 Rules table.

At the top of the LAN2 Rules table, **click** the **Apply Changes button** to implement your new rule.

*The pfSense firewall-router will now allow any inbound traffic from Interface LAN2 to be passed to LAN1.*

**Minimize** the **pfSense browser window**.

**Restore** the **GNS3 window**.

In the topology canvas, **right-click** the **PC4 icon** and **select Console** from the context menu to open the console for the PC4 appliance.

At the command prompt, **type ping 172.30.0.2** and **press Enter** to ping the vWorkstation.

SS45

*Now that the router interfaces and firewall rules have been configured, the PCs attached to Switch1 are able to communicate with the PCs attached to Switch2, and vice-versa.*

**Close** the **PC4 console**.

<u>Part 2 - Capture Network Traffic to Validate Connectivity</u>

In the topology canvas, **right-click** the **link** between Switch1 and the pfSense router, then **select Start Capture** to begin a Wireshark capture on this link.

SS46

At the Packet capture dialog box, **click OK** to continue using the default settings

Wireshark will launch and display an active empty window.

**Move** the **Wireshark window** to the lower-right corner of the virtual desktop.

In the topology canvas, **right-click** the **PC2 icon** and **select Console** from the context menu to open the console for PC2.

In the console window, **type ping 172.30.0.2** and **press Enter** to ping the vWorkstation, then **review** the **results** in the Wireshark window.

SS47

You should see a broadcast from PC2 looking for the IP address 172.30.0.2

At the command prompt, **type ping 172.30.1.2** and **press Enter** to ping PC3, then **review** the **results** in the Wireshark window.

SS48

You should see an ARP request followed by several ICMP packets. These are the Ping requests from PC2 to PC3.

**Close** the **PC2 console window**.

**Restore** the **pfSense browser window**.

The pfSense browser window should still be open to the LAN2 Rules table. If not, repeat the steps in Part 1 to re-open this page.

From the LAN2 Rules table, **click** the **Edit icon** (the pencil) for the firewall rule you created in Part 1.

SS49

From the Edit screen, **change** the Protocol from **Any** to **TCP**, then **click Save**.

SS50

On the LAN2 Rules table, **click** the **Apply Changes button**.

**Minimize** the **pfSense browser window**.

From the GNS3 topology canvas, **right-click** the **PC3 icon** and **select Console** from the context menu to open the PC3 console.

At the command prompt, **type ping 172.30.1.4** and **press Enter** to ping PC4.
*Wireshark should not capture any packets for this ping because the switch is handling the communication between the two PCs.*

At the command prompt, **type ping 172.30.0.2** and **press Enter** to ping the vWorkstation.

*The ping requests should time out because the pfSense firewall-router does not route all communication to LAN2 using the ICMP protocol. The ping request to the vWorkstation uses the LAN2 interface, which you just re-configured to accept TCP packets only. You should see no new packets captured in Wireshark.*

SS51

**Repeat steps 9-13** and **change** the Protocol in the LAN2 firewall rule back to **Any.**

At the PC3 console command prompt, **type ping 172.30.0.2** and **press Enter** to ping the vWorkstation, then **review** the **results** in the Wireshark window.

SS52

Wireshark should now display new ARP and ICMP packets.

# Section 2

<u>Part 1 - Design a More Complex Network Topology</u>

**Launch** the **GNS3 application** and **create** a new project titled _**yourname**_**_section2**.

**Add** the following devices to the topology canvas

vWorkstation  
PC2 (VPCS)  
PC3 (VPCS)  
PC4 (VPCS)  
Switch1 (OpenvSwitch)  
Switch2 (OpenvSwitch)  
pfSense (pfSense Router)

SS53

**Start** all devices in the topology.

SS54

In the topology canvas, **create** the following links:

vWorkstation (eth0) to Switch1 (eth1)  
Switch1 (eth0) to pfSense (em1)

SS55

You will replace these links using VLAN interfaces later in the lab, but for the time being, a connection between the vWorkstation and pfSense router is required to connect to the pfSense web configurator.

**Open** the **console** for the pfSense router and **select** the **Set Interface(s) IP Address option** from the pfSense options menu.

**Set** the LAN (em1) interface IP address to **172.30.0.200/24.  
**(IPv4 address is 172.30.0.200 and the IPv4 subnet bit count is 24).

SS56

Do not assign an IPv4 upstream gateway address or IPv6 address. Do not enable the DHCP server.  
  
Like the links you created earlier, this is a temporary IP assignment created for the purpose of accessing the pfSense web configurator.

**Close** the **pfSense console** and **open** the **pfSense web GUI** (172.30.0.200) in a new browser window.

**Log in** to the pfSense web GUI using the following credentials:  
  
Username: **admin**  
Password: **pfsense**

SS57

*To segment the LAN interface, you will need to create the VLANs that the subnetworks will run on. In the next steps, you create two VLANs: VLAN1 with an IP address of 172.30.0.254, and VLAN2 with an IP address of 172.30.1.254. Later in the lab, you will connect VLAN1 to Switch1 and VLAN2 to Switch2.

**Navigate** to the **Interfaces / Assignments / VLANs page**.
This page should be empty.

SS58

On the VLANs tab, **click** the **Add button**.

**Configure** the VLAN using the following parameters, then **save** your changes.

Parent interface: **em1 - LAN**  
VLAN tag: **1**  
Description: **Software Development**

SS59

**Configure** a second VLAN using the following parameters, then **save** your changes.

SS60

**Navigate** to the **Interface Assignments page** and **add** the **two VLANs** as new interfaces, then **click Save**.

SS61

From the Interfaces menu, **select** the **OPT2 interface**.

SS62

**Rename** the interface to **VLAN1** and **click** the **Enabled checkbox**, then **save** and **apply** the changes.

SS63

**Repeat steps 15-16** for the OPT3 interface, renaming it as VLAN2.

**Navigate** to the **Firewall / Rules / VLAN1 page**.

**Add** a firewall rule that will allow any traffic from the source VLAN1 net.

SS64

**Repeat steps 18-19** for VLAN2, adding a firewall rule that will allow any traffic from the source VLAN2 net.

**Apply** your changes, then **minimize** the **pfSense browser window**.

In the topology canvas, **delete** the **temporary links** between the vWorkstation and the pfSense router.

SS65

**Open** the **pfSense console** and **select** the **Set Interface(s) IP Address option** from the pfSense options menu.

**Select** the **LAN interface**, then **press Enter** at the **next three prompts** to remove the temporary IP address from this interface and return to the Options menu.

From the pfSense options menu, **select** the **Set Interface(s) IP Address option**, then **select** the **VLAN1 interface**.

SS66

**Set** the VLAN1 (opt2) interface IP address to **172.30.0.254/24**.

Do not assign an IPv4 upstream gateway address or IPv6 address. Do not enable the DHCP server.

**Repeat steps 25-26** for the VLAN2 (opt3) interface and set the IP address to **172.30.1.254/24**.

SS67

From the canvas topology, **open** the **Switch1 console**.

At the command prompt, **execute ovs-vsctl del-port br0 eth1** to remove the eth1 interface from the br0 bridge

At the command prompt, **execute ovs-vsctl add-port br0 eth1 tag=1** to add the eth1 interface back to the bridge with a VLAN tag of 1.

At the command prompt, **execute ovs-vsctl del-port br0 eth2** to remove the eth2 interface from the br0 bridge.

At the command prompt, **execute ovs-vsctl add-port br0 eth2 tag=2** to add the eth2 interface back to the bridge with a VLAN tag of 2.

At the command prompt, **execute ovs-vsctl show** to display the current bridge/port configuration.

SS68

You will see a number of bridges and ports attached to them in the output. However, you are only concerned with the eth1 and eth2 interfaces. Specifically, you are looking to verify that both interfaces exist on the br0 bridge, and have been assigned the appropriate VLAN tags.  
  
In the output you may also notice the additional interfaces attached to br0 on Switch1 (eth0 and eth3), which have not been assigned any VLAN tags. These will serve as your dot1q trunk links, which are capable of transporting all VLAN-tagged traffic by default, enabling you to communicate across your two separate VLANs.

**Repeat steps 29-34** for Switch2.

In the GNS3 window, **link the devices** according to the information in the following Network Connectivity table.

|   |   |   |   |
|---|---|---|---|
|**Network Connectivity**|   |   |   |
|**Device**|**Port**|**VLAN and Type**|**Device connected to port**|
|Switch1|Ethernet0|dot1q trunk|pfSense Router (em1)|
||Ethernet1|VLAN – 1|vWorkstation|
||Ethernet2|VLAN – 2|PC2|
||Ethernet3|dot1q trunk|Switch2 (Ethernet0)|
|Switch2|Ethernet0|dot1q trunk|Switch1  (Ethernet3)|
||Ethernet1|VLAN – 1|PC3|
||Ethernet2|VLAN – 2|PC4|
|pfSense|em0|||
||em1||Switch1|
||em2||DMZ|
|vWorkstation|Ethernet0|VLAN – 1|Switch1|
|PC2|Ethernet0|VLAN – 2|Switch1|
|PC3|Ethernet0|VLAN – 1|Switch2|
|PC4|Ethernet0|VLAN – 2|Switch2|
Using the console, **assign IP addresses and default gateways** to PC2, PC3, and PC4 according to the information in the following IP Addressing table.

|   |   |   |   |
|---|---|---|---|
|**IP Addressing**|   |   |   |
|**Device**|**IP Address**|**Subnet mask**|**Gateway**|
|vWorkstation|172.30.0.2|255.255.255.0|172.30.0.254|
|PC2|172.30.1.2|255.255.255.0|172.30.1.254|
|PC3|172.30.0.4|255.255.255.0|172.30.0.254|
|PC4|172.30.1.4|255.255.255.0|172.30.1.254|
||em1.1 interface|em1.2 interface||
|pfSense|172.30.0.254|172.30.1.254||

<u>Part 2 - Capture Network Traffic to Validate Connectivity</u>

**Start a Wireshark capture** between Switch1 and the pfSense router.

**Perform a ping request** from the vWorkstation to PC3.

**Perform a ping request** from PC2 to PC4.  
  
These devices should be on the same VLAN.

**Perform a ping request** from the vWorkstation to PC2.  
  
These devices should not be on the same VLAN, but should still be able to communicate because of the firewall rules to allow any traffic.

**Perform a ping request** from PC2 to PC3.  
  
These devices are not on the same VLAN, but should still be able to communicate because of the firewall rules that allow any traffic

# Section 3

<u>Part 1 - Enhance the Network Topology with a DMZ</u>

The deployment date for your network is quickly approaching, and you have one final request from your supervisor. As a new network engineer at Repair I.T., a software company that develops computer repair utilities, you have been tasked with designing some proof-of-concept scenarios for the new network implementation that is to be erected during the upcoming maintenance window. You have built out several candidates in the GNS3 network simulator and run them by your supervisors, and your last design seemed to hit the mark: a one-armed router configuration that supports multiple VLANs across two switches, with inter-VLAN traffic conveyed over a single 802.1Q trunk. With this approach, you can segment the human resource employees on their own VLAN, and the development environment on the other. This way, you are able to control traffic between VLANs at the router, only permitting certain hosts access to developmental resources on the second VLAN, while local VLAN traffic will flow unimpeded between the switches.

You are about to begin staging the infrastructure in the network closet when the lead engineer tells you that there’s one more thing to be addressed – they are hoping to migrate their website to an on-premise web server. Your lead thinks the best approach to take is to deploy a DMZ (a de-militarized zone) in order to isolate the web server in its own environment, much like you’ve done with the VLANs. However, this network will be exposed to the public internet, because it will host your externally-facing web site that potential customers use to view your product catalog. Shouldn’t be hard, you figure, especially after all the practice you’ve gotten iterating through these topology candidates. All you’ll need to do is assign an IP address to the remaining interfaces, set some rules on the WAN interface that permit inbound traffic to the DMZ, and you’re off! Time to get to it.

On the GNS3 canvas, assign the OPT1 interface a static IP address of 172.30.2.254/24, and the WAN interface a static IP address of 203.0.113.254 (no upstream gateway is required). Then, assign a firewall rule to the WAN interface that permits any IPv4 traffic to the DMZ network.

<u>Part 2 - Validate DMZ Connectivity</u>

Great, you’ve added the DMZ, and made it functional by adding a rule on the WAN interface that permits access to it. With this model, a customer will be able to reach a host in the DMZ, but not any of the resources on any of the internal VLANs. Time to show your lead this proof-of…. ah, right, you should probably test it in order to prove that it works. You can just toss a couple VPCS onto the GNS3 canvas, one for the WAN network and one for the DMZ, give them appropriate addresses, and then test connectivity by first pinging the DMZ host to confirm the traffic passes through, and then pinging an internal host to confirm traffic is blocked. Deploying these targets shouldn’t take much longer, you figure, GNS3 is built to rapidly construct these kinds of demonstrations. Time to add the pudding!

Add two VPCSs to the GNS3 canvas. Connect one to the WAN interface and another to the OPT1 interface. Power both on, and assign them the following addresses:  
  

- WAN-networked VPCS
    - IP address of 203.0.113.2/24, and the WAN interface as its gateway.  
          
        

- OPT1-networked VPCS
    - IP address of 172.30.2.2/24, and the OPT1 interface as its gatway.  
          
        

Validate your firewall rule and network configuration by performing a ping from the host on the WAN to:  
  

- the host on the DMZ (172.30.2.2)
- the internal PC2 host (172.30.1.2)



