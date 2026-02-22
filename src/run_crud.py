# src/run_crud.py
import argparse
from src.db import get_connection

# ---------- CREATE ----------
def add_user(username, email, role):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, email, role) VALUES (%s, %s, %s);",
        (username, email, role)
    )
    conn.commit()
    cur.close()
    conn.close()

# ---------- READ ----------
def list_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    print("Users:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# ---------- UPDATE ----------
def update_user_email(username, new_email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET email = %s WHERE username = %s;",
        (new_email, username)
    )
    conn.commit()
    cur.close()
    conn.close()

# ---------- DELETE ----------
def delete_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM users WHERE username = %s;",
        (username,)
    )
    conn.commit()
    cur.close()
    conn.close()

# ---------- CLI ----------
def main():
    parser = argparse.ArgumentParser(description="CSCE 548 User CRUD CLI")

    group = parser.add_mutually_exclusive_group()

    group.add_argument("--list", action="store_true", help="List all users")

    group.add_argument(
        "--add",
        nargs=3,
        metavar=("USERNAME", "EMAIL", "ROLE"),
        help="Add a user"
    )

    group.add_argument(
        "--update-email",
        nargs=2,
        metavar=("USERNAME", "NEW_EMAIL"),
        help="Update a user's email"
    )

    group.add_argument(
        "--delete",
        metavar="USERNAME",
        help="Delete a user"
    )

    args = parser.parse_args()

    if args.list:
        list_users()

    elif args.add:
        username, email, role = args.add
        add_user(username, email, role)
        print(f"Added user {username}")

    elif args.update_email:
        username, new_email = args.update_email
        update_user_email(username, new_email)
        print(f"Updated email for {username}")

    elif args.delete:
        delete_user(args.delete)
        print(f"Deleted user {args.delete}")

    else:
        list_users()

if __name__ == "__main__":
    main()
