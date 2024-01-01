import socket

def trusted_relationship(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    data = sock.recv(1024).decode()
    return data

# 使用方式
host = "www.example.com"
port = 80
result = trusted_relationship(host, port)
print(result)