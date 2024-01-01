from selenium import webdriver

def establish_social_media_account(username, password):
    # 使用selenium開啟瀏覽器
    driver = webdriver.Chrome()

    # 前往社交媒體註冊頁面
    driver.get("https://www.example.com/signup")

    # 填寫註冊表單
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)

    # 提交註冊表單
    driver.find_element_by_id("signup-button").click()

    # 等待註冊完成
    driver.implicitly_wait(10)

    # 創建社交媒體帳號後，進一步建立帳號的個人資訊、歷史和關聯等資料

    # 關閉瀏覽器
    driver.quit()

# 使用範例
establish_social_media_account("example_username", "example_password")