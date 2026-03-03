# src/business.py
from typing import Dict, Any, List, Optional
from fastapi import HTTPException
from .db import (
    get_all_users as db_get_all_users,
    get_user_by_id as db_get_user_by_id,
    create_user as db_create_user,
    update_user as db_update_user,
    delete_user as db_delete_user,
    get_all_projects as db_get_all_projects,
    get_project_by_id as db_get_project_by_id,
    get_projects_by_owner as db_get_projects_by_owner,
    create_project as db_create_project,
    delete_project as db_delete_project,
    get_all_items as db_get_all_items,
    get_item_by_id as db_get_item_by_id,
    get_items_by_project as db_get_items_by_project,
    create_item as db_create_item,
    delete_item as db_delete_item,
    get_all_tags as db_get_all_tags,
    get_tag_by_id as db_get_tag_by_id,
    create_tag as db_create_tag,
    delete_tag as db_delete_tag,
    get_all_item_tags as db_get_all_item_tags,
    get_tags_for_item as db_get_tags_for_item,
    add_item_tag as db_add_item_tag,
    remove_item_tag as db_remove_item_tag,
)

# ── USERS ─────────────────────────────────────────────────────────────────────

def get_all_users() -> List[Dict]:
    return db_get_all_users()

def get_user(user_id: int) -> Dict:
    user = db_get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

def create_user(username: str, email: str, role: str = "student") -> Dict:
    if not username or not email:
        raise HTTPException(status_code=400, detail="username and email required")
    try:
        return db_create_user(username, email, role)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_user(user_id: int, username: Optional[str] = None,
                email: Optional[str] = None, role: Optional[str] = None) -> Dict:
    if username is None and email is None and role is None:
        raise HTTPException(status_code=400, detail="no fields to update")
    try:
        updated = db_update_user(user_id, username, email, role)
        if not updated:
            raise HTTPException(status_code=404, detail="user not found")
        return updated
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_user(user_id: int) -> None:
    try:
        ok = db_delete_user(user_id)
        if not ok:
            raise HTTPException(status_code=404, detail="user not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── PROJECTS ──────────────────────────────────────────────────────────────────

def get_all_projects() -> List[Dict]:
    return db_get_all_projects()

def get_project(project_id: int) -> Dict:
    proj = db_get_project_by_id(project_id)
    if not proj:
        raise HTTPException(status_code=404, detail="project not found")
    return proj

def get_projects_by_owner(owner_id: int) -> List[Dict]:
    return db_get_projects_by_owner(owner_id)

def create_project(owner_id: int, title: str) -> Dict:
    if not title:
        raise HTTPException(status_code=400, detail="title required")
    try:
        return db_create_project(owner_id, title)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_project(project_id: int) -> None:
    try:
        ok = db_delete_project(project_id)
        if not ok:
            raise HTTPException(status_code=404, detail="project not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── ITEMS ─────────────────────────────────────────────────────────────────────

def get_all_items() -> List[Dict]:
    return db_get_all_items()

def get_item(item_id: int) -> Dict:
    item = db_get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="item not found")
    return item

def get_items_by_project(project_id: int) -> List[Dict]:
    return db_get_items_by_project(project_id)

def create_item(project_id: int, name: str) -> Dict:
    if not name:
        raise HTTPException(status_code=400, detail="name required")
    try:
        return db_create_item(project_id, name)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_item(item_id: int) -> None:
    try:
        ok = db_delete_item(item_id)
        if not ok:
            raise HTTPException(status_code=404, detail="item not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── TAGS ──────────────────────────────────────────────────────────────────────

def get_all_tags() -> List[Dict]:
    return db_get_all_tags()

def get_tag(tag_id: int) -> Dict:
    tag = db_get_tag_by_id(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="tag not found")
    return tag

def create_tag(tag_name: str) -> Dict:
    if not tag_name:
        raise HTTPException(status_code=400, detail="tag_name required")
    try:
        return db_create_tag(tag_name)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_tag(tag_id: int) -> None:
    try:
        ok = db_delete_tag(tag_id)
        if not ok:
            raise HTTPException(status_code=404, detail="tag not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── ITEM_TAGS ─────────────────────────────────────────────────────────────────

def get_all_item_tags() -> List[Dict]:
    return db_get_all_item_tags()

def get_tags_for_item(item_id: int) -> List[Dict]:
    return db_get_tags_for_item(item_id)

def add_item_tag(item_id: int, tag_id: int) -> Dict:
    try:
        return db_add_item_tag(item_id, tag_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def remove_item_tag(item_id: int, tag_id: int) -> None:
    try:
        ok = db_remove_item_tag(item_id, tag_id)
        if not ok:
            raise HTTPException(status_code=404, detail="item_tag not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))