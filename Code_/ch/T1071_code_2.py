import socket

def communicate_electronic_mail():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("smtp.example.com", 25))
    client.sendall("RCPT TO: <target@example.com>\r\n")
    response = client.recv(4096)
    client.close()
    print(response)

communicate_electronic_mail()