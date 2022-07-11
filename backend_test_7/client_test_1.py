import socket
import json
import time
import api


api.register_user("Feluk6174", 6174, "13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390", "your mom is a pinnapple")
api.post("Hello world!", "1", "Feluk6174", "0101010101")
api.post("Hey aixo ja funciona, sembla", "2", "Feluk6174", "0101010101")
api.post("I just wanted to save the world", "3", "Feluk6174", "0101010101")
api.post("ja no se que dir", "4", "Feluk6174", "0101010101")
print(api.get_posts("Feluk6174"))
print(api.get_user("Feluk6174"))

#while True:
#    command = input("Command: ")