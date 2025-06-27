# modes/ask.py

import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.feature_banner import print_feature_banner

from utils.prompt_builder import build_qna_prompt
from utils.hf_model import query_huggingface



def ask_question():
    print_feature_banner("❓ KAIROZ: CYBERSECURITY Q&A MODE")
    question = input(Fore.LIGHTWHITE_EX + "❓ Enter your cybersecurity question:\n> ").strip()
    
    if not question:
        print(Fore.YELLOW + "⚠️ Empty input. Please enter a valid question.")
        return
    
    prompt = build_qna_prompt(question)
    if not prompt:
        print(Fore.RED + "❌ Failed to build prompt.")
        return

    print(Fore.CYAN + "\n🧠 Thinking with Granite model...")
    response = query_huggingface(prompt)
    
    print(Fore.GREEN + "\n📘 Answer:\n" + "-" * 50)
    print(Fore.LIGHTWHITE_EX + response.strip() or "No meaningful response generated.")

if __name__ == "__main__":
    ask_question()
