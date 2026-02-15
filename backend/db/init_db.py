"""To run this, run the command 'uv run python -m db.init_db'"""
import os
from sqlalchemy import create_engine
from db.base import Base
from dotenv import load_dotenv

# Import your models
from modules.test import models

# ---------------------------
# LOAD ENV FILE
# ---------------------------
load_dotenv()  # loads variables from .env file in project root

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")

# ---------------------------
# BUILD DATABASE URL
# ---------------------------

# Host & port for host machine
DB_HOST = "localhost"
DB_PORT = 5555

# If using another container in Docker Compose, use:
# DB_HOST = "db"
# DB_PORT = 5432

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ---------------------------
# CREATE ENGINE & TABLES
# ---------------------------

engine = create_engine(DATABASE_URL)

print(f"Connecting to database at {DB_HOST}:{DB_PORT}...")
Base.metadata.create_all(engine)
print("Tables created successfully!")