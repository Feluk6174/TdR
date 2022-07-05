import socket
import threading
import database
import time

HOST = "127.0.0.1"
PORT = int(input("Input port: "))
PORT = 42069

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

db = database.connection()

connections = []

get_n_connected = lambda n: int(5*math.log2(n))
get_n_connected = lambda n: 2

def broadcast_ip(ip:str):
    #broadcasts ip to all connections
    global conections
    for connection in connections:
        connection.send("IP")
        data = connection.recv(1024).decode("utf-8")
        if data == "OK":
            connection.send(ip.encode("utf-8"))

def ip_manager(ip:str):
    global db
    seconds = 60
    db.execute(f"DELETE FROM ips WHERE time_connected <= {int(time.time()) - seconds}")
    res = db.querry(f"SELECT * WHERE ip == {ip};")
    if len(res) == 0:
        db.execute(f"INSERT INTO ips(ip, time_connected) VALUES({ip}, {time.time()});")
        broadcast_ip(ip)

def mainloop(connection):
    global connections, HOST, PORT
    while True:
        try:
            #connection.send(f"{HOST}:{PORT}: {len(connections)}".encode("utf-8"))
        
            res = connection.recv(1024).decode("utf-8")
            
            if res == "IP":
                connection.send("OK".encode("utf-8"))
                ip = connection.recv(1024).decode("utf-8")
                ip_manager(ip)

            print(res)
            
            #time.sleep(0.1)
                
        except socket.error as e:
            print(e)
            connections.remove(connection)
            break

def connect_to_new_node():
    global connections
    while True:
        ip = db.querry("SELECT ip FROM ips ORDER BY RAND() LIMIT 1;")
        host, port = ip[num].split(":")
    
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((host, int(port)))
    
        if connection.recv(1024).decode("utf-8") == "OK":
            connections.append(connection)

            thread = threading.Thread(target=mainloop, args=(connection,))
            thread.start()
            break


def manage_new_node(connection, address):
    global connections, get_n_connected, db
    n_connected = len(connections)
    n_nodes = len(db.querry("SELECT * FROM ips;"))
    n_suposed_connections = get_n_connected(n_nodes)
    if n_connections < n_suposed_connections:
        difference = n_connected - n_suposed_connections
        connection.send("OK".encode("utf-8"))
        connections.append((connection))
        thread = threading.Thread(target=mainloop, args=(connection,))
        thread.start()

        if not difference == 1:
            for i in range(difference - 1):
                connect_to_new_node()

def ip_share_loop():
    global HOST, PORT
    while True:
        broadcast_ip(HOST+str(PORT))
        time.sleep(60)

def main():
    global connections, server 
    while True:
        connection, address = server.accept()

        print(f"connected by {address}")    
        conn_type = connection.recv(1024)
        if conn_type == "NODE":
            manage_new_node(connection, address)

if __name__ == "__main__":    
    thread = threading.Thread(target=ip_share_loop)
    thread.start()
    connect_to_new_node()
    main()
