from models.anime import Anime
from models.user import User
from models.watchlist import WatchList
from models.base import Base, session, engine

#Base.metadata.drop_all(engine)  # Just in case I change anything or mess up my database

# Current logged-in user
current_user = None

# Anime Functions

def add_anime(title: str, genre: str, episodes: int):  # pass title, genre, episodes and status with default datatypes
    session  # creates a new session
    try:
        anime = Anime(title=title, genre=genre, episodes=episodes)  # creates an instance for an anime
        session.add(anime)  # adds the anime to the session
        session.commit()  # closes the session to allow the next session to begin
        print('\t=========================================')
        print(f"Added anime: {title}")

    except Exception as e:
        session.rollback()  # if any error occurs the session rolls back the changes
        print('-' * 10)
        print(f"Failed to add anime: {e}")
        print('-' * 10)

    finally:
        session.close()

def add_anime_to_watchlist(user_id: int, title: str):
    session
    try:
        anime = session.query(Anime).filter(Anime.title == title).first()  # queries an anime by the title and brings the first result
        if anime:
            watchlist = WatchList(user_id=user_id, anime_id=anime.id, watched_episodes=0)  # creates a new instance of a watchlist
            session.add(watchlist)
            session.commit()
            print('\t=========================================')
            print(f"Anime '{title}' added to your watchlist.")
        else:
            print('-' * 10)
            print(f"Anime '{title}' not found.")
            print('-' * 10)

    finally:
        session.close()

def list_anime():
    session
    try:
        animes = session.query(Anime).all()  # queries the table and brings a list of all animes
        for anime in animes:
            print('\t==================anime=======================')
            print(anime)

    finally:
        session.close()

def view_anime(title: str):
    session
    try:
        anime = session.query(Anime).filter(Anime.title == title).first()  # queries the anime by title
        if anime:
            print('\t=========================================')
            # prints the details of that specific anime
            print(f"Title: {anime.title}")
            print(f"Genre: {anime.genre}")
            print(f"Episodes: {anime.episodes}")
         
        else:
            print('\t=========================================')
            print(f"Anime titled '{title}' not found.")
            print('\t=========================================')

    finally:
        session.close()

def delete_anime(title: str):
    session
    try:
        anime = session.query(Anime).filter(Anime.title == title).first()  # query the anime by the title
        if anime:
            session.delete(anime)
            session.commit()
            print('\t=========================================')
            print(f"Deleted anime: {title}")
            print('\t=========================================')
        else:
            print('-' * 10)
            print(f"Anime titled '{title}' not found.")
            print('-' * 10)

    finally:
        session.close()

def mark_as_watched(user_id: int, title: str, episodes: int, status: str):
    session
    try:
        anime = session.query(Anime).filter(Anime.title == title).first()
        if anime:
            watchlist = session.query(WatchList).filter(WatchList.anime_id == anime.id, WatchList.user_id == user_id).first()
            if watchlist:
                watchlist.watched_episodes = episodes
                watchlist.status = status
                session.commit()
                print('\t=========================================')
                print(f"Updated '{title}': {episodes} episodes watched, Status: {status}")
                print('\t=========================================')
            else:
                print('\t-' * 10)
                print(f"\tAnime '{title}' is not in your watchlist.")
                print('\t-' * 10)
        else:
            print('\t-' * 10)
            print(f"Anime titled '{title}' not found.")
            print('\t-' * 10)

    finally:
        session.close()

def search_anime(title: str):
    session
    try:
        animes = session.query(Anime).filter(Anime.title.ilike(f'%{title}%')).all()
        if animes:
            for anime in animes:
                print(anime)
        else:
            print("No anime found")
    finally:
        session.close()

# User Functions

def add_user(name: str, email: str):
    session
    try:
        if not name.strip() or not email.strip():  # name.strip removes whitespaces
            print("Invalid input: Name and email cannot be empty.")
            return
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print('\t=========================================')
        print(f"Successfully added user: {name}")
        print('\t=========================================')

    except Exception as e:
        session.rollback()
        print('\t-' * 10)
        print(f"Failed to add user: {e}")
        print('\t-' * 10)

    finally:
        session.close()

