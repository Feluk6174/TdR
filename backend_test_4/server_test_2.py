import socket
import threading
import database
import time
import sys
import json

HOST = "192.168.178.138"
try:
    PORT = int(sys.argv[1])
except IndexError:
    PORT = int(input("Input port: "))

IP = HOST+":"+str(PORT)

    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

db = database.connection()

connections = []

get_n_connected = lambda n: int(5*math.log2(n))
get_n_connected = lambda n: 3

server_info = json.loads("{"+f'"type": "NODE", "host": "{HOST}", "port": {PORT}, "ip": "{IP}"'+"}")

def broadcast_ip(ip:str):
    #broadcasts ip to all connections
    global conections

    print("broadcasting:", ip)
    for connection in connections:
        connection[2].send(("{"+f'"type": "IP", "ip": "{ip}"'+"}").encode("utf-8"))

def ip_manager(msg_info:str):
    global db, IP

    print("managing:", msg_info)
    
    ip = msg_info["ip"]

    if ip == IP:
        return

    seconds = 100
    db.execute(f"DELETE FROM ips WHERE time_connected <= {int(time.time()) - seconds}")
    res = db.querry(f"SELECT * FROM ips WHERE ip = '{ip}';")
    
    if len(res) == 0:
        db.execute(f"INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()});")
        broadcast_ip(ip)

def check_if_connected(ip:str):
    global connections
    for connection in connections:
        if connection[0] == ip:
            return True
    return False

def mainloop(connection, ip):
    global connections, HOST, PORT
    while True:
        try:
            msg_info = json.loads(connection.recv(1024).decode("utf-8"))
            
            print(msg_info)

            if msg_info["type"] == "IP":
                ip_manager(msg_info)

        except socket.error as e:
            print(e)
            connections.remove((ip, connection))
            break

def connect_to_new_node():
    global connections, IP, server_info
    while True:
        ip = db.querry("SELECT ip FROM ips ORDER BY RAND() LIMIT 1;")
        print(ip)
        if not check_if_connected(ip[0][0]):
            host, port = ip[0][0].split(":")
    
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((host, int(port)))

            connection.send(json.dumps(server_info).encode("utf-8"))

            if connection.recv(1024).decode("utf-8") == "OK":
                connections.append((ip[0][0], ip[0][0], connection))
                print(f"connected to {ip[0][0]}")
                thread = threading.Thread(target=mainloop, args=(connection, ip[0][0]))
                thread.start()
                break

        if len(db.querry("SELECT * FROM ips;")) <= len(connections):
            break

def manage_new_node(connection, address, conn_info):
    global connections, get_n_connected, db
    n_connected = len(connections)
    n_nodes = len(db.querry("SELECT * FROM ips;"))
    n_suposed_connections = get_n_connected(n_nodes)
    if n_connected < n_suposed_connections and not check_if_connected(address):
        difference = n_connected - n_suposed_connections
        connection.send("OK".encode("utf-8"))
        connections.append((conn_info["ip"], address, connection))
        print(f"connected by {address}", connections)
        thread = threading.Thread(target=mainloop, args=(connection, address))
        thread.start()

        if not difference == 1:
            for i in range(difference - 1):
                connect_to_new_node()

def ip_share_loop():
    global HOST, PORT, IP, connections
    time.sleep(10)
    connect_to_new_node()
    while True:
        print("num connecions: ", len(connections))
        print("connections:" )
        for connection in connections:
            print(f"    {connection[0]}")
        broadcast_ip(IP)

        time.sleep(60)

def main():
    global connections, server
    while True:
        connection, address = server.accept()
        conn_info = json.loads(connection.recv(1024).decode("utf-8"))
        print(conn_info)

        if conn_info["type"] == "NODE":
            manage_new_node(connection, address, conn_info)

if __name__ == "__main__":    
    thread = threading.Thread(target=ip_share_loop)
    thread.start()
    main()
