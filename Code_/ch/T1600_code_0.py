from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt(data, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    return encryptor.update(padded_data) + encryptor.finalize()

def decrypt(encrypted_data, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return unpadder.update(decrypted_data) + unpadder.finalize()

# Example usage
data = b"This is a secret message"
key = b"supersecretpassword"

encrypted_data = encrypt(data, key)
print(f"Encrypted data: {encrypted_data}")

decrypted_data = decrypt(encrypted_data, key)
print(f"Decrypted data: {decrypted_data}")