# project name - weather app

import requests
import json

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])