def login_user(email: str):
    session
    try:
        user = session.query(User).filter(User.email == email).first()
        if user:
            print('\t=========================================')
            print(f"Logged in as {user.name}")
            print('\t=========================================')
            return user
        else:
            print('\t=========================================')
            print(f"No user found with email: {email}")
            print('\t=========================================')
            return None
    finally:
        session.close()

def view_user_watchlist(email: str):
    session
    try:
        user = session.query(User).filter(User.email == email).first()
        
        if user:
            print(f"==== User {user.name} ====")
            watchlist = session.query(WatchList).filter(WatchList.user_id == user.id).all()

            if watchlist:
                print("Title     Watched Episodes   Status")
                print("-" * 40)
                for entry in watchlist:
                    anime = session.query(Anime).filter(Anime.id == entry.anime_id).first()
                    if anime:
                        print(f"{anime.title}   {entry.watched_episodes}    {entry.status}")
            else:
                print('-' * 10)
                print(f"{user.name}, your watchlist is empty.")
                print('-' * 10)

        else:
            print('\t-' * 10)
            print(f"User with email '{email}' not found.")
            print('\t-' * 10)

    finally:
        session.close()

def list_users():
    session
    try:
        users = session.query(User).all()  # Query all users
        if users:
            print("=== User List ===")
            for user in users:
                print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
        else:
            print("No users found.")
    except Exception as e:
        print(f"Error retrieving users: {e}")
    finally:
        session.close()

def delete_user(email: str):
    session
    try:
        user = session.query(User).filter(User.email == email).first()  # Query the user by email
        if user:
            session.delete(user)
            session.commit()
            print(f"Deleted user: {user.name}")
        else:
            print(f"User with email '{email}' not found.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting user: {e}")
    finally:
        session.close()

def main_menu():
    while True:
        print()
        print("\nMain Menu")
        print("1. Add User")
        print("2. Login as User")
        print("3. Add Anime (Requires Login)")
        print("4. List Anime (All)")
        print("5. View Anime")
        print("6. Delete Anime")
        print("7. Mark Anime as Watched (Requires Login)")
        print("8. Search Anime")
        print("9. View Watchlist (Requires Login)")
        print("10. List Users")  
        print("11. Delete User") 
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            add_user(name, email)
        elif choice == "2":
            email = input("Enter your email to log in: ")
            current_user = login_user(email)
        elif choice == "3":
            if current_user:
                title = input("Enter title: ")
                genre = input("Enter genre: ")
                try:
                    episodes = int(input("Enter number of episodes: "))
                except ValueError:
                    print("Invalid input: Episodes must be a number.")
                    continue
                status = input("Enter status: ")
                add_anime(title, genre, episodes, status)
                add_anime_to_watchlist(current_user.id, title)
            else:
                print("You need to log in to add an anime.")
        elif choice == "4":
            list_anime()
        elif choice == "5":
            title = input("Enter title: ")
            view_anime(title)
        elif choice == "6":
            title = input("Enter title: ")
            delete_anime(title)
        elif choice == "7":
            if current_user:
                title = input("Enter title: ")
                try:
                    episodes = int(input("Enter number of episodes watched: "))
                except ValueError:
                    print("Invalid input: Episodes must be a number.")
                    continue
                status = input("Enter new status (e.g., Currently Watching, Completed): ")
                mark_as_watched(current_user.id, title, episodes, status)
            else:
                print("You need to log in to mark an anime as watched.")
        elif choice == "8":
            title = input("Enter title to search: ")
            search_anime(title)
        elif choice == "9":
            if current_user:
                view_user_watchlist(current_user.email)
            else:
                print("You need to log in to view your watchlist.")
        elif choice == "10":
            list_users()  # Call to list users
        elif choice == "11":
            email = input("Enter the email of the user to delete: ")
            delete_user(email)  # Call to delete a user
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main_menu()
