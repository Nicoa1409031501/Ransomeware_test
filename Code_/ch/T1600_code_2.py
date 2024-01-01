from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data, AES.block_size)
    return cipher.encrypt(padded_data)

def decrypt(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    return unpad(decrypted_data, AES.block_size)

# Example usage
data = b"This is a secret message"
key = b"supersecretpassword"

encrypted_data = encrypt(data, key)
print(f"Encrypted data: {encrypted_data}")

decrypted_data = decrypt(encrypted_data, key)
print(f"Decrypted data: {decrypted_data}")