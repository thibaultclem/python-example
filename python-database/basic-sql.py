## SQLite is embedded in python
# Just need to import sqlite package
import sqlite3
import re

# Connect to database
conn = sqlite3.connect('database/emaildb.sqlite')
cur = conn.cursor()

# Drop table if already exist
cur.execute('''
DROP TABLE IF EXISTS Counts''')

# Create the table
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# Insert email from file
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "file/mbox-short.txt"
fh = open(fname)

for line in fh:
    if not line.startswith("From "): continue
    email = re.findall('\S+@\S+',line)[0]
    cur.execute('SELECT count FROM Counts WHERE email=? ',(email, ))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ? ',(email, ))
    except:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)',(email, ))
    conn.commit()

query = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in conn.execute(query):
    print row[0],row[1]

cur.close()
