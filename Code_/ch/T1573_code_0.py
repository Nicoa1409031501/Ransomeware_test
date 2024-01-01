from cryptography.fernet import Fernet

def symmetric_encrypt(key, message):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(message)
    return cipher_text

def symmetric_decrypt(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text