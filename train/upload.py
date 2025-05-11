from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

load_dotenv()
merged_path = os.getenv("MERGED_MODEL_PATH")
htoken = os.getenv("HUGGINGFACE_TOKEN")

api = HfApi(token=htoken)
api.upload_folder(
    folder_path=merged_path,
    repo_id="jayiuk/llm_4_531",
    repo_type="model",
)