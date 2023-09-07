import pytest


# Pytest Fixture --> It's used as teardown methods like in other framework like in TestNg we have @beforeMethod/@afterMethod
# @beforeClass/@afterClass to perform common action for all the test
# Let's see one example

# If we want this test should run only once before class
@pytest.fixture(scope="class")
def login_to_gmail():
    print("Login to Gmail Success")

# Use of yield --> like after method/class
@pytest.fixture(scope="class")
def login_to_gmail():
    print("Login to Gmail Success")
    yield
    print("Logout is Success")

# If we want this test should run after every method
# @pytest.fixture(scope="function")
# def login_to_gmail():
#     print("Login to Gmail Success")

# Now we need to pass this fixture to function, will create one more test file to understand

