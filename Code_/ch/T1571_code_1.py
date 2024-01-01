import requests

def check_non_standard_port(hostname, port):
    try:
        url = f"http://{hostname}:{port}/"
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            print("Non-Standard Port", port, "is open")
        else:
            print("Non-Standard Port", port, "is closed")
    except requests.exceptions.RequestException as err:
        print("Exception:", err)

# 使用範例
check_non_standard_port("example.com", 8088)