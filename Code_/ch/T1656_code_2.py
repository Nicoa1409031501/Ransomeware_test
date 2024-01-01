from selenium import webdriver

def fake_login_page(url, username_input_id, password_input_id, submit_button_id):
    driver = webdriver.Chrome('your_chrome_driver_path')
    driver.get(url)
    
    # 找到帳號欄位並輸入偽造的帳號
    username_input = driver.find_element_by_id(username_input_id)
    username_input.send_keys("fake_username")
    
    # 找到密碼欄位並輸入偽造的密碼
    password_input = driver.find_element_by_id(password_input_id)
    password_input.send_keys("fake_password")
    
    # 找到送出按鈕並點擊
    submit_button = driver.find_element_by_id(submit_button_id)
    submit_button.click()
    
    # 等待網頁反應
    driver.implicitly_wait(10)
    
    # 關閉瀏覽器
    driver.quit()

# 使用方法
fake_login_page("http://www.example.com/login", "username_input", "password_input", "submit_button")