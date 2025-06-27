# modes/monitor.py

import sys
import os
import threading
from threading import Event
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.feature_banner import print_feature_banner
from utils.hf_model import query_huggingface
from utils.log_parser import highlight_suspicious_lines
from utils.prompt_builder import build_threat_prompt
from utils.report_writer import save_combined_markdown_report
from config import LOG_DIR_PATH

file_positions = {}  # Track read positions
trigger_event = Event()


class LogFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".log"):
            filename = os.path.basename(event.src_path)
            new_lines = self.get_new_lines(event.src_path)
            if not new_lines:
                trigger_event.set()
                return

            suspicious = highlight_suspicious_lines(''.join(new_lines)).strip()
            if not suspicious:
                print(f"\n📂 Detected new entries in: {filename}")
                print("⚠️ No new suspicious data found.")
                trigger_event.set()
                return

            print(f"\n📂 Detected new entries in: {filename}")
            print("🔍 Suspicious New Entries\n" + "-" * 40)
            print(suspicious)

            prompt = build_threat_prompt(suspicious)
            if not prompt:
                print("❌ Skipping inference: No prompt generated.")
                trigger_event.set()
                return

            print("\n🧠 Running threat analysis using local Granite model...")
            response = query_huggingface(prompt)

            if not response.strip():
                print("⚠️ AI returned empty response.")
                trigger_event.set()
                return

            save_combined_markdown_report([(filename, response)])
            print(f"\n✅ Combined report saved to: reports/ (latest file)\n")

            trigger_event.set()

    def get_new_lines(self, filepath):
        last_pos = file_positions.get(filepath, 0)
        with open(filepath, "r", encoding="utf-8") as f:
            f.seek(last_pos)
            new_data = f.readlines()
            file_positions[filepath] = f.tell()
        return new_data


def monitor_once():
    print_feature_banner("📡 KAIROZ: REAL-TIME LOG MONITOR", animate=True)

    if not os.path.isdir(LOG_DIR_PATH):
        print(f"❌ Log directory not found: {LOG_DIR_PATH}")
        return

    print(f"📡 Monitoring directory for log changes: {LOG_DIR_PATH}")
    observer = Observer()
    event_handler = LogFileHandler()

    for fname in os.listdir(LOG_DIR_PATH):
        if fname.endswith(".log"):
            path = os.path.join(LOG_DIR_PATH, fname)
            file_positions[path] = os.path.getsize(path)

    observer.schedule(event_handler, LOG_DIR_PATH, recursive=False)
    observer.start()

    # Use a separate thread for waiting to enable Ctrl+C
    wait_thread = threading.Thread(target=trigger_event.wait, kwargs={"timeout": 60})
    wait_thread.start()

    try:
        while wait_thread.is_alive():
            wait_thread.join(timeout=0.5)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring interrupted by user.")
    finally:
        observer.stop()
        observer.join()
        trigger_event.clear()


def monitor_log_directory():
    try:
        while True:
            monitor_once()
            choice = input("🔄 Do you want to continue monitoring? (y/n): ").strip().lower()
            if choice != 'y':
                break
    except KeyboardInterrupt:
        print("\n🛑 Monitoring interrupted by user.")


if __name__ == "__main__":
    monitor_log_directory()
