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

## Network Topology

```mermaid
graph TD
    Internet --&gt;|WAN| Router[Edge Router&lt;br&gt;NAT/PAT]
    Router --&gt;|192.168.1.0/30| Core[L3 Core Switch&lt;br&gt;ip routing]

    Core --&gt;|Trunk: all VLANs| AS1[Access Switch 1]
    Core --&gt;|Trunk: all VLANs| AS2[Access Switch 2]

    subgraph VLANs["VLANs (SVIs on Core)"]
        VLAN10[VLAN 10 - Management&lt;br&gt;192.168.10.0/24]
        VLAN20[VLAN 20 - Sales&lt;br&gt;192.168.20.0/24]
        VLAN30[VLAN 30 - Engineering&lt;br&gt;192.168.30.0/24]
        VLAN40[VLAN 40 - Guest&lt;br&gt;192.168.40.0/24]
        VLAN50[VLAN 50 - VoIP&lt;br&gt;192.168.50.0/24]
        VLAN99[VLAN 99 - Native&lt;br&gt;untagged]
    end

    Core -.-&gt;|SVI .10.1| VLAN10
    Core -.-&gt;|SVI .20.1| VLAN20
    Core -.-&gt;|SVI .30.1| VLAN30
    Core -.-&gt;|SVI .40.1| VLAN40
    Core -.-&gt;|SVI .50.1| VLAN50

    AS1 --&gt; VLAN20
    AS1 --&gt; VLAN30
    AS1 --&gt; VLAN50
    AS2 --&gt; VLAN10
    AS2 --&gt; VLAN40
    AS2 --&gt; VLAN50
```

## Network Highlights

| Feature | Implementation |
|---------|---------------|
| VLANs | 6 (Management, Sales, Engineering, Guest, VoIP, Native) |
| Routing | Static routes + SVI inter-VLAN routing |
| Redundancy | Rapid PVST+ |
| Security | Port Security, ACLs, BPDU Guard |
| Automation | Python (Netmiko), scheduled backups |

## IP Addressing

| VLAN | Subnet | Gateway (SVI) | Purpose |
|------|--------|---------------|---------|
| 10 | 192.168.10.0/24 | 192.168.10.1 | Management |
| 20 | 192.168.20.0/24 | 192.168.20.1 | Sales |
| 30 | 192.168.30.0/24 | 192.168.30.1 | Engineering |
| 40 | 192.168.40.0/24 | 192.168.40.1 | Guest |
| 50 | 192.168.50.0/24 | 192.168.50.1 | VoIP |
| 99 | — | — | Native (untagged) |
| Transit | 192.168.1.0/30 | — | Core ↔ Edge Router |

## Repository Structure

```
├── configs/          # Device configurations (Core, AS1, AS2, Router)
├── diagrams/         # Topology diagrams (this README + source files)
├── scripts/          # Python automation (Netmiko backups, monitoring)
└── docs/             # Implementation notes and troubleshooting log
```

## Skills Demonstrated

- Cisco IOS CLI configuration
- IP subnetting and VLSM
- VLAN trunking (802.1Q)
- DHCP relay and exclusion ranges
- Network security hardening
- Python network automation
- Technical documentation

## Tools Used

- Cisco Packet Tracer / GNS3 (lab environment)
- Python 3 + Netmiko
- Git / GitHub

---

*Documentation and configuration by JoseG — feedback and questions welcome *
