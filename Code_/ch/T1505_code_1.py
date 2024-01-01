import subprocess

# 方法一
subprocess.run('command', shell=True)  # 執行指令，例如安裝惡意組件或建立後門

# 方法二
result = subprocess.Popen('command', shell=True, stdout=subprocess.PIPE).communicate()[0].decode()  # 執行指令，並且回傳結果