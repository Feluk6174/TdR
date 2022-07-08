import socket
import json
import time

#connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connection.connect(("192.168.178.138", 30001))

msg = '{"type": "CLIENT"}'
print(msg)
#connection.send(msg.encode("utf-8"))


time.sleep(1)

msg = '{"type": "REGISTER", "user_name": "Feluk6174", "public_key": 6174, "profile_picture": "hola com estas", "info": "your mom is a pinapple"}'
print(msg)
print(msg.encode("utf").decode("utf-8"))
print(json.dumps(json.loads(msg)))
#connection.send(msg.encode("utf-8"))

time.sleep(1)

#connection.close()