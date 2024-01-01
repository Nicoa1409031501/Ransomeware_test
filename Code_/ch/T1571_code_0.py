import socket

def check_non_standard_port(hostname, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostname, port))
        if result == 0:
            print("Non-Standard Port", port, "is open")
        else:
            print("Non-Standard Port", port, "is closed")
        sock.close()
    except socket.error as err:
        print("Exception:", err)

# 使用範例
check_non_standard_port("example.com", 8088)