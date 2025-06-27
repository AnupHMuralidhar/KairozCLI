import os
from config import PROMPT_TEMPLATE_PATH

def load_template(template_path: str = PROMPT_TEMPLATE_PATH) -> str:
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found at {template_path}")
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

def build_threat_prompt(log_text: str) -> str:
    log_text = log_text.strip()
    if not log_text:
        print("⚠️ Empty log text passed to prompt builder.")
        return ""

    try:
        template = load_template()
        if "{{LOG_CONTENT}}" not in template:
            print("⚠️ Placeholder {{LOG_CONTENT}} missing in template.")
            return ""
        return template.replace("{{LOG_CONTENT}}", log_text)
    except FileNotFoundError:
        print("⚠️ Template not found. Using fallback prompt.")
        return (
            "You are a cybersecurity expert.\n"
            "Analyze the following suspicious log entries and provide a concise threat summary with mitigation steps:\n\n"
            f"{log_text}\n\n"
            "End your response with a recommended mitigation strategy."
        )

def build_remediation_prompt(threat_summary: str) -> str:
    threat_summary = threat_summary.strip()
    if not threat_summary:
        return ""

    try:
        template_path = os.path.join(os.path.dirname(PROMPT_TEMPLATE_PATH), "remediation.txt")
        template = load_template(template_path)
        return template.replace("{{THREAT_SUMMARY}}", threat_summary)
    except FileNotFoundError:
        return (
            "You are a cybersecurity assistant.\n"
            f"Based on this threat summary, suggest mitigation steps:\n\n{threat_summary}"
        )

def build_qna_prompt(question: str) -> str:
    question = question.strip()
    if not question:
        return ""

    try:
        template_path = os.path.join(os.path.dirname(PROMPT_TEMPLATE_PATH), "qna.txt")
        template = load_template(template_path)
        return template.replace("{{QUESTION}}", question)
    except FileNotFoundError:
        return f"As a cybersecurity expert, answer the following question:\n\n{question}"
