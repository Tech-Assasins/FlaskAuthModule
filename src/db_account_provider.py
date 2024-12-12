from src.account_provider import AccountProvider
from src.account import Account


class DbAccountProvider(AccountProvider):
    def __init__(self, connection):
        self.connection = connection

    def get_account(self, account_id: str) -> Account:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_id = ?", account_id)
        acc = cursor.fetchone()
        if acc is None:
            return None
        return Account(acc[0], acc[1], acc[2], acc[3], acc[4], acc[5], acc[6])

    def get_account_by_login(self, login: str) -> Account:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE login = ?", login)
        acc = cursor.fetchone()
        if acc is None:
            return None
        return Account(acc[0], acc[1], acc[2], acc[3], acc[4], acc[5], acc[6])

    def add_account(self, account: Account) -> Account:
        print(account.password.decode("utf-8"))
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO accounts (login, password, salt, email, confirmed, phone) VALUES (?, ?, ?, ?, ?, ?)",
                       (account.login, account.password.decode("utf-8"), account.salt.decode("utf-8"), account.email, account.confirmed, account.phone))
        self.connection.commit()
        account.account_id = cursor.lastrowid
        return account

    def update_account(self, account: Account) -> Account:
        cursor = self.connection.cursor()
        cursor.execute("UPDATE accounts SET login = ?, password = ?, salt = ?, email = ?, confirmed = ?, phone = ? WHERE account_id = ?",
                       (account.login, account.password.decode("utf-8"), account.salt.decode("utf-8"), account.email, account.confirmed, account.phone, account.account_id))
        self.connection.commit()
        return account

    def delete_account(self, account_id: str) -> bool:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM accounts WHERE account_id = ?", account_id)
        self.connection.commit()
        return cursor.rowcount > 0

    def get_all_accounts(self) -> [Account]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accounts")
        accs = cursor.fetchall()
        accounts = []
        for acc in accs:
            accounts.append(Account(acc[0], acc[1], acc[2], acc[3], acc[4], acc[5], acc[6]))
        return accounts

    def get_next_id(self) -> int:
        cursor = self.connection.cursor()
        cursor.execute("SELECT MAX(account_id) FROM accounts")
        max_id = cursor.fetchone()[0]
        if max_id is None:
            return 0
        return max_id + 1