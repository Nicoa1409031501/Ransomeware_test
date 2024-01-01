import paramiko

def remote_access_ssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 輸入目標主機的IP地址、用戶名和密碼
    host = input("Enter target host IP: ")
    user = input("Enter username: ")
    password = input("Enter password: ")

    ssh.connect(host, username=user, password=password)

    while True:
        command = input("Enter command or 'exit' to quit: ")
        if command == 'exit':
            break
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read().decode()
        print(result)

    ssh.close()

remote_access_ssh()