# First We will type the following statement to import the web driver:
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By

# https://testpages.eviltester.com/styled/index.html
class TestPythonSelenium:
    @mark.test12
    def test_browser_test_1(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://testpages.eviltester.com/styled/alerts/alert-test.html")
        time.sleep(5)
        alert_element = driver.find_element(by=By.CSS_SELECTOR, value="#alertexamples")
        alert_element.click()
        time.sleep(2)
        print("Accept Alert")
        # Now alert doesn't have inspect element & we can't inspect , hence use alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("alert_text", alert_text)
        alert.accept()
        driver.close()

    @mark.test12
    def test_browser_test_2(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://testpages.eviltester.com/styled/alerts/alert-test.html")
        time.sleep(5)
        alert_element = driver.find_element(by=By.CSS_SELECTOR, value="#confirmexample")
        alert_element.click()
        print("Dismiss Alert")
        time.sleep(2)
        # Now alert doesn't have inspect element & we can't inspect , hence use alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("alert_text", alert_text)
        alert.dismiss()
        driver.close()

    @mark.test12
    def test_browser_test_3(self):
        # We will open the Google Chrome browser.
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://testpages.eviltester.com/styled/alerts/alert-test.html")
        time.sleep(5)
        alert_element = driver.find_element(by=By.CSS_SELECTOR, value="#promptexample")
        alert_element.click()
        print("Enter into Alert & accept")
        time.sleep(2)
        # Now alert doesn't have inspect element & we can't inspect , hence use alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("alert_text", alert_text)
        alert.send_keys("Hello Pankaj")
        time.sleep(2)
        alert.accept()
        print("Done")
        driver.close()
