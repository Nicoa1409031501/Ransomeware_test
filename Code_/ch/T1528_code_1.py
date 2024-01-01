import http.client
import json

def steal_access_token(url, payload):
    conn = http.client.HTTPSConnection(url)
    headers = {'Content-type': 'application/json'}
    conn.request("POST", "/api/login", json.dumps(payload), headers=headers)
    response = conn.getresponse()

    if response.status == 200:
        access_token = json.loads(response.read())['access_token']
        return access_token
    else:
        return None

# 使用範例:
url = 'example.com'
payload = {'username': 'admin', 'password': 'password'}
access_token = steal_access_token(url, payload)
if access_token:
    print(f"Access Token: {access_token}")
else:
    print("Failed to steal access token")