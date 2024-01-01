import urllib.request

def drive_by_compromise(url):
    # 模擬瀏覽器發送 GET 請求
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        # 讀取網頁內容
        html = response.read().decode('utf-8')

        # 檢查網頁回應，判斷是否包含惡意腳本
        if 'evil-script' in html:
            # 執行相應的操作
            print("Drive-by Compromise攻擊發生")
            # ...執行相應的操作

# 執行Drive-by Compromise攻擊
drive_by_compromise('https://example.com')