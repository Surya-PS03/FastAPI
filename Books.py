from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Julius Caesar", "author": "William Shakespeare",'category':'Tragedy',"country":"England"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald",'category':'Novel',"country":"United States"},
    {"title": "The Odyssey", "author": "Homer",'category':'Epic',"country":"Greece"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger",'category':'Novel',"country":"United States"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee",'category':'Novel',"country":"United States"},
    {"title": "The Grapes of Wrath", "author": "John Steinbeck",'category':'Novel',"country":"United States"},
    {"title": "Godan", "author": "Munshi Premchand",'category':'Novel',"country":"India"},
    {"title": "The Alchemist", "author": "Paulo Coelho",'category':'Novel',"country":"Brazil"},
    {"title": "The Da Vinci Code", "author": "Dan Brown",'category':'Mystery',"country":"United States"},
    {"title": "The Kite Runner", "author": "Khaled Hosseini",'category':'Novel',"country":"Afghanistan"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald",'category':'Novel',"country":"United States"},
    {"title":" The Adventures of Sherlock Holmes", "author": "Arthur Conan Doyle",'category':'Mystery',"country":"United Kingdom"},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde",'category':'Novel',"country":"Ireland"},
    ]


@app.get("/Books/mybook")
async def  mybook():
    return {"title": "Godan", "author": "Munshi Premchand",'category':'Novel'}


@app.get("/Books/")
async def read_books():
    return BOOKS

@app.get("/Books/authors/{author_name}")
async def find_author_books(author_name: str):
    author_books = []

    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            author_books.append(book.get('title'))
    return author_books



@app.get("/Books/by_country/{country}/")
async def get_country(country: str, category: str):
    author_country = []

    for book in BOOKS:
        if (book.get('country').casefold() == country.casefold()) and (book.get('category').casefold() == category.casefold()):
            author_country.append(book.get('author'))
    return author_country

@app.get("/Books/{book_title}")
async def read_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book



#read books by category query parameters version


@app.get("/Books/by_category/")
async def read_books_by_category(category: str):
    books_by_category = []

    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_by_category.append(book.get('title'))
    return books_by_category