from src.account_provider import AccountProvider
from src.account import Account
from src.utility import generate_salt, hash_password_and_generate_salt

class MockAccountProvider(AccountProvider):
    def __init__(self):
        hps = hash_password_and_generate_salt('password'.encode())
        hps2 = hash_password_and_generate_salt('password2'.encode())
        self.accounts = [Account(0, 'login', hps[0], hps[1], 'email', False, 'phone'),
                         Account(1, 'login2', hps2[0], hps2[1], 'email2', False, 'phone2')]

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