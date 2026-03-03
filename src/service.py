# src/service.py
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, HTTPException, status, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .business import (
    # users
    get_all_users, get_user, create_user, update_user, delete_user,
    # projects
    get_all_projects, get_project, get_projects_by_owner, create_project, delete_project,
    # items
    get_all_items, get_item, get_items_by_project, create_item, delete_item,
    # tags
    get_all_tags, get_tag, create_tag, delete_tag,
    # item_tags
    get_all_item_tags, get_tags_for_item, add_item_tag, remove_item_tag,
)

app = FastAPI(title="CSCE-548 Project API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Pydantic models ───────────────────────────────────────────────────────────

class UserCreate(BaseModel):
    username: str
    email: str
    role: str = "student"

class ProjectCreate(BaseModel):
    owner_id: int
    title: str

class ItemCreate(BaseModel):
    project_id: int
    name: str

class TagCreate(BaseModel):
    tag_name: str

class ItemTagCreate(BaseModel):
    item_id: int
    tag_id: int

# ── USERS ─────────────────────────────────────────────────────────────────────

@app.get("/users", tags=["Users"])
def api_get_users():
    return get_all_users()

@app.get("/users/{user_id}", tags=["Users"])
def api_get_user(user_id: int):
    return get_user(user_id)

@app.post("/users", status_code=201, tags=["Users"])
def api_create_user(payload: UserCreate):
    return create_user(payload.username, payload.email, payload.role)

@app.put("/users/{user_id}", tags=["Users"])
def api_update_user(user_id: int, payload: Dict[str, Any] = Body(...)):
    return update_user(user_id, payload.get("username"), payload.get("email"), payload.get("role"))

@app.delete("/users/{user_id}", status_code=204, tags=["Users"])
def api_delete_user(user_id: int):
    delete_user(user_id)

# ── PROJECTS ──────────────────────────────────────────────────────────────────

@app.get("/projects", tags=["Projects"])
def api_get_projects():
    return get_all_projects()

@app.get("/projects/{project_id}", tags=["Projects"])
def api_get_project(project_id: int):
    return get_project(project_id)

@app.get("/projects/owner/{owner_id}", tags=["Projects"])
def api_get_projects_by_owner(owner_id: int):
    return get_projects_by_owner(owner_id)

@app.post("/projects", status_code=201, tags=["Projects"])
def api_create_project(payload: ProjectCreate):
    return create_project(payload.owner_id, payload.title)

@app.delete("/projects/{project_id}", status_code=204, tags=["Projects"])
def api_delete_project(project_id: int):
    delete_project(project_id)

# ── ITEMS ─────────────────────────────────────────────────────────────────────

@app.get("/items", tags=["Items"])
def api_get_items():
    return get_all_items()

@app.get("/items/{item_id}", tags=["Items"])
def api_get_item(item_id: int):
    return get_item(item_id)

@app.get("/items/project/{project_id}", tags=["Items"])
def api_get_items_by_project(project_id: int):
    return get_items_by_project(project_id)

@app.post("/items", status_code=201, tags=["Items"])
def api_create_item(payload: ItemCreate):
    return create_item(payload.project_id, payload.name)

@app.delete("/items/{item_id}", status_code=204, tags=["Items"])
def api_delete_item(item_id: int):
    delete_item(item_id)

# ── TAGS ──────────────────────────────────────────────────────────────────────

@app.get("/tags", tags=["Tags"])
def api_get_tags():
    return get_all_tags()

@app.get("/tags/{tag_id}", tags=["Tags"])
def api_get_tag(tag_id: int):
    return get_tag(tag_id)

@app.post("/tags", status_code=201, tags=["Tags"])
def api_create_tag(payload: TagCreate):
    return create_tag(payload.tag_name)

@app.delete("/tags/{tag_id}", status_code=204, tags=["Tags"])
def api_delete_tag(tag_id: int):
    delete_tag(tag_id)

# ── ITEM_TAGS ─────────────────────────────────────────────────────────────────

@app.get("/item_tags", tags=["ItemTags"])
def api_get_item_tags():
    return get_all_item_tags()

@app.get("/item_tags/{item_id}", tags=["ItemTags"])
def api_get_tags_for_item(item_id: int):
    return get_tags_for_item(item_id)

@app.post("/item_tags", status_code=201, tags=["ItemTags"])
def api_add_item_tag(payload: ItemTagCreate):
    return add_item_tag(payload.item_id, payload.tag_id)

@app.delete("/item_tags/{item_id}/{tag_id}", status_code=204, tags=["ItemTags"])
def api_remove_item_tag(item_id: int, tag_id: int):
    remove_item_tag(item_id, tag_id)