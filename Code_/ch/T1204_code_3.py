# 範例寫入檔案
with open("user_execution.py", "w") as f:
    f.write("""
import webbrowser

def user_click_link(link):
    webbrowser.open(link)

user_click_link("http://malicious-website.com")
""")