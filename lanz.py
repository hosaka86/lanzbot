from bs4 import BeautifulSoup
import urllib.request
from gazpacho import Soup


landing_page = urllib.request.urlopen("https://www.zdf.de/gesellschaft/markus-lanz")
soup = BeautifulSoup(landing_page, "html.parser")

link_list = []

for link in soup.findAll('a'):
    link_list.append(link.get('href'))

followup = f"https://www.zdf.de{link_list[27]}" #get last from "Alle Videos der Sendung"

get_guests = urllib.request.urlopen(followup)
guest_soup = BeautifulSoup(get_guests, "html.parser")

print(guest_soup.find("meta", {"property": "og:title"}).attrs['content'])
print(guest_soup.find("meta", {"property": "og:description"}).attrs['content'])
