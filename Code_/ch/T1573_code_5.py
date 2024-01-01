from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def asymmetric_encrypt(public_key, message):
    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = cipher.encrypt(message)
    return cipher_text

def asymmetric_decrypt(private_key, cipher_text):
    cipher = PKCS1_OAEP.new(private_key)
    plain_text = cipher.decrypt(cipher_text)
    return plain_text