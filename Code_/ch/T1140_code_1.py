import hashlib

   def deobfuscate_hash(hash_value):
       decoded_hash = hashlib.decode(hash_value)
       return decoded_hash