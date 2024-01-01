import urllib.request

target_url = "https://www.example.com"  # 目標網站的URL

# 擷取網頁內容
response = urllib.request.urlopen(target_url)
html = response.read().decode()

# 從HTML中擷取組織資訊
# 假設組織名稱位於<h1>標籤中
start_tag = "<h1>"
end_tag = "</h1>"
start_index = html.find(start_tag) + len(start_tag)
end_index = html.find(end_tag)
organization_name = html[start_index:end_index]

print("組織名稱:", organization_name)