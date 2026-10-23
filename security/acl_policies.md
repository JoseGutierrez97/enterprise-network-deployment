# Access Control List Policies

## Guest Network Isolation (Edge Router)

**Goal:** Guest users may access the internet only. No access to internal corporate resources.

**Implementation:** Extended ACL 110 applied inbound on Gi0/0/1 (LAN interface).

| Rule | Action | Source | Destination | Purpose |
|------|--------|--------|-------------|---------|
| 10 | Deny | 192.168.40.0/24 | 192.168.10.0/26 | Block management |
| 20 | Deny | 192.168.40.0/24 | 192.168.20.0/24 | Block sales |
| 30 | Deny | 192.168.40.0/24 | 192.168.30.0/23 | Block engineering |
| 40 | Deny | 192.168.40.0/24 | 192.168.50.0/24 | Block VoIP |
| 50 | Permit | 192.168.40.0/24 | Any | Allow internet |

## NAT ACL (Standard 100)

Controls which internal networks are permitted to use PAT for internet access.
- Guest VLAN 40 is **intentionally excluded** to force traffic through a captive portal (future phase).

## Verification

```bash
show access-lists
show ip interface gi0/0/1
