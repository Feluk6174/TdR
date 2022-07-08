import socket
import json

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.178.138", 30001))

with open("./user_data.json", "r") as f:
    text = f.read()

data = json.loads(text)
print(data)