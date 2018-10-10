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
	x = str(rows).strip('[]')
	print (x)
#	print (type(x))


    
