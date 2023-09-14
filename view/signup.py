from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from models.user import LoginModel, SignUp
from view.functions import get_session
from controller.user import create_user, get_user


router = APIRouter()


@router.post("/register")
async def signup(user: SignUp, session: Session = Depends(get_session)):
    existing_user = get_user(user.email, session)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email Already Exists")

    create_user(user, session)
    return {"message": "Sign Up successful"}


@router.post("/login")
async def login(user: LoginModel, session: Session = Depends(get_session)):
    # get token from controller, if token is none, return error
    return
