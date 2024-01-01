import requests
from bs4 import BeautifulSoup

def active_crawling_scan(url):
    links = []
    
    # 發送GET請求並獲取響應內容
    response = requests.get(url)
    
    # 使用BeautifulSoup解析HTML內容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 遍歷頁面中的所有連結
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    
    return links

url = 'http://example.com'
links = active_crawling_scan(url)
print("頁面中的連結：", links)