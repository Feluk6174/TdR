import database
import threading, time, socket, sys, json

HOST = "192.168.178.138"
try:
    PORT = int(sys.argv[1])
except IndexError:
    PORT = int(input("Input port: "))
IP = HOST+":"+str(PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

connections = []
clients = []

db = database.Database()

get_suposed_connected = lambda n: int(5*math.log2(n))
get_suposed_connected = lambda n: 2

server_info = json.loads("{"+f'"type": "NODE", "host": "{HOST}", "port": {PORT}, "ip": "{IP}"'+"}")

max_clients = 10

#Client Node comunication

def broadcast(msg, ip):
    print(f"({threading.current_thread().name})[{time.asctime()}] broadcsasting:", msg, ip)
    global connections
    for connection in connections:
        if not connection[0] == ip:
            print("b", ip, connection[0], json.dumps(msg))
            connection[1].send(json.dumps(msg).encode("utf-8"))
            response = connection[1].recv(1024).decode("utf-8")
            if not response == "OK":
                print("b", response)
            
            

def new_post(msg_info, connection, ip=None):
    print(f"({threading.current_thread().name})[{time.asctime()}] posting:", msg_info, ip)
    global db
    #CREATE TABLE posts(id INT NOT NULL PRIMARY KEY, user_id VARCHAR(16) NOT NULL, post VARCHAR(255) NOT NULL, time_posted INT NOT NULL, FOREIGN KEY (user_id) REFERENCES users (user_name));")
    res = db.querry(f"SELECT * FROM posts WHERE id = '{msg_info['post_id']}';")
    if len(res) == 0:
        sql = f"INSERT INTO posts(id, user_id, post, time_posted) VALUES('{msg_info['post_id']}', '{msg_info['user_name']}', '{msg_info['content']}', {int(time.time())});"
        db.querry(sql)
        broadcast(msg_info, ip)
        if ip == None:
            connection.send("OK".encode("utf-8"))
    elif ip == None:
        connection.send("ALREADY EXISTS".encode("utf-8"))


def register_user(msg_info, connection, ip=None):
    print(f"({threading.current_thread().name})[{time.asctime()}] regitering user:", msg_info, ip)
    global db
    #"CREATE TABLE users(user_name VARCHAR(16) NOT NULL UNIQUE PRIMARY KEY, public_key INT NOT NULL UNIQUE, time_created INT NOT NULL, profile_picture VARCHAR(64) NOT NULL, info VARCHAR(255));")
    res = db.querry(f"SELECT * FROM users WHERE user_name = '{msg_info['user_name']}'")

    if len(res) == 0:
        sql = f"INSERT INTO users(user_name, public_key, time_created, profile_picture, info) VALUES('{msg_info['user_name']}', {msg_info['public_key']}, {int(time.time())}, '{msg_info['profile_picture']}', '{msg_info['info']}');"
        print("r",sql)
        db.execute(sql)
        broadcast(msg_info, ip)
        if ip == None:
            connection.send("OK".encode("utf-8"))
    elif ip == None:
        connection.send("ALREADY EXISTS".encode("utf-8"))

def get_posts(msg_info, connection):
    print(f"({threading.current_thread().name})[{time.asctime()}] geting posts:", msg_info)

    posts = db.querry(f"SELECT * FROM posts WHERE user_id = '{msg_info['user_name']}'")

    connection.send(str(len(posts)).encode("utf-8"))

    connection.recv(1024)

    for i, post in enumerate(posts):
        print(i)
        msg = "{"+f'"id": "{post[0]}", "user_id": "{post[1]}", "content": "{post[2]}", "time_posted": {post[3]}'+"}"
        connection.send(msg.encode("utf-8"))
        if not connection.recv(1024).decode("utf-8") == "OK":
            break


def client_main_loop(connection, conn_info):
    global clients
    print(f"[{time.asctime()}] client_main_loop")
    while True:
        try:
            msg = connection.recv(1024).decode("utf-8")
            if msg == "":
                raise socket.error
            print("m", msg)
            msg_info = json.loads(msg)
            print(f"({threading.current_thread().name})[{time.asctime()}] recived:", msg_info)

            if msg_info["type"] == "REGISTER":
                connection.send("OK".encode("utf-8"))
                register_user(msg_info, connection)

            if msg_info["type"] == "POST":
                connection.send("OK".encode("utf-8"))
                new_post(msg_info, connection)

            if msg_info["type"] == "GET POSTS":
                get_posts(msg_info, connection)

        except socket.error as e:
            print("[ERROR]", e)
            clients.remove((connection, conn_info))
            break

def manage_new_client(connection, conn_info):
    global clients, max_clients
    print(f"({threading.current_thread().name})[{time.asctime()}] managing nrew client")
    print(len(clients), max_clients)
    if len(clients) <= max_clients:
        clients.append((connection, conn_info))
        print(3)
        thread = threading.Thread(target=client_main_loop, args=(connection, conn_info))
        thread.start()

# Node - Node comunication
def broadcast_ip(ip, node_ip):
    global connections
    msg_content = "{"+f'"type": "IP", "ip": "{ip}"'+"}"
    for connection in connections:
        if not connection[0] == node_ip:
            connection[1].send(msg_content.encode("utf-8"))

def manage_ip(msg_info, node_ip):
    global IP, db
    ip = msg_info["ip"]
    if ip == IP:
        return

    seconds_to_delete = 120
    seconds_to_update = 60

    db.execute(f"DELETE FROM ips WHERE time_connected <= {int(time.time()) - seconds_to_delete}")
    res = db.querry(f"SELECT * FROM ips WHERE ip = '{ip}';")

    if len(res) == 0:
        db.execute(f"INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()});")
        broadcast_ip(ip, node_ip)

    elif res[0][1] <= int(time.time()) - seconds_to_update:
        db.execute(f"DELETE FROM ips WHERE ip = '{ip}';")
        db.execute(f"INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()});")
        broadcast_ip(ip, node_ip)

def node_main_loop(connection, ip, real_ip):
    global db, get_suposed_connected, connections
    while True:
        try:
            res = connection.recv(1024).decode("utf-8")
            print("n_m", ip, res)
            msg_info = json.loads(res)

            if msg_info["type"] == "IP":
                manage_ip(msg_info, ip)

            if msg_info["type"] == "REGISTER":
                connection.send("OK".encode("utf-8"))
                register_user(msg_info, connection, ip=ip)

            if msg_info["type"] == "POST":
                connection.send("OK".encode("utf-8"))
                new_post(msg_info, connection, ip=ip)


            n_connected = len(connections)
            n_nodes = len(db.querry("SELECT * FROM ips;"))
            n_suposed_connections = get_suposed_connected(n_nodes)
            if n_connected < n_suposed_connections:
                thread = threading.Thread(target=connect_to_new_node)
                thread.start()

        except socket.error as e:
            print("[ERROR]", e)
            connections.remove((ip, connection, real_ip))
            break

def check_if_connected(ip):
    global connections
    for connection in connections:
        if ip == connection[0]:
            return True
    return False

def connect_to_new_node():
    global server_info, db, get_suposed_connected, connections
    n_nodes = len("SELECT * FROM ips;")
    n_suposed_connections = get_suposed_connected(n_nodes)
    n_connected = len(connections)
    if n_suposed_connections < n_connected:
        return
    for i in range(10):
        ip = db.querry("SELECT ip FROM ips ORDER BY RAND() LIMIT 1;")
        if not check_if_connected(ip[0][0]):
            host, port = ip[0][0].split(":")
    
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((host, int(port)))

            connection.send(json.dumps(server_info).encode("utf-8"))

            if connection.recv(1024).decode("utf-8") == "OK":
                connections.append((ip[0][0], connection, ip[0][0]))
                thread = threading.Thread(target=node_main_loop, args=(connection, ip[0][0], ip[0][0]))
                thread.start()
                break

        if len(db.querry("SELECT * FROM ips;")) <= len(connections):
            break
        

def manage_new_node(connection, address, conn_info):
    global connections, get_suposed_connected
    n_connected = len(connections)
    n_nodes = len("SELECT * FROM ips;")
    n_suposed_connections = get_suposed_connected(n_nodes)

    if n_connected < n_suposed_connections and not check_if_connected(conn_info["ip"]):
        connection.send("OK".encode("utf-8"))
        connections.append((conn_info["ip"], connection, address[0]+":"+str(address[1])))
        thread = threading.Thread(target=node_main_loop, args=(connection, conn_info["ip"], address[0]+":"+str(address[1])))
        thread.start()

def clock():
    global connections, db, IP
    while True:
        print("num of connections:", len(connections))
        for connection in connections:
            print(f"    {connection[0]}")
        res = db.querry("SELECT * FROM ips;")
        print("num of known nodes:", len(res))
        for ip in res:
            print(f"    {ip[0]}")
        broadcast_ip(IP, IP)
        time.sleep(60)

def main():
    global server
    while True:
        connection, address = server.accept()
        temp = connection.recv(1024).decode("utf-8")
        print(temp)
        conn_info = json.loads(temp)
        print(f"[{time.asctime()}]", conn_info)

        if conn_info["type"] == "NODE":
            manage_new_node(connection, address, conn_info)

        elif conn_info["type"] == "CLIENT":
            manage_new_client(connection, conn_info)

def start():
    time.sleep(10)
    connect_to_new_node()

if __name__ == "__main__":
    print(f"========[SERVER RUNNING ON {IP}]========")
    thread = threading.Thread(target=clock)
    thread.start()
    thread = threading.Thread(target=start)
    thread.start()
    main()