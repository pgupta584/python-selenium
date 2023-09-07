import pytest


# We can skip a test using a predefined marker called skipped, let's see some examples
# where to use --> We have some known bugs & we know it will fail always so that we can skip in execution so that report will look good
# we can simply skip OR skip with some message
@pytest.mark.skipTest
@pytest.mark.smoke  # We can give multiple marker to a test method/class
@pytest.mark.skip
def test_valid_compose_email():
    assert True
    print("Compose Success")


@pytest.mark.skip("We have Known Bugs FTR-1234")
@pytest.mark.skipTest
def test_valid_draft_save():
    print("Draft Success")
    assert False


@pytest.mark.skipTest
def test_compose_email_with_attachments():
    print("Attachments Success")
    assert True

# How to remove these multiple warning console message
# We can use --disable-pytest-warnings to disable all the warnings
# pytest -m "skipTest" --disable-pytest-warnings
# pytest -s -v -m "skipTest" --disable-pytest-warnings --> to see complete detailed logs
