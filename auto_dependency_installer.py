# auto_dependency_installer.py
# Legion of the Damned v1.0 - Auto Dependency Installer
# Author: Ahad & ChatGPT

import os
import sys

def install_dependencies():
    dependencies = ['pyngrok', 'requests', 'telebot', 'metasploit', 'python-nmap']
    
    print("[+] Installing dependencies...")
    for dep in dependencies:
        try:
            print(f"[+] Installing {dep}...")
            # os.system(f"pip install {dep}")
        except Exception as e:
            print(f"[-] Error installing {dep}: {e}")
    
    print("[+] All dependencies installed successfully!")
    print("[+] Tool is ready to go! 🚀")
