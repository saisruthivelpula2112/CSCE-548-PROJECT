# src/run_crud.py
import requests
import time

BASE_URL = "http://127.0.0.1:9000"

def safe_print_response(resp):
    print(f"Status: {resp.status_code}")
    ct = resp.headers.get("content-type", "")
    print(f"Content-Type: {ct}")
    try:
        print("JSON response:")
        print(resp.json())
    except Exception:
        print("Raw response:")
        print(resp.text[:1000])


def get_users():
    print("\n--- Getting users ---")
    try:
        resp = requests.get(f"{BASE_URL}/users", timeout=5)
        safe_print_response(resp)
    except requests.RequestException as e:
        print("Request error:", e)


def create_user(username, email, role="student"):
    print("\n--- Creating user ---")
    payload = {"username": username, "email": email, "role": role}
    try:
        resp = requests.post(f"{BASE_URL}/users", json=payload, timeout=5)
        safe_print_response(resp)
    except requests.RequestException as e:
        print("Request error:", e)


def get_user(username):
    print("\n--- Getting single user ---")
    try:
        resp = requests.get(f"{BASE_URL}/users/{username}", timeout=5)
        safe_print_response(resp)
    except requests.RequestException as e:
        print("Request error:", e)


def update_user_email(username, new_email):
    print("\n--- Updating user email ---")
    try:
        resp = requests.put(f"{BASE_URL}/users", params={"username": username, "new_email": new_email}, timeout=5)
        safe_print_response(resp)
    except requests.RequestException as e:
        print("Request error:", e)


def delete_user(username):
    print("\n--- Deleting user ---")
    try:
        resp = requests.delete(f"{BASE_URL}/users", params={"username": username}, timeout=5)
        safe_print_response(resp)
    except requests.RequestException as e:
        print("Request error:", e)


if __name__ == "__main__":
    # small demo sequence
    get_users()
    username = f"console_user_{int(time.time()) % 100000}"
    create_user(username, f"{username}@uni.edu")
    get_user(username)
    update_user_email(username, f"{username}+updated@uni.edu")
    get_user(username)
    delete_user(username)
    get_users()