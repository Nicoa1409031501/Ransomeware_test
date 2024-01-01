from urllib.request import urlopen

def trusted_relationship(url):
    response = urlopen(url)
    data = response.read().decode()
    return data

# 使用方式
url = "https://www.example.com"
result = trusted_relationship(url)
print(result)