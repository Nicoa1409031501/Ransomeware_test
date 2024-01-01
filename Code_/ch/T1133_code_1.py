import requests

def check_remote_service(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Service {url} is accessible.")
        else:
            print(f"Service {url} returned status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {url}: {str(e)}")

check_remote_service("https://example.com")