## Sockets in python

# Python has built-in support for TCP Sockets
# Just import socket package
import socket


## Communicate with web server

# Connect to server
# AF_NET: internet Socket
# SOCK_STREAM: stream socket -> send and give me back datas
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Keep a connection between me and www.py4inf.com:80
mysock.connect( ('www.py4inf.com', 80) )

# Send a request to server
mysock.send("GET http://www.pythonlearn.com/code/intro-short.txt HTTP 1.0\n\n")

# Get data
while True:
    #Get data 512 characters by 512 characters
    data = mysock.recv(512)
    #Check if I receive all data (if true break)
    if ( len(data) < 1 ):
        break
    print data

# Close the connection to the server
mysock.close()


## Making HTTP easier with urllib
# urllib make url look like files
import urllib

# GET
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# Return only the body
for line in fhand:
    print line.strip()
