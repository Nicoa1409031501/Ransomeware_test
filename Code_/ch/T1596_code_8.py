import requests

def search_cdn_data(url):
    # Step 1: 使用requests套件發送HTTP請求取得網頁內容
    response = requests.get(url)

    # Step 2: 取得CDN資訊
    cdn_info = response.headers["X-CDN"]

    # Step 3: 輸出結果
    print(cdn_info)

search_cdn_data("http://example.com")