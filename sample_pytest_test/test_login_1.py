# Any pytest file should start with test_ OR end with _test --> then only pytest assume that it's test file
# Python Function/Method name should start with test_ --> then only pytest assume that it's test file
# Any code / Logic must be inside function & name should be meaningful
def test_valid_login():
    print("Login Success")


def test_valid_login_1():
    print("Login 1 Success")


def invalid_login():
    print("invalid_login Success")


def incorrect_login_test():
    print("incorrect_login_test Success")

# We can run specific file with pytest <fileName>
# pytest /Users/pankaj.gup/Documents/MYGIT/Pyhon-Selenium/python-selenium/sample_pytest_test/test_login_1.py
# pytest /Users/pankaj.gup/Documents/MYGIT/Pyhon-Selenium/python-selenium/sample_pytest_test/test_logout_2.py

# We can execute test based on module name like
# -k stand for module/method name execution
# -s stand for logs the information
# -v stand for more information
# pytest -k login
# It's always best practice to run the test using it if we have to run module wise

# If python file name will not start/end with test - that file execution will be skipped,
# however by passing fileName explicitly we can run But not via pytest command
# pytest -m "falseLogin"
