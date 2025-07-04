# 🛡️ Kairoz: AI-Powered Cybersecurity CLI Assistant

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-brightgreen)
![CLI Tool](https://img.shields.io/badge/interface-CLI-informational)

**Category:** AI x Cybersecurity  
**Interface:** Command Line (Text + Voice)  
**Powered by:** IBM Granite (Locally Hosted)

---

## 🚀 Overview

Kairoz is an intelligent, AI-driven command-line cybersecurity assistant designed to help users detect, analyze, and remediate threats using natural language and voice interaction. It works fully offline using locally hosted IBM Granite models — ensuring privacy, speed, and reliability.

From real-time log monitoring to interactive cybersecurity Q&A, Kairoz is a powerful companion for security analysts, system administrators, and students.

---

## 🧩 Key Features

| Feature                   | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 🔍 Static Log Analysis     | Analyze `.log` files for brute-force, malware, and access anomalies         |
| ⏱️ Live System Monitoring   | Monitor system logs in real-time to detect new threats                     |
| 🧠 AI Cybersecurity Q&A     | Ask questions like "What is a buffer overflow?" or "Mitigation for XSS"     |
| 🎙️ Voice Interaction        | Speak your query and hear intelligent answers read back                    |
| 📄 Markdown Threat Reports | Generate structured, shareable threat summaries                            |
| 🛑 Improved Interrupts     | Graceful Ctrl+C handling during real-time monitoring                        |
| ⚙️ CLI Installation         | Install with pip and run `kairoz` command globally                         |

---

## ⚙️ Installation & Setup Instructions

### From Source (Manual Setup)

1. Clone this repository:

```bash
git clone https://github.com/your-username/kairoz.git
cd kairoz
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in root directory:
```bash
USE_LOCAL_MODEL=true
LOCAL_MODEL_NAME=ibm-granite/granite-3.3-2b-instruct
```

4. Log in to Hugging Face for IBM Granite model access:
```bash
huggingface-cli login
```

5. Configure your .env file:
```bash
MODEL_ID=ibm-granite/granite-3.3-2b-instruct
```

## As an Installable CLI Package

### You can install Kairoz as a local package and run it globally as a CLI tool:

1. Navigate to the project root folder (where setup.py is).

2. Install the package using pip:
```bash
pip install .
``` 
✅ Important: Make sure your Python scripts directory
(e.g., C:\Users\<username>\AppData\Roaming\Python\Python311\Scripts)
is added to your system PATH so the kairoz command is recognized globally.

3. Run Kairoz CLI from anywhere:
```bash
kairoz
```

## ▶️ Usage Examples

1. Run the full interactive CLI (main menu):
```bash
kairoz
```

2. Or directly run modes:

- Analyze logs:
```bash
python modes/analyze.py
```

- Monitor logs in real time (Ctrl+C to stop):
```bash
python modes/monitor.py
```

- Ask AI cybersecurity questions:
```bash
python modes/ask.py
```

- Use voice assistant mode:
```bash
python modes/voice.py
```

## 🧪 Running Tests

Run unit tests with:
```bash
python -m unittest tests/test_logs.py
```

## 📦 Sample Output
```bash
📊 Threat Summary
- [2025-06-26] Unauthorized login attempt from 172.16.254.1
- [2025-06-25] Execution of suspicious_payload.exe
- [2025-06-24] Sudo brute-force by user 'temp_worker'

🛠️ Mitigation Strategy
- Block IP 172.16.254.1 at the firewall
- Run full malware scan on host
- Disable or reset 'temp_worker' user account
```

## 🔮 Future Enhancements

- Anomaly detection on running processes
- Integration with Splunk/ELK Stack
- Browser-based visual dashboard
- Auto-remediation via local scripts
- Phishing screenshot analysis using Vision models


## 🧠 Powered By

- IBM Granite 3.3 via Hugging Face (Locally hosted)
- Python 3.11+
- Transformers, PyTorch
- SpeechRecognition + Pyttsx3 (Voice mode)
