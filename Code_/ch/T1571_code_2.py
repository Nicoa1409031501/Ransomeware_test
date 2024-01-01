import nmap

def check_non_standard_port(hostname, port):
    try:
        scanner = nmap.PortScanner()
        result = scanner.scan(hostname, str(port))
        state = result['scan'][hostname]['tcp'][port]['state']
        if state == 'open':
            print("Non-Standard Port", port, "is open")
        else:
            print("Non-Standard Port", port, "is closed")
    except nmap.PortScannerError as err:
        print("Exception:", err)

# 使用範例
check_non_standard_port("example.com", 8088)