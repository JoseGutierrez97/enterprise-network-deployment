```python
#!/usr/bin/env python3
"""
Network Device Configuration Backup
Uses Netmiko to SSH into devices and save running-configs.
"""

from netmiko import ConnectHandler
from datetime import datetime
import os

DEVICES = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.10.1",
        "username": "admin",
        "password": "changeme",
        "secret": "enablepass",
        "name": "CORE-SW-01"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.10.3",
        "username": "admin",
        "password": "changeme",
        "secret": "enablepass",
        "name": "ACCESS-SW-01"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.10.4",
        "username": "admin",
        "password": "changeme",
        "secret": "enablepass",
        "name": "ACCESS-SW-02"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.10.2",
        "username": "admin",
        "password": "changeme",
        "secret": "enablepass",
        "name": "EDGE-ROUTER-01"
    }
]

BACKUP_DIR = "backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

def backup_device(device):
    try:
        print(f"[+] Connecting to {device['name']} ({device['host']})...")
        conn = ConnectHandler(**device)
        conn.enable()
        output = conn.send_command("show running-config")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{BACKUP_DIR}/{device['name']}_{timestamp}.txt"
        
        with open(filename, "w") as f:
            f.write(output)
        
        print(f"[+] Saved: {filename}")
        conn.disconnect()
    except Exception as e:
        print(f"[-] Failed {device['name']}: {e}")

if __name__ == "__main__":
    for dev in DEVICES:
        backup_device(dev)
