import socket
import json
import time
import api

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.178.138", 30001))

msg = '{"type": "CLIENT"}'
print(msg)
connection.send(msg.encode("utf-8"))


api.register_user("Feluk6174", 6174, "caracaracara", "your mom is a pinnapple")

api.post("Hello world!", "1", "Feluk6174")

print(api.get_posts("Feluk6174"))