import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("195.181.244.246", 6969))

msg = input("msg: ")

connection.send(msg.encode("uft-8"))

print(len(msg))
