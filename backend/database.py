# SQLAlchemy is the tool we use to talk to the PostgreSQL database using Python.
from sqlalchemy import create_engine

 #A "session" is like a temporary workspace 
# where we can read or write data to the database safely.
from sqlalchemy.orm import sessionmaker

# This lets us define our database 
# tables as normal Python classes (which is much easier to read).
from sqlalchemy.orm import declarative_base

#Import os to read our secret .env file.
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()