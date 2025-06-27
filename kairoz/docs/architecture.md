# 🏗️ Kairoz Architecture

Kairoz is an AI-powered command-line cybersecurity assistant that integrates IBM Granite language models (running locally) with multiple functional modules. It is designed for intelligent log analysis, voice-driven threat interaction, and real-time system monitoring.

---

## 🧱 High-Level Architecture

```
+----------------------+
|  CLI Interface       |
| (argparse / voice)   |
+----------+-----------+
           |
           v
+----------+-----------+
|   Modes (modes/)     | <-- analyze.py, monitor.py, ask.py, voice.py
+----------+-----------+
           |
           v
+----------+-----------+
|   Prompt Builder     | <-- prompts/qna.txt, threat_analysis.txt
+----------+-----------+
           |
           v
+----------+-----------+
|  HF Model Wrapper    | <-- IBM Granite (Local) via hf_model.py
+----------+-----------+
           |
           v
+----------+-----------+
| Output Formatter     | <-- Markdown reports / TTS audio
+----------------------+
```

---

## 🧩 Key Components

- `main.py`: CLI entry point.
- `modes/`: User-facing interaction modules.
- `utils/`: Core functionality (model, parsing, prompts, reports).
- `prompts/`: Prompt templates for AI generation.
- `data/`: Log file inputs.
- `reports/`: Markdown output summaries.
- `audio/`: Optional audio feedback files.
- `docs/`: Internal documentation.

---

## 🧠 Model Integration

- **Model Used:** `ibm-granite/granite-3.3-2b-instruct`
- **Deployed:** Locally on NVIDIA RTX 3060 GPU
- **Libraries:** Hugging Face Transformers

---

## 🔁 Flow Summary

1. User invokes a mode (e.g., analyze).
2. Logs are parsed for suspicious patterns.
3. Prompt is generated using templates.
4. Granite AI processes the prompt locally.
5. Response is formatted and saved/shown.
6. Optional: spoken via TTS in `voice.py`.
