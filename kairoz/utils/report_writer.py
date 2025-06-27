import os
import re
from datetime import datetime

def extract_sections(text: str) -> tuple[str, str]:
    """
    Extracts 'Threat Summary' and 'Recommended Mitigation Strategy' sections from AI output.
    """
    threat_match = re.search(r"Threat Summary:\s*(.*?)(?:\n\n|Recommended Mitigation Strategy:)", text, re.DOTALL)
    mitigation_match = re.search(r"Recommended Mitigation Strategy:\s*(.*)", text, re.DOTALL)

    threat = threat_match.group(1).strip() if threat_match else ""
    mitigation = mitigation_match.group(1).strip() if mitigation_match else ""

    return threat, mitigation

def format_as_bullets(text: str) -> str:
    """
    Converts a block of text into bullet points (split by sentences).
    """
    # Split by sentence end punctuation, then clean and rejoin as bullet points
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    bullets = [f"- {s.strip()}" for s in sentences if s.strip()]
    return "\n".join(bullets)

def save_combined_markdown_report(reports: list[tuple[str, str]], output_dir: str = "reports") -> str:
    """
    Saves a single markdown file combining all threat analysis summaries per file.
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"combined_threat_summary_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)

    combined = ["# 🛡️ Combined Threat Analysis Report\n"]
    combined.append(f"**📅 Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for source_log, content in reports:
        threat, mitigation = extract_sections(content)
        threat_bullets = format_as_bullets(threat)
        mitigation_bullets = format_as_bullets(mitigation)

        combined.append(f"\n---\n\n## 📂 File: `{source_log}`\n")
        combined.append("### 📊 Threat Summary\n\n" + (threat_bullets or "N/A"))
        combined.append("\n\n### 🛠️ Mitigation Strategy\n\n" + (mitigation_bullets or "N/A"))

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(combined))
        print(f"\n✅ Combined report saved to: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Failed to save combined report: {e}")
        return ""



def print_summary(content: str, max_lines: int = 20) -> None:
    """
    Prints a clean, readable summary to terminal with mitigation steps as bullets.
    """
    threat, mitigation = extract_sections(content)
    threat_bullets = format_as_bullets(threat)
    mitigation_bullets = format_as_bullets(mitigation)

    print("\n📊 Threat Summary:\n" + "-" * 50)
    print(threat_bullets or "N/A")

    print("\n🛠️ Recommended Mitigation:\n" + "-" * 50)
    print(mitigation_bullets or "N/A")
