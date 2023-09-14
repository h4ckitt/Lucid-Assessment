from pydantic import BaseModel, EmailStr


class LoginModel(BaseModel):
    email: EmailStr
    password: str


class SignUp(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str
