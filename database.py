from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_database_config
import os

database_config = get_database_config("deployed")

DB_USER = database_config["user"]
DB_PASSWORD = database_config["password"]
DB_HOST = database_config["host"]
DB_PORT = database_config["port"]
DB_NAME = database_config["database"]

URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()