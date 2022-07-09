import socket
import json
import time
import api


api.register_user("Feluk6174", 6174, "caracaracara", "your mom is a pinnapple")
api.post("Hello world!", "1", "Feluk6174", "010101")
api.post("Hey aixo ja funciona, sembla", "2", "Feluk6174", "010101")
api.post("I just wanted to save the world", "3", "Feluk6174", "010101")
api.post("ja no se que dir", "4", "Feluk6174", "010101")
print(api.get_posts("Feluk6174"))

#while True:
#    command = input("Command: ")