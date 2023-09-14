from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy import JSON
from sqlalchemy.orm import Session
from controller.post import create_post_in_db
from controller.user import get_user
from controller.utils import get_logged_in_user_email
from models.post import PostModel

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

    posts = get_users_posts(user, session)
    return {"data": posts}


@post_router.post("/posts")
async def create_post(
    post: PostModel,
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
