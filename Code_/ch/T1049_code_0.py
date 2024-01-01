import socket

def system_network_connections_discovery(host, port=80):
    # 使用socket建立TCP連接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # 發送網絡查詢命令
    request = "GET / HTTP/1.1\r\n\r\n"
    s.send(request.encode())

    # 接收並解析回傳的資訊
    response = s.recv(4096).decode()
    print(response)

    # 關閉socket連接
    s.close()

# 測試程式碼
system_network_connections_discovery('www.google.com', 80)