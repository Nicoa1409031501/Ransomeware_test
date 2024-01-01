import requests

# 檢查網際網路連線狀態
def check_internet_connectivity():
    try:
        response = requests.get('http://www.google.com')
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# 獲取系統的IP和MAC地址
def get_network_config():
    result = requests.get('http://ipconfig.io')
    return result.text

# 測試
print(check_internet_connectivity())
print(get_network_config())