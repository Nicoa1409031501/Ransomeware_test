from selenium import webdriver

def search_victim_websites(url):
    # 使用瀏覽器驅動程式開啟網頁
    driver = webdriver.Chrome()
    driver.get(url)

    # 使用XPath獲取目標資訊元素
    departments = driver.find_elements_by_xpath('//div[@class="department"]')
    locations = driver.find_elements_by_xpath('//span[@class="location"]')
    employees = driver.find_elements_by_xpath('//div[@class="employee"]')

    # 輸出網站中的資訊
    print("Departments:")
    for department in departments:
        print(department.text)

    print("Locations:")
    for location in locations:
        print(location.text)

    print("Employees:")
    for employee in employees:
        print(employee.text)

    # 關閉瀏覽器
    driver.quit()

# 使用範例
search_victim_websites("https://www.example.com")