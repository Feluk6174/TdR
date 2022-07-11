from urllib import response
import database
import threading, time, socket, sys, json, math

#todo fix

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
        if not connection.ip == ip:
            msg_text = json.dumps(msg)
            formated_msg = msg_text.replace('"', '\\"')
            print("b", ip, connection.ip, json.dumps(msg))
            connection.queue.append("{"+f'"type": "ACTION", "action": "SEND", "msg": "{formated_msg}"'+"}")
            
            

def new_post(msg_info, connection, ip=None):
    print(f"({threading.current_thread().name})[{time.asctime()}] posting:", msg_info, ip)
    global db
    #CREATE TABLE posts(id INT NOT NULL PRIMARY KEY, user_id VARCHAR(16) NOT NULL, post VARCHAR(255) NOT NULL, time_posted INT NOT NULL, FOREIGN KEY (user_id) REFERENCES users (user_name));")
    res = db.querry(f"SELECT * FROM posts WHERE id = '{msg_info['post_id']}';")
    if len(res) == 0:
        sql = f"INSERT INTO posts(id, user_id, post, flags, time_posted) VALUES('{msg_info['post_id']}', '{msg_info['user_name']}', '{msg_info['content']}', '{msg_info['flags']}', {int(time.time())});"
        db.querry(sql)
        broadcast(msg_info, ip)
        if ip == None:
            connection.connection.send('OK'.encode("utf-8"))
    elif ip == None:
        connection.connection.send("ALREADY EXISTS".encode("utf-8"))


def register_user(msg_info, connection, ip=None):
    print(f"({threading.current_thread().name})[{time.asctime()}] regitering user:", msg_info, ip)
    global db
    #"CREATE TABLE users(user_name VARCHAR(16) NOT NULL UNIQUE PRIMARY KEY, public_key INT NOT NULL UNIQUE, time_created INT NOT NULL, profile_picture VARCHAR(64) NOT NULL, info VARCHAR(255));")
    res = db.querry(f"SELECT * FROM users WHERE user_name = '{msg_info['user_name']}'")

    if len(res) == 0:
        sql = f"INSERT INTO users(user_name, public_key, time_created, profile_picture, info) VALUES('{msg_info['user_name']}', '{msg_info['public_key']}', {int(time.time())}, '{msg_info['profile_picture']}', '{msg_info['info']}');"
        print("r",sql)
        db.execute(sql)
        broadcast(msg_info, ip)
        if ip == None:
            connection.connection.send("OK".encode("utf-8"))
    elif ip == None:
        connection.connection.send("ALREADY EXISTS".encode("utf-8"))

def get_posts(msg_info, connection):
    global db
    print(f"({threading.current_thread().name})[{time.asctime()}] geting posts:", msg_info)

    posts = db.querry(f"SELECT * FROM posts WHERE user_id = '{msg_info['user_name']}'")

    connection.send(str(len(posts)).encode("utf-8"))

    #if connection.recv() == "OK":

    for i, post in enumerate(posts):
        print(i)
        msg = "{"+f'"id": "{post[0]}", "user_id": "{post[1]}", "content": "{post[2]}", "flags": "{post[3]}", "time_posted": {post[4]}'+"}"
        connection.send(msg.encode("utf-8"))
        time.sleep(0.1)

def get_user_info(msg_info, connection):
    global db
    # (user_name, public_key, time_created, profile_picture, info)
    user_info = db.querry(f"SELECT * FROM users WHERE user_name = '{msg_info['user_name']}';")
    print(user_info)
    if not len(user_info) == 0:
        user_info = user_info[0]
        msg = "{"+f'"user_name": "{user_info[0]}", "public_key": {user_info[1]}, "time_created": {user_info[2]}, "profile_picture": "{user_info[3]}", "info": "{user_info[4]}"'+"}"
    else:
        msg = "{}"
    connection.send(msg.encode("utf-8"))

class ClientConnection():
    def __init__(self, connection, conn_info):
        self.connection = connection
        self.info = conn_info
        self.queue = []
        self.responses = []

        thread = threading.Thread(target=self.process_queue)
        thread.start()

    def manage_requests(self):
        global clients
        while True:
            try:
                msg = json.loads(self.connection.recv(1024).decode("utf-8"))
                print("----", msg)
                if msg == "":
                    raise socket.error

                if msg["type"] == "ACTION":
                    self.queue.append(msg)
                elif msg["type"] == "RESPONSE":
                    self.responses.append(msg)

            except socket.error as e:
                print("[ERROR]", e)
                clients.remove(self)
                break

    def process_queue(self):
        while True:
            if not len(self.queue) == 0:
                print(f"({threading.current_thread().name})[{time.asctime()}] recived:", msg_info)
                msg_info = self.queue[0]

                if msg_info["action"] == "REGISTER":
                    register_user(msg_info, self)

                elif msg_info["action"] == "POST":
                    new_post(msg_info, self.connection)

                elif msg_info["action"] == "GET POSTS":
                    get_posts(msg_info, self.connection)

                elif msg_info["action"] == "GET USER":
                    get_user_info(msg_info, self.connection)

                elif msg_info["action"] == "SEND":
                    self.connection.send(msg_info["msg"].encode("utf-8"))

                self.queue.pop(0)

    def recv(self):
        while True:
            if not len(self.responses) == 0:
                res = self.responses[0]["response"]
                self.responses.pop(0)
                return res

