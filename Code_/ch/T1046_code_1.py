import nmap

def network_service_discovery(target_ip):
    nm = nmap.PortScanner()
    nm.scan(target_ip, '1-1024')
    
    open_ports = []
    for host in nm.all_hosts():
        for port in nm[host].all_tcp():
            if nm[host]['tcp'][port]['state'] == 'open':
                open_ports.append(port)
    
    return open_ports

target_ip = '192.168.0.1'
result = network_service_discovery(target_ip)
print(result)