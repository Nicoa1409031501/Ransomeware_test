from fabric import Connection

# 方法一
with Connection('hostname') as c:
    c.run('command')  # 執行指令，例如安裝惡意組件或建立後門