# src/models.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    role: str = "student"

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str