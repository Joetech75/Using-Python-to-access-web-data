from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
sum = 0
x=0
list = tags
for tag in tags:
  sum = int(tag.contents[x]) + sum
      
print(sum)   
