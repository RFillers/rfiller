from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int]
    full_name: str

    class Config:
        orm_mode = True


class Document(BaseModel):
    id: int
    title: str
    content: bytes
    user_id: int

    class Config:
        orm_mode = True
