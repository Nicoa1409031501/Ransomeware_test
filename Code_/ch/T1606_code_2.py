import http.cookiejar
import urllib.request

def forge_web_credentials_cookies(url, cookies):
    cookiejar = http.cookiejar.CookieJar()
    cookie = http.cookiejar.Cookie(version=0, name='session', value=cookies, port=None, port_specified=False,
                                    domain='', domain_specified=False, domain_initial_dot=False, path='',
                                    path_specified=False, secure=False, expires=None, discard=False, comment=None,
                                    comment_url=None, rest={}, rfc2109=False)
    cookiejar.set_cookie(cookie)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
    response = opener.open(url)
    # ... handle response

# 調用範例
forge_web_credentials_cookies('http://example.com', 'session=123456789')