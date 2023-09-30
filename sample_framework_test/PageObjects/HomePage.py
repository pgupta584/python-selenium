from selenium.webdriver.common.by import By


class HomePage:
    # Declaring a constructor to pass driver Object
    def __init__(self, driver):
        self.driver = driver

    dashboard = (By.XPATH, "//h6[text()='Dashboard']")  # This is simple tuple
    def get_dashboard_name(self):
        return self.driver.find_element(*HomePage.dashboard)  # Calling Class Variable using class name & instance variable using self
        #  use * to deserialize & use it as tuple