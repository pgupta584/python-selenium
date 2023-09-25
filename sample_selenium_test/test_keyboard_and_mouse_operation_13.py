# First We will type the following statement to import the web driver:
import re
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


# https://testpages.eviltester.com/styled/index.html
class TestPythonSelenium:
    @mark.test13
    def test_double_right_click_1(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        time.sleep(5)
        search_element = driver.find_element(by=By.NAME, value="q")
        search_element.send_keys("Pankaj Gupta")
        time.sleep(2)
        # Create Action class object & pass Driver control/Object
        action = ActionChains(driver)
        # Double Click
        action.double_click(search_element).perform()  # We need to add perform after every action
        print("Double Click is done")
        time.sleep(2)
        # Right Click
        action.context_click(search_element).perform()
        time.sleep(2)
        print("Right click is done")
        # Mouse hover
        hover_element = driver.find_element(by=By.XPATH, value="//div[@aria-label='Search by voice']")
        action.move_to_element(hover_element).perform()
        time.sleep(2)
        hover_element.click()
        time.sleep(5)

        print("Mouse hover is done")
        driver.close()

    @mark.test13
    def test_drag_and_drop_2(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        time.sleep(5)
        source_element = driver.find_element(by=By.LINK_TEXT, value="हिन्दी")
        target_element = driver.find_element(by=By.NAME, value="q")
        time.sleep(2)
        # Create Action class object & pass Driver control/Object
        action = ActionChains(driver)
        action.drag_and_drop(target_element, source_element).perform()
        time.sleep(2)
        print("Done")
        driver.close()

    @mark.test13
    def test_keyboard_action_2(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        time.sleep(5)
        search_element = driver.find_element(by=By.NAME, value="q")
        search_element.send_keys("Pankaj Gupta")
        time.sleep(2)
        # Create Action class object & pass Driver control/Object
        action = ActionChains(driver)
        # KeyBoard Operation
        # Backspace
        action.send_keys(Keys.BACKSPACE).perform()
        time.sleep(2)
        print("Backspace done")
        # Enter
        action.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        print("Keyboard Enter done")
        driver.close()
