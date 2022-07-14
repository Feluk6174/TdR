import api
import auth

conn = api.Connection()

auth.gen_key("Hola")
priv_key, pub_key = auth.get_keys("Hola")

print(pub_key)

with open("rsa_key.bin", "r") as f:
    keys_file = f.read()

conn.register_user("Feluk6174", auth.sanitize_key(pub_key.export_key().decode("utf-8")), auth.sanitize_key(keys_file), "13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390", "your mom is a pinnapple")
conn.post("Hello world!", "1", "Feluk6174", "0101010101", priv_key, pub_key)
conn.post("Hey aixo ja funciona, sembla", "2", "Feluk6174", "0101010101")
conn.post("I just wanted to save the world", "3", "Feluk6174", "0101010101")
conn.post("ja no se que dir", "4", "Feluk6174", "0101010101")
print(conn.get_posts("Feluk6174"))
print(conn.get_user("Feluk6174"))

#a5ea7fc9fb08c80525618acb7d6b5124a3c7f753d8dbbc12d6e669df777ba091
#a5ea7fc9fb08c80525618acb7d6b5124a3c7f753d8dbbc12d6e669df777ba091

#b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAySc/iy2HabBgq1a22xOy\neTcYnGNHTZ/9+c2yv16zVC+R8hubaBoR7KF0IgETklmNjIzAaS8hFq1W9ULdyDPr\njZt+g40MWaRhWmUsGlmzzU4QuUcTjYPGIG72WAxeokTXNfimADZqtYNGWIb6tUci\nvh0lD8LThoZyAiceJf9MvmxTkMlccaAB3s6s/Ru5TpBQ5I7NtQbe1Iz4uKZgSaO3\nXk1Wyrsvjrmd0zcM38TKNeYtsN4KfnhFuPZTpCTkzV+IzxSO+K48v8ld13VFjdxC\n5OhiQMLmfLTe/GNskvFVL5QLnP1y4uJMUPEAxpZhkZxP8edNYhn6zaqAdjyiOjcA\nQQIDAQAB\n-----END PUBLIC KEY-----'
#b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAySc/iy2HabBgq1a22xOy\neTcYnGNHTZ/9+c2yv16zVC+R8hubaBoR7KF0IgETklmNjIzAaS8hFq1W9ULdyDPr\njZt+g40MWaRhWmUsGlmzzU4QuUcTjYPGIG72WAxeokTXNfimADZqtYNGWIb6tUci\nvh0lD8LThoZyAiceJf9MvmxTkMlccaAB3s6s/Ru5TpBQ5I7NtQbe1Iz4uKZgSaO3\nXk1Wyrsvjrmd0zcM38TKNeYtsN4KfnhFuPZTpCTkzV+IzxSO+K48v8ld13VFjdxC\n5OhiQMLmfLTe/GNskvFVL5QLnP1y4uJMUPEAxpZhkZxP8edNYhn6zaqAdjyiOjcA\nQQIDAQAB\n-----END PUBLIC KEY-----'

#while True:
#    command = input("Command: ")
