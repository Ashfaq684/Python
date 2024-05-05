from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

website = 'https://www.adamchoi.co.uk/overs/detailed'
driver.get(website)

wait = WebDriverWait(driver, 10)

all_matches_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@analytics-event="All matches"]')))
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

matches = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'tr')))

# time.sleep(10)

date = []
home_team = []
score = []
away_team = []

for match in matches:
    cells = match.find_elements(By.TAG_NAME, 'td')
    date.append(cells[0].text)
    home_team.append(cells[1].text)
    score.append(cells[2].text)
    away_team.append(cells[3].text)

# print(home_team)

time.sleep(10)

driver.quit()

df = pd.DataFrame({
    'date': date,
    'home_team': home_team,
    'score': score,
    'away_team': away_team
})

df.to_csv('football_data(spain).csv', index=False)
print(df)