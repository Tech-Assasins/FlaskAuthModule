import unittest
from src.account import Account
from src.utility import generate_salt, hash_password_and_generate_salt


class AccountTest(unittest.TestCase):
    def test_account_constructor(self):
        hps = hash_password_and_generate_salt('password'.encode())
        account = Account(0, 'login', hps[0], hps[1], 'email', False, 'phone')
        self.assertEqual(account.account_id, 0)
        self.assertEqual(account.login, 'login')
        self.assertEqual(account.email, 'email')
        self.assertEqual(account.confirmed, False)
        self.assertEqual(account.phone, 'phone')

    def test_compare_password(self):
        hps = hash_password_and_generate_salt('password'.encode())
        account = Account(0, 'login', hps[0], hps[1], 'email', False, 'phone')
        self.assertTrue(account.compare_password('password'))
        self.assertFalse(account.compare_password('wrong_password'))

    def test_generate_salt(self):
        hps = hash_password_and_generate_salt('password'.encode())
        account = Account(0, 'login', hps[0], hps[1], 'email', False, 'phone')
        self.assertNotEqual(account.salt, '')

    # Passwords shouldn't have the same hash even if they are the same
    def test_same_password_hashing(self):
        hps = hash_password_and_generate_salt('password'.encode())
        hps2 = hash_password_and_generate_salt('password'.encode())

        account1 = Account(0, 'login', hps[0], hps[1], 'email', False, 'phone')
        account2 = Account(0, 'login', hps2[0], hps[1], 'email', False, 'phone')
        self.assertFalse(account1.compare_hashed_password(account2.password_hash))