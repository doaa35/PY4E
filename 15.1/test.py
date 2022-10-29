import sqlite3 as sq
# open connecrion
conn = sq.connect('test.sqlite')
# cursor help me to handle the code(add, delete, create, etc...)
cur = conn.cursor()

#tell the file be careful you will have table called <<user>> soon 
cur.execute('DROP TABLE IF EXISTS user')

# create table
cur.execute('CREATE TABLE user (email TEXT, count INTEGER)')

# extract data from file
file = input('ente file name: ')

# check the file
if len(file)<1: file = 'mbox-short.txt'
openFile = open(file)

for line in openFile:
    if not line.startswith('From: '): continue
    # convert it into list
    slice = line.split()
    email = slice[1]
    # >>> (email, ) becouse there is no need for the another param
    # read the data if already exist
    cur.execute('SELECT count FROM user WHERE email = ?',(email,))

    # add record or fetch record
    row = cur.fetchone()

    # if data not exist
    if row is None:
        # if email added to the first time >> count is one :0
        cur.execute('INSERT INTO user (email, count) VALUES (?, 1)', (email,))

    # if the data is already exist updata the count
    else:
        cur.execute('UPDATE user SET count = count +1 WHERE email = ?', (email,))


# if i didn't add these 2 lines >>> no changes gonna happen
# conn.commit()
# cur.close()

# commit first to write data
conn.commit()

sqlstr = 'SELECT email, count FROM user ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])


cur.close()



