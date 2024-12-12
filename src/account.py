import hashlib
import base64

import bcrypt

from src.utility import generate_salt, hash_password

class Account:
    def __init__(self, account_id: int, login: str, password: str, salt: str, email: str, confirmed: bool, phone: str):
        self.account_id = account_id
        self.login = login
        self.salt = salt.encode()
        self.email = email
        self.confirmed = confirmed
        self.phone = phone
        self.password_hash = password

    def __eq__(self, other):
        return self.account_id == other.account_id

    def compare_password(self, password: str) -> bool:
        hashed_password = hash_password(password.encode(), self.salt)
        return hashed_password == self.password_hash

    def compare_hashed_password(self, hashed_password: str) -> bool:
        return self.password_hash == hashed_password






