import socket
import threading
import database as db
import sqlite3
import math
import time

HOST = "127.0.0.1"
PORT = int(input("Input port"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

db.create_ip()

connections = []
connected = []
ips = []

def bradcast_ip(ip):
    #
    global conections
    for connection in connections:
        connection.send(ip.encode("utf-8"))

def handle_ip_broadcast(ip:str):
    sql = f"SELECT * FROM ips WHERE ip = {ip}"
    querry_result = db.execute(sql, "ip_db.db")
    if len(querry_result) == 0:
        sql = "INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()})"
        db.execute(ql, "ip_db.db")
        bradcast_ip(ip)
    elif len(querry_result) == 1:
        time_difference = 60
        if time.time()-querry_result[0][1] = time_difference:
            sql = f"DELETE FROM ips WHERE ip = '{ip}'"
            db.execute(sql, "ip_db.db")
            sql = f"INSERT INTO ips(ip, time_connected) VALUES('{ip}', {time.time()}")
            db.execute(sql, "ip_db.db")

def reciebe_ip():
    while True:
        

