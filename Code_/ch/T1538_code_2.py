import mechanicalsoup

# 使用偷竊的帳戶資訊登入cloud service dashboard
def login_dashboard(username, password):
    login_url = "https://example.com/dashboard/login"  # 以範例網址為示意,請更換成實際的網址
    dashboard_url = "https://example.com/dashboard"  # 以範例網址為示意,請更換成實際的網址

    # 建立browser
    browser = mechanicalsoup.Browser()

    # 輸入帳號密碼並提交
    login_page = browser.get(login_url)
    login_form = login_page.soup.select_one("form")
    login_form.select_one("#username").attrs['value'] = username
    login_form.select_one("#password").attrs['value'] = password
    response = browser.submit(login_form, login_page.url)

    # 登入後進行相關操作，例如查看資源、公開IP等
    dashboard_page = browser.get(dashboard_url)
    # ...

# 呼叫function並傳入帳號密碼
login_dashboard("stolen_username", "stolen_password")