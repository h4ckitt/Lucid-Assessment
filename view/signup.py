from .router import router
from models.login import SignUp
from models.sql_models import User
from models.database import Session_Local
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from view.functions import get_session, hash_password
from controller.user import get_user


@router.post("/signup")
async def signup(user: SignUp, session: Session = Depends(get_session)):
    user = get_user(session, user.email)

    if user:
        raise HTTPException(status_code=400, detail="Email Already Exists")

    hashed_password = hash_password(user.password)

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password,
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": "Sign Up successful"}
