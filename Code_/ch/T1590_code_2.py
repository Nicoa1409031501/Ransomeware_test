import nmap

# Gathering victim network information using python-nmap
def gather_network_info():
    target_ip = "192.168.0.0/24"  # Replace with target IP or subnet
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip, arguments='-p 1-65535 -sS -O')
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    print(f"Host: {host}, Port: {port}, State: {nm[host][proto][port]['state']}")

gather_network_info()