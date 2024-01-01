from selenium import webdriver

def get_browser_info():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 在後台運行瀏覽器
    browser = webdriver.Chrome(options=options)
    browser.get("about:version")  # 獲取瀏覽器版本資訊的URL
    browser_info = browser.find_element_by_tag_name("pre").text
    browser.quit()
    return browser_info

browser_info = get_browser_info()
print(browser_info)