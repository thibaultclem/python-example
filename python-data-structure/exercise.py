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
