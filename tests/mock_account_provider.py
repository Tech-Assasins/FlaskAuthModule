from src.account_provider import AccountProvider
from src.account import Account

class MockAccountProvider(AccountProvider):
    def __init__(self):
        self.accounts = [Account(0, 'login', 'password', '', 'email', False, 'phone'),
                         Account(1, 'login2', 'password2', '', 'email2', False, 'phone2')]

    def get_account(self, account_id: str):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def get_account_by_login(self, login: str):
        for account in self.accounts:
            if account.login == login:
                return account
        return None

    def add_account(self, account):
        self.accounts.append(account)
        return account

    def get_next_id(self):
        return len(self.accounts)