import subprocess

def user_run_command(command):
    subprocess.run(command, shell=True)

# 使用方式
user_run_command("malicious_command.exe")