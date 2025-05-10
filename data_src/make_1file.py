from makedataset import make_1file
import os
from dotenv import load_dotenv

load_dotenv(override=False)

data_path = os.environ.get("DATA_PATH")
name = 'train_data.json'
print(data_path)

new_data = make_1file(data_path, name)