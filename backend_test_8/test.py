import json

try:
    json.loads("jkkk")
except json.decoder.JSONDecodeError:
    print("2")