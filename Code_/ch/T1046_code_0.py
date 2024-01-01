import socket

def network_service_discovery(target_ip):
    open_ports = []
    
    # Scan common ports
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

target_ip = '192.168.0.1'
result = network_service_discovery(target_ip)
print(result)