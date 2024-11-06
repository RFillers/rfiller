from sqlalchemy.orm import Session
from database.db import SessionLocal


from typing import Generator


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
