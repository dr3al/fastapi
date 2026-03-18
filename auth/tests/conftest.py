from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import pytest
from datetime import datetime


@pytest.fixture
def get_test_user():
    return {
        "username": f"User{datetime.now().strftime('%H%M%S')}",
        "email": f"User{datetime.now().strftime('%H%M%S')}@example.com",
        "password": "1234566436",
    }

@pytest.fixture
def get_test_db():
    engine = create_engine(f"postgresql://postgres:taskpass@localhost:5432/test_database")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()