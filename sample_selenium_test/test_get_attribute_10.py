# First We will type the following statement to import the web driver:
import time
from select import select

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestPythonSelenium:
    @mark.test10
    def test_browser_test(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        google_search = driver.find_element(by=By.NAME, value="q")
        google_search.send_keys("Pankaj")
        time.sleep(2)
        roles = driver.find_elements(by=By.XPATH, value="(//li[@class='sbct sbre']/div/div/div/div/span)[1]")
        for drop_down in roles:
            # It will fetch all the text & if matched with value It will click
            if drop_down.text == "Pankaj Tripathi":
                drop_down.click()
                print("Pass")
            else:
                print("Values doesn't exit")
        # Above code will select the desire value , But how to verify it
        # We Can't get text as this is not part of HTML dome rather it's rendering at run time
        # Hence we can use getAttribute method of webdriver
        attribute = driver.find_element(by=By.ID, value="APjFqb")
        name = attribute.get_attribute("value")
        print("name -->> ", name)
        assert name == "pankaj tripathi", "Name not selected"
        time.sleep(5)
        driver.close()
