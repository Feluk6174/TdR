import socket
import time

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("195.181.244.246", 6969))

msg = input("msg: ")

msg_len = len(msg)

num = int(msg_len/1024)
num = num + 1 if not msg_len % 1024 == 0 else num

while True:
    connection.send(str(num).encode("utf-8"))

    temp = connection.recv(1024).decode("utf-8")
    if not temp == "OK":
        print(temp)
    #string[start:end:step]

    for i in range(num):
        print(i)
        connection.send(msg[1024*i:1024*i+1024].encode("utf-8"))
        temp = connection.recv(1024).decode("utf-8")
        if not temp == "OK":
            print(temp)


    print(msg_len, num)

connection.close()