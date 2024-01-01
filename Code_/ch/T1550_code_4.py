import requests

login_url = "<login_url>"
username = "<username>"
password = "<password>"

# 發送POST請求以登入取得session cookies
session = requests.session()
login_data = {
    "username": username,
    "password": password
}
response = session.post(login_url, data=login_data)

# 取得session cookies
session_cookies = session.cookies.get_dict()

print(session_cookies)  # 輸出取得的session cookies