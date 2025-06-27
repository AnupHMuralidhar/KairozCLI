# tests/test_logs.py
import os
import sys
import unittest

# Ensure parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.log_parser import extract_relevant_logs, highlight_suspicious_lines

class TestLogParser(unittest.TestCase):
    def test_extract_logs(self):
        sample_path = os.path.join("data", "sample.log")
        output = extract_relevant_logs(sample_path)
        self.assertIn("Unauthorized login attempt", output)

    def test_highlight_suspicious(self):
        log = "[2025-06-26 11:34:22] Unauthorized login attempt from IP 172.16.254.1"
        highlighted = highlight_suspicious_lines(log)
        self.assertIn("[SUSPICIOUS]", highlighted)

if __name__ == '__main__':
    unittest.main()
