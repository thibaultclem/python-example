## Function is a reusable pieces of code

# define the function
def hello():
    print "hello"
# Call the function
hello()
hello()


## Python functions

# Built-in function
type("string")
float(1)
# Personal function that we define ourselves (using the "def" reserved word)
def myFunction():
    print "I can do what I want"


## Function parameter/argument

# Function can have parameter
def hello(name):
    print "Hello "+name
# Passing argument to function
hello("thib")


## Funtion return

# function can return value
# A "fruitful" function is one that produces a result (or return value)
def bye():
    return "bye bye"
print bye(),"thib"

# When return call the function exit
def uselessLine():
    print "I'm a useful line (not really useful.. :) )"
    return
    print "I'm useless line because never used"
uselessLine()
