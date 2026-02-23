# src/service.py
import traceback
from fastapi import FastAPI, HTTPException, status, Query
from typing import List, Optional

from .models import User, CreateUser
from .business import (
    get_all_users,
    get_user,
    create_user,
    delete_user_by_username,
    update_user_email_by_username,
)

app = FastAPI(title="CSCE-548 User Service")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users", response_model=List[User])
def api_get_users():
    try:
        rows = get_all_users()
        # pydantic will coerce/validate as needed
        return rows
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/users/{username}", response_model=User)
def api_get_user(username: str):
    try:
        user = get_user(username)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def api_create_user(payload: CreateUser):
    try:
        user = create_user(username=payload.username, email=payload.email, role=payload.role)
        return user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/users", status_code=status.HTTP_200_OK)
def api_update_email(username: str = Query(..., description="username to update"), new_email: str = Query(..., description="new email")):
    try:
        updated = update_user_email_by_username(username, new_email)
        if not updated:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return {"message": "User updated"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/users", status_code=status.HTTP_200_OK)
def api_delete_user(username: str = Query(..., description="username to delete")):
    try:
        deleted = delete_user_by_username(username)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return {"message": "User deleted"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))