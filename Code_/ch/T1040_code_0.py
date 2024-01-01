import scapy.all as scapy

def sniff_network_traffic(interface):
    scapy.sniff(iface=interface, prn=lambda x: x.summary())

# 執行
sniff_network_traffic("eth0")