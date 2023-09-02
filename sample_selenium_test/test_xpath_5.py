# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPythonSelenium:
    @mark.test5
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        fb_email = driver.find_element(by=By.XPATH, value="//input[@data-testid='royal_email']")
        fb_email.send_keys("xpath@gmail.com")
        time.sleep(2)
        driver.close()
