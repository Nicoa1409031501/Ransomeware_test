import urllib.request

def impersonate_legitimate_traffic(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36")
    with urllib.request.urlopen(req) as response:
        return response.read().decode()

url = "http://example.com"
response = impersonate_legitimate_traffic(url)
print(response)