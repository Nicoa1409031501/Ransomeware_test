import socket

def active_ip_scan(ip_range):
    open_ports = []
    
    for ip in ip_range:
        try:
            # 建立套接字並設定超時時間為1秒
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            
            # 嘗試連接目標IP的80端口
            result = s.connect_ex((ip, 80))
            
            # 如果連接成功，則將該IP記錄為開放的端口
            if result == 0:
                open_ports.append(ip)
            
            s.close()
        except:
            pass
    
    return open_ports

# 範例IP範圍
ip_range = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
open_ports = active_ip_scan(ip_range)
print("開放的IP端口：", open_ports)