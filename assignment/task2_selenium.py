from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import time

# Launch Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# Open Laravel Login Page
driver.get("http://127.0.0.1:8000/login")

# Wait for page to load
time.sleep(2)

# Generate random email
random_email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@gmail.com"

# Generate random password
random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Locate Email Field
email = driver.find_element(By.NAME, "email_address")

# Locate Password Field
password = driver.find_element(By.NAME, "password")

# Fill the fields
email.send_keys(random_email)
password.send_keys(random_password)

print("Random Email :", random_email)
print("Random Password :", random_password)

# Keep browser open for 10 seconds
time.sleep(10)

# Close browser
driver.quit()