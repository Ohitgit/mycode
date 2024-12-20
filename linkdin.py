from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# LinkedIn credentials
USERNAME = "sourabhpatidar456@gmail.com"
PASSWORD = "sourab#@"



# Initialize WebDriver
driver = webdriver.Chrome()  # Use the correct driver (e.g., Edge, Firefox, etc.)

try:
    # Open LinkedIn login page
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)  # Allow the page to load
    
    # Enter username
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys(USERNAME)
    
    # Enter password
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)
    time.sleep(3)  # Allow login to complete

    # Navigate to the target profile
    driver.get(PROFILE_URL)
    time.sleep(5)  # Allow the profile page to load
    
    print("Profile opened successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
