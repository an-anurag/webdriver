from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser
driver = webdriver.Chrome()  # You need to have chromedriver installed and its path set in your system

# Navigate to a webpage
driver.get("https://www.google.com")

# Close the browser
driver.quit()
