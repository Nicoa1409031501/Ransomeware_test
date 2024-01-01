import sh

# 直接執行命令
sh.ls('-l')

# 執行命令並獲取輸出
output = sh.ls('-l', _out=str)
print(output)

# 執行腳本文件
sh.python('script.py')