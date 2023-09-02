# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestPythonSelenium:
    @mark.test8
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        time.sleep(2)
        create_account = driver.find_element(by=By.XPATH, value="//a[@data-testid='open-registration-form-button']")
        create_account.click()
        time.sleep(2)
        year = driver.find_element(by=By.ID, value="year")
        # put locator inside select class to use it
        select_year = Select(year)
        select_year.select_by_visible_text("2020")
        time.sleep(5)
        driver.close()
