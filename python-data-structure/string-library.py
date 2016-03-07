#
# Learn about String built-in functions in Python
#

# lower function to transform string to lower case
print "\n#lower function \n"
up = "Hello Thib"
print up
low = up.lower()
print low

# upper function to transform string to upper case
print "\n#upper function \n"
low2 = "originally this is lower case"
print low2
up2 = low2.upper()
print up2
print "make me biggggger !!!".upper()

# find function to search for a substring within another substring
# Similar to int except it tells you where it finds the string
print "\n#find function \n"
str = "jordan"
pos = str.find("a")
print "a is on position ",pos+1," in " + str

# Replace function
print "\n#replace function \n"
str1 = "Hello Bob"
print str1
nstr = str1.replace('Bob', 'Thib')
print nstr

# Strip function (stripping whitespace by default if no argument)
print "\n#strip function \n"
wstr = "   here is mty sentence originally starting with whitespace"
print wstr
nwstr = wstr.strip()
print nwstr

# startswith function (Prefixes)
print "\n#startswith function (Prefixes) \n"
line  = "See you tomorrow"
print line + " start with 'See' is",line.startswith('See')
print line + " start with 's' is",line.startswith('s')


# Displays all String built-in functions
# Ignore the one with underscores, these are used by Python itself
print "\n#Displays all String built-in functions \n"
print dir("stringgg")

# Or you can see on https://docs.python.org/2/library/stdtypes.html#string-methods


## Exercise

# Text parsing: Extract host from email
print "\n#Text parsing: Extract host from email \n"
sentby = "From thibault.clem@etu.utc.com Sat Feb 07:15:56 2016"
atpos = sentby.find('@')
stpos = sentby.find(' ',atpos)
host = sentby[atpos+1:stpos]
print "host is "+host
