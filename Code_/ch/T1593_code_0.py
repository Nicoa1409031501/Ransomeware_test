import requests
import re

def search_websites(url):
    response = requests.get(url)
    if response.ok:
        pattern = r"(?<=<title>).+?(?=</title>)"
        matches = re.findall(pattern, response.text)
        return matches
    else:
        return None