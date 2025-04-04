from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional


app = FastAPI()


class BookRequest(BaseModel):

    id: Optional[int] = None
    title: str = Field(min_length = 1)
    author: str = Field(min_length = 1)
    rating: int = Field(gt = 0,lt = 6)
    published_year: int = Field(gt = 0)


class Book:
    
    id: int
    title: str
    author: str
    rating: int
    published_year: int

    def __init__(self,id,author,title,rating,year):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating 
        self.published_year = year


BOOKS = [Book(1,"author1","title1",5,2000),
         Book(2,"author2","title2",4,2001),
         Book(3,"author3","title3",3,2002),
         Book(4,"author4","title4",2,2003),
         Book(5,"author5","title5",1,2003),
         Book(6,"author6","title6",0,2004),
         Book(7,"author7","title7",5,2005),
         Book(8,"author8","title8",4,2005),
         Book(9,"author9","title9",3,2008),
         Book(10,"author10","title10",2,2009),
         Book(11,"author11","title11",1,2010)]




@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/books/")
async def get_books_by_query(year: int):
    for book in BOOKS:
        if book.published_year == year:
            return book
        