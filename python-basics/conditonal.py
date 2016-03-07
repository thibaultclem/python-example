## Comparaison operator

# Same as Java: == for equality, != for not equal, >, <, >=, <=
if 2 == 2:
    print "2 == 2"
if 2 != 3:
    print "2 != 3"


## Indentation

# Python uses indentation as syntaxically significient
# Increase indent after if or for (after ":")
if 1 == 2:
    print "Part of the if"
    print "Still part of the if"
print "Not part of the if"
print "Start loop"
for i in range(5):
    print i
    if i > 2:
        print "Bigger than 2"
    print "Done with i",i
print "Done with loop"
# ! Never turn tabs into spaces in your text editor when writing python code ;)


## Conditional way
x = 5

# One-way: if
if x > 1:
    print "Bigger than 1"

# Two-way: else
if x < 1:
    print "Little than 1"
else:
    print "Bigger than 1"

## Multi-way: elif
if x < 2:
    print "Little"
elif x < 4:
    print "Medium"
else:
    print "Big"
