
## EXERCISE 1 - regular expression
import re

# Extract all email adress by using regular expression
x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
print re.findall('\S+@\S+',x)


# Read through and parse a file with text and numbers. You will extract all
# the numbers in the file and compute the sum of the numbers.
nbList = list()
total = 0
handle = open('regex_sum_252429.txt')
for line in handle:
    line = line.rstrip()
    nbList = nbList + re.findall('[0-9]+',line)
for nb in nbList:
    total = total + int(nb)
print total

# shorter solution
print sum( [ int(v) for v in re.findall('[0-9]+',open('regex_sum_252429.txt').read()) ] )


## EXERCISE 2 - parsing HTML

# In this code we will use BeautifulSoup 3 which is specifically written for Python
# 2.x and will not work in Python 3.x.
# To see example with BeautifulSoup 3 take a look to parsing-html.py
from BeautifulSoup import *
import urllib

url = raw_input('Enter - ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_252434.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Init integers
count = 0
total = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    nb = int(tag.contents[0])
    count = count + 1
    total = total + nb
print 'Count',count
print 'Sum',total


## EXERCISE 3 - parsing HTML

url = raw_input('Enter URL: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/known_by_Aleem.html'
count = raw_input('Enter count: ')
if len(count) < 1 : count = 7
position = raw_input('Enter position: ')
if len(position) < 1 : position = 18

# Init counter
counter = 0

while counter <= count:
    print 'Retrieving:',url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[position-1].get('href', None)
    counter += 1


## EXERCISE 4 - parsing XML

import urllib
import xml.etree.ElementTree as ET

## Get XML
url = raw_input('Enter URL: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_252431.xml'
print 'Retrieving',url
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

# Parsing string to XML
tree = ET.fromstring(data)

## Init integers
total = 0

# Get all counts elements
counts = tree.findall('.//count')
print 'Count:',len(counts)

#Do the sum
for nb in counts:
    total = total + int(nb.text)

# Print sum of comments
print 'Sum:',total


## EXERCISE 5 - parsing JSON

import urllib
import json

url = raw_input('Enter URL: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_252435.json'
print 'Retrieving',url
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

# Parsing string to JSON
js = json.loads(str(data))

## Init integers
total = 0

# Get all comments elements
comments = js['comments']
print 'Count:',len(comments)

#Do the sum
for item in comments:
    total = total + int(item['count'])

# Print sum of comments
print 'Sum:',total


## EXERCISE 6 - parsing JSON from REST API

import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    # Call to the server
    uh = urllib.urlopen(url)
    # Call to the API to retrieve datas
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    # Parse data to JSON
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    # Get lat and lng of the first result
    place_id = js["results"][0]["place_id"]
    print 'Place id',place_id
