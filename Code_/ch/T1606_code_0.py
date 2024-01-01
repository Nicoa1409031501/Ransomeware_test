import requests

def forge_web_credentials_cookies(url, cookies):
    headers = {
        'Cookie': cookies
    }
    response = requests.get(url, headers=headers)
    # ... handle response

# 調用範例
forge_web_credentials_cookies('http://example.com', 'session=123456789')