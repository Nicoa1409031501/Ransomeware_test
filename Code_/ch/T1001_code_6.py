import requests

def impersonate_legitimate_traffic(url):
    headers = {
        # Add legitimate headers
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.text

url = "http://example.com"
response = impersonate_legitimate_traffic(url)
print(response)