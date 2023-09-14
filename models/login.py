from pydantic import BaseModel, EmailStr


class LoginModel(BaseModel):
    email: EmailStr
    password: str


class SignUp(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
