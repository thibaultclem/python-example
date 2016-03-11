import urllib

## Web Scraping

# When a program or a script pretends to be a browser and retrieves/looks web
# pages extracts information and then looks at more web pages
# Search engines scrape web pages. We call this "spidering the web" or
# "web crawling"


## Parsing HTML using BeautifulSoup

# Download http://www.crummy.com/software/BeautifulSoup/bs4/download/4.4/beautifulsoup4-4.4.1.tar.gz
# Unzip
# Paste the bs4 folder in the folder containing your python code
from bs4 import BeautifulSoup

# Choose url
url = raw_input('Enter url: ')
if len(url) < 1 : url = 'http://blog.codinghorror.com/why-cant-programmers-program/'

# Get html pages
html = urllib.urlopen(url).read()

# Parsing the html
soup = BeautifulSoup(html, "html.parser")
# Retrieve a list of anchor tags
tags = soup('a')
# Print all url in the page
for tag in tags:
    print tag.get('href', None)
