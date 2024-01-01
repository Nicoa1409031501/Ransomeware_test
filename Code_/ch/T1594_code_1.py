import requests
import re

def search_victim_websites(url):
    # 發送GET請求並獲取網頁原始碼
    response = requests.get(url)
    html_content = response.text

    # 使用正則表達式尋找目標資訊
    department_pattern = re.compile(r'<div class="department">(.+)</div>')
    location_pattern = re.compile(r'<span class="location">(.+)</span>')
    employee_pattern = re.compile(r'<div class="employee">(.+)</div>')

    # 使用findall函數從原始碼中提取資訊
    departments = re.findall(department_pattern, html_content)
    locations = re.findall(location_pattern, html_content)
    employees = re.findall(employee_pattern, html_content)

    # 輸出網站中的資訊
    print("Departments:")
    for department in departments:
        print(department)

    print("Locations:")
    for location in locations:
        print(location)

    print("Employees:")
    for employee in employees:
        print(employee)

# 使用範例
search_victim_websites("https://www.example.com")