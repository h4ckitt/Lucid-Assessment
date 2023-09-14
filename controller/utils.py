from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt, JWTError


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "SomeSecretasrfvbeorijwe"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expiry: timedelta | None):
    to_encode = data.copy()
    if expiry:
        token_expiry = datetime.utcnow() + expiry
    else:
        token_expiry = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": token_expiry})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def decode_token(token) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None


def get_logged_in_user_email(token: Annotated[str, Depends(oauth2_scheme)]):
    return decode_token(token)
