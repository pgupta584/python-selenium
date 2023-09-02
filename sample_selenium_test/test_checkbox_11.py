# First We will type the following statement to import the web driver:
import time
from select import select

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Check for some Practice website Else Create own html to practice
class TestPythonSelenium:
    @mark.test11
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(5)
        all_checkbox = driver.find_elements(by=By.XPATH, value="//input[@type='checkbox']")
        # Iterate through all the checkbox & select desire one - Checkbox 2
        for checkbox in all_checkbox:
            print("Text --> ", checkbox.text)
            if checkbox.text == "checkbox 1":
                checkbox.click()
                print("Check box selected")
            else:
                print("Not Available")
        driver.close()

    @mark.test11
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(5)
        # Directly Handle using Xpath, Identify the text and select preceding checkbox
        checkbox_name = "checkbox 1"
        checkbox = driver.find_elements(by=By.XPATH, value=f"//input[contains(text(),' {checkbox_name}']//preceeding::input")
        checkbox.clear()
        driver.close()
