import time
from selenium import webdriver

# 使用偷竊的帳戶資訊登入cloud service dashboard
def login_dashboard(username, password):
    driver = webdriver.Chrome()  # 使用Chrome瀏覽器，需安裝ChromeDriver
    driver.get("https://example.com/dashboard")  # 以範例網址為示意,請更換成實際的網址

    # 填入帳號密碼並登入
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login-button").click()

    # 登入後進行相關操作，例如查看資源、公開IP等
    # ...

    driver.quit()

# 呼叫function並傳入帳號密碼
login_dashboard("stolen_username", "stolen_password")