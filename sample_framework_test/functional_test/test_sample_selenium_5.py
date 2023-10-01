from pytest import mark
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from sample_framework_test.PageObjects.LoginPage import LoginPage
from sample_framework_test.utility.TestBase import TestBase


# @pytest.mark.usefixtures("setup")
class TestSampleSelenium(TestBase):
    @mark.sample_test_60
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.get_user_name().send_keys("Admin")
        login_page.get_password().send_keys("admin1234")
        login_page.get_login_button().click()
        TestBase.verify_visibility_of_web_element(self, (login_page.get_invalid_login_message()))
        error_message = login_page.get_invalid_login_message().text
        print("error_message", error_message)
        print("Test Completed")
        self.driver.close()
