import os
   
   def hide_file(file_path):
       os.system(f'attrib +h {file_path}')