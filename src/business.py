# src/business.py
from typing import List, Dict, Optional
from . import db   # relative import — run service as a package (uvicorn src.service:app)


def get_all_users() -> List[Dict]:
    """Return all users (delegates to db layer)."""
    return db.get_all_users()


def get_user(username: str) -> Optional[Dict]:
    """Return single user by username or None."""
    if not username:
        raise ValueError("username is required")
    return db.get_user_by_username(username)


def create_user(username: str, email: str, role: str = "student") -> Dict:
    """Validate then create a user."""
    if not username:
        raise ValueError("username is required")
    if not email:
        raise ValueError("email is required")
    return db.create_user(username, email, role)


def delete_user_by_username(username: str) -> bool:
    if not username:
        raise ValueError("username is required")
    return db.delete_user(username)


def update_user_email_by_username(username: str, new_email: str) -> bool:
    if not username or not new_email:
        raise ValueError("username and new_email are required")
    return db.update_user_email_by_username(username, new_email)