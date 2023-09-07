# Any pytest file should start with test_ OR end with _test --> then only pytest assume that it's test file
# Python Function/Method name should start with test_ --> then only pytest assume that it's test file
# Any code / Logic must be inside function & name should be meaningful

# Pytest marker --> is nothing but used to grouping the test like we have in other framework like in TestNg @group, in cucumber we have tags etc.

# putting assert True/False for assertion purpose only
import pytest


@pytest.mark.compose_email
@pytest.mark.smoke  # We can give multiple marker to a test method/class
def test_valid_compose_email():
    assert True
    print("Compose Success")


@pytest.mark.compose_email
def test_valid_draft_save():
    print("Draft Success")
    assert False


@pytest.mark.compose_email
def test_compose_email_with_attachments():
    print("Attachments Success")
    assert True

# We use -m tag for pytest marker to group the test, we can group Different Modules / Different test level like smoke/regression etc.
# pytest -m "compose_email" --> 3 Test will run because we have compose_email marker for all three test
# pytest -m "smoke" --> 1 Test will run because we have only one test with marker smoke.
# We can run test from multiple files using markers
# Pytest will scan all the test file and look for the marker & execute that functions --> that's the beauty for Marker
