import auth
import sys
import socket
from Crypto.PublicKey import RSA

HOST = "127.0.0.1"
try:
    PORT = int(sys.argv[1])
except IndexError:
    PORT = int(input("Input port: "))
IP = HOST+":"+str(PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

connection, addr = server.accept()
pub_key = connection.recv(4096).decode("utf-8")
pub_key = RSA.import_key(auth.reconstruct_key(pub_key))

data = connection.recv(4096).decode("utf-8")

signature = connection.recv(4096).decode("utf-8")

print(pub_key)
print(data)
print(signature)

print(auth.verify(pub_key, signature, data))

print(pub_key)