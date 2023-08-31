# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPythonSelenium:
    @mark.test2
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(2)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        time.sleep(2)
        driver.minimize_window()
        google_search = driver.find_element(by=By.NAME, value="q")
        google_search.send_keys("Pankaj Gupta Udemy")
        driver.maximize_window()
        time.sleep(2)
        title = driver.title
        print("title --> ", title)
        assert title == "Google", "Title doesn't matched"
        print("Test Pass")
        driver.back()
        time.sleep(2)
        driver.refresh()
        assert title == "Google", "Title doesn't matched"
        driver.forward()
        time.sleep(2)
        driver.close()
