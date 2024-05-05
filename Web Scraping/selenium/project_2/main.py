from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

web = "https://www.audible.com/search"
driver.get(web)
driver.maximize_window()


products = driver.find_elements(By.XPATH, "//div[contains(@class, 'adbl-impression-container')]//li")

book_title = []
book_author = []
book_length = []

for product in products:
    try:
        title = product.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]")
        author = product.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]")
        length = product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]")

        book_title.append(title.text)
        book_author.append(author.text)
        book_length.append(length.text)
    except NoSuchElementException:
        continue

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)

print(df_books)
