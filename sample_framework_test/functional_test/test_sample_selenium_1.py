import time

from pytest import mark
from selenium.webdriver.common.by import By
from sample_framework_test.utility.TestBase import TestBase


# @pytest.mark.usefixtures("setup")
class TestSampleSelenium(TestBase):
    @mark.sample_test_2
    # def test_browser_test(self, setup):  # Since we have inherited, no need to call fixture explicitly
    def test_browser_test(self):
        # fb_email = setup.driver.find_element(by=By.NAME, value="username")
        fb_email = self.driver.find_element(by=By.NAME, value="username")
        fb_email.send_keys("Admin")
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
