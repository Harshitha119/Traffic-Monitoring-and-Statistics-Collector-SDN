# Traffic Monitoring and Statistics Collector (SDN)

## Objective
The objective of this project is to design and implement a Software Defined Networking (SDN) based traffic monitoring system using the POX controller and Mininet. The system collects and displays flow statistics such as packet count and byte count, helping in analyzing network traffic efficiently.



## Tools and Technologies Used
- Mininet – Network emulator for creating virtual network topologies  
- POX Controller – Python-based SDN controller  
- Python – Used to implement controller logic  
- OpenFlow Protocol – Communication between controller and switches  



## System Architecture
The system follows the SDN architecture:
- Control Plane: POX Controller  
- Data Plane: OpenFlow Switch (Mininet)  
- Hosts: Generate network traffic  

The controller manages the network by installing flow rules and collecting statistics from switches.



## How to Run the Project

Step 1: Start POX Controller
cd ~/pox  
./pox.py misc.traffic_monitor  

Step 2: Start Mininet Topology (in a new terminal)
sudo mn --controller=remote --topo single,3  

This creates:
- 1 switch  
- 3 hosts  

Step 3: Test Network Connectivity
pingall  

Expected Result:
- All hosts should communicate successfully  
- 0% packet loss  



## Output
The controller periodically displays flow statistics such as:
- Packet count  
- Byte count  
- Input port  

Example output:
===== FLOW STATS =====  
Flow: in_port=1, Packets=10, Bytes=840  
Flow: in_port=2, Packets=8, Bytes=672  



## Features
- Learning switch implementation  
- Dynamic flow rule installation  
- Real-time traffic monitoring  
- Periodic statistics collection  
- Efficient handling of packet_in events  



## Advantages
- Centralized network control  
- Easy monitoring of traffic  
- Reduced manual configuration  
- Improved network visibility  



## Applications
- Network traffic analysis  
- Intrusion detection systems  
- Performance monitoring  
- SDN-based research  

