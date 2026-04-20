# Traffic Monitoring and Statistics Collector (SDN)

## Objective
To monitor network traffic using POX controller and Mininet.

## Tools Used
- Mininet
- POX Controller
- Python
- OpenFlow

## How to Run

1. Start POX controller:
   ./pox.py misc.traffic_monitor

2. Start Mininet:
   sudo mn --controller=remote --topo single,3

3. Test network:
   pingall

## Output
Displays:
- Packet count
- Byte count for each flow

## Features
- Learning switch
- Flow rule installation
- Traffic monitoring
- Periodic statistics collection

## Author
Harshitha
