from fastapi import FastAPI
from src.business import create_user, get_all_users, update_user, remove_user

app = FastAPI()

@app.get("/users")
def list_users():
    return get_all_users()

@app.post("/users")
def add_user(username: str, email: str, role: str):
    create_user(username, email, role)
    return {"message": "User created"}

@app.put("/users")
def update_email(username: str, new_email: str):
    update_user(username, new_email)
    return {"message": "User updated"}

@app.delete("/users")
def delete(username: str):
    remove_user(username)
    return {"message": "User deleted"}