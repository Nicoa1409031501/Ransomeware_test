from scapy.all import *
from iptcinfo import IPTCInfo

def traffic_signaling(target_ip, target_port, magic_value):
    # 1. 使用scapy發送符合特徵的封包
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, flags="S", seq=12345)
    packet = ip/tcp/magic_value
    send(packet)

    # 2. 使用iptables-wrapper讀取和修改防火牆規則
    info = IPTCInfo()
    info.load()  # 讀取目前的規則

    # 搜尋符合目標IP與目標Port的規則
    delete_index = -1
    for i, rule in enumerate(info.rules):
        if rule['dst'] == target_ip and rule['dport'] == str(target_port):
            delete_index = i

    # 若存在符合的規則則刪除，否則增加一個新規則
    if delete_index != -1:
        del info.rules[delete_index]
        info.save()
        print("Port {} is open!".format(target_port))
    else:
        new_rule = {'dst': target_ip, 'proto': 'tcp', 'dport': str(target_port)}
        info.rules.append(new_rule)
        info.save()
        print("Port {} is closed.".format(target_port))