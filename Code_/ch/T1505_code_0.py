import os

# 方法一
os.system('command')  # 執行指令，例如安裝惡意組件或建立後門

# 方法二
result = os.popen('command').read()  # 執行指令，並且回傳結果