from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from dotenv import load_dotenv
import os

load_dotenv()
tuned_path = os.getenv("TUNED_MODEL_PATH")
merged_path = os.getenv("MERGED_MODEL_PATH")
model_id = "kakaocorp/kanana-nano-2.1b-base"
base_model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
tuned = PeftModel.from_pretrained(base_model, tuned_path)

merged_model = tuned.merge_and_unload()
merged_model.config.use_cache = False

merged_model.save_pretrained(merged_path, safe_serialization=False)
tokenizer.save_pretrained(merged_path)