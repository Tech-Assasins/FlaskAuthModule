import hashlib
import base64
from src.utility import generate_salt, hash_password


class Account:
    def __init__(self, account_id: int, login: str, password: str, salt: str, email: str, confirmed: bool, phone: str):
        self.account_id = account_id
        self.login = login
        self.password = password
        self.salt = salt
        self.email = email
        self.confirmed = confirmed
        self.phone = phone

        if salt is None or salt == '':
            self.salt = generate_salt()

        self.password = hash_password(password, self.salt)

    def __eq__(self, other):
        return self.account_id == other.account_id

    def compare_password(self, password: str) -> bool:
        hashed_password = hash_password(password, self.salt)
        return self.password == hashed_password

    def compare_hashed_password(self, hashed_password: str) -> bool:
        return self.password == hashed_password






