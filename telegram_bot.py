# telegram_bot.py
# Legion of the Damned v1.0 - Telegram Bot Control
# Author: Ahad & ChatGPT

import telebot
import time

# Replace with your bot token
API_TOKEN = '7611090380:AAGNNUqU6itpR_2RxmUTCSMuIFiuYRW5Z80'

bot = telebot.TeleBot(API_TOKEN)

# Start Command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Legion of the Damned! ⚡ Type /help for commands.")

# Help Command
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Available Commands:
    /payload - Generate payload
    /listener - Start listener
    /tunnel - Setup Tunnel
    /exit - Exit the tool
    """
    bot.reply_to(message, help_text)

# Exit Command
@bot.message_handler(commands=['exit'])
def exit_tool(message):
    bot.reply_to(message, "Exiting... Stay dangerous! ☠️")
    print("Exiting...")
    exit()

# Other Commands (Placeholder for future features)
@bot.message_handler(commands=['payload', 'listener', 'tunnel'])
def handle_custom_commands(message):
    bot.reply_to(message, f"Command {message.text} received! (Functionality to be added.)")

# Run the bot
def start_bot():
    print("[+] Telegram Bot started...")
    bot.polling(none_stop=True)
