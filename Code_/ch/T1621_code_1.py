from selenium import webdriver

def simulate_mfa_request(url, username, password):
    driver = webdriver.Chrome()  # 需要先安裝ChromeDriver
    driver.get(url)
    username_input = driver.find_element_by_id('username')
    password_input = driver.find_element_by_id('password')
    submit_button = driver.find_element_by_id('submit')
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button.click()
    
    # 等待頁面跳轉或驗證碼出現等相關操作
    # 根據需要進行後續操作
    
    driver.quit()