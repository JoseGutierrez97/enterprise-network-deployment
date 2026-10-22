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




## Physical Topology

- **Rack 1:** Edge Router (Cisco ISR), Core Switch (Cisco Catalyst 3650)
- **Rack 2:** Access Switch 1 (Cisco Catalyst 2960) - Floor 1
- **Rack 3:** Access Switch 2 (Cisco Catalyst 2960) - Floor 2 / Guest area

## Interface Connections

| From Device | From Port | To Device | To Port | Type |
|-------------|-----------|-----------|---------|------|
| Edge Router | Gi0/0/0 | ISP Modem | Fa0/0 | WAN |
| Edge Router | Gi0/0/1 | Core Switch | Gi1/0/1 | LAN |
| Core Switch | Gi1/0/2 | Access-SW-1 | Gi0/1 | Trunk |
| Core Switch | Gi1/0/3 | Access-SW-2 | Gi0/1 | Trunk |
| Core Switch | Gi1/0/4 | Server | Gi0/0 | Access (VLAN 10) |
