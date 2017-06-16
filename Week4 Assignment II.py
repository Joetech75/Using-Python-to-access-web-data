#  Following Links in HTML Using BeautifulSoup

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program


import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
count = raw_input('Enter count:')
pos = raw_input('Enter position:')

count = int(count)
pos = int(pos) - 1
print 'Retrieving:', url

while 1 :
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags= soup('a')

    if count > 0 :
        link = tags[pos].get('href', None)    # get URL from the pos of the tag
        print 'Retrieving:', link
        count = count - 1
        url = link
        continue
    else : break
