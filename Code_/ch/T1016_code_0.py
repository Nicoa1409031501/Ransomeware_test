import subprocess

# 獲取系統的IP和MAC地址
def get_network_config():
    result = subprocess.run(['ipconfig'], capture_output=True, text=True)
    return result.stdout

# 獲取Wi-Fi資訊
def get_wifi_info():
    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
    return result.stdout

# 測試
print(get_network_config())
print(get_wifi_info())