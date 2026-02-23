# src/models.py
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    role: str


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    role: str = "student"