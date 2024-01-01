from http.cookiejar import CookieJar
import urllib.request

def forge_web_credentials_cookies(url, cookies):
    cookiejar = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
    opener.addheaders.append(('Cookie', cookies))
    response = opener.open(url)
    # ... handle response

# 調用範例
forge_web_credentials_cookies('http://example.com', 'session=123456789')