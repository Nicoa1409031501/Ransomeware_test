import socket
from scapy.all import *

def traffic_signaling(target_ip, target_port, magic_value):
    # 1. 建立socket連接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. 透過scapy發送符合特徵的封包
    send(IP(dst=target_ip)/TCP(dport=target_port, flags="S", seq=12345)/magic_value)
    
    # 3. 接收封包
    sniffed_packet = sniff(filter="tcp and src host {} and dst port {}".format(target_ip, target_port), count=1)
    
    # 4. 當符合特徵的封包抵達，開啟指定的防火牆規則或自定義軟體
    if sniffed_packet:
        os.system("iptables -A INPUT -p tcp --dport {} -j ACCEPT".format(target_port))
        print("Port {} is open!".format(target_port))
    else:
        print("Port {} is still closed.".format(target_port))