import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .user import User
from .anime import Anime


class WatchList(Base):
    __tablename__ = 'watchlist'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    anime_id = Column(Integer, ForeignKey('anime.id'))
    watched_episodes = Column(Integer, default=0)
    status = Column(String, default="Not Started")

    user = relationship('User', back_populates='watchlists')
    anime = relationship('Anime', back_populates='watchlists')

    def __repr__(self):
        return f"<WatchList(user_id={self.user_id}, anime_id={self.anime_id}, watched_episodes={self.watched_episodes}, Status={self.status})>"

User.watchlists = relationship('WatchList', back_populates='user')
Anime.watchlists = relationship('WatchList', back_populates='anime')
