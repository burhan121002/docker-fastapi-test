import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # This now points to the project root
DATA_FOLDER = os.path.join(BASE_DIR, "data")
USERS_FILE = os.path.join(DATA_FOLDER, "users.json")

def check_dataset_exists():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER, exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({"data": []}, f)

def read_usersdata():
    check_dataset_exists()
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    return users

def add_userdata(user: dict):
    users = read_usersdata()
    users["data"].append(user)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

# Initialize the data file if it doesn't exist
check_dataset_exists()
