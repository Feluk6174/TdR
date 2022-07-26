import database
import threading, time, socket, sys, json, math
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import auth
import log
from typing import Union

#todo fix

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
HOST = s.getsockname()[0]
s.close()
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

try:
    if sys.argv[2] == "-v":
        logger = log.Logger("main_log", vervose = True)
    else:
        logger = log.Logger("main_log")
except IndexError:
    logger = log.Logger("main_log")

db = database.Database(logger = logger)

get_suposed_connected = lambda n: int(5*math.log2(n))
get_suposed_connected = lambda n: 3

server_info = json.loads("{"+f'"type": "NODE", "host": "{HOST}", "port": {PORT}, "ip": "{IP}"'+"}")

max_clients = 10



#Client Node comunication

class ClientConnection():
    def __init__(self, connection:socket.socket, conn_info:dict):
        self.connection = connection
        self.info = conn_info
        self.queue = []
        self.responses = []
        self.ip = None

        thread = threading.Thread(target=self.process_queue)
        thread.start()

    def manage_requests(self):
        global clients, logger
        while True:
            try:
                msg = self.recv()
                logger.log("rcvd: " + msg)
                if msg == "":
                    raise socket.error
                msg = json.loads(msg)

                if msg["type"] == "ACTION":
                    self.queue.append(msg)
                elif msg["type"] == "RESPONSE":
                    self.responses.append(msg)

            except socket.error as e:
                logger.log("[ERROR]" + str(e))
                clients.remove(self)
                break

    def process_queue(self):
        global logger
        while True:
            if not len(self.queue) == 0:
                msg_info = self.queue[0]
                logger.log(f"recived: {msg_info} {type(msg_info)}")

                if msg_info["action"] == "REGISTER":
                    register_user(msg_info, self)

                elif msg_info["action"] == "POST":
                    new_post(msg_info, self)

                elif msg_info["action"] == "GET POSTS":
                    get_posts(msg_info, self)

                elif msg_info["action"] == "GET USER":
                    get_user_info(msg_info, self)

                elif msg_info["action"] == "GET POST":
                    get_post(msg_info, self)

                elif msg_info["action"] == "SEND":
                    self.send(msg_info["msg"])

                self.queue.pop(0)

    def recv_from_queue(self):
        while True:
            if not len(self.responses) == 0:
                res = self.responses[0]["response"]
                self.responses.pop(0)
                return res

    def recv(self):
        num = int(self.recv_from_queue())
        self.send('{"type": "RESPONSE", "response": "OK"}')
        msg = ""
        for i in range(num):
            msg += self.recv_from_queue()
            self.send('{"type": "RESPONSE", "response": "OK"}')

        return msg


    def send(self, msg:str):
        global logger
        logger.log("sending: "+msg)
        msg_len = len(msg)

        num = int(msg_len/512)
        num = num + 1 if not msg_len % 512 == 0 else num
        
        self.connection.send("{"+f'"type": "RESPONSE", "response": "{num}"'+"}")

        temp = self.recv_from_queue()
        if not temp == "OK":
            print("S1", temp)

        for i in range(num):
            print(i)
            self.connection.send("{"+f'"type": "RESPONSE", "response": "{msg[512*i:512*i+512]}"'+"}")
            temp = self.recv_from_queue()
            if not temp == "OK":
                print("S2", temp)


class NodeConnection():
    def __init__(self, connection:socket.socket, conn_info:dict, address:str):
        self.connection = connection
        self.info = conn_info
        self.queue = []
        self.responses = []
        self.ip = self.info["ip"]
        self.real_ip = address

        thread = threading.Thread(target=self.process_queue)
        thread.start()

    def manage_requests(self):
        global connections, logger
        while True:
            try:
                msg = self.recv()
                if msg == "":
                    raise socket.error
                
                msg = json.loads(msg)

                if msg["type"] == "ACTION":
                    self.queue.append(msg)
                elif msg["type"] == "RESPONSE":
                    self.responses.append(msg)


            except socket.error as e:
                logger.log("[ERROR]" + str(e))
                connections.remove(self)
                break

    def process_queue(self):
        global logger
        while True:
            if not len(self.queue) == 0:
                msg_info = self.queue[0]
                logger.log(f"recived: {msg_info} {type(msg_info)}")
                print(msg_info["action"])
                if msg_info["action"] == "IP":
                    manage_ip(msg_info, self.ip)

                if msg_info["action"] == "REGISTER":
                    register_user(msg_info, self, ip=self.ip)

                if msg_info["action"] == "POST":
                    new_post(msg_info, self, ip=self.ip)

                if msg_info["action"] == "SEND":
                    self.send(msg_info["msg"])

                n_connected = len(connections)
                n_nodes = len(db.querry("SELECT * FROM ips;"))
                n_suposed_connections = get_suposed_connected(n_nodes)
                if n_connected < n_suposed_connections:
                    thread = threading.Thread(target=connect_to_new_node)
                    thread.start()


                self.queue.pop(0)
    
    def recv_from_queue(self):
        while True:
            if not len(self.responses) == 0:
                res = self.responses[0]
                self.responses.pop(0)
                return res

    def send(self, msg:str):
        global logger
        logger.log("sending:"+msg)
        msg_len = len(msg)

        num = int(msg_len/1024)
        num = num + 1 if not msg_len % 1024 == 0 else num

        self.connection.send(str(num).encode("utf-8"))

        temp = self.recv_from_queue()
        if not temp == "OK":
            print("s1", temp)

        for i in range(num):
            self.connection.send(msg[1024*i:1024*i+1024].encode("utf-8"))
            temp = self.recv_from_queue()
            if not temp == "OK":
                print("s2", temp)

    def recv(self):
        num = int(self.connection.recv(1024).decode("utf-8"))
        self.send('{"type": "RESPONSE", "response": "OK"}')
        msg = ""
        for i in range(num):
            msg += self.connection.recv(1024).decode("utf-8")
            self.send('{"type": "RESPONSE", "response": "OK"}')

        return msg

