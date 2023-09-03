# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


# https://testpages.eviltester.com/styled/index.html
class TestPythonSelenium:
    @mark.test15
    def test_implicit_wait_1(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        # It will wait for all the element to be present upto 15 sec
        # If element appears before that 15 sec it will not wait 15 sec rather move to next code
        # After 15 sec also element not available then it will throw timeout exception
        driver.implicitly_wait(15)
        slow_element = driver.find_element(by=By.XPATH, value="//a[@href='/slow']")
        slow_element.click()
        # It will fail to grab the element from next page as it takes sometime to load
        # Hence we can use implicit wait to wait upto a particular sec
        # Grab the text from Slow Element Page
        text_element = driver.find_element(by=By.TAG_NAME, value="h3")
        print("Grab the text from Slow Element Page --> ", text_element.text)
        driver.close()

    @mark.test15
    def test_implicit_wait_2(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.huffpost.com/entry/worst-website-load-times_n_571889")
        # will se this example in any slow website
        # driver.implicitly_wait(15)
        slow_element = driver.find_element(by=By.XPATH, value="//*[@class='top-trending-title']/div")
        slow_element.click()
        # It will fail to grab the element from next page as it takes sometime to load
        # Hence we can use implicit wait to wait upto a particular sec
        driver.close()
