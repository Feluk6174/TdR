import socket
import json
import time
import api

api.register_user("Feluk6174", 6174, "caracaracara", "your mom is a pinnapple")

api.post("Hello world!", "1", "Feluk6174")

print(api.get_posts("Feluk6174"))