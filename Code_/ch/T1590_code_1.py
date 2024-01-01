import socket

# Gathering victim network information using socket
def gather_network_info():
    target_ip = "192.168.0.0"  # Replace with target IP or subnet
    for port in range(1, 65536):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(0.5)
        result = client_socket.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        client_socket.close()

gather_network_info()