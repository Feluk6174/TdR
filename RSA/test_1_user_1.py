from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

Username = "anijack"
Password = "Anijack2005!"
message = ""
secure_document = "secret_info"
priv_my_key_storage = "test_keys_priv_1.pem"
pub_my_key_storage = "test_keys_pub_1.pem"
pub_other_key_storage = "test_keys_pub_2.pem"
enc_data_file = "encrypted_data" 
#or dec_ + secure_document

def gen_key(Username, Password, priv_my_key_storage, pub_my_key_storage):
    secret_code = (str(Username) + str(Password))

    key = RSA.generate(2048)

    private_key = key.export_key(passphrase = secret_code, pkcs = 8, protection = "scryptAndAES128-CBC")
    file_out = open(priv_my_key_storage, "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open(pub_my_key_storage, "wb")
    file_out.write(public_key)
    file_out.close()


def encrypt(message, sec_doc, pub_other_key_storage, enc_data_file):
    if sec_doc != "":
        file_to_encode = open(sec_doc, "r").read()
        data = file_to_encode.encode("utf-8")
        #file_out = open("enc_" + sec_doc, "wb")
        file_out = open(enc_data_file, "wb")

    elif message != "":
        data = message.encode("utf-8")
        file_out = open(enc_data_file, "wb")

    recipient_key = RSA.import_key(open(pub_other_key_storage).read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()

#gen_key(Username, Password, priv_my_key_storage, pub_my_key_storage)
encrypt(message, secure_document, pub_other_key_storage, enc_data_file)
