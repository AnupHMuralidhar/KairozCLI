import re

def extract_relevant_logs(file_path: str, max_lines: int = 50) -> str:
    """
    Reads a log file and extracts the most relevant lines for analysis.
    Currently, this means grabbing the last `max_lines` of logs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Keep only the last `max_lines`
            relevant_lines = lines[-max_lines:]
            return "".join(relevant_lines)
    except Exception as e:
        return f"⚠️ Error reading log file: {e}"


def highlight_suspicious_lines(log_text: str) -> str:
    """
    Applies basic regex-based filtering to highlight potentially suspicious lines.
    (This helps Watsonx focus on threats.)
    """
    suspicious_patterns = [
        r"failed login", r"unauthorized", r"error", r"exception", r"attack",
        r"denied", r"malware", r"injection", r"breach", r"critical"
    ]

    highlighted = []
    for line in log_text.splitlines():
        for pattern in suspicious_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                line = f"[SUSPICIOUS] {line}"
                break
        highlighted.append(line)
    
    return "\n".join(highlighted)
