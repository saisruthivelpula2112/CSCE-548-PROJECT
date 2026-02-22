from .run_crud import add_user, list_users, update_user_email, delete_user


# Business layer wraps data layer

def create_user(username, email, role):
    # Example business rule
    if not username or not email:
        raise ValueError("Username and email are required")
    return add_user(username, email, role)


def get_all_users():
    return list_users()


def update_user(username, new_email):
    return update_user_email(username, new_email)


def remove_user(username):
    return delete_user(username)
