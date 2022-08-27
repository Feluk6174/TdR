import socket
import threading
import json
from Crypto.Hash import SHA256

import database
import log
import managment

class ClientConnection():
    def __init__(self, connection:socket.socket, conn_info:dict):
        logger.log("client")
        self.connection = connection
        self.info = conn_info
        self.queue = []
        self.responses = []
        self.temp_msgs = {}
        self.send_responses = []
        self.ip = None

        thread = threading.Thread(target=self.process_queue)
        thread.start()

    def manage_requests(self):
        global clients, logger
        while True:
            try:
                msg = self.connection.recv(1024).decode("utf-8")
                if msg == "":
                    raise socket.error

                msgs = msg.replace("}{", "}\0{").split("\0")

                for msg in msgs:
                    msg = json.loads(msg)
                    logger.log("recv", msg)

                    if msg["type"] == "NUM" and not msg["num"] == 0:
                        self.temp_msgs[msg["id"]] = {"content": "", "num": msg["num"], "act_num": 0}
                        send_msg = "{"+f'"type": "CONN RESPONSE", "response": "OK", "id": "{msg["id"]}"'+"}"
                        self.connection.send(send_msg.encode("utf-8"))

                    if msg["type"] == "MSG PART":
                        self.temp_msgs[msg["id"]]["content"] += msg["content"]
                        self.temp_msgs[msg["id"]]["act_num"] += 1

                        if self.temp_msgs[msg["id"]]["num"] == self.temp_msgs[msg["id"]]["act_num"]:
                            res_msg = json.loads(self.temp_msgs[msg["id"]]["content"])
                            if res_msg["type"] == "ACTION":
                                self.queue.append(res_msg)
                            elif res_msg["type"] == "RESPONSE":
                                self.responses.append(res_msg)
                        send_msg = "{"+f'"type": "CONN RESPONSE", "response": "OK", "id": "{msg["id"]}"'+"}"
                        self.connection.send(send_msg.encode("utf-8"))
                    
                    if msg["type"] == "CONN RESPONSE":
                        self.send_responses.append(msg)

            except socket.error as e:
                logger.log("[ERROR]" + str(e))
                clients.remove(self)
                break

            except json.decoder.JSONDecodeError as e:
                logger.log("[ERROR]" + str(e) + " " + str(msg))
                connections.remove(self)
                clients

    def process_queue(self):
        global logger
        logger.log("client queue")
        while True:
            if not len(self.queue) == 0:
                msg_info = self.queue[0]
                logger.log(f"recived: {msg_info} {type(msg_info)}")

                if msg_info["action"] == "REGISTER":
                    user_actions.register_user(msg_info, self)

                elif msg_info["action"] == "POST":
                    user_actions.new_post(msg_info, self)

                elif msg_info["action"] == "GET POSTS":
                    user_actions.get_posts(msg_info, self)

                elif msg_info["action"] == "GET USER":
                    user_actions.get_user_info(msg_info, self)

                elif msg_info["action"] == "GET POST":
                    user_actions.get_post(msg_info, self)

                elif msg_info["action"] == "SEND":
                    self.send(msg_info["msg"])

                self.queue.pop(0)

    def recv_from_queue(self):
        global logger
        while True:
            if not len(self.responses) == 0:
                res = self.responses[0]
                self.responses.pop(0)
                return res

    def recv_send_response(self, msg_id:str):
        global logger
        while True:
            if not len(self.send_responses) == 0:
                for i, response in enumerate(self.send_responses):
                    if response["id"] == msg_id:
                        res = response["response"]
                        self.send_responses.pop(i)
                        return res


    def send(self, msg:str):
        global logger
        logger.log("sending: "+msg)
        msg_len = len(msg)
        msg_id = SHA256.new(msg.encode("utf-8")).hexdigest()

        num = int(msg_len/512)
        num = num + 1 if not msg_len % 512 == 0 else num
        
        send_msg = "{"+f'"type": "NUM", "num": {num}, "id": "{msg_id}"'+"}"
        temp = self.connection.send(send_msg.encode("utf-8"))

        temp = self.recv_send_response(msg_id)
        if not temp == "OK":
            logger.log("S1" + str(temp))

        for i in range(num):
            msg_part = msg[512*i:512*i+512].replace("\"", '\\"')
            send_msg = "{"+f'"type": "MSG PART", "id": "{msg_id}", "content": "{msg_part}"'+"}"
            self.connection.send(send_msg.encode("utf-8"))
            temp = self.recv_send_response(msg_id)
            if not temp == "OK":
                logger.log("S2" + str(temp))


