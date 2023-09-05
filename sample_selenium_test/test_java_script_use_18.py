# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# https://the-internet.herokuapp.com/iframe
# JS use in Selenium --> Since all the browser implemented via Java scripts so using Java scripts we can manupulate
# anything on browser. Like Scroll down etc.
# Selenium doesn't provide direct code to scroll down but given code to execute java scripts.
# So using java Or Python you can execute java scripts
class TestPythonSelenium:
    @mark.test18
    def test_js_1(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        # It will wait for all the element to be present up to 5 sec globally
        driver.implicitly_wait(5)
        # Execute JS using below - to a particular vertex
        driver.execute_script("window.scroll(0,400);")
        time.sleep(1)
        # Execute JS using below to the end
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        time.sleep(2)
        driver.close()
