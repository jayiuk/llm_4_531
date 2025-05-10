from datasets import load_dataset
from dotenv import load_dotenv
import os


load_dotenv()
p = os.getenv("DATA_PATH")
d_files = os.path.join(p, 'train_data.json')

def preprocess(data):
    data['output'] = "\n".join(data["output"])
    return data


def process_data():
    dataset = load_dataset("json", data_files = d_files)
    processed_data = dataset.map(preprocess)
    return processed_data