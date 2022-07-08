import test
import threading
import random
import time

db = test.database()

thread = threading.Thread(target=db.proces_queue)
thread.start()

def lol():
    for i in range(1111, 9999):
        db.querry(f"INSERT INTO ips(ip, time_connected) VALUES('111.111.111.111:{i}', 10);")
        if random.randint(0,1) == 1:
            db.querry(f"DELETE FROM ips WHERE ip = '111.111.111.111:{i}'")
        print(f"[{time.asctime()}]({threading.current_thread().name})", db.querry("SELECT * FROM ips"))

for _ in range(10):
    thread = threading.Thread(target=lol)
    thread.start()
