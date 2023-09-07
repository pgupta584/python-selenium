import pytest
from conftest import load_test_data

# Use of Parameterization with fixture - will create new fixture for it

class TestFixture4:

    # Now Printing from dictionary / Pair - like username & password -> will create new fixture
    @pytest.mark.send_email7  # We must need to give fixture at functional in order to fetch the data via fixture
    def test_send_email(self, multiple_password):  # Else it will not work
        assert True
        # Printing in details
        print("Printing all Param", multiple_password[0])  # Only username will be param
        print("Printing all Param", multiple_password[1])  # Only password will be param, like that we can use for multiple tuple data
#  We can use it as per our requirements
