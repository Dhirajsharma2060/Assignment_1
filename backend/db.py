import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Database URL
#SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:Q5q9MNwchRfL@ep-yellow-bush-a5v1yfum.us-east-2.aws.neon.tech/Task"
SQLALCHEMY_DATABASE_URL = os.getenv("POST_URL")
# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()

def get_db():
    """
    Dependency that provides a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_db_connection():
    """
    Test the database connection.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logging.info("Database connection successful.")
    except OperationalError:
        logging.error("Database connection failed.")