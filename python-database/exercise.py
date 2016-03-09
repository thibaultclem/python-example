# This application will read the mailbox data (mbox.txt) count up the number
# email messages per organization (i.e. domain name of the email address) using
# a database with the following schema to maintain the counts.
# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database file
# above for grading.
# If you run the program multiple times in testing or with dfferent files, make
# sure to empty out the data before each run.
import sqlite3
import re

# Connect to database
conn = sqlite3.connect('database/exercise1.sqlite')
cur = conn.cursor()

# Drop table if already exist
cur.execute('''
DROP TABLE IF EXISTS Counts''')

# Create the table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Insert org from file 'mbox.txt'
fh = open("file/mbox.txt")

for line in fh:
    if not line.startswith("From "): continue
    org = re.findall('@(\S+)',line)[0]
    cur.execute('SELECT count FROM Counts WHERE org=? ',(org, ))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ? ',(org, ))
    except:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)',(org, ))
    conn.commit()

query = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in conn.execute(query):
    print row[0],row[1]

cur.close()
