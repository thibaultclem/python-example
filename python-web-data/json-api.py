# Json represents data as Dictionary and List

## JSON is include in python, just import the library
import json


## JSON datas
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''


## Work with JSON

# Parsing string to JSON
info = json.loads(data)
users = json.loads(input)

# Find attribute in the JSON file
print 'Name:',info["phone"]
print 'Hide:',info["email"]["hide"]
print 'User count:', len(users)

# loop on users
for item in users:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']


## Accesing API with Python

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

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

    # Print indented JSON file
    print json.dumps(js, indent=4)

    # Get lat and lng of the first result
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    # Get the location name of the first result
    location = js['results'][0]['formatted_address']
    print location

    # Loop and display all results
    print 'All results for',address,':'
    results = js['results']
    for result in results:
        lat = result["geometry"]["location"]["lat"]
        lng = result["geometry"]["location"]["lng"]
        location = result['formatted_address']
        print location,' - lat',lat,'lng',lng


## API security and Rate Limiting

# The data providers might limit the number of requests per day, demand an
# API key or charge for usage

## Test with Twitter api
# See twurl.py, oauth.py and hidden.py
# Fill in hidden.py
import urllib
import json
from twurl import augment

print '* Calling Twitter...'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': 'ThibaultClment', 'count': '2'} )
print url
connection = urllib.urlopen(url)
data = connection.read()
js = json.loads(str(data))
# Print the tweets
print '\n### TWEETS'
for item in js:
    print '#',item['text']
# Print the header
print '\n### HEADER'
headers = connection.info().dict
for header,value in headers.items():
    print '#',header,':',value


## Get the friends of a twitter user

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    url = augment(TWITTER_URL,
        {'screen_name': acct, 'count': '5'} )
    print 'Retrieving', url
    connection = urllib.urlopen(url)
    data = connection.read()
    headers = connection.info().dict
    # Print numbers of request I can do
    print 'Remaining', headers['x-rate-limit-remaining']
    js = json.loads(data)
    # Print the JSON
    print json.dumps(js, indent=4)

    # Print the friends username of the user + 50 first characters of their
    # status
    for u in js['users'] :
        print u['screen_name']
        s = u['status']['text']
        print '  ',s[:50]
