# main.py

import os
import sys
import time

from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Import mode functions
from modes.analyze import analyze_logs
from modes.monitor import monitor_log_directory
from modes.ask import ask_question
from modes.voice import main as voice_main
from utils.banner import print_banner


def print_intro():
    print_banner("🔐 WELCOME TO KAIROZ CLI", animate=True)
    print(Fore.CYAN + Style.BRIGHT + "KAIROZ is your AI-powered cybersecurity assistant.")
    print("It helps you detect, analyze, and respond to threats in real time.\n")
    print(Fore.YELLOW + "Available Modes:\n")
    print(Fore.GREEN + "1️⃣  🔍 Analyze Logs      " + Fore.WHITE + "- Detect threats from .log files")
    print(Fore.GREEN + "2️⃣  📡 Monitor Logs      " + Fore.WHITE + "- Real-time log watcher with AI analysis")
    print(Fore.GREEN + "3️⃣  ❓ Ask Expert        " + Fore.WHITE + "- Cybersecurity Q&A powered by Granite AI")
    print(Fore.GREEN + "4️⃣  🎤 Voice Assistant   " + Fore.WHITE + "- Ask questions using your voice")
    print(Fore.RED + "0️⃣  Exit\n")


def main():
    while True:
        print_intro()
        choice = input(Fore.CYAN + Style.BRIGHT + "Select a mode to begin (0–4):\n> ").strip()

        if choice == '1':
            analyze_logs()
        elif choice == '2':
            monitor_log_directory()
        elif choice == '3':
            ask_question()
        elif choice == '4':
            voice_main()
        elif choice == '0':
            print(Fore.RED + "\n👋 Exiting KAIROZ. Stay secure!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please select 1, 2, 3, 4 or 0.")

        input(Fore.YELLOW + "\n🔁 Press Enter to return to the main menu...")


if __name__ == "__main__":
    main()
