import webview

def get_browser_info():
    browser = webview.create_window("Browser Information", "https://www.google.com/")
    webview.start()
    browser_info = browser.get_current_url()
    webview.stop()
    return browser_info

browser_info = get_browser_info()
print(browser_info)