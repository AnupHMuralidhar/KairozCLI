# modes/analyze.py

import sys
import os
import time
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.feature_banner import print_feature_banner
from utils.hf_model import query_huggingface
from utils.log_parser import extract_relevant_logs, highlight_suspicious_lines
from utils.prompt_builder import build_threat_prompt
from utils.report_writer import save_combined_markdown_report
from config import LOG_DIR_PATH

def loading_dots(message="Analyzing", duration=1.2):
    print(Fore.YELLOW + f"{message}", end="", flush=True)
    for _ in range(3):
        time.sleep(duration / 3)
        print(".", end="", flush=True)
    print()

def analyze_logs():
    print_feature_banner("🔍 KAIROZ: LOG THREAT ANALYZER", animate=True)
    print(Fore.BLUE + "🔧 Initializing threat analysis...\n")

    if not os.path.isdir(LOG_DIR_PATH):
        print(Fore.RED + f"❌ Log directory not found: {LOG_DIR_PATH}")
        return

    log_files = [f for f in os.listdir(LOG_DIR_PATH) if f.endswith(".log")]
    if not log_files:
        print(Fore.YELLOW + "⚠️ No .log files found in the directory.")
        return

    combined_results = []

    for filename in log_files:
        filepath = os.path.join(LOG_DIR_PATH, filename)
        print(Fore.MAGENTA + f"\n📂 Analyzing log file: {Style.BRIGHT}{filepath}")

        log_text = extract_relevant_logs(filepath).strip()
        if not log_text or log_text.startswith("⚠️ Error"):
            print(Fore.YELLOW + f"⚠️ Skipping {filename}: empty or invalid logs.")
            continue

        highlighted_logs = highlight_suspicious_lines(log_text).strip()
        if not highlighted_logs:
            print(Fore.YELLOW + f"⚠️ Skipping {filename}: no suspicious activity found.")
            continue

        prompt = build_threat_prompt(highlighted_logs)
        if not prompt:
            print(Fore.RED + f"❌ Skipping {filename}: prompt generation failed.")
            continue

        print(Fore.CYAN + "🧠 Running analysis using local Granite model...")
        loading_dots("⏳ Thinking")

        try:
            start = time.time()
            response = query_huggingface(prompt)
            duration = round(time.time() - start, 2)

            if not response.strip() or "N/A" in response:
                print(Fore.YELLOW + f"⚠️ Skipping {filename}: model returned empty or irrelevant response.")
                continue

            print(Fore.GREEN + f"✅ Inference completed for {filename} in {duration} seconds")
            combined_results.append((filename, response))

        except Exception as e:
            print(Fore.RED + f"❌ Error processing {filename}: {e}")

    if combined_results:
        save_combined_markdown_report(combined_results)
    else:
        print(Fore.YELLOW + "⚠️ No threat analyses were successful. No report generated.")

if __name__ == "__main__":
    analyze_logs()
