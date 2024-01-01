from selenium import webdriver
from selenium.webdriver.common.alert import Alert

def forced_authentication():
    browser = webdriver.Chrome()  # 使用Chrome瀏覽器
    
    # 1. 模擬用戶操作：打開目標網站
    browser.get("https://example.com")
    
    # 2. 注入JavaScript程式碼，彈出要求用戶輸入認證資訊的視窗
    browser.execute_script("alert('Please enter your credentials: ')")
    
    # 3. 使用Selenium的alert函式取得彈出視窗的物件
    alert = Alert(browser)
    
    # 4. 取得用戶輸入的認證資訊
    credentials = alert.text
    
    # 5. 透過其他程式碼處理用戶輸入的認證資訊，例如寫入檔案、傳送到遠端伺服器等等...
    
    # 6. 關閉瀏覽器
    browser.quit()

forced_authentication()