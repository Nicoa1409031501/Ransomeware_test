import requests

# Step 3: 建立服務器 (server.py) 同上

# Step 4: 從服務器下載文件 (client.py)
url = "http://localhost:8000/tool.exe"  # 假設工具的下載連結為 http://localhost:8000/tool.exe
file_name = "tool.exe"  # 下載後的檔案名稱

response = requests.get(url)
with open(file_name, "wb") as f:
    f.write(response.content)