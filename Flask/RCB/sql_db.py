import sqlite3
import bcrypt

def create_db():
	conn = sqlite3.connect('usersdb.db')
	cur = conn.cursor()
	cur.execute('''	CREATE TABLE IF NOT EXISTS User (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
									    email varchar(255) NOT NULL,
									    password varchar(255),
									    age int)''')
	conn.commit()
	conn.close()
 	

def enter_to_db(email, password, age):
	conn = sqlite3.connect('usersdb.db')
	cur = conn.cursor()
	cur.execute('SELECT email FROM User WHERE email = ? ', (email,))
	row = cur.fetchone()
	if row is None:
	    cur.execute('''INSERT INTO User (email, password, age) VALUES (?, ?, ?)''', (email, password, age))
	    conn.commit()
	    conn.close()
	    return (True, "Registered Successfully")
	else:
		conn.commit()
		conn.close()
		return (False,"email already exists!!")
	
def check_if_exist(email, password):
	conn = sqlite3.connect('usersdb.db')
	cur = conn.cursor()
	cur.execute('SELECT email FROM User WHERE email = ? ', (email,))
	row = cur.fetchone()
	if row is None:
		conn.commit()
		conn.close()
		return(False,"This mail is not registered")
	else:
		cur.execute('SELECT password FROM User WHERE email = ? ', (email,))
		password_r = cur.fetchone()[0]
		conn.commit()
		conn.close()
		if bcrypt.checkpw(password.encode(), password_r):
			return (True, "You were successfully logged in")
		else:
			return (False, "Please check the email/password")