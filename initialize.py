
from sqlalchemy import inspect # inspects the database engine for existing tables
from models.base import Base,engine,session #for model definitions,connection to the db,handling transactions
from seed import seed_data  # Import your seed_data function


def main():
   
    # Initialize the database
    print("Checking for existing tables...")
    if not inspect(engine).has_table('anime'): #checks if whether the table exists if doent it evaluates to True hence creates the tables
        print("Creating database tables...")
        Base.metadata.create_all(engine)
        print("Database tables created.")
    
    else:
        print("Error occured when creating the tables...")

    # Seed the database
    
    try:
        seed_data(session)  # Call the function to  seed the data with initial data
        print("Database seeded with initial data.")
    except Exception as e:
        session.rollback() #exception handling if any error occurs while seeding  the session rollsback any changes made
        print(f"Error seeding data: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()
