import sys
from sqlalchemy import Column, Integer, String
from .base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"