from datetime import timedelta
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from controller.utils import create_access_token, hash_password, verify_password
from models.user import LoginModel, SignUp
from models.sql_models import User
from cachetools import cached, TTLCache


@cached(cache=TTLCache(maxsize=10, ttl=60 * 5))
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


def login_controller(user: LoginModel, session: Session):
    get_user = session.query(User).filter_by(email=user.email).first()
    if get_user is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "A user with that Email does not exist."},
        )

    if verify_password(user.password, str(get_user.password)):
        token = create_access_token(
            data={"sub": user.email}, expiry=timedelta(minutes=30)
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"access_token": token, "token_type": "Bearer"},
        )

    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"message": "Invalid Email or Password"},
    )
