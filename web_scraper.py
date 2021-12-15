#хотела изучить модуль requests, так как хотела научится парсить страницы, извлекать информацию из них
import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping/",
)
soup = BeautifulSoup(response.content, 'html.parser')

for title in soup.find_all('title'):
    print(title.get_text())

allLinks = soup.find(id="bodyContent").find_all("a")
linkToScrape = 0

for link in allLinks:
	if link['href'].find("/wiki/") == -1: 
		continue

	linkToScrape = link
	break

print(linkToScrape)
