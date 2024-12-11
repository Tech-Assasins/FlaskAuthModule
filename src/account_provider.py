from account import Account

class AccountProvider:
    def get_account(self, account_id: str) -> Account:
        pass

    def get_account_by_login(self, login: str) -> Account:
        pass