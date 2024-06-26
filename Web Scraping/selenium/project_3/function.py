from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

service = Service(executable_path="chromedriver.exe")
web = "https://twitter.com/search?q=python&src=typed_query"
driver = webdriver.Chrome(service=service)
driver.get(web)
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


# Initializing storage
user_data = []
text_data = []

# Getting all the tweet cards/boxes listed in a single page
tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))

# Looping through the tweets list
for tweet in tweets:
    tweet_list = get_tweet(tweet)  # calling the get_tweet function
    user_data.append(tweet_list[0])  # appending the first element of tweet_list (username)
    text_data.append(" ".join(tweet_list[1].split()))  # appending the second element of tweet_list (text)


driver.quit()

# Storing the data into a DataFrame and exporting to a csv file
df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
df_tweets.to_csv('tweets.csv', index=False)

print(df_tweets)