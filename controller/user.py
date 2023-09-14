from sqlalchemy.orm import Session
from models.sql_models import User


def get_user(session: Session, email: str):
    user = session.query(User).filter_by(email=email).first()
    return user
