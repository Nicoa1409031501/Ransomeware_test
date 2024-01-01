import requests

def steal_access_token(url, payload):
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return access_token
    else:
        return None

# 使用範例:
url = 'https://example.com/api/login'
payload = {'username': 'admin', 'password': 'password'}
access_token = steal_access_token(url, payload)
if access_token:
    print(f"Access Token: {access_token}")
else:
    print("Failed to steal access token")