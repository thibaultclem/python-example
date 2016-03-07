## Constant and Variable

# Constant: Fixed value such as numbers, letters, and strings
print "this is a constant"

# Variable: Named place in the memory where programmer can store / retrieve
#data using the variable "name"
myvariable = 5
print myvariable
# It's possible to change the contents of a variable in later statement:
myvariable = "test"
print myvariable


## Python variable name and rules:

#- Start with a letter or underscore
#- Consist of letters and numbers and underscore
#- Case sensitive
#- Can not use reserved words: del, for, and, ...


## Sentences or Lines

# Assignement statement:
x = 2
# Assignement with expression:
x = x + 2
# Print statement:
print x


## Numeric expression

# Exponentiation / power
print 2**4
# Remainder / modulo
print 23%5

# Order of Evaluation:
#parenthesis -> power -> multiplication -> addition -> left to right

# Python divison is weird.. (this will change in Python 3.0)
# Integer divison truncates: 9/2 = 4
print 9/2
print 9.0/2
# Floating point divison produces floating point numbers
print 4.0/2
