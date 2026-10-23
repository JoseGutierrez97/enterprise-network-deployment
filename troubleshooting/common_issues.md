 Common Issues & Resolutions

## 1. Port in Err-Disabled State

**Symptom:** Interface down, `show interface status err-disabled` shows port-security violation.

**Cause:** Unauthorized MAC connected or max MACs exceeded.

**Resolution:**
```bash
interface fa0/1
 shutdown
 no shutdown

Prevention: Verify sticky MACs with show port-security address
