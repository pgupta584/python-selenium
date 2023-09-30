import time

from pytest import mark
from selenium.webdriver.common.by import By

from sample_framework_test.PageObjects.HomePage import HomePage
from sample_framework_test.PageObjects.LoginPage import LoginPage
from sample_framework_test.utility.TestBase import TestBase


# @pytest.mark.usefixtures("setup")
class TestSampleSelenium(TestBase):
    @mark.sample_test_4
    def test_browser(self):
        login_page = LoginPage(self.driver)
        login_page.get_user_name().send_keys("Admin")
        # fb_password = self.driver.find_element(by=By.NAME, value="password")
        # fb_password.send_keys("admin123")
        login_page.get_password().send_keys("admin123")
        # button = self.driver.find_element(by=By.XPATH, value="//button[@type='submit']")
        # button.click()
        login_page.get_login_button().click()
        # Create page object for different page like home page
        home_page = HomePage(self.driver)
        dashboard = home_page.get_dashboard_name()
        # dashboard = self.driver.find_element(by=By.XPATH, value="//h6[text()='Dashboard']")
        is_dashboard_displayed = dashboard.is_displayed()
        assert is_dashboard_displayed is True, "Login is not success"
        print("Test Completed")
        self.driver.close()
        # Now let's create some utilty like for explicitly wait

