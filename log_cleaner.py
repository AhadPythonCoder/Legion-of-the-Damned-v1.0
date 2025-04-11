# log_cleaner.py
# Legion of the Damned v1.0 - Log Cleaner Module
# Author: Ahad & ChatGPT

import os
import time

def clean_logs():
    log_files = ['msfconsole.log', 'ngrok.log', 'serveo.log']
    
    for file in log_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"[+] Deleted log file: {file}")
            except Exception as e:
                print(f"[-] Error deleting {file}: {e}")
        else:
            print(f"[-] Log file {file} not found.")
    
    print("[+] Log cleaning complete!")
    time.sleep(2)
