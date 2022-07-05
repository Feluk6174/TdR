import database

ports = [11111, 22222, 33333, 44444]

db = database.connection()
db.create()

#db.execute(f"INSERT INTO ips(ip, time_connected) VALUES({ip}, {time.time()});")
