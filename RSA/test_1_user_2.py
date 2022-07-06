from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


Username = "feluk"
Password = "Feluk6174!"
data_file = "encrypted_data"
#data_file = "enc_" + "secret_info"
decrypted_data_file = "decrypted_data"
priv_my_key_storage = "test_keys_priv_2.pem"
pub_my_key_storage = "test_keys_pub_2.pem"


def gen_key_2(Username, Password, priv_my_key_storage, pub_my_key_storage):
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


def decrypt(data_file, Username, Password, priv_my_key_storage, decrypted_data_file):
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

    decrypted_file = open(decrypted_data_file, "w").write(message)
    

#gen_key_2(Username, Password, priv_my_key_storage, pub_my_key_storage)
decrypt(data_file, Username, Password, priv_my_key_storage, decrypted_data_file)