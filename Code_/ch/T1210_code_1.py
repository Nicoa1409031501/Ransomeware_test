services = [
    {"ip": "192.168.0.1", "port": 80},
    {"ip": "192.168.0.2", "port": 22},
    {"ip": "192.168.0.3", "port": 443}
]

for service in services:
    check_remote_service(service["ip"], service["port"])