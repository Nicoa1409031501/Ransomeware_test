import socket

# 連接到服務器
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

# 修改數據的傳輸
payload = b'Modified data'
sock.sendall(payload)

# 確認數據是否修改成功
received_data = sock.recv(1024)
if received_data == payload:
    print('Data modification successful')

# 關閉連接
sock.close()