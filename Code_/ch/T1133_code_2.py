import socket
import subprocess

def check_remote_service(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    
    if result == 0:
        print(f"Port {port} is open on {host}")
    else:
        output = subprocess.getoutput(f"curl -I {host}:{port}")
        if "HTTP/1.1 200 OK" in output:
            print(f"Service {host}:{port} is accessible.")
        else:
            print(f"Service {host}:{port} is not accessible.")

check_remote_service("example.com", 443)