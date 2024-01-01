from Cryptodome.Cipher import AES
   from Cryptodome.Random import get_random_bytes

   def pad(data):
       return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

   def encrypt_data(data, key):
       data = pad(data)
       cipher = AES.new(key, AES.MODE_ECB)
       encrypted_data = cipher.encrypt(data)
       return encrypted_data