from pydantic import BaseModel
from typing import Optional


class UserDto(BaseModel):
    id: Optional[int]
    full_name: str

    class Config:
        from_attributes = True


class DocumentDto(BaseModel):
    id: int
    title: str
    content: bytes
    user_id: int

    class Config:
        from_attributes = True
