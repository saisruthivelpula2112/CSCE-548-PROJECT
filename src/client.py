# src/client.py
import requests

BASE_URL = "http://127.0.0.1:9000"   # matches how we'll run uvicorn (port 9000 recommended)


def safe_print_response(resp):
    print("URL:", resp.url)
    print("Status:", resp.status_code)
    print("Content-Type:", resp.headers.get("Content-Type"))
    try:
        print("JSON response:")
        print(resp.json())
    except Exception:
        print("Non-JSON response body (raw):")
        print(resp.text)


def create_user():
    print("Creating user...")
    resp = requests.post(f"{BASE_URL}/users", json={
        "username": "console_user",
        "email": "console@test.com",
        "role": "student"
    })
    safe_print_response(resp)


def get_users():
    print("--- Getting users ---")
    resp = requests.get(f"{BASE_URL}/users")
    safe_print_response(resp)


def update_email(username, new_email):
    print("Updating user...")
    resp = requests.put(f"{BASE_URL}/users", params={"username": username, "new_email": new_email})
    safe_print_response(resp)


def delete_user(username):
    print("Deleting user...")
    resp = requests.delete(f"{BASE_URL}/users", params={"username": username})
    safe_print_response(resp)


if __name__ == "__main__":
    # quick smoke calls (ensure server is running)
    get_users()
    create_user()
    get_users()
    update_email("console_user", "newemail@test.com")
    get_users()
    delete_user("console_user")
    get_users()