# 使用requests套件
import requests

# 取得瀏覽器的session cookie
cookies = {
    'sessionid': 'your_session_id',
    'csrftoken': 'your_csrf_token',
    # 其他必要的session cookies
}

# 篡改session cookie的值
cookies['sessionid'] = 'modified_session_id'

# 建立一個具有修改後session的requests session
session = requests.Session()
session.cookies = requests.cookies.cookiejar_from_dict(cookies)

# 發送請求
response = session.get('https://www.example.com')

# 輸出回應內容
print(response.text)