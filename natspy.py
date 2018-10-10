import sqlite3
f=open('/etc/passwd','r')

db = sqlite3.connect('myusers.db')
cursor = db.cursor()
# cursor.execute('''
#     CREATE TABLE users(userid INTEGER PRIMARY KEY, passwd TEXT,
#                        uid TEXT,gid  TEXT ,generic_desc TEXT,homedirectory TEXT,shell TEXT)
# ''')
for i in f:
    rows=i.split(':')
    print(rows)
    userid=rows[0]
    passwd = rows[1]
    uid = rows[2]
    gid = rows[3]
    generic_desc = rows[4]
    homedirectory = rows[5]
    shell=rows[6]
# cursor.execute('''INSERT INTO users(userid, passwd, uid, gid,generic_desc,homedirectory,shell)
                  # VALUES(?,?,?,?,?,?,?)''', (userid,passwd, uid, gid,generic_desc,homedirectory,shell))

# db.commit()