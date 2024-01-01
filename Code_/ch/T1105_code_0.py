import urllib

# Step 3: 建立服務器 (server.py)
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()

# Step 4: 從服務器下載文件 (client.py)
url = "http://localhost:8000/tool.exe"  # 假設工具的下載連結為 http://localhost:8000/tool.exe
file_name = "tool.exe"  # 下載後的檔案名稱

urllib.request.urlretrieve(url, file_name)