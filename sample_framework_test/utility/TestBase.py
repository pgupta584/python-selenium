import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")  # Moving to TestBase because we can use it in all the classes
class TestBase:
    # pass  # Just passing for now
    def verify_visibility_of_web_element(self, web_element):
        # Create WebDriverWait Object & passing driver & wait in sec
        wait = WebDriverWait(self.driver, 15)
        # Using wait we can use it based on our requirement
        wait.until(expected_conditions.visibility_of(web_element))

