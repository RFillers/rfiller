from sqlalchemy import Column, Integer, LargeBinary, String
from database.db import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    documents = relationship("Document", order_by="Document.id", back_populates="user")


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(LargeBinary)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="documents")
