# This script checks the strength of a password based on length, uppercase, lowercase, digits, and special characters.
import re

def check_password_strength(password):
    """
    Checks the strength of a given password.

    Args:
        password (str): The password to check.

    Returns:
        str: A message indicating the strength of the password.
    """
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    return "Password is strong."

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    result = check_password_strength(user_password)
    print(result)