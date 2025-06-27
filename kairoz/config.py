import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Use local IBM Granite model
USE_LOCAL_MODEL = True

# Local model config
LOCAL_MODEL_NAME = os.getenv("LOCAL_MODEL_NAME", "ibm-granite/granite-3.3-2b-instruct")

# Directory containing multiple log files
LOG_DIR_PATH = "data/"  # <-- Updated from LOG_FILE_PATH

# Prompt template for AI model
PROMPT_TEMPLATE_PATH = "prompts/threat_analysis.txt"
