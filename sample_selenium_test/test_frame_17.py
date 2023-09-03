# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# https://the-internet.herokuapp.com/iframe
# Frame - > When a webpage is inside another webpage, means that inner page is not local to html webpage
# Here Browser driver can handle only web element present inside local html webpage, not embedded page/frame
# So browser need to switch to frame by frame id and perform action
# How to identify frame - inspect & check if there is iframe in a webpage, also you can check with your dev & asked

class TestPythonSelenium:
    @mark.test17
    def test_frame_1(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/iframe")
        # It will wait for all the element to be present up to 5 sec globally
        driver.implicitly_wait(5)
        # Without switching to frame - Let's try
        # frame_element = driver.find_element(by=By.XPATH, value="//p[text()='Your content goes here.']")
        # frame_element.clear()
        # frame_element.send_keys("Hello Pankaj ")
        # will get selenium.common.exceptions.NoSuchElementException: As using normal way we can't do it

        # Handle by switching to frame - Let's try
        driver.switch_to.frame("mce_0_ifr")
        frame_element = driver.find_element(by=By.XPATH, value="//p[text()='Your content goes here.']")
        frame_element.clear()
        frame_element.send_keys("Hello Pankaj ")
        time.sleep(2)
        # print("Grab the text from Slow Element Page --> ", text_element.text)
        driver.close()
