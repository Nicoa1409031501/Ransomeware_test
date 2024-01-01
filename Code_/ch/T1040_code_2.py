import socket

def sniff_network_traffic():
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    while True:
        packet, addr = sock.recvfrom(65535)
        print(packet)

# 執行
sniff_network_traffic()