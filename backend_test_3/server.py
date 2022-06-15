import socket
import therading


HOST = "127.0.0.1"
PORT = 69420
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
    
connections = []

def bradcast_ip(ip):
    global connections
    for connection in connections:
        connection.send("ip".encode("utf-8"))
        if connectios.recv(1024).decode("utf-8") == "OK":
            connection.send(ip)


