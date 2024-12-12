import bcrypt

def generate_salt() -> str:
    return bcrypt.gensalt().decode()

def hash_password(password: bytes, salt: str) -> str:
    return bcrypt.hashpw(password, salt).decode()

def hash_password_and_generate_salt(password: bytes) -> (str, str):
    salt = generate_salt()
    return hash_password(password, salt.encode()), salt