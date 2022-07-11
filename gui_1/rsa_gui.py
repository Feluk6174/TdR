from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import acces_my_info


def gen_key(Username, Password):
    print("2")
    priv_my_key_storage = "priv_my_key_storage.pem"
    pub_my_key_storage = "pub_my_key_storage.pem"
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
    print("3")


def encrypt(message, sec_doc, pub_other_key_1):
    enc_data_file = "encoded_message.pem"
    pub_other_key_storage = open("public_other_key.pem", "w")
    pub_other_key_storage.write(pub_other_key_1)
    pub_other_key_storage.close()

    if sec_doc != "":
        file_to_encode = open(sec_doc, "r").read()
        data = file_to_encode.encode("utf-8")
        #file_out = open("enc_" + sec_doc, "wb")
        file_out = open(enc_data_file, "wb")

    elif message != "":
        data = message.encode("utf-8")
        file_out = open(enc_data_file, "wb")

    recipient_key = RSA.import_key(open("public_other_key.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()
    fin_mess = open(enc_data_file, "r")
    f = fin_mess.read()
    fin_mess.close()
    return f



def decrypt(data_file, s_message):
    Username = acces_my_info.GetName()
    Password = acces_my_info.GetPassword()
    decrypted_data_file = "decrypted_data.pem"
    priv_my_key_storage = "pub_my_key_storage.pem"
    
    if data_file == "":
        file_to_decode = open("to_decode.pem", "w")
        file_to_decode.write(s_message)
        file_to_decode.close()
        file_in = open("to_decode.pem", "wb")

    elif s_message == "":
        file_in = open(data_file, "rb")

    secret_code = (str(Username) + str(Password))
    encoded_key = open(priv_my_key_storage, "rb").read()
    private_key = RSA.import_key(encoded_key, passphrase=secret_code)
    
    enc_session_key, nonce, tag, ciphertext = \
    [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    message = data.decode("utf-8")

    decrypted_file = open(decrypted_data_file, "w")
    decrypted_file.write(message)
    decrypted_file.close

    return message
    

