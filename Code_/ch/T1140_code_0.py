import base64

   def deobfuscate_base64(encoded_string):
       decoded_string = base64.b64decode(encoded_string).decode('utf-8')
       return decoded_string