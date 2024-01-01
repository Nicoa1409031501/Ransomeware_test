from urllib.parse import unquote

   def deobfuscate_url(url_encoded_string):
       decoded_string = unquote(url_encoded_string)
       return decoded_string