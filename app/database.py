# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Create the SQLAlchemy engine using the database URL from settings.
# For SQLite, we pass an extra connect_arg to allow usage in multiple threads.
engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# SessionLocal is a factory for new database sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the base class for all SQLAlchemy models.
Base = declarative_base()

# Dependency to be used in routes to get a DB session.
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db       # Yield the session to the route
    finally:
        db.close()     # Close the session after the request is done
