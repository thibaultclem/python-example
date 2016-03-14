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


# This application will read an iTunes export file in XML and produce a
# properly normalized database
import sqlite3
import xml.etree.ElementTree as ET

# Connect to database
conn = sqlite3.connect('database/itunes.sqlite')
cur = conn.cursor()

# Drop tables if already exist
cur.executescript('''
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Artist;
''')

# Create the tables
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Insert xml from file 'Library.xml'
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'file/Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
for entry in all:
    # Chek if the entry is a Track
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    # Check that name / artist / album is not NULL
    if name is None or artist is None or album is None or genre is None :
        continue

    print name, artist, album, genre, count, rating, length

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
