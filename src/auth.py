from src.account_provider import AccountProvider
from src.account import Account
from src.utility import generate_salt, hash_password


class Auth:
    def __init__(self, account_provider: AccountProvider):
        self.account_provider = account_provider

    # 0 - success
    # -1 - account not found
    # -2 - wrong password
    def login(self, login: str, password: str) -> (int, Account):
        account = self.account_provider.get_account_by_login(login)
        if account is None:
            return -1, None
        if account.compare_password(password) is False:
            return -2, None
        return 0, account

    def register(self, login: str, password: str, email: str, phone: str) -> Account:
        salt = generate_salt().encode()
        hashed_password = hash_password(password.encode(), salt)
        account = Account(0, login, hashed_password, generate_salt(), email, False, phone)
        account = self.account_provider.add_account(account)
        return account
