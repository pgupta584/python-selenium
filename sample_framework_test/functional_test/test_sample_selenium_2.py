import time

from pytest import mark
from selenium.webdriver.common.by import By
from sample_framework_test.PageObjects.LoginPage import LoginPage
from sample_framework_test.utility.TestBase import TestBase


# @pytest.mark.usefixtures("setup")
class TestSampleSelenium(TestBase):
    @mark.sample_test_3
    def test_browser(self):
        fb_email = LoginPage(self.driver)
        fb_email.get_user_name().send_keys("Admin")
        time.sleep(2)
        fb_password = self.driver.find_element(by=By.NAME, value="password")
        fb_password.send_keys("admin123")
        time.sleep(2)
        button = self.driver.find_element(by=By.XPATH, value="//button[@type='submit']")
        button.click()
        dashboard = self.driver.find_element(by=By.XPATH, value="//h6[text()='Dashboard']")
        is_dashboard_displayed = dashboard.is_displayed()
        assert is_dashboard_displayed is True, "Login is not success"
        print("Test Completed")
        self.driver.close()
