import requests
from bs4 import BeautifulSoup

def search_open_technical_databases(url):
    # Step 1: 使用requests套件發送HTTP請求取得網頁內容
    response = requests.get(url)

    # Step 2: 使用BeautifulSoup解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: 搜尋目標資訊
    target_info = soup.find_all(class_="target-info")

    # Step 4: 輸出結果
    for info in target_info:
        print(info.text)

search_open_technical_databases("http://example.com")