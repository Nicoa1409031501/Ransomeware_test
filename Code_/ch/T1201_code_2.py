import paramiko

def password_policy_discovery(hostname, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    
    stdin, stdout, stderr = client.exec_command(command)
    
    # 解析命令輸出，提取密碼政策的相關資訊
    
    # ...