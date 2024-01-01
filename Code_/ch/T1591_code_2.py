from selenium import webdriver

target_url = "https://www.example.com"  # 目標網站的URL

# 啟動瀏覽器
driver = webdriver.Chrome()
driver.get(target_url)

# 擷取組織名稱
organization_name = driver.find_element_by_tag_name("h1").text

print("組織名稱:", organization_name)

# 關閉瀏覽器
driver.quit()