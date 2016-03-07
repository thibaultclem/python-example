
## Indefinitie loops: while

# While loops
n = 5
while n > 0:
    print n
    n = n-1
print "finish while"
print n

## Definite loops: for

# For loops
for i in [1,2,3,4,5]:
    print i
print "finish for"

friends = ['rinam','max','guigui']
for friend in friends:
    print "Hello ",friend
print "I said hello to all my friend"

## "break" statement: Breaking out of Loop

# example with 'break'
text = ""
while True:
    line = raw_input("Type text (enter 'done' to quit): ")
    if line == 'done':
        break
    text = text+" "+line
print text


## "continue" statement: end the current iteration and start the next

# example with 'continue'
text = ""
while True:
    line = raw_input("Type text (enter 'done' to quit): ")
    # Don't store line starting with '#'
    if line[0] == '#':
        continue
    if line == 'done':
        break
    text = text+" "+line
    print line
print text


## 'None' and the 'is' and 'is not' Operators
# Use 'is' for checking None. 'is' is stringer than '=='

# Looking for the smallest value in a list
smallest = None
for value in [23,1,76,54,67,78,3,34]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print "smallest value is ",smallest

## Variable in loops

# Find the average in a loop
count = 0
sum = 0
for value in [23,1,76,54,67,78,3,34]:
    count = count + 1
    sum = sum + value
avg = sum / count
print "Average =",avg
