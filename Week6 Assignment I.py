import urllib
import json

while 1:
    url = 'http://python-data.dr-chuck.net/comments_266871.json'
    print 'Retrieving', url

    data = urllib.urlopen(url).read()
    print 'Retrieved', len(data), 'characters'
    
    js = json.loads(data)
    count = 0
    sum = 0
    for user in js['comments'] :
        count += 1
        sum += int(user['count'])
    
    print 'Count:', count
    print 'Sum:', sum
    break
    
