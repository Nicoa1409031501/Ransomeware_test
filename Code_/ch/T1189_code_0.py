import requests

def drive_by_compromise(url):
    # 模擬瀏覽器發送 GET 請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    
    # 檢查網頁回應，判斷是否包含惡意腳本
    if 'evil-script' in response.text:
        # 執行相應的操作
        print("Drive-by Compromise攻擊發生")
        # ...執行相應的操作
    
    # 如果需要，還可以對回應進行進一步的分析和處理

# 執行Drive-by Compromise攻擊
drive_by_compromise('https://example.com')