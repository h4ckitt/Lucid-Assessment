from sqlalchemy import Column, Integer, String
from models.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)
