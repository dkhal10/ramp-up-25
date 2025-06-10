from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
class Book(BaseModel):
    title: str
    author: str
    year: int
    id: int

books = {}
@app.post("/books/")
def create(book: Book):
    id = book.id
    title = book.title
    author = book.author
    year = book.year
    books[id] = book
    return {"message": f"added {id} {book}"}
@app.get("/books/")
def get():
    return books
@app.get("/books/{id}")
def get(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        return books[id]
@app.put("/books/{id}")
def put(id: int, book: Book):
    books[id] = book
    return {"message": f"updated {id} {book}"}
@app.delete("/books/{id}")
def delete(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        del books[id]
        return {"message": f"deleted {id}"}