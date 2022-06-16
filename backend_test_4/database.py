import mysql.connector

def connect():
    connection = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            password = "root",
            database = "TdR"
    )
    return connection

def querry(connection:mysql.connector.connection_cext.CMySQLConnection, querry:str):
    cursor = connection.cursor()
    cursor.execute(querry)
    return cursor.fetchall()

def execute(connection:mysql.connector.connection_cext.CMySQLConnection, sql:str):
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

def create(connection:mysql.connector.connection_cext.CMySQLConnection):
    cursor = connection.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS comments;")
    cursor.execute("DROP TABLE IF EXISTS posts;")
    cursor.execute("DROP TABLE IF EXISTS users;")

    cursor.execute("CREATE TABLE users(id INT NOT NULL PRIMARY KEY, user_name VARCHAR(16) NOT NULL UNIQUE, public_key INT NOT NULL UNIQUE, info VARCHAR(255));")
    cursor.execute("CREATE TABLE posts(id INT NOT NULL PRIMARY KEY, user_id INT NOT NULL, post VARCHAR(255) NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id));")
    cursor.execute("CREATE TABLE comments(id INT NOT NULL PRIMARY KEY, user_id INT NOT NULL, post_id INT NOT NULL, comment VARCHAR(255) NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id), FOREIGN KEY (post_id) REFERENCES posts (id));")

   
    cursor.execute("DROP TABLE IF EXISTS ips;")
    cursor.execute("DROP TABLE IF EXISTS connected;")

    cursor.execute("CREATE TABLE ips(ip VARCHAR(21) NOT NULL PRIMARY KEY, time_connected INT NOT NULL, id INT AUTO_INCREMENT);")
    cursor.execute("CREATE TABLE connected_ips(ip VARCHAR(21) NOT NULL PRIMARY KEY, time_connected INT NOT NULL);")

    connection.commit()


if __name__ == "__main__":
    connection = connect()
    create(connection)
