import pyodbc
import unittest
from src.db_account_provider import DbAccountProvider
from src.auth import Auth

class DbTest(unittest.TestCase):
    def test_connection(self):
        conn = pyodbc.connect('DRIVER={MySQL ODBC 9.1 ANSI Driver};SERVER=localhost;DATABASE=test;UID=test;PWD=test')
        cursor = conn.cursor()
        cursor.execute('SELECT @@VERSION')
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        conn.close()

    # def test_create_account(self):
    #     print("create_account")
    #     conn = pyodbc.connect('DRIVER={MySQL ODBC 9.1 ANSI Driver};SERVER=localhost;DATABASE=test;UID=test;PWD=test')
    #     last_count = len(DbAccountProvider(conn).get_all_accounts())
    #     msSqlAccountProvider = DbAccountProvider(conn)
    #     auth = Auth(msSqlAccountProvider)
    #     account = auth.register('testLogin', 'testPassword', 'testEmail', 'testPhone')
    #     self.assertEqual(last_count+1, len(DbAccountProvider(conn).get_all_accounts()))


    def test_login(self):
        conn = pyodbc.connect('DRIVER={MySQL ODBC 9.1 ANSI Driver};SERVER=localhost;DATABASE=test;UID=test;PWD=test')
        msSqlAccountProvider = DbAccountProvider(conn)
        auth = Auth(msSqlAccountProvider)
        result, account = auth.login('testLogin', 'testPassword')
        self.assertEqual(0, result, "Login failed")

