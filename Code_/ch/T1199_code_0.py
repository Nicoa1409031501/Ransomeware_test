import requests

def trusted_relationship(url):
    response = requests.get(url)
    data = response.text
    return data

# 使用方式
url = "https://www.example.com"
result = trusted_relationship(url)
print(result)