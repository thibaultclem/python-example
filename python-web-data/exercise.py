
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
