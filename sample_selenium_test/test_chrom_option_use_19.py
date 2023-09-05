# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# https://the-internet.herokuapp.com/iframe
# Chrom Option use in Selenium -->
class TestPythonSelenium:
    @mark.test19
    def test_chrom_option_1(self):
        # Using Chrom Option
        #
        chrom_option = webdriver.ChromeOptions()
        chrom_option.add_argument("--start-maximized")  # to Maximized browser
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome(options=chrom_option)  # We need to pass chrom option to the chrom object
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        # It will wait for all the element to be present up to 5 sec globally
        driver.implicitly_wait(5)
        driver.close()

    @mark.test19
    def test_run_headless_1(self):
        # Using Chrom Option
        #
        chrom_option = webdriver.ChromeOptions()
        chrom_option.add_argument("headless")  # to Run in Headless browser
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome(options=chrom_option)  # We need to pass chrom option to the chrom object
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        # It will wait for all the element to be present up to 5 sec globally
        driver.implicitly_wait(5)
        driver.close()

    @mark.test19
    def test_ignore_certificate_1(self):
        # Using Chrom Option
        #
        chrom_option = webdriver.ChromeOptions()
        chrom_option.add_argument("--ignore-certificate-errors")  # to ignore certificate
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome(options=chrom_option)  # We need to pass chrom option to the chrom object
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        # It will wait for all the element to be present up to 5 sec globally
        driver.implicitly_wait(5)
        driver.close()

    # We can explore other Chrome options available
