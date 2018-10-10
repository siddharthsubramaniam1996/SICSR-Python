import sqlite3

print ("Siddharth Subramaniam's program for /etc/passwd reader using sqlite3")
print ("Sent on Fourth October 2018")

f=open('/etc/passwd','r')

db = sqlite3.connect('myusers.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE if not exists user(userid TEXT, passwd TEXT, uid TEXT,gid TEXT ,generic_desc TEXT,homedirectory TEXT,shell TEXT)")
for line in f:
	data =line.split(":")
	cursor.execute('INSERT INTO user VALUES (?,?,?,?,?,?,?)', data)
cursor = cursor.execute("select * from user")
for row in cursor:
	print(row)
