from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import Crypto.Hash.MD5 as MD5
import base64
from Crypto.Signature import pss
from Crypto.Hash import SHA256

text = "Hello world"

secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")

with open("rsa_key.bin", "w") as file_out:
    file_out.write(encrypted_key.decode("utf-8"))


message = 'Hello world'

#key = RSA.import_key(open('rsa_key.bin').read())
key = RSA.import_key(open('rsa_key.bin').read(), passphrase=secret_code)

h = SHA256.new(message.encode("utf-8"))

print(h.digest())

signature = pss.new(key).sign(h)

print(signature)

verifier = pss.new(key)


try:
    verifier.verify(h, signature)
    print("The signature is authentic.")

except (ValueError, TypeError):
    print("The signature is not authentic.")