# tunnel.py
# Legion of the Damned v1.0 - Tunnel Setup (Ngrok/Serveo)
# Author: Ahad & ChatGPT

import os
import time
import subprocess

def start_ngrok(lport):
    print(f"[+] Starting Ngrok on port {lport}...")
    command = f"ngrok tcp {lport}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    print(stderr.decode())

def start_serveo(lport):
    print(f"[+] Starting Serveo on port {lport}...")
    command = f"ssh -R 80:localhost:{lport} serveo.net"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    print(stderr.decode())

def tunnel_setup():
    print("\n--- Tunnel Setup ---")
    print("[1] Ngrok")
    print("[2] Serveo")
    choice = input("Select tunnel option: ")

    lport = input("Enter LPORT (Your Port): ")

    if choice == '1':
        start_ngrok(lport)
    elif choice == '2':
        start_serveo(lport)
    else:
        print("[-] Invalid choice!")

    time.sleep(2)
