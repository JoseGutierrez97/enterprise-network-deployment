# Port Security Implementation

## Objective
Prevent unauthorized devices from connecting to the internal network via physical access ports.

## Configuration Summary

| Parameter | Sales/Eng | Guest | Rationale |
|-----------|-----------|-------|-----------|
| Maximum MACs | 2 | 3 | Phone + PC on sales; APs on guest |
| Violation Mode | Restrict | Shutdown | Guest = higher risk |
| Sticky MAC | Yes | Yes | Learn dynamically, save to config |
| BPDU Guard | Enabled | Enabled | Prevent rogue switches |

## Verification Commands

```bash
show port-security
show port-security interface fa0/1
show port-security address
