import pytest


# Pytest Fixture --> It's used as teardown methods like in other framework like in TestNg we have @beforeMethod/@afterMethod
# @beforeClass/@afterClass to perform common action for all the test
# Let's see one example
class TestFixture:  # Test Name should start/End with Test to follow best practice
    @pytest.mark.send_email
    def test_send_email(self, login_to_gmail_method):
        assert True
        print("Email sent is Success")

    @pytest.mark.send_email
    def test_send_email_with_attachments(self, login_to_gmail_method):
        assert True
        print("Email sent with attachments is Success")
