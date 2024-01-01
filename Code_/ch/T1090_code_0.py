import requests

def send_request_with_proxy(url, proxy):
    session = requests.Session()
    session.proxies = {'http': proxy, 'https': proxy}
    response = session.get(url)
    return response.text

# 使用代理發送請求
url = 'https://www.example.com'
proxy = 'http://127.0.0.1:8080'  # 代理伺服器的IP和埠號
response = send_request_with_proxy(url, proxy)
print(response)