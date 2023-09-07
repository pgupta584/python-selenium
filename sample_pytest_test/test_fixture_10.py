import pytest
from conftest import load_test_data

# Use of Parameterization with fixture - will create new fixture for it

class TestFixture3:
    @pytest.mark.send_email5  # We must need to give fixture at functional in order to fetch the data via fixture
    def test_send_email(self, multiple_valid_phone_number):  # Else it will not work
        assert True
        # Printing in details one by one all param
        print("Printing all Param", multiple_valid_phone_number)
