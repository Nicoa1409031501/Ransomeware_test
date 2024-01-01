import nmap

def active_vulnerability_scan(target):
    open_ports = []
    
    # 建立nmap掃描器
    nm = nmap.PortScanner()
    
    # 使用預設參數掃描指定目標的所有端口
    result = nm.scan(target, arguments='-p-')
    
    # 遍歷每個掃描結果
    for port in nm[target]['tcp']:
        if nm[target]['tcp'][port]['state'] == 'open':
            open_ports.append(port)
    
    return open_ports

target = '192.168.0.1'
open_ports = active_vulnerability_scan(target)
print("開放的漏洞端口：", open_ports)