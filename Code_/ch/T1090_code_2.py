import socks
import socket
import urllib.request

def send_request_with_socks_proxy(url, proxy):
    proxy_type, proxy_host, proxy_port = proxy.split(':')

    # 設定全域默認代理
    socks.set_default_proxy(socks.SOCKS5, proxy_host, int(proxy_port))
    socket.socket = socks.socksocket

    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')

# 使用SOCKS代理發送請求
url = 'https://www.example.com'
proxy = 'socks5://127.0.0.1:1080'  # SOCKS代理伺服器的IP和埠號
response = send_request_with_socks_proxy(url, proxy)
print(response)