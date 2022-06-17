
import socket
import threading
import database as db
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

db_connection = db.connect()

db.create(db_connection)

connections = []
connected = []
ips = []

get_n_connected = lambda n: int(5*math.log2(n))


def bradcast_ip(ip):
    #broadcasts ip to all connections
    global conections
    for connection in connections:
        connection.send("IP")
        data = connection.recv(1024).decode("utf-8")
        if data == "OK":
            connection.send(ip.encode("utf-8"))

def ip_manager(ip):
    global db_connection
    res = db.querry(db_connection, f"SELECT * WHERE ip == {ip};")
    if len(res) == 0:
        db.execute(db_connection, f"INSERT INTO ips(ip, time_connected) VALUES({ip}, {time.time()})")
    else:
        seconds = 24*60*60
        if res[0][1] <= time.time() - seconds:
            db.execute(db_connection, f"INSERT INTO ips(ip, time_connected) VALUES({ip}, {time.time()})")
            bradcast_ip(ip)

    db.execute(db_connection, f"DELETE FROM ips WHERE time_connected <= {int(time.time()) - seconds}")


def main_loop(connection):
    msg_type = connection.recv(1024).decode("utf-8")
    if msg_type == "IP":
        connection.send("OK")
        ip_manager(connection.recv(1024).decode("utf-8"))

def check_connections():
    global connections

def connect_to_node(n_nodes):
    global connections, db_connection
    ip = db.querry(db_connection, "SELECT ip FROM ips ORDER BY RAND() LIMIT 1;")
    server.connect()


def manage_node(connection, data):
    global connections, get_n_connected, db_connection
    check_connections()
    n_connected = len(connections)
    n_nodes = len(db.querry(db_connection, "SELECT * FROM ips;")))
    n_suposed_connections = get_n_connected(n_nodes)
    if n_connections < n_suposed_connections:
        difference = n_connected - n_suposed_connections
        connections.append((connections))
        #Falta crear thread amb la nova conexio
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
        manage_node(connection, data, address)

    if data["type"] == "client":
        manage_client(connection, data, address)
