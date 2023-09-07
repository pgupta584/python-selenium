import pytest
from conftest import load_test_data

# Loading Test data from Fixture

@pytest.mark.usefixtures("load_test_data")
class TestFixture2:
    @pytest.mark.send_email2  # We must need to give fixture at functional in order to fetch the data via fixture
    def test_send_email(self):  # Else it will not work
        assert True
        print("load_test_data", load_test_data)
        print("Email sent is Success")

# If we try below it will not work
# pytest -s -v -m "send_email2" --disable-pytest-warnings

    @pytest.mark.send_email3
    def test_send_email_with_attachments(self, load_test_data):  # Here passing the fixture at test to make it work
        assert True
        print("load_test_data", load_test_data)
        print("Email sent with attachments is Success")
        # Can fetch by indexing also, like a list
        first_name = load_test_data[0]
        last_name = load_test_data[1]
        print(f"first name is -> {first_name} and last name is -> {last_name}")

# If we try below it will not work
# pytest -s -v -m "send_email3" --disable-pytest-warnings

    @pytest.mark.send_email4
    def test_send_email_with_notes(self, login_to_gmail_method, load_test_data):  # We can use multiple fixture in the test like it
        assert True
        print("load_test_data", load_test_data)
        print("Email sent with attachments is Success")