def broadcast(msg, ip):
    global connections, logger

    logger.log(f"bradcasting: {msg} {ip}")

    for connection in connections:
        if not connection.ip == ip:
            msg_text = json.dumps(msg)
            formated_msg = msg_text.replace('"', '\\"')
            connection.queue.append(json.loads("{"+f'"type": "ACTION", "action": "SEND", "msg": "{formated_msg}"'+"}"))
            
            

def new_post(msg_info:dict, connection:Union[ClientConnection, NodeConnection], ip:str=None):
    global db, logger
    logger.log(f"posting: {msg_info} {ip}")
    if not database.is_safe(msg_info["post_id"]):
        connection.send("WRONG CHARS")
        return

    pub_key = db.querry(f"SELECT public_key FROM users WHERE user_name = '{msg_info['user_name']}'")
    pub_key = RSA.import_key(auth.reconstruct_key(pub_key[0][0], key_type="pub"))

    if not auth.verify(pub_key, msg_info["signature"], msg_info["content"], msg_info["post_id"], msg_info["user_name"], msg_info["flags"], msg_info["time"]):
        connection.send("WRONG SIGNATURE")
        return

    #CREATE TABLE posts(id INT NOT NULL PRIMARY KEY, user_id VARCHAR(16) NOT NULL, post VARCHAR(255) NOT NULL, time_posted INT NOT NULL, FOREIGN KEY (user_id) REFERENCES users (user_name));")
    res = db.querry(f"SELECT * FROM posts WHERE id = '{msg_info['post_id']}';")
    if len(res) == 0:
        sql = f"INSERT INTO posts(id, user_id, post, flags, time_posted, signature) VALUES('{msg_info['post_id']}', '{msg_info['user_name']}', '{msg_info['content']}', '{msg_info['flags']}', {int(msg_info['time'])}, '{msg_info['signature']}');"
        err = db.execute(sql)
        if not err == "ERROR":
            broadcast(msg_info, ip)
            if ip == None:
                connection.send('OK')
        else:
            connection.send('DATABASE ERROR')
    elif ip == None:
        connection.send("ALREADY EXISTS")


def register_user(msg_info:dict, connection:Union[ClientConnection, NodeConnection], ip:str=None):
    global db, logger
    logger.log(f"registering user: {msg_info} {ip}")
    if not database.is_safe(msg_info["user_name"], msg_info['public_key'], msg_info['public_key'], msg_info['profile_picture'], msg_info['info']):
        connection.send("WRONG CHARS")
        return

    #"CREATE TABLE users(user_name VARCHAR(16) NOT NULL UNIQUE PRIMARY KEY, public_key INT NOT NULL UNIQUE, time_created INT NOT NULL, profile_picture VARCHAR(64) NOT NULL, info VARCHAR(255));")
    res = db.querry(f"SELECT * FROM users WHERE user_name = '{msg_info['user_name']}'")

    if len(res) == 0:
        sql = f"INSERT INTO users(user_name, public_key, key_file, time_created, profile_picture, info) VALUES('{msg_info['user_name']}', '{msg_info['public_key']}', '{msg_info['private_key']}', {int(time.time())}, '{msg_info['profile_picture']}', '{msg_info['info']}');"
        logger.log("r"+sql)
        err = db.execute(sql)
        if not err == "ERROR":
            broadcast(msg_info, ip)
            if ip == None:
                connection.send("OK")
        else:
            connection.send("DATABASE ERROR")
    elif ip == None:
        connection.send("ALREADY EXISTS")

