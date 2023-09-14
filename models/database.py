from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://root:mysql@localhost:3306/job"

engine = create_engine(DB_URL)

Base = declarative_base()

Session_Local = sessionmaker(bind=engine, expire_on_commit=False)
