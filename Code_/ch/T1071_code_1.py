import socket

def communicate_transferring_files():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("remote_server", 21))
    client.sendall("USER anonymous\r\n")
    response = client.recv(4096)
    client.close()
    print(response)

communicate_transferring_files()