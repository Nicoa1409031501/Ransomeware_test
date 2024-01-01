import subprocess

def network_service_discovery(target_ip):
    command = f'nmap -p 1-1024 {target_ip}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    open_ports = []
    for line in result.stdout.splitlines():
        if '/tcp' in line and 'open' in line:
            port = line.split('/')[0]
            open_ports.append(port)
    
    return open_ports

target_ip = '192.168.0.1'
result = network_service_discovery(target_ip)
print(result)