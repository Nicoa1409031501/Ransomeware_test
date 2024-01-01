import pyminifier

   def deobfuscate_python_code(obfuscated_code):
       decoded_code = pyminifier.minify(obfuscated_code)
       return decoded_code