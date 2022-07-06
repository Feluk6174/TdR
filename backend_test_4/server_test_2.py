import socket
import threading
import database
import time

HOST = "192.168.178.138"
PORT = int(input("Input port: "))
#PORT = 42069

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
        connection[1].send("IP")
        data = connection[1].recv(1024).decode("utf-8")
        if data == "OK":
            connection[1].send(ip.encode("utf-8"))

def ip_manager(ip:str):
    global db
    seconds = 60
    db.execute(f"DELETE FROM ips WHERE time_connected <= {int(time.time()) - seconds}")
    res = db.querry(f"SELECT * WHERE ip == {ip};")
    if len(res) == 0:
        db.execute(f"INSERT INTO ips(ip, time_connected) VALUES({ip}, {time.time()});")
        broadcast_ip(ip)

def check_if_connected(ip):
    global connections
    for connection in connections:
        if connection[0] == ip:
            return True
    return False

def mainloop(connection, ip):
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
            connections.remove((ip, connection))
            break

def connect_to_new_node():
    global connections
    while True:
        ip = db.querry("SELECT ip FROM ips ORDER BY RAND() LIMIT 1;")
        print(ip)

        if not check_if_connected(ip[0][0]):
            host, port = ip[0][0].split(":")
    
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((host, int(port)))

            connection.send("NODE".encode("utf-8"))
            print(21)
            if connection.recv(1024).decode("utf-8") == "OK":
                print(22)
                connections.append((ip[0][0], connection))
                print(f"connected to {ip[0][0]}")
                thread = threading.Thread(target=mainloop, args=(connection, ip[0][0]))
                print(23)
                thread.start()
                print(24)
                break
            print(25)


def manage_new_node(connection, address):
    global connections, get_n_connected, db
    print(10)
    n_connected = len(connections)
    n_nodes = len(db.querry("SELECT * FROM ips;"))
    n_suposed_connections = get_n_connected(n_nodes)
    print(n_connected, n_suposed_connections)
    if n_connections < n_suposed_connections and not check_if_connected(address):
        print(11)
        difference = n_connected - n_suposed_connections
        print(difference)
        connection.send("OK".encode("utf-8"))
        print(12)
        connections.append((address, connection))
        print(f"connected by {adddress}", connections)
        thread = threading.Thread(target=mainloop, args=(connection, address))
        thread.start()

        if not difference == 1:
            for i in range(difference - 1):
                connect_to_new_node()

def ip_share_loop():
    global HOST, PORT
    time.sleep(10)
    connect_to_new_node()
    print("heyyyyy")
    while True:
        broadcast_ip(HOST+str(PORT))
        time.sleep(60)

def main():
    global connections, server 
    while True:
        connection, address = server.accept()

        #print(f"connected by {address}")    
        conn_type = connection.recv(1024).decode("utf-8")
        print(conn_type)

        if conn_type == "NODE":
            manage_new_node(connection, address)

if __name__ == "__main__":    
    thread = threading.Thread(target=ip_share_loop)
    thread.start()
    print(2)
    main()
