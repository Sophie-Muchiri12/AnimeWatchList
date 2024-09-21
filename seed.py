# seed.py

from models.anime import Anime
from models.user import User
from models.watchlist import WatchList
from models.base import session

def seed_data(session):
    """Seed initial data for the database."""
    try:
        # Create  users
        user1 = User(name="nick", email="nick@gmail.com")
        user2 = User(name="finn", email="finn@gmail.com")

        # Add users to the session
        session.add_all([user1, user2])
        session.commit()  # Commit to generate IDs for users

        # Create  animes
        anime1 = Anime(title="Attack on Titan", genre="Action", episodes=25, status="Completed")
        anime2 = Anime(title="My Hero Academia", genre="Action", episodes=88, status="Currently Watching")

        # Add animes to the session
        session.add_all([anime1, anime2])
        session.commit()  # Commit to generate IDs for anime

        # Create watchlists for users
        watchlist1 = WatchList(user_id=user1.id, anime_id=anime1.id, watched_episodes=25, status="Completed")
        watchlist2 = WatchList(user_id=user1.id, anime_id=anime2.id, watched_episodes=20, status="Currently Watching")
        watchlist3 = WatchList(user_id=user2.id, anime_id=anime2.id, watched_episodes=10, status="Currently Watching")

        # Add watchlists to the session
        session.add_all([watchlist1, watchlist2, watchlist3])
        session.commit()

    except Exception as e:
        print(f"Error seeding data: {e}")
        session.rollback()
