import mysql.connector
import random
import threading
import time

def is_safe(*args):
    invalid_chars = ["\\", "\'", "\"", "\n", "\t", "\r", "\0", "%", "\b", ";", "="]

    arguments = ""
    for argument in args:
        arguments += argument

    for char in invalid_chars:
        if char in arguments:
            print("[ERROR] Invalid char ", char)
            return False
    return True


class Database():
    def __init__(self):
        self.connect()
        self.queue = []
        self.return_response = []
        thread = threading.Thread(target=self.proces_queue)
        thread.start()

    def connect(self):
        self.connection = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            password = "root",
            database = "TdR"
        )

    def stop(self):
        queue_id = random.randint(1000000000, 9999999999)
        self.queue.append(("s", "stop", queue_id))

    def querry(self, querry:str):
        queue_id = random.randint(1000000000, 9999999999)
        self.queue.append(("q", querry, queue_id))
        while True:
            for response in self.return_response:
                if response[0] == queue_id:
                    self.return_response.remove((queue_id, response[1]))
                    return response[1]


    def execute(self, sql:str):
        queue_id = random.randint(1000000000, 9999999999)
        self.queue.append(("e", sql, queue_id))
        while True:
            for response in self.return_response:
                if response[0] == queue_id:
                    self.return_response.remove((queue_id, response[1]))
                    return 

    def proces_queue(self):
        print("[STARTED QUEUE PROCESOR]")
        while True:
            if len(self.queue) > 0:
                if self.queue[0][0] == "q":
                    try:
                        cursor = self.connection.cursor()
                        cursor.execute(self.queue[0][1])
                        self.return_response.append((self.queue[0][2], cursor.fetchall()))

                    except mysql.connector.Error as e:
                        print(f"[ERROR]({threading.current_thread().name})", e)
                        self.connect()
                        self.return_response.append((self.queue[0][2], "ERROR"))

                elif self.queue[0][0] == "e":
                    try:
                        cursor = self.connection.cursor()
                        cursor.execute(self.queue[0][1])
                        self.connection.commit()
                        self.return_response.append((self.queue[0][2], None))
                        
                    except mysql.connector.Error as e:
                        print(f"[ERROR]{threading.current_thread().name}", e)
                        self.connect()
                        self.return_response.append((self.queue[0][2], "ERROR"))
                
                elif self.queue[0][0] == "s":
                    self.queue.pop(0)
                    break

                self.queue.pop(0)
            time.sleep(0.1)


    def create(self):
        cursor = self.connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS posts;")
        cursor.execute("DROP TABLE IF EXISTS users;")

        cursor.execute("CREATE TABLE users(user_name VARCHAR(16) NOT NULL UNIQUE PRIMARY KEY, public_key VARCHAR(392) NOT NULL UNIQUE, key_file VARCHAR(1764) NOT NULL UNIQUE, time_created INT NOT NULL, profile_picture VARCHAR(64) NOT NULL, info VARCHAR(255));")
        cursor.execute("CREATE TABLE posts(id VARCHAR(23) NOT NULL PRIMARY KEY, user_id VARCHAR(16) NOT NULL, post VARCHAR(255) NOT NULL, flags VARCHAR(10) NOT NULL, time_posted INT NOT NULL, FOREIGN KEY (user_id) REFERENCES users (user_name), signature VARCHAR(344));")
    
        cursor.execute("DROP TABLE IF EXISTS ips;")
        cursor.execute("DROP TABLE IF EXISTS connected_ips;")

        cursor.execute("CREATE TABLE ips(ip VARCHAR(21) NOT NULL PRIMARY KEY, time_connected INT NOT NULL);")
        cursor.execute("CREATE TABLE connected_ips(ip VARCHAR(21) NOT NULL PRIMARY KEY, time_connected INT NOT NULL);")

        self.connection.commit()