def manage_new_client(connection, conn_info):
    global clients, max_clients
    print(f"({threading.current_thread().name})[{time.asctime()}] managing nrew client")
    print(len(clients), max_clients)
    conn_class = ClientConnection(connection, conn_info)
    if len(clients) <= max_clients:
        clients.append(conn_class)
        print(3)
        thread = threading.Thread(target=conn_class.manage_requests)
        thread.start()

# Node - Node comunication
def broadcast_ip(ip, node_ip):
    global connections
    msg_content = "{"+f'"type": "ACTION", "action": "IP", "ip": "{ip}"'+"}"
    for connection in connections:
        if not connection.ip == node_ip:
            connection.queue.append("{"+f'"type": "ACTION", "action": "SEND", "msg": {json.dumps(msg_content)}'+"}")

def manage_ip(msg_info, node_ip):
    global IP, db
    ip = msg_info["ip"]
    if ip == IP:
        return

    seconds_to_delete = 60
    seconds_to_update = 30

    db.execute(f"DELETE FROM ips WHERE time_connected <= {int(time.time()) - seconds_to_delete}")
    res = db.querry(f"SELECT * FROM ips WHERE ip = '{ip}';")

    if len(res) == 0:
        db.execute(f"INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()});")
        broadcast_ip(ip, node_ip)

    elif res[0][1] <= int(time.time()) - seconds_to_update:
        db.execute(f"DELETE FROM ips WHERE ip = '{ip}';")
        db.execute(f"INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()});")
        broadcast_ip(ip, node_ip)

class NodeConnection():
    def __init__(self, connection, conn_info, address):
        self.connection = connection
        self.info = conn_info
        self.queue = []
        self.responses = []
        self.ip = self.info["ip"]
        self.real_ip = address

        thread = threading.Thread(target=self.process_queue)
        thread.start()

    def manage_requests(self):
        global connections
        while True:
            try:
                msg = json.loads(self.connection.recv(1024).decode("utf-8"))
                if msg == "":
                    raise socket.error

                if msg["type"] == "ACTION":
                    self.queue.append(msg)
                elif msg["type"] == "RESPONSE":
                    self.responses.append(msg)


            except socket.error as e:
                print("[ERROR]", e)
                connections.remove(self)
                break

    def process_queue(self):
        while True:
            if not len(self.queue) == 0:
                print(self.queue)
                msg_info = self.queue[0]
                print("wtf", msg_info)

                if msg_info["action"] == "IP":
                    manage_ip(msg_info, self.ip)

                if msg_info["action"] == "REGISTER":
                    register_user(msg_info, self.connection, ip=self.ip)

                if msg_info["action"] == "POST":
                    new_post(msg_info, self.connection, ip=self.ip)

                if msg_info["action"] == "SEND":
                    self.connection.send(msg_info["msg"].encode("utf-8"))

                n_connected = len(connections)
                n_nodes = len(db.querry("SELECT * FROM ips;"))
                n_suposed_connections = get_suposed_connected(n_nodes)
                if n_connected < n_suposed_connections:
                    thread = threading.Thread(target=connect_to_new_node)
                    thread.start()


                self.queue.pop(0)
    
    def recv(self):
        while True:
            if not len(self.responses) == 0:
                res = self.responses[0]
                self.responses.pop(0)
                return res

def check_if_connected(ip):
    global connections
    for connection in connections:
        if ip == connection.ip:
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
                #(ip[0][0], connection, ip[0][0])
                conn_class = NodeConnection(connection, {"ip": ip[0][0]}, ip[0][0])
                connections.append(conn_class)
                thread = threading.Thread(target=conn_class.manage_requests)
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
        conn_class = NodeConnection(connection, conn_info, address[0]+":"+str(address[1]))
        connections.append(conn_class)
        thread = threading.Thread(target=conn_class.manage_requests)
        thread.start()

def clock():
    global connections, db, IP
    while True:
        print("num of connections:", len(connections))
        for connection in connections:
            print(f"    {connection.ip}")
        res = db.querry("SELECT * FROM ips;")
        print("num of known nodes:", len(res))
        for ip in res:
            print(f"    {ip[0]}")
        broadcast_ip(IP, IP)
        time.sleep(30)

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