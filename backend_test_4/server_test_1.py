
import socket
import threading
import database
import mysql.connector
import math
import time
import json
import random

HOST = "127.0.0.1"
PORT = int(input("Input port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

db = database.connect()

db.create()

connections = []
connected = []
ips = []

get_n_connected = lambda n: int(5*math.log2(n))


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
    seconds = 24*60*60
    db.execute(f"DELETE FROM ips WHERE time_connected <= {int(time.time()) - seconds}")
    res = db.querry(f"SELECT * WHERE ip == {ip};")
    if len(res) == 0:
        db.execute(f"INSERT INTO ips(ip, time_connected) VALUES({ip}, {time.time()});")
        broadcast_ip(ip)

def main_loop(connection):
    connection.send("CONNECTED")
    while True:
        msg_type = connection.recv(1024).decode("utf-8")
        if msg_type == "IP":
            connection.send("OK")
            ip_manager(connection.recv(1024).decode("utf-8"))

def check_connections():
    global connections

def connect_to_node(n_nodes):
    global connections, db_connection, node_data
    ip = db.querry("SELECT ip FROM ips ORDER BY RAND() LIMIT 1;")
    ip = ip.split(":")
    server.connect((ip[0], int(ip[1])))
    server.send(json.dumps(node_data).decode("utf-8"))

def manage_new_node(connection, data):
    global connections, get_n_connected, db, node_data
    check_connections()
    n_connected = len(connections)
    n_nodes = len(db.querry("SELECT * FROM ips;"))
    n_suposed_connections = get_n_connected(n_nodes)
    if n_connections < n_suposed_connections:
        difference = n_connected - n_suposed_connections
        connections.append((connection))
        thread = threading.Thread(target=manage_node, args=(connection,))
        thread.start()
        
        for i in range(difference - 1):
            connect_to_node(n_nodea)

    else:
        connection.send("FULL")
        connection.close()

def manage_client(connection, data):
    pass

def main(server):
    global connections
    connection, address = server.accept()
    print(f"connected by {address}")
    data = json.loads(connection.recv(1024).decode("utf-8"))
    if data["type"] == "node":
        manage_new_node(connection, data, address)

    if data["type"] == "client":
                manage_client(connection, data, address)
