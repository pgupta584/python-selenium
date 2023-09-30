from selenium.webdriver.common.by import By


class LoginPage:
    # Declaring a constructor to pass driver Object
    def __init__(self, driver):
        self.driver = driver

    user_name = (By.NAME, "username")  # This is simple tuple
    def get_user_name(self):
        return self.driver.find_element(*LoginPage.user_name)  # Calling Class Variable using class name & instance variable using self
        #  use * to deserialize & use it as tuple

    # Keeping all the web elements here
    password = (By.NAME, "password")
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    login_button = (By.XPATH, "//button[@type='submit']")
    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    # Invalid login
    invalid_login = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    def get_invalid_login_message(self):
        return self.driver.find_element(*LoginPage.invalid_login)
