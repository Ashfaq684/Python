from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

# options = Options()
# options.add_argument("--headless")
# options.add_argument('window-size=1920x1080')
# options.add_argument("--log-level=3")

service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)

web = "https://www.audible.com/search"
driver.get(web)
driver.maximize_window()

# pagination
pagination = driver.find_element(By.XPATH, "//ul[contains(@class, 'pagingElements')]")
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)


book_title = []
book_author = []
book_length = []

current_page = 1
while current_page <= last_page:
    time.sleep(2)
    products = driver.find_elements(By.XPATH, "//div[contains(@class, 'adbl-impression-container')]//li")

    for product in products:
        try:
            title = product.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]")
            author = product.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]")
            length = product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]")

            book_title.append(title.text)
            print(title)
            book_author.append(author.text)
            book_length.append(length.text)
        except NoSuchElementException:
            continue
    
    current_page += 1
    
    try:
        next_page = driver.find_element(By.XPATH, "//span[contains(@class, 'nextButton')]")
        next_page.click()
    except:
        pass

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
# df_books.to_csv('books_headless.csv', index=False)
df_books.to_csv('all_books.csv', index=False)

print(df_books)
