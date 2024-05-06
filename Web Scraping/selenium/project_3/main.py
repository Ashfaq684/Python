from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

load_dotenv()


service = Service(executable_path="chromedriver.exe")
web = 'https://twitter.com/'
driver = webdriver.Chrome(service=service)
driver.get(web)
driver.maximize_window()

login = driver.find_element(By.XPATH, "//a[@href='/login']")
login.click()
time.sleep(2)


wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
username.send_keys(os.getenv("TWITTER_USER"))

next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
next_button.click()

password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
password.send_keys(os.getenv("TWITTER_PASS"))

login_button = driver.find_element(By.XPATH, "//span[text()='Log in']")
login_button.click()

time.sleep(20)

driver.quit()