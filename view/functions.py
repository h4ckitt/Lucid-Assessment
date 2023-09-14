from models.database import Session_Local


def get_session():
    session = Session_Local()
    try:
        yield session
    finally:
        session.close()


def hash_password(password: str) -> str:
    return ""
