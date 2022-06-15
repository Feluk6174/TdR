import sqlite3, asyncio

def querry(command:str, db:str):
	connection = sqlite3.connect(db)
	cursor = connection.cursor()

	cursor.execute(command)

	connection.commit()
	connection.close()


def create():
	#Conects to database drops the tables if they exists and it creates them

	connection = sqlite3.connect("db.db")
	cursor = connection.cursor()

	cursor.execute("DROP TABLE IF EXISTS users;")
	cursor.execute("DROP TABLE IF EXISTS posts;")
	cursor.execute("DROP TABLE IF EXISTS coments;")

	cursor.execute("CREATE TABLE users(id INTEGER NOT NULL PRIMARY KEY, user_name TEXT NOT NULL UNIQUE, public_key INTEGER NOT NULL UNIQUE, info TEXT)WITHOUT ROWID;")
	cursor.execute("CREATE TABLE posts(id INTEGER NOT NULL PRIMARY KEY, user_id INTEGER NOT NULL, post TEXT NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id))WITHOUT ROWID;")
	cursor.execute("CREATE TABLE coments(id INTEGER NOT NULL PRIMARY KEY, user_id INTEGER NOT NULL, post_id INTEGER NOT NULL, comment TEXT NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id), FOREIGN KEY (post_id) REFERENCES posts (id))WITHOUT ROWID;")

	connection.commit()
	connection.close()

def create_ip():
	connection = sqlite3.connect("ip_db.db")
	cursor = connection.cursor()

	cursor.execute("DROP TABLE IF EXISTS ips;")
	cursor.execute("DROP TABLE IF EXISTS conected;")

	cursor.execute("CREATE TABLE ips(ip TEXT NOT NULL PRIMARY KEY, time_conected INTEGER NOT NULL);")
	cursor.execute("CREATE TABLE conected(ip TEXT NOT NULL PRIMARY KEY, time_conected INTEGER NOT NULL);")

	connection.commit()
	connection.close()