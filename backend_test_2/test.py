import sqlite3
import database
import random
import time

database.create_ip()

num = int(input("Numer of entries: "))

connection = sqlite3.connect("ip_db.db")
cursor = connection.cursor()

for i in range(num):
    sql = f"INSERT INTO ips(ip, time_connected) VALUES('{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0, 255)}:{random.randint(10000, 70000)}', {time.time()})"
    print(sql)
    connection.execute(sql)


connection.commit()
connection.close()
