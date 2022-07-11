import socket
import json
import time

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.178.138", 30003))

msg = '{"type": "CLIENT"}'
connection.send(msg.encode("utf-8"))
if connection.recv(1024).decode("utf-8") == "OK":
    print("[ESTABLISHED CONNECTION]")

def register_user(user_name:str, public_key:str, profile_picture:str, info:str):
    global connection
    msg = "{"+f'"type": "ACTION", "action": "REGISTER", "user_name": "{user_name}", "public_key": "{public_key}", "profile_picture": "{profile_picture}", "info": "{info}"'+"}"
    connection.send(msg.encode("utf-8"))
    response = connection.recv(1024).decode("utf-8")
    if not response == "OK":
        print(response)


def post(content:str, post_id:str, user_name:str, flags:str):
    global connection
    msg = "{"+f'"type": "ACTION", "action": "POST", "post_id": "{post_id}", "user_name": "{user_name}", "content": "{content}", "flags": "{flags}"'+"}"
    connection.send(msg.encode("utf-8"))
    response = connection.recv(1024).decode("utf-8")
    if not response == "OK":
        print(response)

def get_posts(user_name:str):
    #return format: {'id': 'str(23)', 'user_id': 'str(16)', 'content': 'str(255)', 'flags': 'str(10)', 'time_posted': int}
    global connection
    posts = []
    msg = "{"+f'"type": "ACTION", "action": "GET POSTS", "user_name": "{user_name}"'+"}"
    connection.send(msg.encode("utf-8"))
    num = int(connection.recv(1024).decode("utf-8"))
    connection.send('{"type": "RESPONSE", "response": "OK"}'.encode("utf-8"))
    if not num == 0: 
        for _ in range(num):
            posts.append(json.loads(connection.recv(1024).decode("utf-8")))
            connection.send('{"type": "RESPONSE", "response": "OK"}'.encode("utf-8"))
        response = connection.recv(1024).decode("utf-8")
        if not response == "OK":
            print(response)
        print(posts)
        return posts
    print("{}")
    return {}

def get_user(user_name:str):
    global connection
    msg = "{"+f'"type": "ACTION", "action": "GET USER", "user_name": "{user_name}"'+"}"
    connection.send(msg.encode("utf-8"))
    response = connection.recv(1024).decode("utf-8")
    print(1, response)
    return json.loads(response)

def close():
    global connection
    connection.close()



