import os
import socket

def network_share_discovery():
    # 列出網絡上所有的電腦名稱（hostname）
    computer_names = []
    for ip in range(1, 256):
        ip_address = f'192.168.1.{ip}' # 修改成目標網段
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            computer_names.append(hostname)
        except socket.herror or socket.timeout:
            pass
            
    # 列出所有共享資料夾
    shared_folders = []
    for computer_name in computer_names:
        shared_folder_cmd = f'net view \\\\{computer_name}'
        try:
            result = os.popen(shared_folder_cmd).read()
            lines = result.split('\n')
            for line in lines:
                if line.startswith('\\'):
                    shared_folders.append(line.strip())
        except:
            pass
    
    return shared_folders

result = network_share_discovery()
print(result)