import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("195.181.244.246", 6969))

msg = input("msg: ")

while True:
    connection.send(msg.encode("utf-8"))

    print(len(msg))
