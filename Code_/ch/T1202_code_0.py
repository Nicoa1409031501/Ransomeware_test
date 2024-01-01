import subprocess

def run_command(command):
    subprocess.call(command, shell=True)

# 使用subprocess.call()執行指定的命令
run_command("notepad.exe")