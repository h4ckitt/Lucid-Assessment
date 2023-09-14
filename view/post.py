from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from controller.post import create_post_in_db, get_users_db_posts
from controller.user import get_user
from controller.utils import get_logged_in_user_email
from models.post import PostIn

from view.functions import get_session


post_router = APIRouter()


@post_router.get("/posts")
async def get_users_posts(
    current_user: Annotated[str | None, Depends(get_logged_in_user_email)],
    session: Session = Depends(get_session),
):
    if current_user is None:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Invalid User"},
        )
    user = get_user(current_user, session)
    if user is None:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "User with Email not found"},
        )
    print(user.id, user.email)
    posts = get_users_db_posts(user, session)
    return posts


@post_router.post("/posts")
async def create_post(
    post: PostIn,
    current_user: Annotated[str | None, Depends(get_logged_in_user_email)],
    session: Session = Depends(get_session),
):
    if current_user is None:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Invalid User"},
        )
    user = get_user(current_user, session)

    if user is None:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "User with Email not found"},
        )

    create_post_in_db(post=post, user=user, session=session)
    return JSONResponse(content={"message": "Created Successfully"})
