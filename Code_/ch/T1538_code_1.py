import requests

# 使用偷竊的帳戶資訊登入cloud service dashboard
def login_dashboard(username, password):
    login_url = "https://example.com/dashboard/login"  # 以範例網址為示意,請更換成實際的網址
    dashboard_url = "https://example.com/dashboard"  # 以範例網址為示意,請更換成實際的網址

    # 建立session
    session = requests.session()

    # 填入帳號密碼並登入
    login_data = {
        "username": username,
        "password": password
    }
    session.post(login_url, data=login_data)

    # 登入後進行相關操作，例如查看資源、公開IP等
    response = session.get(dashboard_url)
    # ...

# 呼叫function並傳入帳號密碼
login_dashboard("stolen_username", "stolen_password")