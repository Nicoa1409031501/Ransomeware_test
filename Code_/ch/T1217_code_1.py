import requests

def get_browser_info():
    response = requests.get("https://httpbin.org/user-agent")
    user_agent = response.json()["user-agent"]
    return user_agent

browser_info = get_browser_info()
print(browser_info)