# src/client.py
import requests
import time
import json

BASE = "http://127.0.0.1:8000"

def pretty(resp):
    print("STATUS:", resp.status_code)
    try:
        print(json.dumps(resp.json(), indent=2))
    except:
        print(resp.text)
    print("-" * 60)


def add_user(username, email, role="student"):
    params = {"username": username, "email": email, "role": role}
    r = requests.post(f"{BASE}/users", params=params)
    print("ADD USER:", username)
    pretty(r)
    return r


def list_users():
    r = requests.get(f"{BASE}/users")
    print("LIST USERS")
    pretty(r)
    return r


def update_user(username, new_email):
    params = {"username": username, "new_email": new_email}
    r = requests.put(f"{BASE}/users", params=params)
    print("UPDATE USER:", username)
    pretty(r)
    return r


def delete_user(username):
    params = {"username": username}
    r = requests.delete(f"{BASE}/users", params=params)
    print("DELETE USER:", username)
    pretty(r)
    return r


if __name__ == "__main__":
    print("Waiting for server...")
    time.sleep(1)

    add_user("service_test", "service@test.com", "student")
    list_users()
    update_user("service_test", "updated@test.com")
    list_users()
    delete_user("service_test")
    list_users()

    print("Client run complete.")