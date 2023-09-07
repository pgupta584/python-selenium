import pytest


# Apply only once at class level based on requirements

@pytest.mark.usefixtures("login_to_gmail_class")
class TestFixture1:
    @pytest.mark.send_email1
    def test_send_email(self):
        assert True
        print("Email sent is Success")

    @pytest.mark.send_email1
    def test_send_email_with_attachments(self):
        assert True
        print("Email sent with attachments is Success")
