import pyshark

def sniff_network_traffic(interface):
    capture = pyshark.LiveCapture(interface=interface)
    for packet in capture.sniff_continuously():
        print(packet)

# 執行
sniff_network_traffic("eth0")