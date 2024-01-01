import subprocess

# 使用subprocess.run執行命令
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)

# 使用subprocess.call執行命令，並將輸出重定向到文件
with open('output.txt', 'w') as f:
    subprocess.call(['ls', '-l'], stdout=f)