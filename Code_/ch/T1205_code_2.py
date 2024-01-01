import subprocess
import socket
import time

def traffic_signaling(target_ip, target_port, magic_value):
    # 1. 使用socket套件建立連接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 透過socket發送符合特徵的封包
    s.connect((target_ip, target_port))
    s.sendall(magic_value.encode())

    # 3. 暫停適當時間以等待回應
    time.sleep(1)

    # 4. 使用subprocess執行開啟關閉的系統命令
    if is_port_open(target_ip, target_port):
        subprocess.call(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(target_port), "-j", "ACCEPT"])
        print("Port {} is open!".format(target_port))
    else:
        subprocess.call(["iptables", "-D", "INPUT", "-p", "tcp", "--dport", str(target_port), "-j", "ACCEPT"])
        print("Port {} is closed.".format(target_port))

def is_port_open(target_ip, target_port):
    # 使用socket套件檢查端口是否開啟
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target_ip, target_port))
    if result == 0:
        return True  # 端口開啟
    else:
        return False  # 端口關閉