from selenium import webdriver

# 方法二：使用selenium套件模擬瀏覽器操作，並獲取cookie
def steal_cookie_method2(url):
    driver = webdriver.Chrome()  # 需要下載ChromeDriver並放在程式碼的同一目錄下，或配置環境變數
    driver.get(url)
    
    # 獲取cookie
    cookies = driver.get_cookies()
    
    # 在這裡可以處理cookies的內容或是將cookie儲存起來
    print(cookies)
    
    driver.quit()

# 使用範例
steal_cookie_method2('https://example.com')