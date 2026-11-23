"""User helpers. Contains intentional bugs for debugger testing."""


def get_user_email(user: dict | None) -> str:
    """Return a user's email.

    BUG: This function does not handle user=None.
    """
    return user["email"]


def find_user(users: list[dict], user_id: int) -> dict | None:
    """Find a user by ID.

    BUG: Compares the name field with user_id instead of comparing IDs.
    """
    for user in users:
        if user.get("name") == user_id:
            return user
    return None
