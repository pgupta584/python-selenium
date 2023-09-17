from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# This will automatically download the chrome driver and give the control to chrome driver
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get("http://www.google.com")

# We can do it by passing the path by manually download the chrome driver also.
# service_obj = Service("/Users/pankaj.gup/Documents/BrowserDriver/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("http://www.google.com")

# This will automatically download the chrome driver and give the control to chrome driver without service also
driver = webdriver.Chrome()
driver.get("http://www.google.com")
