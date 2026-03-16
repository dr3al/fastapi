from fastapi import Depends

from schemas import BookSchema, UpdateBookSchema, CreateBookSchema
from repositories.books import BookRepository
from core.exceptions import BookNotFoundException


class BookService:
    def __init__(self, repository: BookRepository = Depends()):
        self.repo = repository

    def add_book(self, new_book: CreateBookSchema):
        self.repo.create(new_book)

        return new_book

    def get_book_by_id(self, id: int):
        book_db = self.repo.get_by_id(id)

        if not book_db:
            raise BookNotFoundException(book_id=id)

        return book_db

    def get_books(self, limit, offset) -> list[BookSchema] | None:
        return self.repo.get_all(limit, offset)

    def update_book(self, id: int, payload: UpdateBookSchema) -> BookSchema | None:
        db_book = self.repo.update(id, payload)
        if not db_book:
            raise BookNotFoundException(book_id=id)

        return db_book

    def delete_book(self, id: int) -> bool:
        result = self.repo.delete(id)
        if not result:
            raise BookNotFoundException(book_id=id)

        return result