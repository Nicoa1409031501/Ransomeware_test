from selenium import webdriver

def browse_with_proxy(url, proxy):
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=' + proxy)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    return page_source

# 使用代理瀏覽網頁
url = 'https://www.example.com'
proxy = 'http://127.0.0.1:8080'  # 代理伺服器的IP和埠號
page_source = browse_with_proxy(url, proxy)
print(page_source)