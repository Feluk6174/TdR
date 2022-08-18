import api
import auth
from Crypto.Hash import SHA256

conn = api.Connection()

auth.gen_key("Hola")
priv_key, pub_key = auth.get_keys("Hola")

print(priv_key.export_key())

with open("rsa_key.bin", "r") as f:
    keys_file = f.read()

conn.register_user("Feluk6174", pub_key, "rsa_key.bin", "13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390", "your mom is a pinnapple")
conn.post("Hello world!", "1", "Feluk6174", "0101010101", priv_key)
conn.post("Hey aixo ja funciona, sembla", "2", "Feluk6174", "0101010101", priv_key)
conn.post("I just wanted to save the world", "3", "Feluk6174", "0101010101", priv_key)
conn.post("ja no se que dir", "4", "Feluk6174", "0101010101", priv_key)
print(conn.get_user_posts("Feluk6174"))
print(conn.get_post("1"))
print(conn.get_user("Feluk6174"))

#b65672e9397175e9c099e86c608f2c5c10e48680172cd126e9ac14dfa3df534a
#b65672e9397175e9c099e86c608f2c5c10e48680172cd126e9ac14dfa3df534a

#056e80877c57b931b5666694ed06ec8cb2259234f95d75c4a9bb815791503f35
#056e80877c57b931b5666694ed06ec8cb2259234f95d75c4a9bb815791503f35

#b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArxw4jr4UdsuAsKZmh0jp\nn+DAQmz3dKO7et7FuWscYZNIXHSK/H1h9WQlqqqrtpVVKeYm7aGbHQ+DI1aBvZn4\nvXnf1d4Z6dYRZzZ6vcJEf5XZ3QsvZYNo36Y1aUXfZ+rbPsH2S3zGyYj/Plqi8F64\njO11lWu4+YTFA7C/DmFO8jVigyFKRsPiKsYYf2MMhQFZcv/hjYPOqfMjHhnp2lG8\niuRgaBtPAmUwSTjad8tVF9w2T/j+fz/MGNbhFz7rkYbfBy5Z/DjItw5/lSiQcnKg\nS0cck60ZR46N4YTE4Tp2OXcP0+O73q5BwgJbmkQc3oHNRPohEkqsADxJN3wK76G/\nTwIDAQAB\n-----END PUBLIC KEY-----'
#b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArxw4jr4UdsuAsKZmh0jp\nn+DAQmz3dKO7et7FuWscYZNIXHSK/H1h9WQlqqqrtpVVKeYm7aGbHQ+DI1aBvZn4\nvXnf1d4Z6dYRZzZ6vcJEf5XZ3QsvZYNo36Y1aUXfZ+rbPsH2S3zGyYj/Plqi8F64\njO11lWu4+YTFA7C/DmFO8jVigyFKRsPiKsYYf2MMhQFZcv/hjYPOqfMjHhnp2lG8\niuRgaBtPAmUwSTjad8tVF9w2T/j+fz/MGNbhFz7rkYbfBy5Z/DjItw5/lSiQcnKg\nS0cck60ZR46N4YTE4Tp2OXcP0+O73q5BwgJbmkQc3oHNRPohEkqsADxJN3wK76G/\nTwIDAQAB\n-----END PUBLIC KEY-----''

#while True:
#    command = input("Command: ")
