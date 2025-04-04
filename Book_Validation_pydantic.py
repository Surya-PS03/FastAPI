from fastapi import FastAPI,Query,Path,HTTPException
from pydantic import BaseModel,Field
from typing import Optional
import starlette.status as status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self,id,author,title,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description 
        self.rating = rating
    

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id not needed during creation",default = None)
    title: str = Field(min_length = 1,max_length = 25)
    author: str = Field(min_length = 1,max_length = 25)
    description: str = Field(min_length = 1,max_length = 150)
    rating: int = Field(min_value = 0,max_value = 6)

    model_config = {
        "json_schema_extra":
                    {"examaple":
                     {
                         "title":"Book Title",
                            "author":"Author Name",
                            "description":"Book Description",
                            "rating":5  
                        }
                    }
    }

BOOKS = [Book(1,"author1","title1","description1",5),
         Book(2,"author2","title2","description2",4),
         Book(3,"author3","title3","description3",3),
         Book(4,"author4","title4","description4",2),
         Book(5,"author5","title5","description5",1),
         Book(6,"author6","title6","description6",0),
         Book(7,"author7","title7","description7",5),
         Book(8,"author8","title8","description8",4),
         Book(9,"author9","title9","description9",3),
         Book(10,"author10","title10","description10",2)]







def increment_id(book: BookRequest):
    book.id  = book.id = 0 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.delete("/books/remove_book/{book_id}", status_code = status.HTTP_204_NO_CONTENT)
async def remove_book(book_id: int = Path(gt = 0)):
    book_found = False
    for book in BOOKS:
        if book.id == book_id:
            book_found = True
            BOOKS.remove(book)
            return {"message":"Book removed"}
    if  not book_found:
        raise HTTPException(status_code = 404,detail = "Book not found")

@app.post("/books/create_book", status_code = status.HTTP_201_CREATED)
async def create_book(book: BookRequest):
    book = increment_id(book)
    new_book = Book(**book.model_dump())
    print(type(new_book))
    BOOKS.append(new_book)

@app.put("/books/updated_books", status_code = status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):

    for i in range (len(BOOKS)):
        if book.id == BOOKS[i].id:
            BOOKS[i] = Book(**book.model_dump())
    raise HTTPException(status_code = 404,detail = "Book not Found")

@app.get("/books/{book_id}", status_code = status.HTTP_200_OK)
async def get_book(book_id: int = Path(gt = 0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code = 404,detail = "Book not Found")

@app.get("/books/", status_code = status.HTTP_200_OK)  #this works because of query parameters if i had been a path parameter it would have been clashing with the above get_book
async def get_book_by_rating(rating: int = Query(gt = 0,lt = 6)):
    books_to_return =[]
    for book in BOOKS:
        if book.rating == rating:
            books_to_return.append(book)
    if not books_to_return:
        raise HTTPException(status_code = 404,detail = "Book not Found")
    return books_to_return

@app.get("/books", status_code = status.HTTP_200_OK)
async def get_books():
    if not BOOKS:
        raise HTTPException(status_code = 404,detail = "No Books Found")
    return BOOKS


      


