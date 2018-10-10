import sqlite3
f=open('/etc/passwd','r')

db = sqlite3.connect('x.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE users(userid INTEGER PRIMARY KEY, passwd TEXT, uid TEXT, gid TEXT ,generic_desc TEXT, homedirectory TEXT, shell TEXT)''')
for i in f:
	rows=i.split(':')
	print(rows)
	#makeitastring = ''.join(map(str, i))
	
	userid=rows[0]
	print (userid)
	print("\n")
	
	passwd = rows[1]
	print(passwd)
	print("\n")
	
	uid = rows[2]
	print(uid)
	print("\n")
	
	gid = rows[3]
	print (gid)
	print("\n")
	
	generic_desc = rows[4]
	print (generic_desc)
	print("\n")
	
	homedirectory = rows[5]
	print (homedirectory)
	print("\n")
	
	shell=rows[6]
	print (shell)
	print("\n")
cursor.execute('''INSERT INTO users(userid, passwd, uid, gid, generic_desc, homedirectory, shell)
                  VALUES(?,?,?,?,?,?,?)''', (userid, passwd, uid, gid, generic_desc, homedirectory, shell))

db.commit()
