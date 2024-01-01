import os

# 使用os.system執行命令
os.system('ls -l')

# 使用os.popen執行命令，並獲取輸出
output = os.popen('ls -l').read()
print(output)

# 使用os.spawn系列方法執行命令
pid = os.spawnlp(os.P_NOWAIT, 'ls', 'ls', '-l')