from pydantic import BaseModel, ConfigDict

from models.user import SignUp


class PostModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str
    owner: SignUp
    owner_id: int


class PostIn(BaseModel):
    title: str
    content: str
