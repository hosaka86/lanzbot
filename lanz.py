import requests
from bs4 import BeautifulSoup
import time
import unicodedata

URL = 'https://www.fernsehmacher.de/markus-lanz-aktuell/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='main')

fubar = []

for i in results.text.split("\n"):
    fubar.append(i)


print(fubar[1:3])
time.sleep(2.4)
print(fubar[3:6])
