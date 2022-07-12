import socket
import json

class Connection():
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect(("192.168.178.138", 30003))

        msg = '{"type": "CLIENT"}'
        self.connection.send(msg.encode("utf-8"))
        if self.connection.recv(1024).decode("utf-8") == "OK":
            print("[ESTABLISHED CONNECTION]")

    def register_user(self, user_name:str, public_key:str, profile_picture:str, info:str):
        msg = "{"+f'"type": "ACTION", "action": "REGISTER", "user_name": "{user_name}", "public_key": "{public_key}", "profile_picture": "{profile_picture}", "info": "{info}"'+"}"
        self.connection.send(msg.encode("utf-8"))
        response = self.connection.recv(1024).decode("utf-8")
        if not response == "OK":
            if response == "ALREADY EXISTS":
                raise UserAlreadyExists(user_name)
            elif response == "WRONG CHARS":
                raise WrongCaracters(user_name=user_name, public_key=public_key, profile_picture=profile_picture, info=info)


    def post(self, content:str, post_id:str, user_name:str, flags:str):
        msg = "{"+f'"type": "ACTION", "action": "POST", "post_id": "{post_id}", "user_name": "{user_name}", "content": "{content}", "flags": "{flags}"'+"}"
        self.connection.send(msg.encode("utf-8"))
        response = self.connection.recv(1024).decode("utf-8")
        if not response == "OK":
            print(response)

    def get_posts(self, user_name:str):
        #return format: {'id': 'str(23)', 'user_id': 'str(16)', 'content': 'str(255)', 'flags': 'str(10)', 'time_posted': int}
        posts = []
        msg = "{"+f'"type": "ACTION", "action": "GET POSTS", "user_name": "{user_name}"'+"}"
        self.connection.send(msg.encode("utf-8"))
        num = int(self.connection.recv(1024).decode("utf-8"))
        self.connection.send('{"type": "RESPONSE", "response": "OK"}'.encode("utf-8"))
        if not num == 0: 
            for _ in range(num):
                posts.append(json.loads(self.connection.recv(1024).decode("utf-8")))
                self.connection.send('{"type": "RESPONSE", "response": "OK"}'.encode("utf-8"))
            response = self.connection.recv(1024).decode("utf-8")
            if not response == "OK":
                print(response)

            return posts
        if not response == "OK":
            print(response)
        return {}

    def get_user(self, user_name:str):
        msg = "{"+f'"type": "ACTION", "action": "GET USER", "user_name": "{user_name}"'+"}"
        self.connection.send(msg.encode("utf-8"))
        response = self.connection.recv(1024).decode("utf-8")
        try:
            return json.loads(response)
        except json.decoder.JSONDecodeError:
            print(response)
            return {}

    def close(self):
        self.connection.close()

def check_chars(argument:str):
    invalid_chars = ["\\", "\'", "\"", "\n", "\t", " ", "\r", "\0", "%", "\b", "-", ";", "="]

    for i, char in enumerate(invalid_chars):
        if char in argument:
            print(char, i)
            return False, char
    return True, None

class UserAlreadyExists(Exception):
    def __init__(self, user_name):
        self.message = f"User {user_name} already exists"
        super().__init__(self.message)

class WrongCaracters(Exception):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            check, char = check_chars(value)
            if not check:
                self.message = f"{key}(value = {value}) contains the character {char}"
        self.message = "wtf"
        super().__init__(self.message)