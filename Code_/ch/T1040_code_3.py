from scapy.all import *
from scapy.layers.http import HTTPRequest

def sniff_network_traffic(interface):
    sniff(iface=interface, filter="tcp port 80", prn=lambda x: x.show())

# 執行
sniff_network_traffic("eth0")