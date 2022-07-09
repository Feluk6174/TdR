import socket
import json
import time
import api

api.register_user("Feluk6174", 6174, "caracaracara", "your mom is a pinnapple")
time.sleep(1)
api.post("Hello world!", "1", "Feluk6174")
time.sleep(1)
api.post("Hey aixo ja funciona, sembla", "2", "Feluk6174")
time.sleep(1)
api.post("I just wanted to save the world", "3", "Feluk6174")
time.sleep(1)
api.post("ja no se que dir", "4", "Feluk6174")
time.sleep(1)
print(api.get_posts("Feluk6174"))

#while True:
#    command = input("Command: ")