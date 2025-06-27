# 📘 Kairoz Usage Examples

This document provides real-world usage examples for each major Kairoz mode.

---

## 🔍 Static Threat Analysis (analyze.py)

Analyze a log file to detect suspicious behavior.

**Command:**
```bash
python modes/analyze.py
```

**Sample Output:**
```
📂 Analyzing log file: data/sample.log

🧠 Running analysis using local Granite model...

📊 Threat Summary:
- Unauthorized login attempt from 172.16.254.1
- Successful login by root shortly after
- Multiple failed access attempts from same IP

🛠️ Mitigation Strategy:
- Block IP 172.16.254.1 in firewall
- Rotate root user credentials
- Enable MFA for admin endpoints
```

---

## ⏱️ Real-Time Monitoring (monitor.py)

Continuously monitor a log file and get instant AI insights when suspicious activity is detected.

**Command:**
```bash
python modes/monitor.py
```

**Behavior:**
- Automatically re-parses the log file on changes.
- Triggers AI inference if suspicious logs are found.
- Shows analysis in real-time.

---

## ❓ Ask Mode (ask.py)

Ask any cybersecurity-related question and receive an answer from Granite.

**Command:**
```bash
python modes/ask.py
```

**Sample Prompt:**
```
> What is the difference between IDS and IPS?
```

**AI Response:**
```
IDS monitors and reports threats. IPS actively blocks or prevents them. IDS is passive; IPS is proactive.
```

---

## 🎙️ Voice Interaction (voice.py)

Interact with Kairoz using your microphone.

**Command:**
```bash
python modes/voice.py
```

**Behavior:**
- Listens to your spoken question.
- Confirms transcription.
- Sends it to Granite for inference.
- Optionally reads the response aloud.
- Asks if you want to ask another question.

---

## 🗂️ Example Log Input (sample.log)

```
[2025-06-26 11:34:22] Unauthorized login attempt from IP 172.16.254.1
[2025-06-26 11:35:01] Successful login for user: root
[2025-06-26 11:36:45] Multiple failed access attempts from IP 172.16.254.1
```

---

## 🛠️ Requirements Setup

```bash
pip install -r requirements.txt
```

**Make sure `.env` or `config.py` contains:**
- `MODEL_ID=ibm-granite/granite-3.3-2b-instruct`
- Proper Hugging Face authentication (via CLI or token)

---

## 🧪 Run Tests

```bash
python -m unittest tests/test_logs.py
```

---

## 🔚 That's it!

Use Kairoz as your intelligent CLI companion for cybersecurity.
