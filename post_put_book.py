from fastapi import FastAPI,Body
import uvicorn

app = FastAPI()

BOOKS = []



@app.post("/books/create_book")
async def create_book(book = Body()):
    BOOKS.append(book)
    return book


@app.get("/books")
async def get_books():
    return BOOKS

@app.put("/books/update_book")
async def update_book(book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==book.get("title").casefold():
            BOOKS[i] = book
    return BOOKS


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
            BOOKS.pop(i)
            break
    return BOOKS



BOOKS = [
    {"title":"book one","author":"author one","year":1990},
    {"title":"book two","author":"author two","year":1991},
    {"title":"book three","author":"author three","year":1992},
    {"title":"book four","author":"author four","year":1993},
    {"title":"book five","author":"author five","year":1994},
    {"title":"book six","author":"author six","year":1995},
    {"title":"book seven","author":"author seven","year":1996},
    {"title":"book eight","author":"author eight","year":1997},
    {"title":"book nine","author":"author nine","year":1998},
    {"title":"book ten","author":"author ten","year":1999}]
