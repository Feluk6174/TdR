import api
import auth


conn = api.Connection()

password = "Hola"
auth.gen_key(password)
priv_key, pub_key = auth.get_keys(password)

print(priv_key.export_key())

user_name = "login_10"

with open("rsa_key.bin", "r") as f:
    keys_file = f.read()
    
print(1.1)
conn.register_user(user_name, pub_key, "rsa_key.bin", "13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390", "your mom is a pinnapple")
print(2.1)
conn.post("Hello world!", user_name, user_name, "0101101010", priv_key)
print(3.1)
"""conn.post("Hey aixo ja funciona, sembla", "2", user_name, "0100010101", priv_key)
print(4.1)
conn.change_info(user_name, "a"*128, priv_key)
print(5.1)
conn.post("ja no se que dir", "4", user_name, "0101010101", priv_key)
print(6.1)"""
print(conn.get_posts(user_name=user_name))
"""print(6.1)
print(conn.get_posts(user_name=user_name))
print(7.1)
print(conn.get_posts(include_flags="0000100000"))
print(8.1)
print(conn.get_posts(exclude_flags="0001000000"))
print(9.1)
print(conn.get_posts(hashtag="ja", user_name=user_name, exclude_flags="0001000000"))
print(10.1)
print(conn.get_posts(hashtag="ja", sort_by="id", sort_order="desc"))
print(11.1)
print(conn.get_posts(num=2))
print(12.1)
print(conn.get_post("1"))
print(13.1)
print(conn.get_user(user_name))"""

print(7.1)
with open("rsa_key.bin", "w") as f:
    f.write("")
priv_key = None

print(7.2)
key = conn.get_user(user_name=user_name)["private_key"]
print(key)
print(7.3)
auth.login(key, password)
priv_key, pub_key = auth.get_keys(password)
print(8.1)
conn.post("login?", user_name+"1", user_name, "0101010101", priv_key)
print(9.1)
print(conn.get_posts(user_name=user_name))


