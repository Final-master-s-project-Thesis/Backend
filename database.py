from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_database_config
import os

database_config = get_database_config("local")

env = os.getenv("ENV", "local")
database_config = get_database_config(env)

DB_USER = database_config["user"]
DB_PASSWORD = database_config["password"]
DB_HOST = database_config["host"]
DB_PORT = database_config["port"]
DB_NAME = database_config["database"]

if env == "local":
	URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
elif env == "deployed":
	URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
	raise ValueError("ENV debe ser 'local' o 'deployed'")

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()