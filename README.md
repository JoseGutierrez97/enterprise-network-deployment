# enterprise-network-deployment
Enterprise network design with VLANs, inter-VLAN routing, ACLs, NAT, port security, and Python automation. Built for a network technician portfolio.


# Enterprise Network Deployment

**Role:** Network Technician / Junior Network Engineer  
**Environment:** Cisco IOS, Layer 2/3 Switches, Edge Router  
**Objective:** Design and implement a secure, segmented network for a 150-user small business with separate departments, guest access, and centralized internet egress.

## Project Overview

This repository documents the complete deployment of a hierarchical campus network including:
- Layer 2 segmentation with VLANs
- Layer 3 inter-VLAN routing
- NAT and PAT for internet access
- Access Control Lists (ACLs) for traffic filtering
- Port security to prevent unauthorized device connections
- Automated configuration backup and connectivity monitoring

## Network Highlights

| Feature | Implementation |
|---------|---------------|
| VLANs | 6 (Management, Sales, Engineering, Guest, VoIP, Native) |
| Routing | Static routes + SVI inter-VLAN routing |
| Redundancy | Rapid PVST+ |
| Security | Port Security, ACLs, BPDU Guard |
| Automation | Python (Netmiko), scheduled backups |

## Skills Demonstrated

- Cisco IOS CLI configuration
- IP subnetting and VLSM
- VLAN trunking (802.1Q)
- DHCP relay and exclusion ranges
- Network security hardening
- Python network automation
- Technical documentation`
