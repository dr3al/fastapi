from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from models import Book
from schemas.books import CreateBookSchema, UpdateBookSchema

from core.database import get_db

# Класс взаимодействия с таблицей БД. Для других это будет абстракция, набор методов
# в __init__ (инициализация объектов класса) указали зависимость от функции, которая выдает соединение.
class BookRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_all(self, limit, offset) -> List[Book]:
        return self.db.query(Book).limit(limit).offset(offset).all()

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return self.db.query(Book).filter(Book.id == book_id).first()

    def update(self, book_id: int, book: UpdateBookSchema) -> Optional[Book]:
        book_db = self.get_by_id(book_id)
        if not book_db:
            return None

        update_data = book.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(book_db, field, value)

        self.db.commit()
        self.db.refresh(book_db)
        return book_db

    def create(self, book: CreateBookSchema) -> Book:
        book_db = Book(**book.model_dump())
        self.db.add(book_db)
        self.db.commit()
        self.db.refresh(book_db)
        return book_db

    def delete(self, book_id: int) -> bool:
        book = self.get_by_id(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
            return True
        return False