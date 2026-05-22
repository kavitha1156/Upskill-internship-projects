import json
import os

DATA_PATH = "data/passwords.json"

def load_data():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_PATH):
        return {}

    if os.stat(DATA_PATH).st_size == 0:
        return {}

    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)