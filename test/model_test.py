from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
from dotenv import load_dotenv
import os

load_dotenv()
path = os.getenv("TUNED_MODEL_PATH")

peft_config = PeftConfig.from_pretrained(path)


base_model = AutoModelForCausalLM.from_pretrained(peft_config.base_model_name_or_path)
model = PeftModel.from_pretrained(base_model, path)
tokenizer = AutoTokenizer.from_pretrained(peft_config.base_model_name_or_path)
tokenizer.pad_token = tokenizer.eos_token

prompt = "5/3/1 루틴이 뭐야?"

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

output = model.generate(
    **inputs,
    max_new_tokens = 1024,
    do_sample = True,
    temperature = 0.1,
    top_p = 0.9,
    eos_token_id = tokenizer.eos_token_id
)

print(tokenizer.decode(output[0], skip_special_tokens=True))