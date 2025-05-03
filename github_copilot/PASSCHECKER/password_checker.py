def validate_password(password):
    # Check if the password length is less than 8 or greater than 20 characters
    if len(password) < 8 or len(password) > 20:
        return False
    
    # Check if the password contains at least one numeric digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False