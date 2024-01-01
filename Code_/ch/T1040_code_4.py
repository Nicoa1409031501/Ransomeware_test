import subprocess

def sniff_network_traffic(interface):
    command = f"tcpdump -i {interface}"
    subprocess.call(command.split())

# 執行
sniff_network_traffic("eth0")