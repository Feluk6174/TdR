from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64
from Crypto.Signature import pss
from Crypto.Hash import SHA256

def gen_key(passphrase):
    secret_code = "Unguessable"
    key = RSA.generate(2048)
    encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                                  protection="scryptAndAES128-CBC")

    file_out = open("rsa_key.bin", "wb")
    file_out.write(encrypted_key)
    file_out.close()

    print(key.publickey().export_key())

def gen_hash(*args):
    message = ""
    for arg in args:
        message += arg
    print(message)
    return SHA256.new(message.encode("utf-8"))

def sign(key, *args):
    h = gen_hash(*args)
    
    signature =pss.new(key).sign(h)
    return base64.urlsafe_b64encode(signature)

def verify(pub_key, signature, *args):
    signature = base64.urlsafe_b64decode(signature)
    h = gen_hash(*args)
    verifier = pss.new(pub_key)

    try:
        verifier.verify(h, signature)
        return True

    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    key = RSA.import_key(open('rsa_key.bin').read(), passphrase="Unguessable")

    data = "Hola em dic Felix!"

    signature = sign(key, data)

    print(verify(key.public_key(), signature, data))


