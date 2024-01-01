import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 檢查瀏覽器擴展(extension)列表中是否存在可疑的擴展
def check_suspicious_extensions(browser):
    options = Options()
    options.add_argument("--load-extension=/path/to/extension")  # 使用指定的Chrome擴展路徑
    driver = webdriver.Chrome(options=options)  # 請確保已安裝Chrome WebDriver
    driver.get("chrome://extensions")

    extensions = driver.find_elements_by_css_selector('div.extension-list-item')  # 取得擴展列表的元素
    suspicious_extensions = []

    for extension in extensions:
        name = extension.find_element_by_css_selector('h2').text
        if is_suspicious_extension(name):
            suspicious_extensions.append(name)
    
    driver.quit()
    return suspicious_extensions

# 判斷是否為可疑的擴展
def is_suspicious_extension(name):
    # 在此實作自己的邏輯來判斷擴展是否可疑
    return False

# 列出所有的瀏覽器擴展
def list_all_extensions(browser):
    options = Options()
    options.add_argument("--load-extension=/path/to/extension")  # 使用指定的Chrome擴展路徑
    driver = webdriver.Chrome(options=options)  # 請確保已安裝Chrome WebDriver
    driver.get("chrome://extensions")

    extensions = driver.find_elements_by_css_selector('div.extension-list-item')  # 取得擴展列表的元素

    for extension in extensions:
        print(extension.find_element_by_css_selector('h2').text)  # 列出擴展名稱
    
    driver.quit()

# 偵測已安裝的擴展是否有任何異常行為
def detect_anomaly_extensions(browser):
    # 在此實作自己的偵測邏輯
    pass

# 使用示例
browser = "Chrome"
suspicious_extensions = check_suspicious_extensions(browser)
print("Suspicious extensions:", suspicious_extensions)

list_all_extensions(browser)

detect_anomaly_extensions(browser)