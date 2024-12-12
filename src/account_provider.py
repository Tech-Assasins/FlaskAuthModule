from src.account import Account

class AccountProvider:
    def get_account(self, account_id: str) -> Account:
        pass

    def get_account_by_login(self, login: str) -> Account:
        pass

    def add_account(self, account: Account) -> Account:
        pass

    def update_account(self, account: Account) -> Account:
        pass

    def delete_account(self, account_id: str) -> bool:
        pass

    def get_all_accounts(self) -> [Account]:
        pass

    def get_next_id(self) -> int:
        pass