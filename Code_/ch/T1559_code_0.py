import subprocess

# 使用subprocess模塊執行命令
command = "whoami"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)