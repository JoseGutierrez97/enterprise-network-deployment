```markdown
# Essential Diagnostic Commands

## Layer 1
```bash
show interface status
show interface fa0/1 transceiver detail
show logging | include err-disable

##Layer 2
```bash
show vlan brief
show interfaces trunk
show mac address-table
show spanning-tree
show port-security

##Layer 3
show ip interface brief
show ip route
show ip arp
ping 192.168.x.x
traceroute 192.168.x.x

##Security
show access-lists
show ip interface gi0/0/1
show port-security interface fa0/1
show ssh

##Performance
show processes cpu
show processes memory
show interface fa0/1 | include rate

