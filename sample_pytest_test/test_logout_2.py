# Any pytest file should start with test_ OR end with _test --> then only pytest assume that it's test file
# Python Function/Method name should start with test_ --> then only pytest assume that it's test file
# Any code / Logic must be inside function & name should be meaningful
def test_valid_logout():
    print("Logout Success")
    assert True

def test_verify_title():
    expected_title = "Google"
    assert expected_title == "Google", "title verification failed"

# Duplicate method name will be overriden
def test_verify_title():
    expected_title = "Google"
    actual = "Googlee"
    assert expected_title == actual, f"title verification failed expected is {expected_title} but actual is {actual}"
