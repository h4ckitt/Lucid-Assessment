from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "SomeSecretasrfvbeorijwe"
ALGORITHM = "HS256"


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