def get_posts(msg_info:dict, connection:ClientConnection):
    global db, logger
    logger.log(f"geting posts: {msg_info}")

    if not database.is_safe(msg_info['user_name']):
        connection.send("0")
        res = connection.recv_from_queue()
        if not res == "OK":
            logger.log(res)
        connection.send("WRONG CHARS")
        return

    posts = db.querry(f"SELECT * FROM posts WHERE user_id = '{msg_info['user_name']}'")

    connection.send(str(len(posts)))

    res = connection.recv_from_queue()
    if not res == "OK":
        logger.log(res)

    for i, post in enumerate(posts):
        msg = "{"+f'"id": "{post[0]}", "user_id": "{post[1]}", "content": "{post[2]}", "flags": "{post[3]}", "time_posted": {post[4]}, "signature": "{post[5]}"'+"}"
        connection.send(msg)
        res = connection.recv_from_queue()
        if not res == "OK":
            logger.log(res)

    connection.send("OK")

def get_user_info(msg_info:dict, connection:ClientConnection):
    global db, logger
    if not database.is_safe(msg_info["user_name"]):
        connection.send("WRONG CHARS")
        return
    # (user_name, public_key, key_file, time_created, profile_picture, info)
    user_info = db.querry(f"SELECT * FROM users WHERE user_name = '{msg_info['user_name']}';")
    logger.log(user_info)
    if not len(user_info) == 0 and not user_info == "ERROR":
        user_info = user_info[0]
        msg = "{"+f'"user_name": "{user_info[0]}", "public_key": "{user_info[1]}", "private_key": "{user_info[2]}",  "time_created": {user_info[3]}, "profile_picture": "{user_info[4]}", "info": "{user_info[5]}"'+"}"
    else:
        msg = "{}"
    connection.send(msg)

def get_post(msg_info:dict, connection:ClientConnection):
    global db, logger
    if not database.is_safe(msg_info["post_id"]):
        connection.send("WRONG CHARS")
        return
    # (id, user_id, post, flags, time_posted, signature)
    post = db.querry(f"SELECT * FROM posts WHERE id = '{msg_info['post_id']}';")
    logger.log(post)
    if not len(post) == 0:
        post = post[0]
        msg = "{"+f'"id": "{post[0]}", "user_id": "{post[1]}", "content": "{post[2]}", "flags": "{post[3]}", "time_posted": {post[4]}, "signature": "{post[5]}"'+"}"
    else:
        msg = "{}"
    connection.send(msg)









def manage_new_client(connection, conn_info):
    global clients, max_clients, logger
    logger.log(f"managing new client")
    conn_class = ClientConnection(connection, conn_info)
    if len(clients) <= max_clients:
        clients.append(conn_class)
        connection.send("OK".encode("utf-8"))
        thread = threading.Thread(target=conn_class.manage_requests)
        thread.start()

# Node - Node comunication
def broadcast_ip(ip:str, node_ip:str):
    global connections
    msg_content = "{"+f'"type": "ACTION", "action": "IP", "ip": "{ip}"'+"}"
    for connection in connections:
        if not connection.ip == node_ip:
            connection.queue.append(json.loads("{"+f'"type": "ACTION", "action": "SEND", "msg": {json.dumps(msg_content)}'+"}"))

def manage_ip(msg_info:dict, node_ip:str):
    global IP, db
    ip = msg_info["ip"]
    if ip == IP:
        return

    seconds_to_delete = 60
    seconds_to_update = 30

    db.execute(f"DELETE FROM ips WHERE time_connected <= {int(time.time()) - seconds_to_delete}")
    res = db.querry(f"SELECT * FROM ips WHERE ip = '{ip}';")

    if len(res) == 0:
        error = db.execute(f"INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()});")
        if not error == "ERROR":
            broadcast_ip(ip, node_ip)

    elif res[0][1] <= int(time.time()) - seconds_to_update:
        err1 = db.execute(f"DELETE FROM ips WHERE ip = '{ip}';")
        err2 = db.execute(f"INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()});")
        if not err1 == "ERROR" and not err2 == "ERROR":
            broadcast_ip(ip, node_ip)









def check_if_connected(ip:str):
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
    global connections, clients, db, IP, logger
    while True:
        logger.log("num of connected clients: " + str(len(clients)))
        logger.log("num of connections: " + str(len(connections)))
        for connection in connections:
            logger.log(f"    {connection.ip}")
        res = db.querry("SELECT * FROM ips;")
        logger.log("num of known nodes:" + str(len(res)))
        for ip in res:
            logger.log(f"    {ip[0]}")
        broadcast_ip(IP, IP)
        time.sleep(30)

def main():
    global server, logger
    while True:
        connection, address = server.accept()
        temp = connection.recv(1024).decode("utf-8")
        logger.log(temp)
        conn_info = json.loads(temp)
        logger.log(conn_info)

        if conn_info["type"] == "NODE":
            manage_new_node(connection, address, conn_info)

        elif conn_info["type"] == "CLIENT":
            manage_new_client(connection, conn_info)

def start():
    time.sleep(10)
    connect_to_new_node()

if __name__ == "__main__":
    logger.log(f"========[SERVER RUNNING ON {IP}]========")
    thread = threading.Thread(target=clock)
    thread.start()
    thread = threading.Thread(target=start)
    thread.start()
    main()
