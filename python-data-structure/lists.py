
## Lists is a Collection variable

# A Collection allows us to put many values in a single 'variable'
friends = ['bob','max','marine']

## List constants

# List constants are surronded by sqaure brackets and the elements in the List
#are separated by comms

# A list can be any Python object
print ['hello',12,3.89]

# Even another list
print ['hello',12,['other','list'],3.89]

# A list can be empty
print []


## Looking inside List

# Like list we can get any single element in a list using square brackets
friends = ['bob','max','marine']
print friends[1]


## List are Mutable (contrary to String)

# String are 'immutable': we cannot change the content of a String
# We must make a new string to make any change
str1 = "My String"
try:
    str1[2] = 'o'
except:
    print "String is immutable"

# List are 'mutable'
lst = [1,2,3,4,5]
lst[2] = 'CHANGE'
print lst


## Length of a list
lst = [1,2,3,4,5]
print len(lst)


## the 'range' function : returns a lisrt of numbers that range from zero to
#one less than the paramater
print range(5)


## Loop on List
friends = ['bob','max','marine']

for friend in friends:
    print 'Hello',friend

# with range
for i in range(len(friends)):
    print 'Hello',friends[i]


## Concatenating List

# Using '+' operator
a = [1,2,3]
b = [4,5,6]
c = a + b
print c


## Slices List

# like for string
a = [1,2,3,4,5,6]
print a[1:3]
print a[:4]
print a[:]


## Built-in functions for list

print dir([])
# take a look to https://docs.python.org/2/tutorial/datastructures.html

# building list from scratch
stuff = list()

# add element to list
stuff.append('new element')
stuff.append(3)
print stuff

# search in a list
friends = ['bob','max','marine']
print 'max' in friends

# sort a list
friends = ['bob','max','marine']
print friends
friends.sort()
print friends

# min and max in list
friends = ['bob','max','marine']
print max(friends)
print min(friends)

# sum in list
a = [1,2,3,4,5,6]
print sum(a)

# break a String to List: split()
hello = "Hello les loulous"
stuff = hello.split()
print stuff
print len(stuff)
print stuff[0]

# split with specific delimiter (by default whitespaqce)
str1 = "bob;max;marine"
friends = str1.split()
print friends
friends = str1.split(';')
print friends
