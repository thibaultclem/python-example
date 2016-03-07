## The try / except structure

# You surround a dangerous section of code with try
# If the code in the try fails it jumps to the except section
# Example:
integer = 2
string = "my String"
try:
    # This will trigger an error:
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    concat = integer+string
except Exception as e:
    print "Error catched"
    print "The exception is: ",e

# Useful for user input
rawstr = raw_input("Enter a number: ")
try:
    nbr = int(rawstr)
except:
    nbr = -1

if nbr > 0:
    print "Nice work"
else:
    print "Not a number"
