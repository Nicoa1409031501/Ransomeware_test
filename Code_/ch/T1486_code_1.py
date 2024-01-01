from cryptography.fernet import Fernet

   def encrypt_data(data, key):
       cipher_suite = Fernet(key)
       encrypted_data = cipher_suite.encrypt(data)
       return encrypted_data