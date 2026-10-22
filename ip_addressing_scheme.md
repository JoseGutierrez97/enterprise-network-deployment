# IP Addressing Scheme

## VLAN Table

| VLAN ID | Name | Purpose | Subnet | Gateway | DHCP Range |
|---------|------|---------|--------|---------|------------|
| 10 | MGMT | Network management | 192.168.10.0/26 | 192.168.10.1 | 192.168.10.10 - .50 |
| 20 | SALES | Sales department | 192.168.20.0/24 | 192.168.20.1 | 192.168.20.10 - .200 |
| 30 | ENG | Engineering / R&D | 192.168.30.0/23 | 192.168.30.1 | 192.168.30.10 - .250 |
| 40 | GUEST | Guest Wi-Fi | 192.168.40.0/24 | 192.168.40.1 | 192.168.40.10 - .200 |
| 50 | VOIP | VoIP phones | 192.168.50.0/24 | 192.168.50.1 | 192.168.50.10 - .100 |
| 99 | NATIVE | Unused native VLAN | 192.168.99.0/30 | 192.168.99.1 | None |

## WAN / Edge

| Interface | IP Address | Description |
|-----------|------------|-------------|
| Gi0/0/0 | DHCP (ISP) | WAN interface |
| Gi0/0/1 | 192.168.10.2/26 | LAN interface to Core |

## Point-to-Point Links

| Link | Network | Subnet Mask |
|------|---------|-------------|
| Core to Edge | 192.168.10.0/26 | 255.255.255.192 |
| Core SVIs | See VLAN table | - |

## Subnetting Notes

- **VLAN 10 (/26):** 62 usable hosts. Reserved for infrastructure management.
- **VLAN 30 (/23):** 510 usable hosts. Engineering requested room for lab devices.
- **VLAN 40:** Isolated guest network with client isolation at AP level.
- **VLAN 99:** Shut down and unused. Native VLAN moved off default for security.
