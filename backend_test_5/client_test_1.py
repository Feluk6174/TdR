import socket
import json

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connection.connect(("192.168.178.138", 30001))

msg = '{"type": "CLIENT"}'
print(msg)
#connection.send(msg.encode("utf-8"))

j = json.loads(msg)
print(j)

msg = '{"type": "REGISTER", "user_name": "Feluk6174", "public_key": 6174, "profile_picture": "hola com estas", "info": "your mom is a pinapple"}'
print(msg)
#connection.send(msg.encode("utf-8"))



#connection.close()