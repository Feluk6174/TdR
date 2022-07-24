import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
HOST = s.getsockname()[0]
s.close()

PORT = 6969

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

conn, addr = server.accept()

temp = []

while True:
    msg = conn.recv(4096).decode("utf-8")
    if len(msg) == 0:
        break
    temp.append(msg)
    print(msg)
    print(len(msg))