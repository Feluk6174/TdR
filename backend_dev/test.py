import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
HOST = s.getsockname()[0]
s.close()

PORT = 6969

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"running on {HOST}:{PORT}")

conn, addr = server.accept()

while True:
    num = int(conn.recv(1024).decode("utf-8"))
    conn.send("OK".encode("utf-8"))
    msg = ""
    for i in range(num):
        msg += conn.recv(1024).decode("utf-8")
        conn.send("OK".encode("utf-8"))


    print(msg)
    print(len(msg))