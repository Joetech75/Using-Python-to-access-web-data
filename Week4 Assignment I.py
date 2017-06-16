# Scraping HTML Data with BeautifulSoup

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum = 0
list = []

tags = soup('span')
for tag in tags:
	list.append([int(number) for number in tag.contents])

new_list = [item for sublist in list for item in sublist]
for x in new_list:
	sum = sum + x

print(sum)
