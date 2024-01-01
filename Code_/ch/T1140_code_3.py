import gzip

   def deobfuscate_gzip(compressed_file):
       with gzip.open(compressed_file, 'rb') as f:
           decompressed_data = f.read()
       return decompressed_data