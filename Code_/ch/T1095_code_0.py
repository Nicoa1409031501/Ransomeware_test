import socket

def send_icmp():
    target_ip = "192.168.1.100"  # 目標IP地址
    payload = b"Hello, C2 server!"  # 要傳送的資料

    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.sendto(payload, (target_ip, 0))
    sock.close()

send_icmp()