import auth
import socket
import time
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

auth.gen_key("Hola")
priv_key, pub_key = auth.get_keys("Hola")

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("127.0.0.1", 2222))

connection.send(auth.sanitize_key(pub_key.export_key().decode("utf-8")).encode("utf-8"))
 
time.sleep(1)
data = "Hello World"
connection.send(data.encode("utf-8"))

time.sleep(1)

signature = auth.sign(priv_key, data)

connection.send(signature)

print(pub_key)
print(data)
print(signature)

print(auth.verify(pub_key, signature, data))
print("sent")