import socket

def drive_by_compromise(url):
    # 解析網址
    domain = url.split('/')[2]
    path = '/' + '/'.join(url.split('/')[3:])
    port = 80

    # 建立TCP連接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((domain, port))

    # 構造HTTP GET請求
    request = f"GET {path} HTTP/1.1\r\nHost: {domain}\r\nUser-Agent: Mozilla/5.0\r\n\r\n"

    # 發送請求
    s.sendall(request.encode())

    # 接收回應
    response = s.recv(4096).decode()

    # 檢查網頁回應，判斷是否包含惡意腳本
    if 'evil-script' in response:
        # 執行相應的操作
        print("Drive-by Compromise攻擊發生")
        # ...執行相應的操作

    # 關閉連接
    s.close()

# 執行Drive-by Compromise攻擊
drive_by_compromise('https://example.com')