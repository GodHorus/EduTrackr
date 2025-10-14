import toml
import os
from pymongo import MongoClient

# Load the secrets.toml file with absolute path
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secrets_path = os.path.join(current_dir, ".streamlit", "secrets.toml")
secrets = toml.load(secrets_path)

# Extract the MongoDB connection string and database name
MONGO_CONNECTION_STRING = secrets["mongo_connection"]["MONGO_CONNECTION_STRING"]
DB_NAME = secrets["mongo_connection"]["DB_NAME"]

def get_db():
    client = MongoClient(MONGO_CONNECTION_STRING)
    return client[DB_NAME]
