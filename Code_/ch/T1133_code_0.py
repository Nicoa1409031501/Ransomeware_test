import socket

def check_remote_service(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    
    if result == 0:
        print(f"Port {port} is open on {host}")
    else:
        print(f"Port {port} is closed on {host}")

check_remote_service("example.com", 443)