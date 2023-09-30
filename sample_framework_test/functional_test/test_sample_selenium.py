import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSampleSelenium:
    @mark.sample_test_1
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(30)
        fb_email = driver.find_element(by=By.NAME, value="username")
        fb_email.send_keys("Admin")
        time.sleep(2)
        fb_password = driver.find_element(by=By.NAME, value="password")
        fb_password.send_keys("admin123")
        time.sleep(2)
        button = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
        button.click()
        dashboard = driver.find_element(by=By.XPATH, value="//h6[text()='Dashboard']")
        is_dashboard_displayed = dashboard.is_displayed()
        assert is_dashboard_displayed is True, "Login is not success"
        print("Test Completed")
        driver.close()
    # let's generalise the browser now, will write common test TestBase where we will keep all common test
