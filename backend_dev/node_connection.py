from msilib.schema import MsiPatchHeaders
import socket
import threading
import json

class NodeConnection():
    def __init__(self, connection, conn_info, address):
        self.connection = connection
        self.info = conn_info
        self.info["real_ip"] = address
        self.responses = []
        self.queue = []
        self.connected = True

        thread = threading.Thread(target=self.process_queue)
        thread.start()

    def manage_msgs(self):
        while True:
            try:
                msg = json.loads(self.connection.recv(1024).decode("utf-8"))
                if msg["type"] == "RSPONSE":
                    self.responses.append(msg)
                elif msg["type"] == "ACTION":
                    self.queue.append(msg)
                
            except socket.error as e:
                self.connected = False
                print("[ERROR]", e)
                break

    def process_queue(self):
        while True:
            pass