import requests
from bs4 import BeautifulSoup

target_url = "https://www.example.com"  # 目標網站的URL

# 發送GET請求取得網頁內容
response = requests.get(target_url)
html = response.text

# 解析HTML
soup = BeautifulSoup(html, "html.parser")

# 擷取組織名稱
organization_name = soup.find("h1").text

print("組織名稱:", organization_name)