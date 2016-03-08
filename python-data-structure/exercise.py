# Write a program that prompts for a file name, then opens that file and reads
#through the file, and print the contents of the file in upper case.
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
f = fh.read()
fup = f.upper()
print fup.rstrip()

# Write a program that prompts for a file name, then opens that file and reads
#through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
count = 0
total = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    s = line.find(':')
    value = float(line[s+1:])
    total = total + value
avg = total/count
print "Average spam confidence:",avg


# List and split
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print 'day =',words[2]


# Open the file romeo.txt and read it line by line. For each line, split the
#line into a list of words using the split() method. The program should build a
#list of words. For each word on each line check to see if the word is already
#in the list and if not append it to the list. When the program completes, sort
#and print the resulting words in alphabetical order.
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    words = line.split()
    for word in words:
        if word in lst: continue
        lst.append(word)
lst.sort()
print lst

# Open the file mbox-short.txt and read it line by line. When you find a line
#that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in
#the line (i.e. the entire address of the person who sent the message). Then
#print out a count at the end.
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "): continue
    count = count +1
    words = line.split()
    print words[1]
print "There were", count, "lines in the file with From as the first word"
