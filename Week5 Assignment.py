import urllib
import xml.etree.ElementTree as ET

while 1:
    url = 'http://python-data.dr-chuck.net/comments_266867.xml'
    
    print 'Retrieving', url
    data = urllib.urlopen(url).read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)
    
    
    counts = tree.findall('.//comment')    # find all comment tags' position or use ./comments/comment
    print 'Count:', len(counts)
    sum = 0
    for score in counts:
        score = score.find('count').text    # find text in count tag
        sum = sum + int(score)
    print 'Sum:', sum
    break
