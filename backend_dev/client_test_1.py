import api
import auth
from Crypto.Hash import SHA256

conn = api.Connection()

auth.gen_key("Hola")
priv_key, pub_key = auth.get_keys("Hola")

print(priv_key.export_key())

user_name = "test"

with open("rsa_key.bin", "r") as f:
    keys_file = f.read()
print(1.1)
conn.register_user(user_name, pub_key, "rsa_key.bin", "13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390", "your mom is a pinnapple")
print(2.1)
conn.post("Hello world!", "1", user_name, "0101101010", priv_key)
print(3.1)
conn.post("Hey aixo ja funciona, sembla", "2", user_name, "0100010101", priv_key)
print(4.1)
conn.post("I just wanted to save the world", "3", user_name, "0101010101", priv_key)
print(5.1)
conn.post("ja no se que dir", "4", user_name, "0101010101", priv_key)
print(6.1)
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
<<<<<<< HEAD
print(conn.get_user(user_name))

#b65672e9397175e9c099e86c608f2c5c10e48680172cd126e9ac14dfa3df534a
#b65672e9397175e9c099e86c608f2c5c10e48680172cd126e9ac14dfa3df534a

#056e80877c57b931b5666694ed06ec8cb2259234f95d75c4a9bb815791503f35
#056e80877c57b931b5666694ed06ec8cb2259234f95d75c4a9bb815791503f35

#b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArxw4jr4UdsuAsKZmh0jp\nn+DAQmz3dKO7et7FuWscYZNIXHSK/H1h9WQlqqqrtpVVKeYm7aGbHQ+DI1aBvZn4\nvXnf1d4Z6dYRZzZ6vcJEf5XZ3QsvZYNo36Y1aUXfZ+rbPsH2S3zGyYj/Plqi8F64\njO11lWu4+YTFA7C/DmFO8jVigyFKRsPiKsYYf2MMhQFZcv/hjYPOqfMjHhnp2lG8\niuRgaBtPAmUwSTjad8tVF9w2T/j+fz/MGNbhFz7rkYbfBy5Z/DjItw5/lSiQcnKg\nS0cck60ZR46N4YTE4Tp2OXcP0+O73q5BwgJbmkQc3oHNRPohEkqsADxJN3wK76G/\nTwIDAQAB\n-----END PUBLIC KEY-----'
#b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArxw4jr4UdsuAsKZmh0jp\nn+DAQmz3dKO7et7FuWscYZNIXHSK/H1h9WQlqqqrtpVVKeYm7aGbHQ+DI1aBvZn4\nvXnf1d4Z6dYRZzZ6vcJEf5XZ3QsvZYNo36Y1aUXfZ+rbPsH2S3zGyYj/Plqi8F64\njO11lWu4+YTFA7C/DmFO8jVigyFKRsPiKsYYf2MMhQFZcv/hjYPOqfMjHhnp2lG8\niuRgaBtPAmUwSTjad8tVF9w2T/j+fz/MGNbhFz7rkYbfBy5Z/DjItw5/lSiQcnKg\nS0cck60ZR46N4YTE4Tp2OXcP0+O73q5BwgJbmkQc3oHNRPohEkqsADxJN3wK76G/\nTwIDAQAB\n-----END PUBLIC KEY-----''

#while True:
#    command = input("Command: ")
=======
print(conn.get_user("Feluk6174"))
>>>>>>> 53f262aa13ba0c585eb62cec2fbf1be2efc3c0f7
