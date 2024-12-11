import hashlib
import base64
from utility import generate_salt

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

    def __eq__(self, other):
        return self.account_id == other.account_id

    def compare_password(self, password: str) -> bool:
        t_sha = hashlib.sha512()
        t_sha.update(password + self.salt)
        hashed_password = base64.urlsafe_b64encode(t_sha.digest())
        return self.password == hashed_password





