# First We will type the following statement to import the web driver:
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPythonSelenium:
    @mark.test1
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        google_search = driver.find_element(by=By.NAME, value="q")
        google_search.send_keys("Pankaj Gupta Udemy")
        driver.implicitly_wait(10000)
        print("Success")
        driver.close()
