from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
import os

db_user = os.environ.get("DB_USERNAME", "test")
db_pass = os.environ.get("DB_PASSWORD", "test")

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@postgresserver/fz"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
