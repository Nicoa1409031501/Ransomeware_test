import socket
import os

# 檢查網際網路連線狀態
def check_internet_connectivity():
    try:
        socket.create_connection(('www.google.com', 80))
        return True
    except OSError:
        return False

# 獲取系統的IP和MAC地址
def get_network_config():
    result = os.popen('ipconfig').read()
    return result

# 測試
print(check_internet_connectivity())
print(get_network_config())