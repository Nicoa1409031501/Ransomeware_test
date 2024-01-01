import requests

# 方法一：使用requests套件進行HTTP請求，並在請求中包含cookie
def steal_cookie_method1(url, cookie):
    headers = {
        'Cookie': cookie
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # 在這裡可以處理response的內容或是將cookie儲存起來
        print(response.text)
    else:
        print('Failed to steal session cookie')

# 使用範例
steal_cookie_method1('https://example.com', 'session_cookie=abcdef123456')