import socket

# Step 3: 建立服務器 (server.py)
HOST = '127.0.0.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()

with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        with open('tool.exe', 'wb') as f:
            f.write(data)

# Step 4: 從服務器下載文件 (client.py)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 8000))
    with open('tool.exe', 'rb') as f:
        s.sendall(f.read())