import socket
   
def establish_connection():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect(('127.0.0.1', 8888))