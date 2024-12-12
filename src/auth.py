from src.account_provider import AccountProvider
from src.account import Account

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
        if account.password != password:
            return -2, None
        return 0, account

    def register(self, login: str, password: str, email: str, phone: str) -> Account:
        account = Account(self.account_provider.get_next_id(), login, password, '', email, False, phone)
        return account
