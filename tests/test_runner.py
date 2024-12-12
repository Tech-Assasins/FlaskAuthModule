from tests.account_test import AccountTest
from tests.auth_test import AuthTest

def run_auth_lib_tests():
    AccountTest()
    AuthTest()


if __name__ == '__main__':
    run_auth_lib_tests()