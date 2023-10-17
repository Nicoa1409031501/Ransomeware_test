import os
with os.popen(r"net user",'r') as text:
    text_read=text.read()
print(text_read.splitlines()[5].split(' ')[0])
