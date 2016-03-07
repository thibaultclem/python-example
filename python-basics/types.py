## Types matters

# In python variables, literals and constants have "type"
# You can ask python what type something is by using type()
print type("this is a string")

# operators function can change following the type
# "+" means addition for integer
print 2 + 2
# "+" means concatenation for string
print "hello "+"World"g
# "*" means multiplication for integer
print 2 * 2
# "*" means multiple concatenation for string
print "hello "*5


## Numbers Types

# Numbers have two mains Types
# Integer
print type(2)
# Floating point numbers
print type(2.0)
# There are anothers numbers types (variations on float and integer)


## Conversions

# Number type conversion using built in functionss float() and int()
print float(2)
print int(2.6)

# String conversions to float or integer
print type(float("2.5"))
print type(int("2"))


## User input

# Read data from the user using raw_input function (return a string)
name = raw_input("Who are you ? ")
print "Welcome "+name
print type(name)

# Read data from the user using input() (equivalent to eval(raw_input()))
userinput = input("Enter something (use quotes for string): ")
print type(userinput)
# same as:
userinput2 = eval(raw_input("Enter something (use quotes for string): "))
print type(userinput2)
