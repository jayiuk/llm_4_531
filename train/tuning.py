from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model
from dataset import process_data
from trl import SFTTrainer
from dotenv import load_dotenv
import os

def format_func(data):
    return f"### 질문:\n{data['input']}\n\n### 답변:\n{data['output']}"

load_dotenv()
tuned_model_path = os.environ.get("TUNED_MODEL_PATH")

model_id = "kakaocorp/kanana-nano-2.1b-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token = tokenizer.eos_token


model = AutoModelForCausalLM.from_pretrained(model_id)

t_model = prepare_model_for_kbit_training(model)

loraconfig = LoraConfig(
    r = 8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout = 0.05,
    bias = 'none',
    task_type="CAUSAL_LM"
)

model_for_tuning = get_peft_model(t_model, loraconfig)

training_args = TrainingArguments(
    output_dir = tuned_model_path,
    per_device_train_batch_size = 2,
    gradient_accumulation_steps=4,
    learning_rate = 2e-4,
    logging_steps = 10,
    num_train_epochs = 10,
    save_strategy = "epoch",
    bf16 = True,
    report_to = "none"
)

dataset = process_data()

trainer = SFTTrainer(
    model = model_for_tuning,
    train_dataset=dataset['train'],
    tokenizer = tokenizer,
    args = training_args,
    packing = True,
    max_seq_length = 1024,
    formatting_func=format_func
)

trainer.train()