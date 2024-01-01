from scapy.all import *

def send_udp():
    target_ip = "192.168.1.100"  # 目標IP地址
    payload = b"Hello, C2 server!"  # 要傳送的資料

    packet = IP(dst=target_ip)/UDP(dport=12345)/Raw(load=payload)
    send(packet)

send_udp()