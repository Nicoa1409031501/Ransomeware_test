import requests

def discover_cloud_services(target_url):
    response = requests.get(target_url)
    if response.status_code == 200:
        cloud_services = response.json()  # 假設 API 回傳 JSON 格式的雲端服務資料
        return cloud_services
    else:
        return None

target_url = "https://example.com/cloud-services"
cloud_services = discover_cloud_services(target_url)
if cloud_services:
    for service in cloud_services:
        print(service)
else:
    print("Failed to discover cloud services.")