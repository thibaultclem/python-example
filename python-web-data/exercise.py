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