class NodeConnection():
    def __init__(self, connection:socket.socket, conn_info:dict, address:str):
        self.connection = connection
        self.info = conn_info
        self.queue = []
        self.responses = []
        self.send_responses = []
        self.temp_msgs = {}
        self.ip = self.info["ip"]
        self.real_ip = address
        global logger 
        logger.log("connected by", self.ip)

        thread = threading.Thread(target=self.process_queue)
        thread.start()

    def manage_requests(self):
        global connections, logger
        while True:
            try:
                msg = self.connection.recv(1024).decode("utf-8")
                if msg == "":
                    raise socket.error

                msgs = msg.replace("}{", "}\0{").split("\0")
                for msg in msgs:
                    msg = json.loads(msg)
                    logger.log("msg", msg)

                    if msg["type"] == "NUM" and not msg["num"] == 0:
                        self.temp_msgs[msg["id"]] = {"content": "", "num": msg["num"], "act_num": 0}
                        send_msg = "{"+f'"type": "CONN RESPONSE", "response": "OK", "id": "{msg["id"]}"'+"}"
                        self.connection.send(send_msg.encode("utf-8"))

                    if msg["type"] == "MSG PART":
                        self.temp_msgs[msg["id"]]["content"] += msg["content"]
                        self.temp_msgs[msg["id"]]["act_num"] += 1

                        if self.temp_msgs[msg["id"]]["num"] == self.temp_msgs[msg["id"]]["act_num"]:
                            res_msg = json.loads(self.temp_msgs[msg["id"]]["content"])
                            if res_msg["type"] == "ACTION":
                                self.queue.append(res_msg)
                            elif res_msg["type"] == "RESPONSE":
                                self.responses.append(res_msg)
                        send_msg = "{"+f'"type": "CONN RESPONSE", "response": "OK", "id": "{msg["id"]}"'+"}"
                        self.connection.send(send_msg.encode("utf-8"))
                    
                    if msg["type"] == "CONN RESPONSE":
                        logger.log("queueing", msg)
                        self.send_responses.append(msg)
                        #send_msg = "{"+f'"type": "CONN RESPONSE", "response": "OK", "id": "{msg["id"]}"'+"}"
                        #self.connection.send(send_msg.encode("utf-8"))

            except socket.error as e:
                logger.log("[ERROR]" + str(e))
                connections.remove(self)
                break

            except json.decoder.JSONDecodeError as e:
                logger.log("[ERROR]" + str(e) + " " + str(msg))
                connections.remove(self)
                break

    def process_queue(self):
        global logger
        while True:
            if not len(self.queue) == 0:
                msg_info = self.queue[0]
                logger.log(f"recived: {msg_info} {type(msg_info)}")
                if msg_info["action"] == "IP":
                    managment.manage_ip(msg_info, self.ip)

                if msg_info["action"] == "REGISTER":
                    user_actions.register_user(msg_info, self, ip=self.ip)

                if msg_info["action"] == "POST":
                    user_actions.new_post(msg_info, self, ip=self.ip)

                if msg_info["action"] == "SEND":
                    self.send(msg_info["msg"])

                n_connected = len(connections)
                n_nodes = len(db.querry("SELECT * FROM ips;"))
                n_suposed_connections = managment.get_suposed_connected(n_nodes)
                if n_connected < n_suposed_connections:
                    thread = threading.Thread(target=managment.connect_to_new_node)
                    thread.start()


                self.queue.pop(0)
    
    def recv_from_queue(self):
        while True:
            if not len(self.responses) == 0:
                res = self.responses[0]
                self.responses.pop(0)
                return res

    def recv_send_response(self, msg_id:str):
        global logger
        while True:
            if not len(self.send_responses) == 0:
                for i, response in enumerate(self.send_responses):
                    if response["id"] == msg_id:
                        res = response["response"]
                        self.send_responses.pop(i)
                        return res


    def send(self, msg:str):
        global logger
        logger.log("sending: "+msg)
        msg_len = len(msg)
        msg_id = SHA256.new(msg.encode("utf-8")).hexdigest()

        num = int(msg_len/512)
        num = num + 1 if not msg_len % 512 == 0 else num
        send_msg = "{"+f'"type": "NUM", "num": {num}, "id": "{msg_id}"'+"}"
        temp = self.connection.send(send_msg.encode("utf-8"))

        temp = self.recv_send_response(msg_id)
        if not temp == "OK":
            logger.log("S1" + str(temp))

        for i in range(num):
            msg_part = msg[512*i:512*i+512].replace("\"", '\\"')
            send_msg = "{"+f'"type": "MSG PART", "id": "{msg_id}", "content": "{msg_part}"'+"}"
            self.connection.send(send_msg.encode("utf-8"))
            temp = self.recv_send_response(msg_id)
            if not temp == "OK":
                logger.log("S2" + str(temp))


def init(get_logger:log.Logger, get_clients:list, get_connections:list, get_db:database.Database):
    # sets global variables
    global logger, clients, connections, db

    logger.stop()
    logger = get_logger
    clients = get_clients
    connections = get_connections
    db.stop()
    db = get_db

logger = log.Logger(None)
clients = []
connections = []
db = database.Database()

import user_actions