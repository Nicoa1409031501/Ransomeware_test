from bs4 import BeautifulSoup
import requests

def search_websites(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tags = soup.find_all('title')
        titles = [tag.get_text() for tag in title_tags]
        return titles
    else:
        return None