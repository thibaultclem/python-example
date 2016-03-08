## File processing

# Take a look to built-in fucntions:
# https://docs.python.org/2.7/library/functions.html

# Opening a file
# open() returns a handle use to manipulate the file
# mode (optional): 'r' to read a file, 'w' to write to the file
handle = open('mbox.txt','r')
# handle is not all data but a connection to the data to perform operation on
print handle

# Iterate on each line: use for statement
xfile = open('mbox-short.txt','r')
for line in xfile:
    print line

# Counting line
xfile = open('mbox.txt','r')
countLine = 0
for line in xfile:
    countLine = countLine + 1
print countLine,"lines in the file"

# Reading the all file: read() returns a String
xfile = open('mbox-short.txt','r')
inp = xfile.read()
print len(inp)," lines in the file"
print inp[:50]

# Searching in a file (print only sentence starting with 'From')
xfile = open('mbox-short.txt')
for line in xfile:
    if line.startswith('From'):
        print line
# ! The print statement adds a new line to each line and each line from the file
#also has a newline at the end

# Stripe the whitespaces/newline from the right hand side using rstrip()
xfile = open('mbox-short.txt')
for line in xfile:
    line = line.rstrip()
    if line.startswith('From'):
        print line

# Using in to select line
xfile = open('mbox-short.txt')
for line in xfile:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print line

# Prompt for File name
fname = raw_input("Enter the file name (use mbox-short.txt): " )
try:
    fhand = open(fname)
except:
    print "Cannot open file: ",fname
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print "There were",count,"subject lines in",fname


# The newline characters: \n
stuff = "X\nY"
print stuff
print len(stuff)
