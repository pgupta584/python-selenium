import pytest


@pytest.Mark.falseLogin
def test_false_login():
    assert True
    print("False Login Success")

# If python file name will not start/end with test - that file execution will be skipped,
# however by passing fileName explicitly we can run But not via pytest command
# pytest -m "falseLogin"
