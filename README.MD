Anime Watchlist Application

Overview
This is a Python-based CLI (Command Line Interface) application that allows users to manage an anime watchlist. The application is built using SQLAlchemy for database management and supports features like adding anime, managing user accounts, tracking watchlists, and marking episodes as watched.


### Features

#### User Management:

Add new users.

Login with an existing user account.

List users

Delete user

#### Anime Management:

Add anime to the database.

List all available anime.

Search for specific anime.

Delete anime from the database.

View detailed information on any specific anime.

#### Watchlist Management:

Add anime to your watchlist after logging in.

Mark episodes as watched.

View your watchlist and progress.

### Prerequisites

Python : Required to run the project.

SQLAlchemy: The ORM used for database interactions.

SQLite (or another SQL database): The database used to store the data.

Alembic: Used for database migrations.


### Setup and Installation

##### 1. clone the repository
- Clone the repository

##### 2. create a virtual environment

###### For Linux/MacOS
python3 -m venv venv
source venv/bin/activate

######  For Windows
python -m venv venv
venv\Scripts\activate

##### 3. Install Required Dependencies

pip install SQLAlchemy

pip install alembic


##### 4. Setup Database

using SQLite, the database file will be created automatically. To set up your database schema and apply any migrations:

1. set up Alembic for migrations :

- alembic init migrations

- (if cloned the repository then no need to set up alembic for migration)

2. Create the initial migration for your database :

- alembic revision --autogenerate -m "Initial migration"

3. Apply the migration to create the necessary tables :

- alembic upgrade head


### Running the Application


To initialize the database and start the application, run:

python initialize.py


This will:

Check for existing database tables.

Create tables if they don’t exist.

Seed the database with initial data.

Next run the main menu :

python3 main.py



# Structure

### Database Initialization:

initialize.py is responsible for:

Check for existing database tables.

Create tables if they don’t exist.

Seed the database with initial data.


### Seeding

seed.py :

The seed_data function populates the database with sample users and anime entries. This makes it easier to test and develop the application. Users and anime are created, and watchlists are populated accordingly.

