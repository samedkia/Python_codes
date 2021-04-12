import sqlite3
conn = sqlite3.connect('DBemails.sqlite')
cur = conn.cursor()

# Creating table
cur.execute('DROP TABLE IF EXISTS counts')
cur.execute('CREATE TABLE counts (org TEXT, count INTEGER)')

# Extracting emails
fname = input('enter file: ')
if len(fname) < 1 :
    fname = mbox.txt
fh = open(fname)
for line in fh:
    line.rstrip()
    if line.startswith('From:'):
        piecess = line.split()
        pieces = piecess[1].split('@')
        email = pieces[1]
        cur.execute('SELECT count FROM counts WHERE org = ?', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO counts (org, count) VALUES (?, 1)', (email,))
        else:
            cur.execute('UPDATE counts SET count = count+1 WHERE org = ?', (email,))

    cur.execute('SELECT org, count FROM counts ORDER BY count DESC')
conn.commit()
cur.close()
