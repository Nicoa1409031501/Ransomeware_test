import requests

# 方法三：使用Burp Suite等代理工具截取瀏覽器發送的HTTP請求，直接複製cookie
def steal_cookie_method3(url):
    # 使用代理工具設置代理地址，例如 Burp Suite 默認監聽地址為 127.0.0.1，監聽端口為 8080
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    
    response = requests.get(url, proxies=proxies, verify=False)  # verify=False是為了忽略SSL證書驗證
    
    if response.status_code == 200:
        # 在這裡可以處理response的內容或是將cookie儲存起來
        print(response.text)
    else:
        print('Failed to steal session cookie')

# 使用範例
steal_cookie_method3('https://example.com')