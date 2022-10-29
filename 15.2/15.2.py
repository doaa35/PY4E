import sqlite3 as sq

conn = sq.connect('org.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts ')
cur.execute('CREATE TABLE Counts  (org TEXT, count INTEGER)')

file = open('mbox.txt')

for line in file:
    if not line.startswith('From: '): continue
    slice = line.split()[1]
    # org = ' '
    if '@' in slice:
        index = slice.index('@')
        org = slice[index+1:]
    
    cur.execute('SELECT count FROM Counts  WHERE org = ?', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts  (org, count) VALUES (?, 1)', (org,))

    else:
        cur.execute('UPDATE Counts  SET count = count +1 WHERE org = ?', (org,))

conn.commit()

data = 'SELECT org, count FROM Counts  ORDER BY count DESC LIMIT 10'

for record in cur.execute(data):
    print(record[0], record[1])

cur.close()