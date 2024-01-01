import socket

def communicate_web_traffic():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("remote_server", 80))
    client.sendall("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    response = client.recv(4096)
    client.close()
    print(response)

communicate_web_traffic()