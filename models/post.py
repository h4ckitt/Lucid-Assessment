from pydantic import BaseModel

from models.user import SignUp


class Post(BaseModel):
    id: int
    title: str
    content: str
    owner: SignUp
    owner_id: int

    class Config:
        orm_mode = True
