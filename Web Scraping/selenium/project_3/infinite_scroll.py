from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Chrome WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Twitter and log in
driver.get("https://twitter.com/login")

username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
username_input.send_keys(os.getenv("TWITTER_USER"))

next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
next_button.click()

password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
password_input.send_keys(os.getenv("TWITTER_PASS"))

login_button = driver.find_element(By.XPATH, "//span[text()='Log in']")
login_button.click()


# Wait for the login process to complete
WebDriverWait(driver, 10).until(EC.url_contains("https://twitter.com/home"))

# Open the search page
driver.get("https://twitter.com/PhysInHistory/status/1787031477084991971")
driver.maximize_window()


def get_tweet(element):
    """This function scrapes data of tweets. It returns a list with 2 elements; username and text"""
    try:
        user = element.find_element(By.XPATH, ".//span[contains(text(), '@')]").text
        text = element.find_element(By.XPATH, ".//div[@lang]").text
        tweets_data = [user, text]
    except:
        tweets_data = ['user', 'text']
    return tweets_data


user_data = []
text_data = []
tweet_ids = set()
scrolling = True

while scrolling:
    tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))

    for tweet in tweets[-15:]:
        tweet_list = get_tweet(tweet)
        tweet_id = ''.join(tweet_list)
        if tweet_id not in tweet_ids:
            tweet_ids.add(tweet_id)
            user_data.append(tweet_list[0])
            text_data.append(" ".join(tweet_list[1].split()))
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        #     scrolling = False
        #     break
        if len(user_data) > 60:
            scrolling = False
            break
        else:
            last_height = new_height
            break

driver.quit()
df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
df_tweets.to_csv('tweets_infinite_scroll_2.csv', index=False)

print(df_tweets)