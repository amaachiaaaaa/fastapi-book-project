from fastapi import APIRouter,status, HTTPException

from api.routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])

@router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: int):
    book = db.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
