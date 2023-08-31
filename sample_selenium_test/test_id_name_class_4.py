# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPythonSelenium:
    @mark.test4
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        time.sleep(2)
        fb_email = driver.find_element(by=By.NAME, value="email")
        fb_email.send_keys("name@gmail.com")
        time.sleep(2)
        fb_email.clear()
        fb_email_1 = driver.find_element(by=By.ID, value="email")
        fb_email_1.send_keys("id@gmail.com")
        time.sleep(2)
        fb_email.clear()
        fb_email_2 = driver.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy")
        fb_email_2.send_keys("class@gmail.com")
        time.sleep(2)
        driver.close()
