# Network Topology

## Logical Topology



[Internet]
|
[Edge Router] --- [Firewall] (future)
|
[Core Switch L3] --(Trunk)-- [Access Switch 1] --- [Sales/Engineering PCs]
|                         [VoIP Phones]
|
+--(Trunk)-- [Access Switch 2] --- [Guest Wi-Fi AP]
|                                [Management Workstation
|
[Server VLAN] - [Domain Controller / DHCP Server]
