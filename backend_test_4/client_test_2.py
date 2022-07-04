import socket

HOST = "127.0.0.1"
PORT = int(input("Server port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send("0".encode("utf-8"))

while True:
    res = client.recv(1028).decode("utf-8")
    print(res+"\n")
    #client.send("hello world".encode("utf-8"))
