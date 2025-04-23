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
    priority : int = Field(gt=0,lt = 6)
    status: bool = Field(default=False)

@app.get('/todos/all', status_code=status.HTTP_200_OK)
async def read_all(db : Session = Depends(get_db)):
    return db.query(Todo).all()

@app.get('/todos/get/{todo_id}',status_code  = status.HTTP_200_OK)

async def get_todo(db: Session = Depends(get_db), todo_id: int = Path(gt=0)):

    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()

    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code = 404, detail = "Todo not found")


@app.post('/todos/create/{todo_id}',status_code = status.HTTP_201_CREATED)
async def create_todo(todo_request: TodoRequest, db: Session = Depends(get_db)):
    todo_model = Todo(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()


@app.put("/todos/update/{todo_id}",status_code = status.HTTP_204_NO_CONTENT)
async def update_todos(todo_request:TodoRequest ,db: Session = Depends(get_db)  , todo_id: int = Path(gt=0)):  #all path validation will be at last


    todo_model = db.query(Todo).filter(Todo.id==todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code = 404,detail = "Todo not found...")

    todo_model.title = todo_request.title
    todo_model.priority = todo_request.priority
    todo_model.status = todo_request.status

    db.add(todo_model)
    db.commit()


@app.delete("/todos/delete/{todo_id}",status_code = status.HTTP_204_NO_CONTENT)
async def del_todo(db:Session = Depends(get_db),todo_id :int =Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id==todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404,detail = "Todo not found...")
    
    db.delete(todo_model)
    db.commit()
    