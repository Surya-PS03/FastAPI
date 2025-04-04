from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from models import Base
from database import engine,SessionLocal
from typing import Annotated
from models import Todo

app = FastAPI()

Base.metadata.create_all(bind = engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def read_all(db : Session = Depends(get_db)):
    return db.query(Todo).all()
