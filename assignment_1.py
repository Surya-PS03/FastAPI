from fastapi import FastAPI
import uvicorn


BOOKS = [{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
         {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez"},
         {"title": "A Passage to India", "author": "E.M. Forster"},
         {"title": "Invisible", "author": "Paul Auster"},
         {"title":"Julius Caesar","author":"William Shakespeare"},
         {"title":"Hamlet","author":"William Shakespeare"},
         {"title":"Othello","author":"William Shakespeare"},
         {"title":"Macbeth","author":"William Shakespeare"},
         {"title":"The Tempest","author":"William Shakespeare"},
         {"title":"The Merchant of Venice","author":"William Shakespeare"},
         {"title":"Romeo and Juliet","author":"William Shakespeare"},
         {"title":"King Lear","author":"William Shakespeare"},
         {"title":"Twelfth Night","author":"William Shakespeare"},
         {"title":"As You Like It","author":"William Shakespeare"},
         {"title":"A Midsummer Night's Dream","author":"William Shakespeare"},
         {"title":"The Taming of the Shrew","author":"William Shakespeare"},
         {"title":"The Comedy of Errors","author":"William Shakespeare"},
         {"title":"Measure for Measure","author":"William Shakespeare"},
         {"title":"Much Ado About Nothing","author":"William Shakespeare"},
         {"title":"All's Well That Ends Well","author":"William Shakespeare"},
         {"title":"Pericles","author":"William Shakespeare"},
         {"title":"Cymbeline","author":"William Shakespeare"},
         {"title":"The Winter's Tale","author":"William Shakespeare"},
         {"title":"Henry V","author":"William Shakespeare"},
         {"title":"Richard III","author":"William Shakespeare"},
         {"title":"Henry IV","author":"William Shakespeare"},
         {"title":"Henry VIII","author":"William Shakespeare"},
         {"title":"Antony and Cleopatra","author":"William Shakespeare"},
         {"title":"Coriolanus","author":"William Shakespeare"},
         {"title":"Timon of Athens","author":"William Shakespeare"},
         {"title":"Titus Andronicus","author":"William Shakespeare"},
         {"title":"Troilus and Cressida","author":"William Shakespeare"},
         {"title":"The Two Gentlemen of Verona","author":"William Shakespeare"},
         {"title":"Love's Labour's Lost","author":"William Shakespeare"},
         {"title":"The Merry Wives of Windsor","author":"William Shakespeare"},
         {"title":"Henry VI","author":"William Shakespeare"},
         {"title":"The Sonnets","author":"William Shakespeare"}]


app = FastAPI()


@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/books/{author_name}/")
async def get_book_by_author(author_name: str):
    by_author = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            by_author.append(book)
    return by_author