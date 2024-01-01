import subprocess
import os

def execute_command(command, password):
    # 使用subprocess執行指令
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    # 等待sudo工具輸入密碼
    p.stdin.write(password.encode())
    p.stdin.flush()
    # 取得輸出
    output, error = p.communicate()
    # 寫入檔案
    with open('output.txt', 'w') as f:
        f.write(output.decode())

# 呼叫函式
execute_command('sudo -S -l lsass_dump.py', 'password')