import bcrypt

def generate_salt() -> str:
    return bcrypt.gensalt()

def hash_password(password: str, salt: str) -> str:
    return bcrypt.hashpw(password.encode(), salt)