import socket
import json
import auth
import time
#todo func to change pp and info

class Connection():
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect(("195.181.244.246", 30003))

        msg = '{"type": "CLIENT"}'
        self.connection.send(msg.encode("utf-8"))
        if self.connection.recv(1024).decode("utf-8") == "OK":
            print("[ESTABLISHED CONNECTION]")

    def register_user(self, user_name:str, public_key, key_path:str, profile_picture:str, info:str):
        time_registered = int(time.time())
        public_key = auth.sanitize_key(public_key.export_key().decode("utf-8"))
        with open(key_path, "r") as f:
            keys_file = f.read()
        private_key = auth.sanitize_key(keys_file)
        msg = "{"+f'"type": "ACTION", "action": "REGISTER", "user_name": "{user_name}", "public_key": "{public_key}", "private_key": "{private_key}", "profile_picture": "{profile_picture}", "info": "{info}", "time": {time_registered}'+"}"
        temp = self.send(msg)
        print(temp, len(msg))
        response = self.recv()
        if not response == "OK":
            if response == "ALREADY EXISTS":
                raise UserAlreadyExists(user_name)
            elif response == "WRONG CHARS":
                raise WrongCaracters(user_name=user_name, public_key=public_key, profile_picture=profile_picture, info=info)
            elif response == "DATABASE ERROR":
                raise DatabaseError(msg)

    def post(self, content:str, post_id:str, user_name:str, flags:str, priv_key):
        time_posted = int(time.time())
        signature = auth.sign(priv_key, content, post_id, user_name, flags, time_posted).decode("utf-8")
        msg = "{"+f'"type": "ACTION", "action": "POST", "post_id": "{post_id}", "user_name": "{user_name}", "content": "{content}", "flags": "{flags}", "time": {time_posted}, "signature": "{signature}"'+"}"
        self.send(msg)
        response = self.recv()
        if not response == "OK":
            if response == "WRONG CHARS":
                raise WrongCaracters(user_name=user_name, public_key=content, profile_picture=post_id, info=flags)
            elif response == "WRONG SIGNATURE":
                raise WrongSignature()
            elif response == "DATABASE ERROR":
                raise DatabaseError(msg)

    def get_user_posts(self, user_name:str):
        #return format: {'id': 'str(23)', 'user_id': 'str(16)', 'content': 'str(255)', 'flags': 'str(10)', 'time_posted': int}
        posts = []
        msg = "{"+f'"type": "ACTION", "action": "GET POSTS", "user_name": "{user_name}"'+"}"
        self.send(msg)
        num = int(self.recv())
        self.send('{"type": "RESPONSE", "response": "OK"}')
        if not num == 0: 
            for _ in range(num):
                posts.append(json.loads(self.recv()))
                self.send('{"type": "RESPONSE", "response": "OK"}')
            response = self.recv()
            if not response == "OK":
                if response == "WRONG CHARS":
                    raise WrongCaracters(user_name=user_name)

            return posts
        response = self.recv()
        if not response == "OK":
            if response == "WRONG CHARS":
                raise WrongCaracters(user_name=user_name)
        return {}

    def get_user(self, user_name:str):
        msg = "{"+f'"type": "ACTION", "action": "GET USER", "user_name": "{user_name}"'+"}"
        self.send(msg.encode("utf-8"))
        response = self.recv()
        try:
            return json.loads(response)
        except json.decoder.JSONDecodeError:
            if response == "WRONG CHARS":
                raise WrongCaracters(user_name=user_name)
            return {}

    def close(self):
        self.connection.close()

    def get_post(self, post_id:str):
        msg = "{"+f'"type": "ACTION", "action": "GET POST", "post_id": "{post_id}"'+"}"
        self.send(msg.encode("utf-8"))
        response = self.recv()
        try:
            return json.loads(response)
        except json.decoder.JSONDecodeError:
            if response == "WRONG CHARS":
                raise WrongCaracters(post_id=post_id)
            return {}

    def send(self, msg):
        msg_len = len(msg)

        num = int(msg_len/1024)
        num = num + 1 if not msg_len % 1024 == 0 else num

        self.connection.send(str(num).encode("utf-8"))

        temp = self.connection.recv(1024).decode("utf-8")
        if not temp == "OK":
            print(temp)

        for i in range(num):
            print(i)
            self.connection.send(msg[1024*i:1024*i+1024].encode("utf-8"))
            temp = self.connection.recv(1024).decode("utf-8")
            if not temp == "OK":
                print(temp)

    def recv(self):
        num = int(self.connection.recv(1024).decode("utf-8"))
        self.connection.send("OK".encode("utf-8"))
        msg = ""
        for i in range(num):
            msg += self.connection.recv(1024).decode("utf-8")
            self.connection.send("OK".encode("utf-8"))

        return msg



def check_chars(*args):
    invalid_chars = ["\\", "\'", "\"", "\n", "\t", "\r", "\0", "%", "\b", ";", "="]

    arguments = ""
    for argument in args:
        arguments += argument


    for i, char in enumerate(invalid_chars):
        if char in arguments:
            return False, char
    return True, None


class UserAlreadyExists(Exception):
    def __init__(self, user_name):
        self.message = f"User {user_name} already exists"
        super().__init__(self.message)

class WrongCaracters(Exception):
    def __init__(self, **kwargs):
        self.message = "wtf"
        for key, value in kwargs.items():
            check, char = check_chars(value)
            if not check:
                self.message = f"{key}(value = {value}) contains the character {char}"
                
        super().__init__(self.message)

class WrongSignature(Exception):
    def __init__(self, **kwargs: object):
        super().__init__("key verification failed")

class DatabaseError(Exception):
    def __init__(self, request):
        super().__init__(f"The request '{request}' caused a database error")