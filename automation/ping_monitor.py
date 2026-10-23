#!/usr/bin/env python3
"""
Simple Network Connectivity Monitor
Pings critical infrastructure and logs failures.
"""

import subprocess
import datetime
import time

TARGETS = {
    "CORE-SW-01": "192.168.10.1",
    "EDGE-ROUTER": "192.168.10.2",
    "ACCESS-SW-01": "192.168.10.3",
    "ACCESS-SW-02": "192.168.10.4",
    "DNS-GOOGLE": "8.8.8.8"
}

LOG_FILE = "connectivity_log.txt"

def ping_host(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def main():
    while True:
        timestamp = datetime.datetime.now().isoformat()
        for name, ip in TARGETS.items():
            status = "UP" if ping_host(ip) else "DOWN"
            log_line = f"{timestamp} | {name} ({ip}) | {status}\n"
            
            with open(LOG_FILE, "a") as f:
                f.write(log_line)
            
            print(log_line.strip())
        
        time.sleep(60)

if __name__ == "__main__":
    main()
