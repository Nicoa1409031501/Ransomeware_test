import socket

def communicate_dns():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b"example.com", ("dns_server", 53))
    response, _ = client.recvfrom(4096)
    client.close()
    print(response)

communicate_dns()