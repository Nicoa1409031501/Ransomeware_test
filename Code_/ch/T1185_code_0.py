# 使用selenium套件
from selenium import webdriver

# 啟動瀏覽器
driver = webdriver.Chrome()

# 篡改瀏覽器的session
driver.execute_cdp_cmd('Network.addInterception', {
    'patterns': [{'urlPattern': '*', 'resourceType': 'Document', 'interceptionStage': 'HeadersReceived'}]
})
driver.execute_cdp_cmd('Network.setInterceptionEnabled', {'enabled': True})

# 關閉瀏覽器
driver.quit()