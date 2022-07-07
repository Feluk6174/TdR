import mysql.connector

class connection():
    def __init__(self, thread_lock):
        self.thread_lock = thread_lock
        self.connect()


    def connect(self):
        with self.thread_lock:
            self.connection = mysql.connector.connect(
                host = "localhost", 
                user = "root", 
                password = "root",
                database = "TdR"
            )

    def querry(self, querry:str):
        with self.thread_lock: 
            while True:
                try:
                    print("t")
                    cursor = self.connection.cursor()
                    cursor.execute(querry)
                    return cursor.fetchall()
                except mysql.connector.Error as e:
                    print("[ERROR]", e)
                    self.connect()

    def execute(self, sql:str):
        with self.thread_lock:
            while True:
                try:
                    cursor = self.connection.cursor()
                    cursor.execute(sql)
                    self.connection.commit()
                    break
                except mysql.connector.Error as e:
                    print("[ERROR]", e)
                    self.connect()


    def create(self):
        with self.thread_lock:
            cursor = self.connection.cursor()

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

            self.connection.commit()


if __name__ == "__main__":
    connection = connect()
    create(connection)
