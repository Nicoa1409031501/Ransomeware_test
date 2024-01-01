import urllib.request
import json

def steal_access_token(url, payload):
    req = urllib.request.Request(url, json.dumps(payload).encode('utf-8'), method='POST')
    req.add_header('Content-Type', 'application/json')

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            access_token = json.loads(response.read())['access_token']
            return access_token
    except urllib.error.HTTPError as e:
        print(f"Error: {e.reason}")

    return None

# 使用範例:
url = 'https://example.com/api/login'
payload = {'username': 'admin', 'password': 'password'}
access_token = steal_access_token(url, payload)
if access_token:
    print(f"Access Token: {access_token}")
else:
    print("Failed to steal access token")