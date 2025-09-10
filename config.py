from dotenv import load_dotenv
import os

load_dotenv()

localhost = {
    "user": os.getenv("LOCAL_DB_USER"),
    "password": os.getenv("LOCAL_DB_PASSWORD"),
    "host": os.getenv("LOCAL_DB_HOST"),
    "port": os.getenv("LOCAL_DB_PORT"),
    "database": os.getenv("LOCAL_DB_NAME"),
}

deployed = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}

def get_database_config(env: str = "local"):
    if env == "local":
        return localhost
    elif env == "deployed":
        return deployed
    else:
        raise ValueError(f"Unknown environment: {env}")