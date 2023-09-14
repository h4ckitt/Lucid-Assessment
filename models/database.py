from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite://"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

Session_Local = sessionmaker(bind=engine, expire_on_commit=False)
