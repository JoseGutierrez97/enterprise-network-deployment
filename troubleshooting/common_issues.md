 Common Issues & Resolutions

## 1. Port in Err-Disabled State

**Symptom:** Interface down, `show interface status err-disabled` shows port-security violation.

**Cause:** Unauthorized MAC connected or max MACs exceeded.

**Resolution:**
```bash
interface fa0/1
 shutdown
 no shutdown
```

Prevention: Verify sticky MACs with show port-security address

## 2. Inter-VLAN Routing Fails
**Symptom:** Devices on VLAN 20 cannot ping VLAN 30.
Checklist:

    [ ] ip routing enabled on core switch?
    [ ] SVI interfaces in up/up state? (Requires at least one active access port in VLAN)
    [ ] Default gateway on end devices pointing to correct SVI IP?
    [ ] VLANs exist in VLAN database?

   ## 3. DHCP Not Working
**Symptom:** Clients get 169.254.x.x APIPA address.
Resolution:

    Verify ip helper-address 192.168.10.10 on SVIs.
    Check DHCP scope on server includes correct subnet.
    Ensure trunk allows VLAN between core and access switch.

   ## 4. Guest Users Accessing Internal Resources
**Symptom:** Guest on 192.168.40.x can ping 192.168.20.x.
Checklist:

    [ ] ACL 110 applied inbound on router LAN interface?
    [ ] Guest VLAN 40 NOT in NAT ACL 100 (forces traffic through router)?
    [ ] No alternate path (e.g., Layer 2 bridging) between guest and internal VLANs?

    
