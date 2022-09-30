import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.tools import get_env_path

load_dotenv(get_env_path())

engine = create_engine("postgresql+psycopg2://postgres:123@localhost:5432/shop_db")
Base = declarative_base(BaseException)
metadata = Base.metadata
engine.connect()
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)


def get_db() -> Generator:
    while True:
        db = None
        try:
            db = SessionLocal()
            yield db
        finally:
            if db:
                db.close()
