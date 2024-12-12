from tests.account_test import AccountTest
from tests.auth_test import AuthTest
from tests.db_test import DbTest
import pyodbc

def run_auth_lib_tests():
    AccountTest()
    AuthTest()
    DbTest()


if __name__ == '__main__':
    run_auth_lib_tests()