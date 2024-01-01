from scapy.all import *

def content_injection():
    #建立一個IP封包，目的IP為受害者IP
    packet = IP(dst="受害者IP")/TCP(dport=80)/Raw(load="惡意內容")
    
    #發送封包
    send(packet)

content_injection()