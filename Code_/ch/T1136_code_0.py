import subprocess

# 創建本地帳戶的函式
def create_local_account(username, password):
    command = f"net user {username} {password} /add"
    subprocess.run(command, shell=True)

# 呼叫函式來創建本地帳戶
create_local_account("test_user", "password123")