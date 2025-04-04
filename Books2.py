from fastapi import FastAPI,Body
import uvicorn

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.rating = rating

BOOKS = [ Book(1,'The Great Gatsby','F. Scott Fitzgerald','The Great Gatsby is a novel by American author F. Scott Fitzgerald. The book was published in 1925 and follows a cast of characters living in the fictional town of West Egg on Long Island. The story primarily concerns the young and mysterious millionaire Jay Gatsby and his quixotic passion and obsession with the beautiful former debutante Daisy Buchanan.',4),
          Book(2,'To Kill a Mockingbird','Harper Lee','To Kill a Mockingbird is a novel by Harper Lee published in 1960. It was immediately successful, winning the Pulitzer Prize, and has become a classic of modern American literature. The plot and characters are loosely based on the author\'s observations of her family, her neighbors and an event that occurred near her hometown of Monroeville, Alabama, in 1936, when she was 10 years old.',5),
          Book(3,'1984','George Orwell','1984 is a dystopian social science fiction novel by English novelist George Orwell. It was published on 8 June 1949 by Secker & Warburg as Orwell\'s ninth and final book completed in his lifetime. Thematically, Nineteen Eighty-Four centres on the consequences of totalitarianism, mass surveillance, and repressive regimentation of persons and behaviours within society.',4),
          Book(4,'The Catcher in the Rye','J. D. Salinger','The Catcher in the Rye is a novel by J. D. Salinger, partially published in serial form in 1946 and as a novel in 1951. It was originally intended for adults, but is often read by adolescents for its themes of angst, alienation, and as a critique on superficiality in society.',3),
          Book(5,'The Lord of the Rings','J. R. R. Tolkien','The Lord of the Rings is an epic high-fantasy novel by English author and scholar J. R. R. Tolkien. Set in Middle-earth, the world at some distant time in the past, the story began as a sequel to Tolkien\'s 1937 children\'s book The Hobbit, but eventually developed into a much larger work.',5),
          Book(6,'The Grapes of Wrath','John Steinbeck','The Grapes of Wrath is an American realist novel written by John Steinbeck and published in 1939. The book won the National Book Award and Pulitzer Prize for Fiction, and it was cited prominently when Steinbeck was awarded the Nobel Prize in 1962.',4),
          Book(7,'Panchtantra','Vishnu Sharma','The Panchatantra is an ancient Indian collection of interrelated animal fables in Sanskrit verse and prose, arranged within a frame story. The surviving work is dated to roughly 200 BCE, based on older oral tradition.',4),
          Book(8,'The Alchemist','Paulo Coelho','The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it became a widely translated international bestseller. An allegorical novel, The Alchemist follows a young Andalusian shepherd in his journey to the pyramids of Egypt, after having a recurring dream of finding a treasure there.',5),
          Book(9,'The Da Vinci Code','Dan Brown','The Da Vinci Code is a 2003 mystery thriller novel by Dan Brown. It is Brown\'s second novel to include the character Robert Langdon: the first was his 2000 novel Angels & Demons. The Da Vinci Code follows "symbologist" Robert Langdon and cryptologist Sophie',4)          
        ]


@app.get("/books")
async def get_books():
    return BOOKS



@app.post("/books/create_book")
async def create_book(book = Body()):
    BOOKS.append(book)