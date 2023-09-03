# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By


# https://testpages.eviltester.com/styled/index.html
class TestPythonSelenium:
    @mark.test142
    def test_window_handle_1(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(5)
        # Get Parent Window ID
        parent_window = driver.current_window_handle
        link_element = driver.find_element(by=By.XPATH, value="//a[text()='Click Here']")
        link_element.click()
        time.sleep(2)
        # Fetch all the window
        all_window = driver.window_handles  # return list of windows id
        for window in all_window:
            if window != parent_window:
                # Switch to new Window
                driver.switch_to.window(window)
                print("Switched to Child Window")
                time.sleep(2)
                driver.close()
        # Switch to Parent Window
        driver.switch_to.window(parent_window)
        print("Window switch is done")
        driver.close()

    @mark.test14
    def test_window_handle_2(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(5)
        # Get Parent Window ID
        parent_window = driver.current_window_handle
        link_element = driver.find_element(by=By.XPATH, value="//a[text()='Click Here']")
        # Grab the text before switch
        main_text_element = driver.find_element(by=By.TAG_NAME, value="h3")
        print("Grab the text before switch --> ", main_text_element.text)
        link_element.click()
        time.sleep(2)
        # Fetch all the window
        all_window = driver.window_handles  # return list of windows id
        for window in all_window:
            if window != parent_window:
                # Switch to new Window
                driver.switch_to.window(window)
                print("Switched to Child Window")
                # Grab the text after switch
                text_element = driver.find_element(by=By.TAG_NAME, value="h3")
                print("Grab the text after switch --> ", text_element.text)
                time.sleep(2)
                driver.close()
        # Switch to Parent Window
        driver.switch_to.window(parent_window)
        print("Window switch is done")
        # Grab the text After switch to Main again
        main_text_element = driver.find_element(by=By.TAG_NAME, value="h3")
        print("Grab the text After switch to main Again --> ", main_text_element.text)
        driver.close()
