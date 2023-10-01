#  Go to this URL https://docs.pytest.org/en/7.1.x/example/simple.html
#  Now Create a pytest addoption and use inside a fixture
from pytest import mark


@mark.environment_test
def test_environment(get_environment):
    if get_environment == "preprod":
        print("This is PREPROD URL")
    elif get_environment == "uat":
        print("This is UAT URL")
    else:
        print("Please check the Environment setting")
