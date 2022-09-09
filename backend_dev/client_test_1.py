import api
import auth
from Crypto.Hash import SHA256

conn = api.Connection()

auth.gen_key("Hola")
priv_key, pub_key = auth.get_keys("Hola")

print(priv_key.export_key())

with open("rsa_key.bin", "r") as f:
    keys_file = f.read()
print(1.1)
conn.register_user("Feluk6174", pub_key, "rsa_key.bin", "13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390", "your mom is a pinnapple")
print(2.1)
conn.post("Hello world!", "1", "Feluk6174", "0101101010", priv_key)
print(3.1)
conn.post("Hey aixo ja funciona, sembla", "2", "Feluk6174", "0100010101", priv_key)
print(4.1)
conn.post("I just wanted to save the world", "3", "Feluk6174", "0101010101", priv_key)
print(5.1)
conn.post("ja no se que dir", "4", "Feluk6174", "0101010101", priv_key)
print(6.1)
print(conn.get_posts(user_name="Feluk6174"))
print(7.1)
print(conn.get_posts(include_flags="0000100000"))
print(8.1)
print(conn.get_posts(exclude_flags="0001000000"))
print(9.1)
print(conn.get_posts(hashtag="ja", user_name="Feluk6174", exclude_flags="0001000000"))
print(10.1)
print(conn.get_posts(hashtag="ja", sort_by="id", sort_order="desc"))
print(11.1)
print(conn.get_posts(num=2))
print(12.1)
print(conn.get_post("1"))
print(13.1)
print(conn.get_user("Feluk6174"))