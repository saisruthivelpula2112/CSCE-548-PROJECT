# src/db.py
import os
from typing import Dict, List, Optional
import psycopg2
from psycopg2.extras import RealDictCursor

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "csce548_project1")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

def get_conn():
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
        user=DB_USER, password=DB_PASS,
    )

# ── USERS ─────────────────────────────────────────────────────────────────────

def get_all_users() -> List[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT user_id AS id, username, email, role FROM users ORDER BY user_id;")
            return cur.fetchall()

def get_user_by_id(user_id: int) -> Optional[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT user_id AS id, username, email, role FROM users WHERE user_id=%s;", (user_id,))
            return cur.fetchone()

def create_user(username: str, email: str, role: str = "student") -> Dict:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO users (username, email, role) VALUES (%s,%s,%s) RETURNING user_id AS id, username, email, role;",
                (username, email, role),
            )
            return cur.fetchone()

def update_user(user_id: int, username: Optional[str], email: Optional[str], role: Optional[str]) -> Optional[Dict]:
    fields, vals = [], []
    if username is not None: fields.append("username=%s"); vals.append(username)
    if email    is not None: fields.append("email=%s");    vals.append(email)
    if role     is not None: fields.append("role=%s");     vals.append(role)
    if not fields:
        return get_user_by_id(user_id)
    vals.append(user_id)
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            sql = f"UPDATE users SET {', '.join(fields)} WHERE user_id=%s RETURNING user_id AS id, username, email, role;"
            cur.execute(sql, tuple(vals))
            return cur.fetchone()

def delete_user(user_id: int) -> bool:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE user_id=%s;", (user_id,))
            return cur.rowcount > 0

# ── PROJECTS ──────────────────────────────────────────────────────────────────

def get_all_projects() -> List[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT project_id, owner_id, title FROM projects ORDER BY project_id;")
            return cur.fetchall()

def get_project_by_id(project_id: int) -> Optional[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT project_id, owner_id, title FROM projects WHERE project_id=%s;", (project_id,))
            return cur.fetchone()

def get_projects_by_owner(owner_id: int) -> List[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT project_id, owner_id, title FROM projects WHERE owner_id=%s ORDER BY project_id;", (owner_id,))
            return cur.fetchall()

def create_project(owner_id: int, title: str) -> Dict:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO projects (owner_id, title) VALUES (%s,%s) RETURNING project_id, owner_id, title;",
                (owner_id, title),
            )
            return cur.fetchone()

def update_project(project_id: int, title: str) -> Optional[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "UPDATE projects SET title=%s WHERE project_id=%s RETURNING project_id, owner_id, title;",
                (title, project_id),
            )
            return cur.fetchone()

def delete_project(project_id: int) -> bool:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM projects WHERE project_id=%s;", (project_id,))
            return cur.rowcount > 0

# ── ITEMS ─────────────────────────────────────────────────────────────────────

def get_all_items() -> List[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT item_id, project_id, name FROM items ORDER BY item_id;")
            return cur.fetchall()

def get_item_by_id(item_id: int) -> Optional[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT item_id, project_id, name FROM items WHERE item_id=%s;", (item_id,))
            return cur.fetchone()

def get_items_by_project(project_id: int) -> List[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT item_id, project_id, name FROM items WHERE project_id=%s ORDER BY item_id;", (project_id,))
            return cur.fetchall()

def create_item(project_id: int, name: str) -> Dict:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO items (project_id, name) VALUES (%s,%s) RETURNING item_id, project_id, name;",
                (project_id, name),
            )
            return cur.fetchone()

def update_item(item_id: int, name: str) -> Optional[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "UPDATE items SET name=%s WHERE item_id=%s RETURNING item_id, project_id, name;",
                (name, item_id),
            )
            return cur.fetchone()

def delete_item(item_id: int) -> bool:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM items WHERE item_id=%s;", (item_id,))
            return cur.rowcount > 0

# ── TAGS ──────────────────────────────────────────────────────────────────────

def get_all_tags() -> List[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT tag_id, tag_name FROM tags ORDER BY tag_id;")
            return cur.fetchall()

def get_tag_by_id(tag_id: int) -> Optional[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT tag_id, tag_name FROM tags WHERE tag_id=%s;", (tag_id,))
            return cur.fetchone()

def create_tag(tag_name: str) -> Dict:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO tags (tag_name) VALUES (%s) RETURNING tag_id, tag_name;",
                (tag_name,),
            )
            return cur.fetchone()

def update_tag(tag_id: int, tag_name: str) -> Optional[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "UPDATE tags SET tag_name=%s WHERE tag_id=%s RETURNING tag_id, tag_name;",
                (tag_name, tag_id),
            )
            return cur.fetchone()

def delete_tag(tag_id: int) -> bool:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM tags WHERE tag_id=%s;", (tag_id,))
            return cur.rowcount > 0

# ── ITEM_TAGS ─────────────────────────────────────────────────────────────────

def get_all_item_tags() -> List[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT it.item_id, it.tag_id, i.name AS item_name, t.tag_name
                FROM item_tags it
                JOIN items i ON it.item_id = i.item_id
                JOIN tags  t ON it.tag_id  = t.tag_id
                ORDER BY it.item_id, it.tag_id;
            """)
            return cur.fetchall()

def get_tags_for_item(item_id: int) -> List[Dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT it.item_id, it.tag_id, t.tag_name
                FROM item_tags it
                JOIN tags t ON it.tag_id = t.tag_id
                WHERE it.item_id=%s ORDER BY it.tag_id;
            """, (item_id,))
            return cur.fetchall()

def add_item_tag(item_id: int, tag_id: int) -> Dict:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO item_tags (item_id, tag_id) VALUES (%s,%s) RETURNING item_id, tag_id;",
                (item_id, tag_id),
            )
            return cur.fetchone()

def remove_item_tag(item_id: int, tag_id: int) -> bool:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM item_tags WHERE item_id=%s AND tag_id=%s;", (item_id, tag_id))
            return cur.rowcount > 0