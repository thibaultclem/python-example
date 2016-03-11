## XML and python

# XML is include in Python, just import:
import xml.etree.ElementTree as ET


## Example of XML file
data = '''
<person>
  <name>Thib</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''


## Work with XML

# Parsing a String to get an XML Tree Object
tree = ET.fromstring(data)
stuff = ET.fromstring(input)

# Find element in the tree
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')

import xml.etree.ElementTree as ET

# get all users node to a List
lst = stuff.findall('users/user')
print 'User count:', len(lst)

# Work on XML node (a user)
for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")
