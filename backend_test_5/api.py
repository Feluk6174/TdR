import socket
import json
import time

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.178.138", 30003))

msg = '{"type": "CLIENT"}'
connection.send(msg.encode("utf-8"))

time.sleep(1)

def register_user(user_name, public_key, profile_picture, info):
    global connection
    print(1)
    msg = "{"+f'"type": "REGISTER", "user_name": "{user_name}", "public_key": {public_key}, "profile_picture": "{profile_picture}", "info": "{info}"'+"}"
    connection.send(msg.encode("utf-8"))
    response = connection.recv(1024).decode("utf-8")
    if not response == "OK":
        print(response)
    time.sleep(1)


def post(content, post_id, user_name, flags):
    global connection
    print(2)
    msg = "{"+f'"type": "POST", "post_id": "{post_id}", "user_name": "{user_name}", "content": "{content}", "flags": "{flags}"'+"}"
    connection.send(msg.encode("utf-8"))
    response = connection.recv(1024).decode("utf-8")
    if not response == "OK":
        print(response)
    time.sleep(1)


def get_posts(user_name):
    print(3)
    global connection
    posts = []
    msg = "{"+f'"type": "GET POSTS", "user_name": "{user_name}"'+"}"
    connection.send(msg.encode("utf-8"))
    num = int(connection.recv(1024).decode("utf-8"))
    connection.send("OK".encode("utf-8"))
    for _ in range(num):
        posts.append(json.loads(connection.recv(1024).decode("utf-8")))
        connection.send("OK".encode("utf-8"))
    time.sleep(1)
    return posts

def close():
    global connection
    connection.close()



