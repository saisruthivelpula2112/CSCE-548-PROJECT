# src/client.py
import requests
from typing import Any, Dict

BASE_URL = "http://127.0.0.1:9000"  # make sure uvicorn is running on this port

def safe_print_response(resp: requests.Response) -> None:
    """Print status, headers, and JSON if possible, otherwise raw text."""
    print(f"URL: {resp.url}")
    print(f"Status: {resp.status_code}")
    # helpful headers
    ct = resp.headers.get("content-type", "")
    print(f"Content-Type: {ct}")
    try:
        data = resp.json()
        print("JSON response:")
        print(data)
    except ValueError:
        print("Non-JSON response body (raw):")
        print(resp.text[:1000])  # limit print length

def create_user(username: str, email: str, role: str = "student") -> None:
    print("\n--- Creating user ---")
    url = f"{BASE_URL}/users"
    payload = {"username": username, "email": email, "role": role}
    try:
        resp = requests.post(url, json=payload, timeout=10)
    except requests.RequestException as e:
        print("Request error:", e)
        return
    safe_print_response(resp)

def get_users() -> None:
    print("\n--- Getting users ---")
    url = f"{BASE_URL}/users"
    try:
        resp = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print("Request error:", e)
        return
    safe_print_response(resp)

def update_email(username: str, new_email: str) -> None:
    print("\n--- Updating email ---")
    # According to your swagger, PUT /users takes query params username & new_email
    url = f"{BASE_URL}/users"
    params = {"username": username, "new_email": new_email}
    try:
        resp = requests.put(url, params=params, timeout=10)
    except requests.RequestException as e:
        print("Request error:", e)
        return
    safe_print_response(resp)

def delete_user(username: str) -> None:
    print("\n--- Deleting user ---")
    # DELETE /users?username=<...>
    url = f"{BASE_URL}/users"
    params = {"username": username}
    try:
        resp = requests.delete(url, params=params, timeout=10)
    except requests.RequestException as e:
        print("Request error:", e)
        return
    safe_print_response(resp)

if __name__ == "__main__":
    # Replace these test values as needed
    test_username = "console_user"
    test_email = "console@test.com"
    updated_email = "console_updated@test.com"

    # 1) create
    create_user(test_username, test_email)

    # 2) list
    get_users()

    # 3) update
    update_email(test_username, updated_email)

    # 4) list again to verify
    get_users()

    # 5) delete
    delete_user(test_username)

    # 6) list again to verify deletion
    get_users()