from transformers import AutoTokenizer, AutoModelForCausalLM, logging as hf_logging
import torch

hf_logging.set_verbosity_error()

MODEL_ID = "ibm-granite/granite-3.3-2b-instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

print(f"🔧 Model device: {device.upper()} ({torch.cuda.get_device_name(0) if device == 'cuda' else 'CPU'})")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype=dtype).to(device)

def query_huggingface(prompt: str) -> str:
    try:
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Optional: You can return only response part by stripping the prompt
        if decoded.startswith(prompt):
            decoded = decoded[len(prompt):].strip()

        return decoded if decoded else "[❌ No meaningful output from model]"
    except Exception as e:
        return f"[❌ Local Model Error] {str(e)}"
