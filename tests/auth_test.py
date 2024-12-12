import unittest
from src.auth import Auth
from tests.mock_account_provider import MockAccountProvider
from src.account import Account

class AuthTest(unittest.TestCase):
    def test_login_success(self):
        auth = Auth(MockAccountProvider())
        result, account = auth.login('login', 'password')
        self.assertEqual(result, 0)
        self.assertEqual(account.login, 'login')

    def test_login_account_not_found(self):
        auth = Auth(MockAccountProvider())
        result, account = auth.login('unknown_login', 'password')
        self.assertEqual(result, -1)
        self.assertEqual(account, None)

    def test_login_fail(self):
        auth = Auth(MockAccountProvider())
        result, account = auth.login('login', 'wrong_password')
        self.assertEqual(result, -2)
        self.assertEqual(account, None)

    def test_register(self):
        auth = Auth(MockAccountProvider())
        account = auth.register('login3', 'password3', 'email3', 'phone3')
        self.assertEqual(account.login, 'login3')
        self.assertEqual(account.email, 'email3')
        self.assertEqual(account.phone, 'phone3')
        self.assertFalse(account.confirmed)
        self.assertNotEqual(account.salt, '')
        self.assertNotEqual(account.password, 'password3')
        self.assertTrue(account.compare_password('password3'))

