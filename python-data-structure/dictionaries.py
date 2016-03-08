
## What's a Dictionary ?

# Dictionaries are python's most powerful data collection
# Collection is a bunch of values in a single variable:
# List is a linear collections of values that stay in order
# Dictionary is a "bag" of values, each with its own label
# Dictionary is a key/value structure equivalent to Properties or Map in Java
purse = dict()
purse['money'] = 16
purse['candy'] = 7
purse['tissue'] = 10
print purse
print purse['candy']
purse['candy'] = purse['candy'] + 2
print purse


## Dictionaries vs Lists

# dicitonaries are like list except that they use keys instead of numbers to
#look up value and do not maintain order

# Lists
lst = list()
lst.append(18)
lst.append(182)
print lst #[18, 182]

# Dictionaries
dty = dict()
dty['age'] = 18
dty['course'] = 182
print dty # {'course': 182, 'age': 18}


## Dictionary literals (Constants

# Dictionary literals use curly braces and have a list of key:value paris
dd = {'bob':1,'max':2,'marine':3}
print dd
dd['other'] = 5
print dd

# Empty Dictionary
dde = {}
print dde


## Get a value in a Dictionary

# in
counts = dict()
names = ['thib','max','marine','thib']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts [name] + 1
print counts

# get()
dd = {'bob':1,'max':2,'marine':3}
print dd.get('max')

# get() with default value if key not exist
dd = {'bob':1,'max':2,'marine':3}
print dd.get('john',0)

# get better than in :)
counts = dict()
names = ['thib','max','marine','thib']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts


## Loop on dicitonaries

# Print key/values
dd = {'bob':1,'max':2,'marine':3}
for key in dd:
    print key,dd[key]


## Retrieving list from Dictionaries
dd = {'bob':1,'max':2,'marine':3}

# list of keys
print dd.keys()

# list of values
print dd.values()

# list of tuples
print dd.items()


## Two iterations variables (using tuples)
dd = {'bob':1,'max':2,'marine':3}
for key,value in dd.items():
    print key,value
