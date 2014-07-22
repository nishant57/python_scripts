import urllib2, urllib
from bs4 import BeautifulSoup

url = raw_input("Enter the url of the pages to copy its source HTML: ")
#response = urllib2.urlopen(url)
response = urllib.urlopen(url)
source = response.read()
soup = BeautifulSoup(source)
title = soup.title.string

for link in soup.find_all('a'):
	print(link.get('href'))
