# src/db.py
import os
from typing import List, Optional, Dict
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()  # reads .env in project root (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "csce548_project1")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")


def get_conn():
    """Return a new psycopg2 connection using RealDictCursor for dict rows."""
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        cursor_factory=RealDictCursor,
    )


# ---- CRUD functions expected by business layer ----

def get_all_users() -> List[Dict]:
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id AS user_id, username, email, role FROM users ORDER BY id;")
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    finally:
        cur.close()
        conn.close()


def get_user_by_username(username: str) -> Optional[Dict]:
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id AS user_id, username, email, role FROM users WHERE username = %s;", (username,))
        row = cur.fetchone()
        return dict(row) if row else None
    finally:
        cur.close()
        conn.close()


def create_user(username: str, email: str, role: str = "student") -> Dict:
    """
    Insert a user and return the created row (id, username, email, role).
    """
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, email, role) VALUES (%s, %s, %s) RETURNING id;",
            (username, email, role),
        )
        created_id = cur.fetchone()["id"]
        conn.commit()
        # return the inserted record
        cur.execute("SELECT id AS user_id, username, email, role FROM users WHERE id = %s;", (created_id,))
        row = cur.fetchone()
        return dict(row)
    finally:
        cur.close()
        conn.close()


def update_user_email_by_username(username: str, new_email: str) -> bool:
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE users SET email = %s WHERE username = %s RETURNING id;",
            (new_email, username),
        )
        updated = cur.fetchone()
        conn.commit()
        return bool(updated)
    finally:
        cur.close()
        conn.close()


def delete_user(username: str) -> bool:
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM users WHERE username = %s RETURNING id;", (username,))
        deleted = cur.fetchone()
        conn.commit()
        return bool(deleted)
    finally:
        cur.close()
        conn.close()