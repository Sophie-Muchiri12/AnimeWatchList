import sys
from sqlalchemy import Column, Integer, String
from .base import Base

class Anime(Base):
    __tablename__ = 'anime'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    episodes = Column(Integer)
    status = Column(String)

    def __repr__(self):
        return f"<Anime(title='{self.title}', genre='{self.genre}', episodes={self.episodes}, status='{self.status}')>"
