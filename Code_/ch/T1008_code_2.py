import paramiko

# 使用 SSH 進行 command and control
def ssh_c2(hostname, username, password):
    try:
        # 建立 SSH 連線
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        # 執行命令
        command = ssh.exec_command("command")
        result = command[1].read()
        # 將結果輸出
        print(result)
        # 關閉 SSH 連線
        ssh.close()
        
    except Exception as e:
        print("Error: %s" % str(e))

# 呼叫方法
ssh_c2("C2_SERVER_HOSTNAME", "USERNAME", "PASSWORD")