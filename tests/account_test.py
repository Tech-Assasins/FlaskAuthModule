import unittest
from src.account import Account

class AccountTest(unittest.TestCase):
    def test_account(self):
        account = Account(0, 'login', 'password', '', 'email', False, 'phone')
        self.assertEqual(account.account_id, 0)
        self.assertEqual(account.login, 'login')
        self.assertEqual(account.email, 'email')
        self.assertEqual(account.confirmed, False)
        self.assertEqual(account.phone, 'phone')
        print('Account test passed')

    def test_compare_password(self):
        account = Account(0, 'login', 'password', '', 'email', False, 'phone')
        self.assertTrue(account.compare_password('password'))
        print('Compare password test passed')
        self.assertFalse(account.compare_password('wrong_password'))
        print('Compare wrong password test passed')

    def test_generate_salt(self):
        account = Account(0, 'login', 'password', '', 'email', False, 'phone')
        self.assertNotEqual(account.salt, '')
        print('Generate salt test passed')

    # Passwords shouldn't have the same hash even if they are the same
    def test_same_password_hashing(self):
        account1 = Account(0, 'login', 'password', '', 'email', False, 'phone')
        account2 = Account(0, 'login', 'password', '', 'email', False, 'phone')
        self.assertFalse(account1.compare_hashed_password(account2.password))
        print('Same password hashing test passed')