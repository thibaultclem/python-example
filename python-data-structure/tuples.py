
## What's tuples

# Tuples are like list. They ahve elements which are indexed starting at 0
x = ('thib','max','marine')
print x[2]
# but contrary to Lists, Tuples are immutable (like Strings)
try:
    x[2] = 'john'
except:
    print "Tuple are immutable"
# So you cannot sort, append or reverse tuples
# You can only count() or index()
print dir(tuple())

## Tuples are more efficient

# Tuples are simpler and more efficient in terms of memory use and performance
# than Lists
# So when we are making "temporary variables" we prefer Tuples over Lists


## Tuples and Assignement

(x, y) = (4, 'fred')
print y
a, b = (99, 98)
print a
c, d = "to", "ti"
print c


## Tuples and dictionaries

# items() method on dictionaries return a list of (key,value) tuples
dic = {'bob':1,'max':2,'marine':3}
tups = dic.items()
print tups

# Reverse a dictionary in a list of tuples. Return a list of (value,key) tuples
lst = [(v,k) for k,v in dic.items()]
print lst

## Tuples are comparable

# compare list of Tuples
print (0, 1, 2) < (5, 1, 2) #true
print (0, 1, 2666778) < (0, 2, 3) #true
print (2, 1, 2) < (1, 14567865, 2458765) #false


## List of tuples can be sorted (Tuples cannot be sorted -> immutable)

# sort a list of Tuples by key
dic = {'bob':1,'max':2,'marine':3}
tups = dic.items()
print tups
tups.sort()
print tups

# directly using sorted() (still by key)
dic = {'bob':1,'max':2,'marine':3}
tups = sorted(dic.items())
print tups

# sorted() used in a loop (still by key)
dic = {'bob':1,'max':2,'marine':3}
for k,v in sorted(dic.items()):
    print k,v

# Sort by values (by reversing order of key and values in a list)
dic = {'bob':5,'max':2,'marine':3}
tmp = list()
for k,v in dic.items():
    tmp.append((v,k))
print tmp
tmp.sort()
print tmp

# Or shorter :)
dic = {'bob':5,'max':2,'marine':3}
print sorted([(v,k) for k,v in dic.items()])

# Sort in reverse order
dic = {'bob':1,'max':2,'marine':3}
for k,v in sorted(dic.items(),reverse=True):
    print k,v
