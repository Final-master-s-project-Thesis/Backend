from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from models import Club, League

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

