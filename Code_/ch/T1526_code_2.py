import http.client
import json

def discover_cloud_services(target_url):
    conn = http.client.HTTPSConnection(target_url)
    conn.request("GET", "/cloud-services")
    response = conn.getresponse()
    if response.code == 200:
        cloud_services = json.loads(response.read().decode())  # 假設 API 回傳 JSON 格式的雲端服務資料
        return cloud_services
    else:
        return None

target_url = "example.com"
cloud_services = discover_cloud_services(target_url)
if cloud_services:
    for service in cloud_services:
        print(service)
else:
    print("Failed to discover cloud services.")