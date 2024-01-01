import requests
import json

def search_public_scan_databases(url):
    # Step 1: 使用requests套件發送HTTP請求取得網頁內容
    response = requests.get(url)

    # Step 2: 解析JSON格式的回應
    scan_data = json.loads(response.text)

    # Step 3: 取得掃描資訊
    scan_info = scan_data["scan_info"]

    # Step 4: 輸出結果
    print(scan_info)

search_public_scan_databases("http://example.com")