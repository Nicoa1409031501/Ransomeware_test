import requests
from bs4 import BeautifulSoup

def extract_confluence_info(url):
    # 發送HTTP請求並將回應解析為HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 使用CSS選擇器選取有價值的資訊元素
    valuable_info_elements = soup.select('.valuable-info-class')

    # 提取有價值的資訊內容
    valuable_info = []
    for element in valuable_info_elements:
        valuable_info.append(element.text)

    return valuable_info

# 使用範例：提取Confluence網頁中的有價值資訊
confluence_url = 'https://example.com/confluence'
info_list = extract_confluence_info(confluence_url)
print(info_list)