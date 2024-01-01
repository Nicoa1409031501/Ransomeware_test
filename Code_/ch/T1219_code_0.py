import socket

def remote_access_server():
    HOST = '127.0.0.1'  # 目標主機的IP地址
    PORT = 12345  # 目標主機的端口號

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        print('Connected by', addr)
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # 執行接收到的命令，並將結果傳回給遠端使用者
            result = execute_command(data.decode())
            conn.sendall(result.encode())

def execute_command(command):
    # 在這裡執行你想要的命令，並將結果回傳

remote_access_server()