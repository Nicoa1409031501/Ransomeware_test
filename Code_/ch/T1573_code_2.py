from Crypto.Cipher import AES

def symmetric_encrypt(key, message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    cipher_text, tag = cipher.encrypt_and_digest(message)
    return nonce + cipher_text + tag

def symmetric_decrypt(key, cipher_text):
    nonce = cipher_text[:16]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plain_text = cipher.decrypt_and_verify(cipher_text[16:-16], cipher_text[-16:])
    return plain_text