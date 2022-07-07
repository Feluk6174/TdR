import mysql.connector, threading


def connect():
        connection = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            password = "root",
            database = "TdR"
        )
        return connection

def querry(querry:str): 
    print("t1")
    connection = connect()
    while True:
        print("t2")
        try:
            print("t3")
            cursor = connection.cursor()
            print("t3.1")
            cursor.execute(querry)
            print("3.2")
            connection.close()
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print("t4")
            print(f"[ERROR]({threading.current_thread().name})", e)
            connect()
    connection.close()

def execute(sql:str):
    connection = connect()
    while True:
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            break
        except mysql.connector.Error as e:
            print(f"[ERROR]{threading.current_thread().name}", e)
            connect()
    connection.close()


def create():
    with thread_lock:
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS comments;")
        cursor.execute("DROP TABLE IF EXISTS posts;")
        cursor.execute("DROP TABLE IF EXISTS users;")

        cursor.execute("CREATE TABLE users(id INT NOT NULL PRIMARY KEY, user_name VARCHAR(16) NOT NULL UNIQUE, public_key INT NOT NULL UNIQUE, info VARCHAR(255));")
        cursor.execute("CREATE TABLE posts(id INT NOT NULL PRIMARY KEY, user_id INT NOT NULL, post VARCHAR(255) NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id));")
        cursor.execute("CREATE TABLE comments(id INT NOT NULL PRIMARY KEY, user_id INT NOT NULL, post_id INT NOT NULL, comment VARCHAR(255) NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id), FOREIGN KEY (post_id) REFERENCES posts (id));")

   
        cursor.execute("DROP TABLE IF EXISTS ips;")
        cursor.execute("DROP TABLE IF EXISTS connected_ips;")

        cursor.execute("CREATE TABLE ips(ip VARCHAR(21) NOT NULL PRIMARY KEY, time_connected INT NOT NULL);")
        cursor.execute("CREATE TABLE connected_ips(ip VARCHAR(21) NOT NULL PRIMARY KEY, time_connected INT NOT NULL);")

        connection.commit()
    connection.close()


if __name__ == "__main__":
    connection = connect()
    create(connection)
