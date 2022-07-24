import socket
import time

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("195.181.244.246", 6969))

msg = input("msg: ")

while True:
    connection.sendall(msg.encode("utf-8"))

    print(len(msg))

    msg = connection.recv(4096).decode("utf-8")

    if not msg == "ok":
        break
    else:
        print("[ERROR]", msg)
