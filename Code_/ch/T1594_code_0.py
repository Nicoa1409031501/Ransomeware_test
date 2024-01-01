import requests
from bs4 import BeautifulSoup

def search_victim_websites(url):
    # 發送GET請求並獲取網頁內容
    response = requests.get(url)
    # 使用BeautifulSoup解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 從網頁中尋找目標資訊，例如部門、地點、員工資料等
    departments = soup.find_all('div', class_='department')
    locations = soup.find_all('span', class_='location')
    employees = soup.find_all('div', class_='employee')

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

# 使用範例
search_victim_websites("https://www.example.com")