from fastapi import FastAPI,Depends,HTTPException,Path
from sqlalchemy.orm import Session
from models import Base
from database import engine,SessionLocal
from models import Todo
from starlette import status

app = FastAPI()

Base.metadata.create_all(bind = engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/todos')
async def read_all(db : Session = Depends(get_db)):
    return db.query(Todo).all()

@app.get('/todos/{todo_id}',status_code  = status.HTTP_200_OK)

async def get_todo(db: Session = Depends(get_db), todo_id: int = Path(gt=0)):

    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()

    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code = 404, detail = "Todo not found")
