import socket

# 1. 使用socket套件建立TCP連線
def connect_tcp(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

# 2. 使用socket套件建立UDP連線
def connect_udp(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    return s

# 3. 使用socket套件進行DNS解析
def resolve_dns(domain):
    ip = socket.gethostbyname(domain)
    return ip

# 4. 使用socket套件進行DNS反向解析
def reverse_resolve_dns(ip):
    domain = socket.gethostbyaddr(ip)[0]
    return domain