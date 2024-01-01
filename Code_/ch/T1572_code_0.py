import socket

def tcp_tunnel():
    target_ip = '192.168.1.100'
    target_port = 1234
    
    tunnel_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tunnel_socket.connect((target_ip, target_port))
    
    # 在這裡進行隧道化的內容
    
    tunnel_socket.close()