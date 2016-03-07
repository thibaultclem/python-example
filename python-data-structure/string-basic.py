# 
# Learn basics about String in Python
# 

# A String is a sequence of characters (can use simple or double quotes)
str1 = "Hello"
str2 = "MJ"

# Concatenate a String
concat = str1 + " " + str2
print concat

# Convert String to number
str3 = "22"
mj = int(str3) + 1
print mj

# Reading a String enter by user
name = raw_input("Enter your name: ")
print "Hello "+name

# Looking inside String
jordan = "jordan"
letter = jordan[1]
print "Second letter of " + jordan + " is " + letter

# Length of a String
lenghtJordan = len(jordan)

# Print mixed String and int
print "Length of " + jordan + " is",lenghtJordan

# Loop on String
index = 0
while index < len(jordan):
  letter = jordan[index]
  print letter
  index += 1

# More elegant loop on String
for letter in jordan:
  print letter
# Same as
for letter in "jordan":
  print letter

# Slicing String
s = "Monty Python"
print s[0:4]
print s[6:30]
print s[:3]
print s[3:]
print s[:]

# Using operator in to check if a string is present in a string
if 'n' in jordan:
  print "n in "+jordan
if 'an' in jordan:
  print "an in "+jordan
if 'ed' in jordan:
  print "ed in "+jordan
else:
  print "no ed in "+jordan

# String comparaison
if jordan == "jordan":
  print "Well done MJ"

if jordan < "magic":
  print jordan + " come before magic"
elif jordan > "magic":
  print jordan + " come after magic"
else:
  print jordan + " and magic are the same"
