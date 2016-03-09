
## Regular expression something refers to regex or regexp
# Clever expressions for matching and parsing string (extract information)
# Take a look to https://docs.python.org/2/library/re.html

## Regular expressions package

# Import the 're' package (needed to use regular expression in Pyhton)
import re

# Few Examples:
# ^         Start of line
# .         any character
# .*        any characters (0 or more time)
# .*?       any characters but not greedy
# .+        any characters (1 or more time)
# .+?       any characters but not greedy
# .{3}      exactly 3 characters
# .{3,}     3 or more characters
# .{3,5}    3,4 or 5 characters
# \S        any non-whitespace character
# \S+       any non-whitespace characters
# [^ ]*     any non-blank characters
# [0-9]     any one-digit number
# [0-9]+    any integer (one or more digits)
# [0-9.]+   any float
# [AED]     any upper A or E or D
# [^AED]    any characters except upper A or E or D
# [a-z0-9]  any lowercase letter or digit

str1 = 'X-a:'
str2 = 'X-DSPAM-Confidence: 0.8475'

# the dot character ('.') matches any character (only one character)
# ^X.: means starting line with a 'X-' then any character (only one) then ':'
if re.search('^X-.:',str1): print str1,"matches '^X-.:'"
if not re.search('^X-.:',str2): print str2,"not matches '^X-.:'"

# by adding the asterix ('*'), the character is 'any number of times'
# ^X.*: means starting line with a 'X-' then any characters then ':'
if re.search('^X-.*:',str1): print str1,"matches '^X-.*:'"
if re.search('^X-.*:',str2): print str2,"matches '^X-.*:'"

# match any non-whitespace character ('\S') or non-whitespace characters ('\S+')
# ^X.*: means starting line with a 'X-' then any non-whitespace characters and
# then ':'
if re.search('^X-\S:',str1): print str1,"matches '^X-\S:'"
if re.search('^X-\S+:',str2): print str2,"matches '^X-\S+:'"


## re.search() method returns True or False if the regular expression is find
if re.search('e', "hello"):
    print True
else:
    print False


## findall() method extract the matching string and returns them as List

x = "My 2 favorite numbers are 5 and 23"
y = re.findall('[0-9]+',x)
print y


## Greedy matching
# The repeat character ('*' or '+') push outward in both direction (greedy) to
# match the largest posible string

# Example returns 'From: Again:' and not only 'From:'
x = "From: Again: blablabla"
y = re.findall('^F.+:',x)
print y


## Not Greedy matching
# By adding a '?' to the '+' or '*'

# Example returns 'From:' and not 'From: Again:'
x = "From: Again: blablabla"
y = re.findall('^F.+?:',x)
print y


## Fine-Tuning String Extraction with parenthesis
# Parenthesis are not part of the match but they tell where to start and stop
# what string to Extraction

# I want all email adresses in line starting by 'From ' (but I don't want to
# extract 'From', only the email adress)
x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
emails = re.findall('^From (\S+@\S+)', x)
print emails


## The escape character
# If you want a special regular expression character to just behave normally
# you prefix it with '\' (most of the time)
x = "I sent you $10.00 yesterday"
y = re.findall('\$[0-9.]+',x)
print y
