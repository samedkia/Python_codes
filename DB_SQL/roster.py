import json
import sqlite3

conn = sqlite3.connect('coursedb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member
''')

cur.executescript('''
    CREATE TABLE User (
        id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Course (
        id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title   TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id    INTEGER,
        course_id  INTEGER,
        role       INTEGER,
        PRIMARY KEY(user_id, course_id)
    )
''')

# opening json file
fname = input('enter file: ')
if len(fname) < 1 : fname = roster_data.json

kh = open(fname)
data = kh.read()
js = json.loads(data)
for row in js:
    nam = row[0]
    tit = row[1]
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (nam, ) )
    cur.execute('''SELECT id FROM User WHERE name = ?''', (nam,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (tit, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (tit, ))
    course_id = cur.fetchone()[0]

    rol = row[2]
    cur.execute('''INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''', (user_id, course_id, rol))
conn.commit()
