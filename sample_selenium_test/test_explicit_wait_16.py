# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# https://testpages.eviltester.com/styled/index.html
# Explicit wait - > If in a web page only one/two element taking sometime(20sec) to load in that case applying implicit wait
# globally up to 20sec is bad coding practice.
# hence only for that web element I want to handle that It should wait up to 20sec and if it's going beyond failed it
# as performance issue like that scenario - we can use explicit wait
class TestPythonSelenium:
    # Need to search a website to show demo
    @mark.test16
    def test_explicit_wait_1(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.huffpost.com/entry/worst-website-load-times_n_571889")
        # It will wait for all the element to be present up to 5 sec globally
        driver.implicitly_wait(5)
        # If any element taking more than that we can handle using explicit wait and failed
        # If it's going beyond expected time
        slow_element = driver.find_element(by=By.XPATH, value="//*[@class='top-trending-title']/div")
        # It will click on web element & wait for the web element up to 5 sec only
        slow_element.click()
        # Let's use explicit wait to handle it
        # Implicit wait also known as webdriver wait
        text_element = driver.find_element(by=By.XPATH, value="//*[text()='Careers']")
        # Create WebDriverWait Object & passing driver & wait in sec
        wait = WebDriverWait(driver, 15)
        # Using wait we can use it based on our requirement
        wait.until(expected_conditions.presence_of_element_located(text_element))
        # Grab the text from Slow Element Page
        print("Grab the text from Slow Element Page --> ", text_element.text)
        driver.close()
