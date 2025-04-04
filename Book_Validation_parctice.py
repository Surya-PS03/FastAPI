from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional


app = FastAPI()


class BookRequest(BaseModel):

    id: Optional[int] = None
    title: str = Field(min_length = 1)
    author: str = Field(min_length = 1)
    rating: int = Field(gt = 0,lt = 6)


class Book:
    
    id: int
    title: str
    author: str
    rating: int

    def __init__(self,id,author,title,rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating 


BOOKS = [Book(1,"author1","title1",5),
         Book(2,"author2","title2",4),
         Book(3,"author3","title3",3),
         Book(4,"author4","title4",2),
         Book(5,"author5","title5",1),
         Book(6,"author6","title6",0),
         Book(7,"author7","title7",5),
         Book(8,"author8","title8",4),
         Book(9,"author9","title9",3),
         Book(10,"author10","title10",2)]


@app.get("/books")
async def get_books():
    return BOOKS


@app.post("/books/create_book")
async def create_book(book: BookRequest):

    new_book = Book(**book.model_dump())
    BOOKS.append(new_book)

@app.get("/books/")
async def get_book_by_rating(rating: int):
    books_to_return =[]
    for book in BOOKS:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/books/updated_books")
async def update_book(book: BookRequest):

    for i in range (len(BOOKS)):
        if book.id == BOOKS[i].id:
            BOOKS[i] = Book(**book.model_dump())

