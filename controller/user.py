from sqlalchemy.orm import Session
from controller.utils import hash_password
from models.login import SignUp
from models.sql_models import User


def get_user(email: str, session: Session):
    user = session.query(User).filter_by(email=email).first()
    return user


def create_user(user: SignUp, session: Session):
    user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hash_password(user.password),
    )

    session.add(user)
    session.commit()
    session.refresh(user)
