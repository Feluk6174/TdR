import database as db

connection = db.connection()

res = connection.querry("SELECT ip FROM ips ORDER BY RAND() LIMIT 1;")

ip = res[0][0].split(":")

host = (ip[0], int(ip[1]))

print(host, ip)
