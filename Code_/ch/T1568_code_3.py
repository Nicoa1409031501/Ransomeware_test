import socket
import struct

# 1. 使用socket套件建立TCP連線，使用動態計算的IP地址和端口
def connect_tcp_dynamic(ip_calculation, port_calculation):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_calculation(), port_calculation()))
    return s

# 2. 使用socket套件建立UDP連線，使用動態計算的IP地址和端口
def connect_udp_dynamic(ip_calculation, port_calculation):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip_calculation(), port_calculation()))
    return s

# 3. 使用struct套件進行IP地址和端口的動態計算
def calculate_ip():
    ip_bytes = struct.pack('BBBB', 192, 168, 1, 1)  # 假設計算結果為192.168.1.1
    ip = socket.inet_ntoa(ip_bytes)
    return ip

def calculate_port():
    port = 8080  # 假設計算結果為8080
    return port