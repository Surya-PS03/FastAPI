from fastapi import FastAPI,Depends,HTTPException,Path
from sqlalchemy.orm import Session
from models import Base
from database import engine,SessionLocal
from models import Todo
from starlette import status
from pydantic import BaseModel,Field

app = FastAPI()

Base.metadata.create_all(bind = engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TodoRequest(BaseModel):
    title : str = Field(min_length = 1)
    priority : int = Field(lt = 5,gt=0)
    status: bool

@app.get('/todos', status_code=status.HTTP_200_OK)
async def read_all(db : Session = Depends(get_db)):
    return db.query(Todo).all()

@app.get('/todos/{todo_id}',status_code  = status.HTTP_200_OK)

async def get_todo(db: Session = Depends(get_db), todo_id: int = Path(gt=0)):

    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()

    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code = 404, detail = "Todo not found")


@app.post('/todos/create_todos',status_code = status.HTTP_201_CREATED)
async def create_todo(todo_request: TodoRequest, db: Session = Depends(get_db)):
    todo_model = Todo(**todo_request.model_dump())

    db.add(todo_model)

    db.commit()



