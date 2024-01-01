import requests

def search_public_scan_databases(url):
    # Step 1: 使用requests套件發送HTTP請求取得網頁內容
    response = requests.get(url)

    # Step 2: 取得掃描資訊
    scan_info = response.json()["scan_info"]

    # Step 3: 輸出結果
    print(scan_info)

search_public_scan_databases("http://example.com")