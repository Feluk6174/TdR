import api
import auth

conn = api.Connection()

auth.gen_key("Hola")
priv_key, pub_key = auth.get_keys("Hola")

with open("rsa_key.bin", "r") as f:
    keys_file = f.read()

conn.register_user("Feluk6174", auth.sanitize_key(pub_key.export_key().decode("utf-8")), auth.sanitize_key(keys_file), "13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390", "your mom is a pinnapple")
conn.post("Hello world!", "1", "Feluk6174", "0101010101")
conn.post("Hey aixo ja funciona, sembla", "2", "Feluk6174", "0101010101")
conn.post("I just wanted to save the world", "3", "Feluk6174", "0101010101")
conn.post("ja no se que dir", "4", "Feluk6174", "0101010101")
print(conn.get_posts("Feluk6174"))
print(conn.get_user("Feluk6174"))

#while True:
#    command = input("Command: ")
